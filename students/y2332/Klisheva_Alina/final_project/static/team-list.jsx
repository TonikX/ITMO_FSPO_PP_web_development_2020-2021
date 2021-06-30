import React from 'react'
import Load from "./load";

class TeamsList extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
            loading: true,
        }

        fetch('/hack/team/list', {
            headers: {
                'Authorization': 'Token ' + sessionStorage.getItem('token')
            }
        }).then(r => r.json().then(json => {
                this.teams = json

                this.setState({
                    loading: false
                })
            })
        )
    }

    render() {
        if (this.state.loading)
            return (
                <Load/>
            )
        else {
            let teams = []
            teams.push(<thead>
            <tr>
                <th>Команда</th>
                <th>Командир</th>
                <th>К-во решений</th>
            </tr>
            </thead>)
            teams.push(
                <tbody>
                {this.teams.map((team) => {
                        return (
                            <tr>
                                <td>{team['teamName']}</td>
                                <td>{team['captain']['email']}</td>
                                <td>{team['solutions'].length}</td>
                                {/*<td>{team['solutions'].forEach((team) => {sum += team['score']}}</td>*/}
                            </tr>
                        )
                    }
                )}
                </tbody>)
            return <table className="table">
                {teams}
            </table>
        }
    }
}

export default TeamsList