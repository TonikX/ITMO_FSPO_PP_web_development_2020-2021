import React from "react";
import Load from "./load";

class SolutionList extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            loading: true,
            is_editing: false,
            is_done: false

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
        this.MakeEditAble = this.MakeEditAble.bind(this);
        this.EditSolution = this.EditSolution.bind(this);
    }

    MakeEditAble(e) {
        e.preventDefault()
        this.setState((state) => {
            return {is_editing: !state.is_editing}
        })
    }
    EditSolution(e, id){
        e.preventDefault()
        fetch('/hack/solution/update/' + id, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            },
            body: JSON.stringify(Object.fromEntries(new FormData(document.getElementById('solution-form'))))
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
                    <tbody>
                    <thead>

                    <th>Команда</th>
                    <th>Дата публикации</th>
                    <th>Ссылка на решение</th>


                    </thead>
                    {this.team.map((team) => {
                        return (
                            <div>{team['jury'] === null ?

                                <tr>
                                    <td>{team['team']['teamName']}</td>
                                    <td>{team['score']}</td>
                                    <td>{team['pubDate']}</td>
                                    <td>{team['comment']}</td>
                                    <td>{team['solutionLink']}</td>
                                    {!this.state.is_editing ? <button className="button is-danger"
                                                                      onClick={(e) => this.deleteSolution(e, team['id'])}>Проверить
                                    </button> : <button className="button is-primary"
                                                        onClick={(e) => this.deleteSolution(e, team['id'])}>Отменить
                                    </button>}
                                </tr> : <> </>}</div>


                        )

                    })}</tbody>)

                solutionslist1.push(
                    <tbody>
                    <thead>

                    <th>Команда</th>
                    <th>Баллы</th>
                    <th>Дата публикации</th>
                    <th>Комментарий</th>
                    <th>Ссылка на решение</th>
                    <th></th>


                    </thead>
                    {this.team.map((team) => {
                        return (
                            <div>{team['jury'] !== null ?

                                <tr>
                                    <form id="solution-from">
                                    {this.state.is_editing ?
                                        <td><input className="input" type="text" name="teamName" readOnly={true}
                                                   defaultValue={team['team']['teamName']}></input></td> :
                                        <td>{team['team']['teamName']}</td>
                                    }
                                    {this.state.is_editing ? <td><input className="input" type="int" name="score"
                                                                        defaultValue={team['score']}></input></td> :
                                        <td>{team['score']}</td>
                                    }
                                    {this.state.is_editing ? <td><input className="input" type="date" name="pubDate"
                                                                        defaultValue={team['pubDate']}
                                                                        readOnly={true}></input></td> :
                                        <td>{team['pubDate']}</td>
                                    }
                                    {this.state.is_editing ?
                                        <td><input className="input" type="text" name="comment"
                                                   defaultValue={team['comment']}></input></td> :
                                        <td>{team['comment']}</td>
                                    }
                                    {this.state.is_editing ?
                                        <td><input className="input" type="text" name="solutionLink"
                                                   defaultValue={team['solutionLink']} readOnly={true}></input>
                                        </td> :
                                        <td>{team['pubDate']}</td>
                                    }

                                    {!this.state.is_editing ?

                                        <button className="button is-primary"
                                                onClick={(e) => this.MakeEditAble(e)}>Редактировать
                                        </button>
                                        :
                                        <button className="button is-danger"
                                                onClick={(e) => this.MakeEditAble(e)}>Отменить
                                        </button>
                                    }
                                    {!this.state.is_editing ?

                                        <></>
                                        :
                                        <button className="button is-danger"
                                                onClick={(e) => this.EditSolution(e)}>Применить
                                        </button>
                                    }</form>
                                </tr> : <></>}
                            </div>


                        )

                    })}</tbody>)
            } else {
                solutionslist.push(
                    <tbody>
                    <thead>

                    <th>Команда</th>
                    <th>Дата публикации</th>
                    <th>Ссылка на решение</th>


                    </thead>
                    {this.team.map((team) => {
                        return (
                            <div>{team['jury'] === null ?

                                <tr>
                                    <td>{team['team']['teamName']}</td>
                                    <td>{team['score']}</td>
                                    <td>{team['pubDate']}</td>
                                    <td>{team['comment']}</td>
                                    <td>{team['solutionLink']}</td>
                                </tr> : <> </>}</div>


                        )

                    })}</tbody>)
                solutionslist1.push(
                    <tbody>
                    <thead>

                    <th>Команда</th>
                    <th>Баллы</th>
                    <th>Дата публикации</th>
                    <th>Комментарий</th>
                    <th>Ссылка на решение</th>


                    </thead>
                    {this.team.map((team) => {
                        return (
                            <div>{team['jury'] !== null ?

                                <tr>
                                    <td>{team['team']['teamName']}</td>
                                    <td>{team['score']}</td>
                                    <td>{team['pubDate']}</td>
                                    <td>{team['comment']}</td>
                                    <td>{team['solutionLink']}</td>
                                </tr> : <></>}
                            </div>


                        )

                    })}</tbody>
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
                </div>)
        }
    }


}

export default SolutionList