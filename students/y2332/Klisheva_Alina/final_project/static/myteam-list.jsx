import React from 'react'
import Load from "./load";
import AddMember from "./add-member";
import TeamCreate from "./team-create";

class MyTeamGet extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            loading: true,
            is_edditing: -1,
            team_edit: false,
            is_added: false,
            result: 0,
            create: false
        }

        fetch('/hack/captain/get/' + this.props.user, {
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            }
        }).then(r => r.json().then(json => {
                this.team = json
                if (this.team['team'] === null) {
                    this.setState({
                        create: true,
                         loading: false
                    })
                }
                let sum = 0
            this.team['team']['solutions'].forEach((team) => {
                    sum += team['score']
                })
                this.state.result = sum

                this.setState({
                    loading: false
                })


            }
        ))
        this.makeTeamEditable = this.makeTeamEditable.bind(this);
        this.makeMemberEditable = this.makeMemberEditable.bind(this);
        this.editMember = this.editMember.bind(this);
        this.addMember = this.addMember.bind(this);
        this.deleteMember = this.deleteMember.bind(this);
        this.deleteSolution = this.deleteSolution.bind(this);
        this.editTeam = this.editTeam.bind(this);
    }

    makeMemberEditable(e, i) {
        e.preventDefault()
        this.setState(
            {is_editing: i}
        )
    }

    makeTeamEditable(e) {
        e.preventDefault()

        this.setState((state) => {
            return {team_edit: !state.team_edit}
        })
    }

    editTeam(e, id) {
        e.preventDefault()
        fetch('/hack/team/update/' + id, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            },
            body: JSON.stringify(Object.fromEntries(new FormData(document.getElementById('team-form'))))
        }).then(r => {
            if (r.status === 200) {
                this.props.reload_issues()
            } else {
                alert('Ошибка')
            }
        })
    }

    editMember(e, id) {
        e.preventDefault()
        let form = new FormData()
        form.append('fio', document.getElementById("member-fio-input").value)
        form.append('role', document.getElementById("member-role-input").value)
        form.append('phoneNumber', document.getElementById("member-phone-input").value)
        fetch('/hack/member/update/' + id, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            },
            body: JSON.stringify(Object.fromEntries(form))
        }).then(r => {
            if (r.status === 200) {
                this.props.reload_issues()
            } else {
                alert('Ошибка')
            }
        })
    }

    deleteMember(e, id) {
        e.preventDefault()
        fetch('/hack/member/delete/' + id, {
            method: "DELETE",
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            }
        }).then(r => {
            if (Math.floor(r.status / 100) === 2) {
                this.props.reload_issues()
            } else
                alert("Ошибка")
        })
    }

    deleteSolution(e, id) {
        e.preventDefault()
        fetch('/hack/solution/delete/' + id, {
            method: "DELETE",
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            }
        }).then(r => {
            if (Math.floor(r.status / 100) === 2) {
                this.props.reload_issues()
            } else
                alert("Ошибка")
        })
    }

    addMember(e) {
        e.preventDefault()
        this.setState((state) => {
            return {is_added: !state.is_added}
        })
    }



    render() {
        if (this.state.loading)
            return (
                <Load/>
            )
        if (this.state.create)
            return (
                <TeamCreate reload_issues={this.props.reload_issues} user={this.props.user}/>
            )
        else {
            let solutions = []
            solutions.push(<thead>

            <th>Дата публикации</th>
            <th>Баллы</th>
            <th>Комментарий</th>
            <th>Ссылка на решение</th>
            <th>Задача</th>
            <th>Проверяющий</th>

            </thead>)
            solutions.push(
                <tbody>
                {this.team['team']['solutions'].map((team) => {
                    return (
                        <tr>
                            <td>{team['pubDate']}</td>
                            <td>{team['score']}</td>
                            <td>{team['comment']}</td>
                            <td>{team['solutionLink']}</td>
                            <td>{team['issue']['name']}</td>
                            <td>{team['jury'] === null ? <>Непроверено</> : team['jury']['username']}</td>
                            <td>
                                <button className="button is-danger"
                                        onClick={(e) => this.deleteSolution(e, team['id'])}>Удалить
                                </button>
                            </td>
                        </tr>
                    )

                })}
                </tbody>)


            let members = []
            members.push(<thead>

            <th>ФИО</th>
            <th>Роль</th>
            <th>Номер телефона</th>
            <th/>
            <th/>

            </thead>)
            members.push(
                <tbody>
                {
                    this.team['team']['team_members'].map((team, i) => {
                            return (
                                <>
                                    {
                                        this.state.is_editing === i ?
                                            <>
                                                <tr>
                                                    <td>
                                                        <input id="member-fio-input" className="input" type="text"
                                                               name="fio"
                                                               defaultValue={team['fio']}
                                                               />
                                                    </td>
                                                    <td>
                                                        <select id="member-role-input" name="role" className="select"
                                                                defaultValue={team['role']}>
                                                            <option value="1" name="role">Developer</option>
                                                            <option value="2" name="role">Designer</option>
                                                            <option value="3" name="role">Entrepreneur</option>
                                                        </select>
                                                    </td>
                                                    <td>
                                                        <input id="member-phone-input" className="input" type="text"
                                                               name="phoneNumber"
                                                               defaultValue={team['phoneNumber']}/>
                                                    </td>
                                                    <td>
                                                        <button className="button is-primary"
                                                                onClick={(e) => this.editMember(e, team['id'])}>Применить
                                                        </button>
                                                    </td>
                                                    <td>
                                                        <button className="button is-danger"
                                                                onClick={(e) => this.makeMemberEditable(e, -1)}>Отменить
                                                        </button>
                                                    </td>
                                                </tr>
                                            </>

                                            : <>
                                                <tr>
                                                    <td>{team['fio']}</td>
                                                    <td>{team['role']}</td>
                                                    <td>{team['phoneNumber']}</td>
                                                    <td>
                                                        <button className="button is-primary"
                                                                onClick={(e) => this.makeMemberEditable(e, i)}>Редактировать
                                                        </button>

                                                    </td>
                                                    <td>
                                                        <button className="button is-danger"
                                                                onClick={(e) => this.deleteMember(e, team['id'])}>Удалить
                                                        </button>
                                                    </td>

                                                </tr>
                                            </>
                                    }
                                < />

                            )
                        }
                    )
                }
                </tbody>)


            let myteams = []
            myteams.push(
                <div className="Box">
                    <h3 className="title is-3 ">Команда</h3>
                    <form id="team-form">
                        <div className="field">
                            <div className="control">
                                <label className="label">Название:</label>
                                {this.state.team_edit ? <input className="input" type="text" name="teamName"
                                                               defaultValue={this.team['team']['teamName']}/> :
                                    <h5>{this.team['team']['teamName']}</h5>}
                            </div>
                        </div>
                        <div className="field">
                            <div className="control">
                                <label className="label">Девиз: </label>
                                {this.state.team_edit ? <input className="input" type="text" name="motto"
                                                               defaultValue={this.team['team']['motto']}/> :
                                    <h5>{this.team['team']['motto']}</h5>}
                            </div>
                        </div>
                        <div className="field">
                            <div className="control">
                                <label className="label">Командир: </label>
                                {this.state.team_edit ?
                                    <input className="input" type="text" name="username" readOnly='true'
                                           defaultValue={this.team['team']['captain']['username']}/> :
                                    <h5> {this.team['team']['captain']['username']}</h5>}
                            </div>
                        </div>
                        <div className="field">
                            <div className="control">
                                <label className="label">Количество решений: </label>
                                {this.state.team_edit ?
                                    <input className="input" type="text" name="solutions" readOnly='true'
                                           defaultValue={this.team['team']['solutions'].length}/> :
                                    <h5>{this.team['team']['solutions'].length}</h5>}
                            </div>
                        </div>
                         <div className="field">
                            <div className="control">
                                <label className="label">Всего баллов: </label>
                                {this.state.team_edit ?
                                    <input className="input" type="text" name="sum" readOnly='true'
                                           defaultValue={this.state.result}/> :
                                    <h5>{this.state.result}</h5>}
                            </div>
                        </div>
                        <div className="field is-grouped">
                            <div className="control">
                                {this.state.team_edit ?
                                    <button className="button is-danger"
                                            onClick={(e) => this.makeTeamEditable(e)}>Отменить
                                    </button> : <button className="button is-primary"
                                                        onClick={(e) => this.makeTeamEditable(e)}>Изменить
                                    </button>}
                            </div>
                            <div className="control">
                                {this.state.team_edit ? <button className="button is-primary"
                                                                onClick={(e) => this.editTeam(e, this.team['team']['id'])}>Применить
                                </button> : <></>}
                            </div>
                        </div>
                    </form>

                </div>)


            return (<div className="Box">
                    <div className="block">
                        {myteams}
                    </div>
                    <div className="block">
                        <h3 className="title is-3 ">Участники</h3>


                        <table className="table">

                            {members}
                        </table>

                        <div>
                            {!this.state.is_added ?
                                <div>
                                    <button className="button is-primary"
                                            onClick={(e) => this.addMember(e)}>Добавить
                                        участника
                                    </button>
                                </div> : <div>
                                    <button className="button is-danger" onClick={(e) => this.addMember(e)}>Отменить
                                    </button>
                                </div>}
                        </div>
                    </div>
                    <div>
                        {this.state.is_added ?
                            <div className="block"><AddMember team={this.team['team']['id']}
                                                              reload_issues={this.props.reload_issues}/></div> :
                            <div></div>}

                    </div>
                    <div className="block">
                        <h3 className="title is-3 ">Решения</h3>
                        <table className="table">

                            {solutions}
                        </table>


                    </div>
                </div>
            )


        }
    }
}


export default MyTeamGet