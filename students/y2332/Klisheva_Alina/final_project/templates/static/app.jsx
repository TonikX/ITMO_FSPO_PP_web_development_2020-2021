import React from 'react'
import ReactDOM from 'react-dom'
import Menu from "./menu";
import TeamsList from "./team-list"
import TeamEdit from "./team-edit"
import Task from "./task";
import Load from "./load";
import AddTask from "./task-add";
import SolutionList from "./solution-list";

import MyTeamGet from "./myteam-list";
import {ADMIN, CAPTAIN, JURI} from "./roles";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loading_queue: 0,
            selected_section: 'unset',
            issues: []
        }

        this.state.loading_queue++
        fetch('/auth/users/me/', {
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            }
        }).then(r => {
                if (r.status === 200)
                    r.json().then(json => {
                            this.role = parseInt(json['role'])
                            console.log(this.role)
                            this.user = parseInt(json['id'])
                            if (this.role == 1) {
                                fetch('/hack/captain/get/' + parseInt(json['id']), {
                                    headers: {
                                        'Authorization': 'Token ' + sessionStorage.getItem('token')
                                    }
                                }).then(r => r.json().then(json => {

                                        this.team_id = parseInt(json['team']['id'])
                                        console.log(team_id)
                                    })
                                )

                            }
                            this.load_change(-1)
                        }
                    )
                else
                    document.location = '/hack/login/'
            }
        )

        this.state.loading_queue++
        this.load_issues()

        this.load_issues = this.load_issues.bind(this)
        this.reload_issues = this.reload_issues.bind(this)
        this.set_section = this.set_section.bind(this)
    }

    load_issues() {
        fetch('/hack/issue/list', {
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            }
        }).then(r => r.json().then(json => {
                this.setState({
                    selected_section: 'unset',
                    issues: json
                })
                this.load_change(-1)
            })
        )
    }


    reload_issues() {
        this.load_change(1)
        this.load_issues()
    }

    load_change(v) {
        this.setState((state) => {
            return {loading_queue: state.loading_queue + v}
        })
    }

    set_section(code) {
        this.setState({
            selected_section: code
        })
    }

    render() {
        if (this.state.loading_queue === 0)
            return (
                <div key="columns" className="columns">
                    <div key="menu-column" className="column is-narrow">
                        <Menu
                            role={this.role}
                            issues={this.state.issues}
                            reload_issues={this.reload_issues}
                            selected_section={this.state.selected_section}
                            set_section={this.set_section}
                        />
                    </div>
                    <div key="section-column" className="column">
                        <Section reload_issues={this.reload_issues} role={this.role}
                                 section_code={this.state.selected_section}
                                 user={this.user} team_id={this.team_id}/>
                    </div>
                </div>
            )
        else
            return <Load/>
    }
}

class Section extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let tmp = this.props.section_code.split(' ')
        let code = tmp[0]
        let index = tmp[1]
        console.log(code, index)
        if (code === 'task') {
            return <Task
                team_id={this.props.team_id}
                key={this.props.section_code}
                task_id={parseInt(index)}
                reload_issues={this.props.reload_issues}
                editable={this.props.role === ADMIN
                }
                addable={this.props.role === CAPTAIN}
                user={this.props.user}
            />
        }
        console.log(code)
        if (code === 'task-add') {
            return <AddTask
                key={this.props.section_code} reload_issues={this.props.reload_issues}/>
        }
        console.log(this.props.user)
        switch (code) {
            case 'unset':
                return <p>Выберите пункт в меню</p>
            case 'teams':
                return <TeamsList/>
            case 'my-teams':
                return <MyTeamGet
                    reload_issues={this.props.reload_issues}
                    user={this.props.user}/>
            case 'team-edit':
                return <TeamEdit/>
            case 'solution':
                return <SolutionList task_id={parseInt(index)}
                                     key={this.props.section_code}
                                     editable={this.props.role === JURI}/>
            default:
                return <p>Недореализовали(((</p>
        }
    }
}

ReactDOM.render(<App/>, document.getElementById("app"))