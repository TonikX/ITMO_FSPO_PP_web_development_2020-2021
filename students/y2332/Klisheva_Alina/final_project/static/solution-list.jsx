import React from "react";
import Load from "./load";

class SolutionList extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            loading: true,
            is_editing: -1,
            is_done: false,
            header_edit: true

        }
        fetch('/hack/issue/get/' + this.props.task_id, {
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            }
        }).then(r => r.json().then(json => {
                this.team = json['solutions']
                console.log(this.team)
                this.setState({
                    loading: false
                })
            })
        )
        console.log("dvdd" + this.props.user)
        this.MakeEditAble = this.MakeEditAble.bind(this);
        this.MakeItEditAble = this.MakeItEditAble.bind(this);
        this.EditSolution = this.EditSolution.bind(this);
        this.CheckSolution = this.CheckSolution.bind(this);
    }

    MakeEditAble(e, i) {
        e.preventDefault()
        this.setState(
            {is_editing: i}
        )
    }

    MakeItEditAble(e, i) {
        e.preventDefault()
        this.setState(
            {
                is_editing: i,
                header_edit: !this.state.header_edit
            }
        )
    }

    CheckSolution(e, id, jury) {
        e.preventDefault()
        let form = new FormData()
        form.append('score', document.getElementById("score-input").value)
        form.append('checkDate', new Date().toLocaleDateString())
        form.append('comment', document.getElementById("comment-input").value)
        form.append('jury', this.props.user)
        fetch('/hack/solution/update/' + id, {
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

    EditSolution(e, id) {
        e.preventDefault()
        let form = new FormData()
        form.append('teamName', document.getElementById("teamName-solution").value)
        form.append('score', document.getElementById("score-solution").value)
        form.append('comment', document.getElementById("comment-solution").value)
        form.append('solutionLink', document.getElementById("solutionLink-solution").value)
        console.log(JSON.stringify(Object.fromEntries(form)))
        fetch('/hack/solution/update/' + id, {
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

    render() {
        if (this.state.loading)
            return (
                <Load/>
            )
        else {

            console.log(this.team)
            let solutionslist = []

            let solutionslist1 = []
            if (this.props.editable) {
                solutionslist.push(
                    <>

                        {this.state.header_edit ? <thead>
                            <th>Команда</th>
                            <th>Дата публикации</th>
                            <th>Ссылка на решение</th>
                            </thead>
                            : <thead>
                            <th>Баллы</th>
                            <th>Дата проверки</th>
                            <th>Комментарий</th>
                            </thead>}


                    </>)
                solutionslist.push(
                    <tbody>
                    {this.team.map((team, i) => {
                        return (
                            <>
                                {team['jury'] === null ?
                                    <>
                                        <tr>
                                            {this.state.is_editing === i ?
                                                <td><input id="score-input" className="input" type="int" name="score"
                                                           defaultValue={team['score']}></input></td> :
                                                <td>{team['team']['teamName']}</td>
                                            }
                                            {this.state.is_editing === i ?
                                                <td><input id="checkDate-input" className="input" type="date"
                                                           name="checkDate"
                                                           defaultValue={new Date().toLocaleDateString()}
                                                           readOnly={true}></input></td> :
                                                <td>{team['pubDate']}</td>
                                            }
                                            {this.state.is_editing === i ?
                                                <td><input id="comment-input" className="input" type="text"
                                                           name="comment"
                                                           defaultValue={team['comment']}></input></td> :
                                                <td>{team['solutionLink']}</td>
                                            }


                                            {this.state.is_editing === i ?

                                                <td>
                                                    <button className="button is-danger"
                                                            onClick={(e) => this.MakeItEditAble(e, -1)}>Отменить
                                                    </button>
                                                </td> : <td>
                                                    <button className="button is-primary"
                                                            onClick={(e) => this.MakeItEditAble(e, i)}>Проверить
                                                    </button>
                                                </td>

                                            }
                                            {this.state.is_editing === i ?

                                                <td>
                                                    <button className="button is-primary"
                                                            onClick={(e) => this.CheckSolution(e, team['id'])}>Применить
                                                    </button>
                                                </td> :
                                                <></>

                                            }
                                        </tr>
                                    </>

                                    : <></>
                                }
                            </>)
                    })}
                    </tbody>
                )

                solutionslist1.push(
                    <>
                        <thead>
                        <th>Дата проверки</th>
                        <th>Команда</th>
                        <th>Баллы</th>
                        <th>Дата публикации</th>
                        <th>Комментарий</th>
                        <th>Ссылка на решение</th>
                        <th></th>


                        </thead>
                    </>
                )
                solutionslist1.push(
                    <tbody>
                    {this.team.map((team, i) => {
                        return (<>{team['jury'] != null ?
                                <>{team['jury']['id'] === this.props.user ?

                                    <tr>
                                        {this.state.is_editing === i ?
                                            <td><input id="checkDate-solution" className="input" type="date"
                                                       name="chekDate"
                                                       defaultValue={team['pubDate']}
                                                       readOnly={true}></input></td> :
                                            <td>{team['pubDate']}</td>
                                        }
                                        {this.state.is_editing === i ?
                                            <td><input id="teamName-solution" className="input" type="text"
                                                       name="teamName"
                                                       readOnly={true}
                                                       defaultValue={team['team']['teamName']}></input></td> :
                                            <td>{team['team']['teamName']}</td>
                                        }
                                        {this.state.is_editing === i ?
                                            <td><input id="score-solution" className="input" type="int"
                                                       name="score"
                                                       defaultValue={team['score']}></input></td> :
                                            <td>{team['score']}</td>
                                        }
                                        {this.state.is_editing === i ?
                                            <td><input id="pubDate-solution" className="input" type="date"
                                                       name="pubDate"
                                                       defaultValue={team['pubDate']}
                                                       readOnly={true}></input></td> :
                                            <td>{team['pubDate']}</td>
                                        }
                                        {this.state.is_editing === i ?
                                            <td><input id="comment-solution" className="input" type="text"
                                                       name="comment"
                                                       defaultValue={team['comment']}></input></td> :
                                            <td>{team['comment']}</td>
                                        }
                                        {this.state.is_editing === i ?
                                            <td><input id="solutionLink-solution" className="input" type="text"
                                                       name="solutionLink"
                                                       defaultValue={team['solutionLink']}
                                                       readOnly={true}></input>
                                            </td> :
                                            <td>{team['solutionLink']}</td>
                                        }

                                        {this.state.is_editing === i ?

                                            <td>
                                                <button className="button is-danger"
                                                        onClick={(e) => this.MakeEditAble(e, -1)}>Отменить
                                                </button>
                                            </td>
                                            : <td>
                                                <button className="button is-primary"
                                                        onClick={(e) => this.MakeEditAble(e, i)}>Редактировать
                                                </button>
                                            </td>

                                        }
                                        {this.state.is_editing === i ?

                                            <td>
                                                <button className="button is-primary"
                                                        onClick={(e) => this.EditSolution(e, team['id'])}>Применить
                                                </button>
                                            </td> :
                                            <></>
                                        }
                                    </tr> : <></>}
                                </> : <></>}
                            </>


                        )

                    })}</tbody>
                )
            } else {
                solutionslist.push(
                    <>
                        <thead>

                        <th>Команда</th>
                        <th>Дата публикации</th>
                        <th>Ссылка на решение</th>


                        </thead>
                        <tbody>
                        {this.team.map((team) => {
                            return (
                                <>{team['jury'] === null ?

                                    <tr>
                                        <td>{team['team']['teamName']}</td>
                                        <td>{team['score']}</td>
                                        <td>{team['pubDate']}</td>
                                        <td>{team['comment']}</td>
                                        <td>{team['solutionLink']}</td>
                                    </tr> : <> </>}</>


                            )

                        })
                        }
                        </tbody>
                    </>)

                solutionslist1.push(
                    <>
                        <thead>
                        <th>Дата проверки</th>
                        <th>Команда</th>
                        <th>Баллы</th>
                        <th>Дата публикации</th>
                        <th>Комментарий</th>
                        <th>Ссылка на решение</th>


                        </thead>
                        <tbody>
                        {this.team.map((team) => {
                            return (
                                <>{team['jury'] !== null ?

                                    <tr>
                                        <td>{team['checkDate']}</td>
                                        <td>{team['team']['teamName']}</td>
                                        <td>{team['score']}</td>
                                        <td>{team['pubDate']}</td>
                                        <td>{team['comment']}</td>
                                        <td>{team['solutionLink']}</td>
                                    </tr> : <></>}
                                </>


                            )

                        })}</tbody>
                    </>
                )
            }


            return (
                <div className="Box">
                    <h3 className="title is-3 ">Непроверенные решения</h3>
                    <table className="table">

                        {solutionslist}
                    </table>

                    <h3 className="title is-3">Проверенные решения</h3>
                    <table className="table">

                        {solutionslist1}
                    </table>
                </div>
            )
        }
    }


    }

    export default SolutionList