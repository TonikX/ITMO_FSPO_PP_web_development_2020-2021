import React from "react";

class TeamCreate extends React.Component {
    constructor(props) {
        super(props)
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        console.log(this.props.user)
        let form = new FormData(document.getElementById('team-form'))
        form.append('captain', this.props.user)
        fetch('/hack/team/create', {
            method: 'POST',
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token'),
                'Content-Type': 'application/json;charset=UTF-8'
            },
            body: JSON.stringify(Object.fromEntries(form))
        }).then(r => {
            if (Math.floor(r.status / 100) === 2) {
                this.props.reload_issues()
            } else
                alert("Ошибка")
        })
    }

    render() {
        return (
            <div className="Box">
                <form id="team-form" onSubmit={this.handleSubmit}>
                    <div className="field">
                        <div className="control">
                            <label className="label">Название: </label>
                            <input className="input" type="text" name="teamName"/>
                        </div>
                    </div>
                    <div className="field">
                        <div className="control">
                            <label className="label">Девиз: </label>
                            <input className="input" type="text" name="motto"/>

                        </div>
                    </div>
                    <div className="control">
                        <button className="button is-primary">Создать</button>
                    </div>
                </form>
            </div>
        )
    }
}

export default TeamCreate