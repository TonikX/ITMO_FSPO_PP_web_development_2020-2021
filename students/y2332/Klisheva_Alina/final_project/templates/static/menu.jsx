import React from "react";
import {ADMIN, CAPTAIN, JURI} from "./roles";

function MenuLabel(props) {
    return (
        <p className="menu-label">
            {props.name}
        </p>
    )
}

function MenuListItem(props) {
    return (
        <li>
            <a className={props.selected_section === props.section_code ? "is-active" : ""}
               onClick={() => props.set_section(props.section_code)}>
                {props.name}
            </a>
        </li>
    )
}

class Menu extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let menu = []
        const is_admin = ADMIN === this.props.role
        const is_captain = CAPTAIN === this.props.role
        const is_juri = JURI === this.props.role
        if (is_admin || is_juri) {

            menu.push(<MenuLabel key="teams" name="Команды"/>)
            menu.push(<ul key="teams-list" className="menu-list">
                    <MenuListItem key="team-list-label" section_code={"teams"} name="Список"
                                  selected_section={this.props.selected_section}
                                  set_section={this.props.set_section}/>
                </ul>
            )
        }
        if (is_captain)
            menu.push(
                <MenuLabel key="my-teams" name="Личный кабинет"/>,
                <ul key="my-team-list" className="menu-list">
                    <MenuListItem key="my-team-list-label" section_code={"my-teams"} name="Моя команда"
                                  selected_section={this.props.selected_section}
                                  set_section={this.props.set_section}/>
                </ul>
            )
        let tasks = this.props.issues.map((task, i) => {
            return <MenuListItem key={"task-" + i} section_code={'task ' + task['id']} name={task['name']}
                                 selected_section={this.props.selected_section}
                                 set_section={this.props.set_section}/>
        })
        if (is_admin)
            tasks.push(<MenuListItem key="task-add" section_code={"task-add"} name="Добавить задачу"
                                     selected_section={this.props.selected_section}
                                     set_section={this.props.set_section}/>)
        menu.push(<MenuLabel key="tasks" name="Задачи"/>)
        menu.push(<ul key="tasks-list" className="menu-list">{tasks}</ul>)
        if (is_admin || is_juri) {
            let tasks = this.props.issues.map((task, i) => {
                return <MenuListItem key={"solution-" + i} section_code={'solution ' + task['id']} name={task['name']}
                                     selected_section={this.props.selected_section}
                                     set_section={this.props.set_section}/>
            })
            menu.push(<MenuLabel key="solutions" name="Решения"/>)
            menu.push(<ul key="solutions-list" className="menu-list">{tasks}</ul>)

        }

        return (
            <aside key="menu-root" className="menu">
                {menu}
            </aside>
        )
    }

}

export default Menu