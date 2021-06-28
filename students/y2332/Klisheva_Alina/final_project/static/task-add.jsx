import React from "react";
import Load from "./load";

class AddTask extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            loading: false,
            name: '',
            condition: '',
            limits: '',
            links: ''
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
        alert('Создано задание: ' + this.state.name);
        console.log(JSON.stringify({
                name: this.state.name, condition: this.state.condition,
                limits: this.state.limits, links: this.state.links
            })
        )
        fetch('/hack/issue/create', {
            method: 'POST',
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token'),
                'Content-Type': 'application/json;charset=UTF-8'
            },
            body: JSON.stringify({
                name: this.state.name, condition: this.state.condition, dateCreate: new Date().toLocaleDateString(),
                limits: this.state.limits, links: this.state.links, solutions: null
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
                    <label className="label">Название</label>
                    <div className="control">
                        <input className="input" type="text" name="name" onChange={this.handleChange}/>
                    </div>
                </div>
                <div className="field">
                    <label className="label">Условие</label>
                    <div className="control">
                        <textarea className="textarea has-fixed-size" type="text" name="condition"
                                  onChange={this.handleChange}/>
                    </div>
                </div>
                <div className="field">
                    <label className="label">Ограничение</label>
                    <div className="control">
                        <textarea className="textarea has-fixed-size" type="text" name="limits"
                                  onChange={this.handleChange}/>
                    </div>
                </div>
                <div className="field">
                    <label className="label">Ссылка</label>
                    <div className="control">
                        <input className="input" type="text" name="links" onChange={this.handleChange}/>
                    </div>
                </div>

                <div className="control">
                    <button className="button is-primary">Создать</button>
                </div>
            </form>
        );
    }
}

export default AddTask