import React from "react";
import Load from "./load";
import AddSolution from "./add-solution";

class Task extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            loading: true,
            is_editing: false,
            is_addable: false
        }

        fetch('/hack/issue/get/' + this.props.task_id, {
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            }
        }).then(r => r.json().then(json => {
                this.task = json
                this.setState({
                    loading: false
                })
            })
        )

        this.makeTaskEditable = this.makeTaskEditable.bind(this);
        this.editTask = this.editTask.bind(this);
        this.deleteTask = this.deleteTask.bind(this);
        this.addSolution = this.addSolution.bind(this);
    }

    makeTaskEditable(e) {
        e.preventDefault()
        this.setState((state) => {
            return {is_editing: !state.is_editing}
        })
    }

    editTask(e) {
        e.preventDefault()
        fetch('/hack/issue/update/' + this.task['id'], {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            },
            body: JSON.stringify(Object.fromEntries(new FormData(document.getElementById('task-form'))))
        }).then(r => {
            if (r.status === 200) {
                this.props.reload_issues()
            } else {
                alert('Ошибка')
            }
        })
    }

    deleteTask(e) {
        e.preventDefault()
        fetch('/hack/issue/delete/' + this.props.task_id, {
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

    addSolution(e) {
        e.preventDefault()
        this.setState((state) => {
            return {is_addable: !state.is_addable}
        })
        console.log(this.props.team_id)
    }


    render() {
        if (this.state.loading)
            return <Load/>
        if (this.props.addable)
            return (<div className="box">
                <h3 className="title is-3">{this.task['name']}</h3>
                <p>Описание: {this.task['condition']}</p>
                <p>Дата публикации: {this.task['dateCreate']}</p>
                <p>Ограничения: {this.task['limits']}</p>
                <a href={this.task['links']}>Ссылка</a>
                <div>
                    <button className="button is-primary" onClick={(e) => this.addSolution(e)}>Добавить решение</button>
                </div>
                {this.state.is_addable ?
                    <AddSolution
                        task={this.task}
                        team_id={this.props.team_id}
                    reload_issues={this.props.reload_issues}/> : <></>}

            </div>)
        if (this.props.editable)
            return (
                (<div className="box">
                    <form id="task-form">
                        <div className="field">
                            {this.state.is_editing ? <label className="label">Название</label> : <></>}
                            <div className="control">
                                {this.state.is_editing ?
                                    <input className="input" type="text" name="name" defaultValue={this.task['name']}/>
                                    : <h3 className="title is-3">{this.task['name']}</h3>}
                            </div>
                        </div>
                        <div className="field">
                            <label className="label">Условие</label>
                            <div className="control">
                                {this.state.is_editing ?
                                    <textarea className="textarea has-fixed-size" type="text" name="condition"
                                              defaultValue={this.task['condition']}/>
                                    : this.task['condition']}
                            </div>
                        </div>
                        <div className="field">
                            <label className="label">Ограничения</label>
                            <div className="control">
                                {this.state.is_editing ?
                                    <textarea className="textarea has-fixes-size" type="text" name="limits"
                                              defaultValue={this.task['limits']}/>
                                    : this.task['limits']}
                            </div>
                        </div>
                        <div className="field">
                            <label className="label">Ссылка</label>
                            <div className="control">
                                {this.state.is_editing ?
                                    <input className="input" type="text" name="links"
                                           defaultValue={this.task['links']}/>
                                    : this.task['links']}
                            </div>
                        </div>
                        <div className="field is-grouped">
                            <div className="control">
                                {this.state.is_editing ?
                                    <button className="button is-info"
                                            onClick={(e) => this.editTask(e)}>Применить</button>
                                    : <button className="button is-primary"
                                              onClick={(e) => this.makeTaskEditable(e)}>Редактировать</button>}
                            </div>
                            <div className="control">
                                {this.state.is_editing ?
                                    <button className="button is-danger"
                                            onClick={(e) => this.makeTaskEditable(e)}>Отменить</button> :
                                    <button className="button is-danger"
                                            onClick={(e) => this.deleteTask(e)}>Удалить</button>}
                            </div>
                        </div>
                    </form>
                </div>)

            )
        return (<div className="box">
            <h3 className="title is-3">{this.task['name']}</h3>
            <p>Описание: {this.task['condition']}</p>
            <p>Дата публикации: {this.task['dateCreate']}</p>
            <p>Ограничения: {this.task['limits']}</p>
            <a href={this.task['links']}>Ссылка</a>
        </div>)

    }

}


export default Task