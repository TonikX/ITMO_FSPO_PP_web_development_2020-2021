import React from 'react'
import Load from "./load";

class AddSolution extends React.Component {
    constructor(props) {
               super(props)

        this.state = {
            loading: false,
            solutionLink: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    handleChange(e) {
        console.log([e.target.name])
        console.log(e.target.value)
        this.setState({
            [e.target.name]: e.target.value
        })
    }

    handleSubmit(event) {

        event.preventDefault();
        alert('Создано решение: ' + this.props.issue);
        fetch('/hack/solution/create', {
            method: 'POST',
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token'),
                'Content-Type': 'application/json;charset=UTF-8'
            },
            body: JSON.stringify({
                team: this.props.team_id, issue: this.props.task['id'], solutionLink: this.state.solutionLink, pubDate: new Date().toLocaleDateString(),
                comment: null, score: null, jury: null,  checkDate: null
            })
        }).then(r => {
            if (Math.floor(r.status / 100) === 2) {
                this.props.reload_issues()
            } else
                alert("Ошибка")
        })

    }

    render() {
        if (this.state.loading)
            return <Load/>
        return (
            <form onSubmit={this.handleSubmit}>
                <div className="field">
                    <label className="label">Ссылка на решение</label>
                    <div className="control">
                        <input className="input" type="text" name="solutionLink" onChange={this.handleChange}/>
                    </div>
                </div>

                <div className="control">
                    <button className="button is-primary">Добавить</button>
                </div>
            </form>
        );
    }
}
export  default AddSolution;