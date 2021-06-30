import React from 'react'
import Load from "./load";

class AddMember extends React.Component {
    constructor(props) {
               super(props)

        this.state = {
            loading: false,
            solutionLink: '',
            role: 1,
            fio: '',
            phoneNumber: ''
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
        alert('Добавлен участник: ' + this.state.name);
        console.log(JSON.stringify({
                team: this.props.team, fio: this.state.fio,
                role: this.state.role, phoneNumber: this.state.phoneNumber
            })
        )
        fetch('/hack/member/create', {
            method: 'POST',
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token'),
                'Content-Type': 'application/json;charset=UTF-8'
            },
            body: JSON.stringify({
                team: this.props.team, fio: this.state.fio,
                role: this.state.role, phoneNumber: this.state.phoneNumber
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
                    <label className="label">ФИО</label>
                    <div className="control">
                        <input className="input" type="text" name="fio" onChange={this.handleChange}/>
                    </div>
                </div>
                <div className="field">
                    <label className="label">Роль</label>
                    <div className="control">
                        <div className="select" name="role" onChange={this.handleChange}>
                            <select>
                                <option value="1">Developer</option>
                                <option value="2">Designer</option>
                                <option value="3">Entrepreneur</option>
                            </select>
                        </div>
                    </div>
                </div>

                <div className="field">
                    <label className="label">Номер телефона</label>
                    <div className="control">
                        <input className="input" type="tel" name="phoneNumber" onChange={this.handleChange}/>
                    </div>
                </div>


                <div className="control">
                    <button className="button is-primary">Добавить</button>
                </div>
            </form>
        );
    }
}
export  default AddMember;