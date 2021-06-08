import React from 'react'
import ReactDOM from 'react-dom'

import delete_img from './delete.svg'
import edit_img from './edit.svg'

function getCSRF() {
    let csrf = document.cookie.match(new RegExp('csrftoken=.{64}'))[0]
    return csrf.substring(10)
}

function create(type, reload) {
    let modal = document.getElementById('modal')
    let modal_box = document.getElementById('modal-box')
    modal_box.innerHTML = ''

    fetch('/api/' + type + '/create/')
        .then(r => r.text().then(html => {
            modal_box.innerHTML = html
            if (type === 'units') {
                let user_id = document.getElementById('id_user')
                user_id.value = 1
                let user_field = user_id.parentElement.parentElement
                user_field.classList.add('is-hidden')
            }
            let submit_button = document.getElementById('submit')
            submit_button.addEventListener('click', (e) => {
                e.preventDefault()
                let form = new FormData(document.querySelector('form'))
                fetch('/api/' + type + '/create/', {
                    method: 'POST',
                    body: form
                })
                    .then(r => {
                        if (r.status === 200) {
                            reload().finally(() => {
                            })
                        } else {
                            alert('Ошибка')
                        }
                    })
                    .finally(() => modal.classList.remove('is-active'))
            })
            let cancel_button = document.getElementById('cancel')
            cancel_button.addEventListener('click', (e) => {
                e.preventDefault()
                modal.classList.remove('is-active')
                modal_box.innerHTML = ''
            })
            modal.classList.add('is-active')
        }))
}

function update(id, type, reload) {
    let modal = document.getElementById('modal')
    let modal_box = document.getElementById('modal-box')
    modal_box.innerHTML = ''

    fetch('/api/' + type + '/update/' + id + '/')
        .then(r => r.text().then(html => {
            modal_box.innerHTML = html
            if (type === 'units') {
                let user_id = document.getElementById('id_user')
                //user_id.value = 1
                let user_field = user_id.parentElement.parentElement
                user_field.classList.add('is-hidden')
            }
            let submit_button = document.getElementById('submit')
            submit_button.innerText = 'Изменить' + submit_button.innerText.slice(8)
            submit_button.addEventListener('click', (e) => {
                e.preventDefault()
                let form = new FormData(document.querySelector('form'))
                fetch('/api/' + type + '/update/' + id + '/', {
                    method: 'POST',
                    body: form
                })
                    .then(r => {
                        if (r.status === 200) {
                            reload().finally(() => {
                            })
                        } else {
                            alert('Ошибка')
                        }
                    })
                    .finally(() => modal.classList.remove('is-active'))
            })
            let cancel_button = document.getElementById('cancel')
            cancel_button.addEventListener('click', (e) => {
                e.preventDefault()
                modal.classList.remove('is-active')
                modal_box.innerHTML = ''
            })
            modal.classList.add('is-active')
        }))
}

function del(id, type, reload) {
    fetch('/api/' + type + '/delete/' + id + '/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRF()
        }
    }).then(r => {
        if (r.status === 200) {
            reload().finally(() => {
            })
        } else {
            alert('Ошибка')
        }
    })
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'loading': true,
            'data': {
                'units': [],
                'items:': [],
                'manufactures': [],
                'active_substances': [],
                'users': []
            }
        }
        this.url = "http://127.0.0.1:8000/"

        this.reload_data = this.reload_data.bind(this)
    }

    async reload_data() {
        let resp

        resp = await fetch(this.url + 'api/manufactures?format=json')
        let manufactures = await resp.json()

        resp = await fetch(this.url + 'api/active-substances?format=json')
        let active_substances = await resp.json()

        resp = await fetch(this.url + 'api/items?format=json')
        let items = await resp.json()

        resp = await fetch(this.url + 'api/units?format=json')
        let units = await resp.json()

        resp = await fetch(this.url + 'api/users?format=json')
        let users = await resp.json()

        this.setState({
            'loading': false,
            'data': {
                'units': units,
                'items': items,
                'manufactures': manufactures,
                'active_substances': active_substances,
                'users': users
            }
        })
    }

    async componentDidMount() {
        await this.reload_data()
    }

    render() {
        if (this.state.loading) return <span>Loading...</span>
        return <InteractiveTable data={this.state.data} reload={this.reload_data}/>
    }
}

class InteractiveTable extends React.Component {
    constructor(props) {
        super(props)
        this.tabs = [
            {'code': 'units', 'name': 'Аптека'},
            {'code': 'items', 'name': 'Препараты'},
            {'code': 'active_substances', 'name': 'Действующие вещества'},
            {'code': 'manufactures', 'name': 'Производители'},
            {'code': 'users', 'name': 'Пользователи'}
        ]
        this.headers = {
            'units': ['Название', 'Количество', 'Дата производства'],
            'items': ['Название', 'Упаковка', 'Действующее вещество', 'Производитель'],
            'active_substances': ['Название'],
            'manufactures': ['Название', 'Страна'],
            'users': ['ID', 'Логин']
        }
        this.state = {
            'selected': 'units'
        }

        this.selectTab = this.selectTab.bind(this)
    }

    selectTab(selected) {
        this.setState({
            'selected': selected
        })
    }

    render() {
        let tabs = [];
        this.tabs.forEach(({code, name}) => {
            tabs.push(<li className={this.state.selected === code ? "is-active" : ""}>
                <a onClick={() => this.selectTab(code)}>
                    {name}
                </a>
            </li>)
        })

        if (this.props.data['users'].length === 0)
            tabs.pop()

        let body
        switch (this.state.selected) {
            case 'units':
                body = this.props.data['units'].map((item) =>
                    [item['id'], item['item'], item['amount'], item['product_date']])
                break
            case 'items':
                body = this.props.data['items'].map((item) =>
                    [item['id'], item['name'], item['packaging'], item['active_substance'], item['manufacturer']])
                break
            case 'active_substances':
                body = this.props.data['active_substances'].map((item) =>
                    [item['id'], item['name']])
                break
            case 'manufactures':
                body = this.props.data['manufactures'].map((item) =>
                    [item['id'], item['name'], item['country']])
                break
            case 'users':
                body = this.props.data['users'].map((item) =>
                    [item['id'], item['id'], item['username']])
                break
        }
        return (
            <>
                <div className="tabs is-boxed mb-1">
                    <ul>
                        {tabs}
                    </ul>
                </div>
                <Table
                    selected={this.state.selected}
                    headers={this.headers[this.state.selected]}
                    body={body}
                    type={this.state.selected}
                    reload={this.props.reload}
                />
                <button className="button is-info is-light"
                        onClick={() => create(this.state.selected, this.props.reload)}>Добавить
                </button>
            </>
        )
    }
}

class ItemRow extends React.Component {
    constructor(props) {
        super(props)
        this.state = 'list'
    }

    render() {
        let columns = []
        this.props.item.forEach((i) => {
            columns.push(<td>{i}</td>)
        })
        return (<tr>
            {columns}
            <td>
                <i className="icon"><img src={edit_img} alt="update" onClick={this.props.update}/></i>
                <i className="icon"><img src={delete_img} alt="delete" onClick={this.props.del}/></i>
            </td>
        </tr>)
    }
}

function Table(props) {
    let table_headers = [];
    props.headers.forEach((header, i) => {
        table_headers.push(<th key={i}>{header}</th>)
    })
    table_headers.push(<th/>)

    let table_body = [];
    props.body.forEach((row, i) => {
        i++
        table_body.push(<ItemRow type={props.selected} pk={row[0]} item={row.slice(1)}
                                 update={() => update(row[0], props.type, props.reload)}
                                 del={() => del(row[0], props.type, props.reload)}/>)
    })

    return (
        <table className="table is-fullwidth mb-1">
            <thead>
            <tr>
                {table_headers}
            </tr>
            </thead>
            <tbody>
            {table_body}
            </tbody>
        </table>
    )
}

ReactDOM.render(<App/>, document.getElementById("app"))