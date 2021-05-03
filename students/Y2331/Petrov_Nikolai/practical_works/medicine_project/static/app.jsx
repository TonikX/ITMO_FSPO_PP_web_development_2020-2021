import React from 'react'
import ReactDOM from 'react-dom'

import delete_img from './delete.svg'
import edit_img from './edit.svg'

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'loading': true
        }
        this.url = "http://127.0.0.1:8000/"
    }

    async componentDidMount() {
        let resp;

        resp = await fetch(this.url + 'api/manufactures?format=json')
        let manufactures = await resp.json()

        resp = await fetch(this.url + 'api/active-substances?format=json')
        let active_substances = await resp.json()

        resp = await fetch(this.url + 'api/items?format=json')
        let items = await resp.json()

        resp = await fetch(this.url + 'api/units?format=json')
        let units = await resp.json()

        this.setState({
            'loading': false,
            'data': {
                'items': items.map((item) =>
                    [item['name'], item['packaging'], item['active_substance'], item['manufacturer']]),
                'active_substances': active_substances.map((item) =>
                    [item['name']]
                ),
                'manufactures': manufactures.map((item) =>
                    [item['name'], item['country']]
                ),
                'units': units.map((item) =>
                    [item['item'], item['amount'], item['product_date']]
                )
            }
        })
    }

    render() {
        if (this.state.loading) return <span>Loading...</span>
        return <InteractiveTable items={this.state.data}/>
    }
}

class InteractiveTable extends React.Component {
    constructor(props) {
        super(props)
        this.tabs = [
            {'code': 'units', 'name': 'Аптека'},
            {'code': 'items', 'name': 'Препараты'},
            {'code': 'active_substances', 'name': 'Действующие вещества'},
            {'code': 'manufactures', 'name': 'Производители'}
        ]
        this.headers = {
            'units': ['Название', 'Количество', 'Дата производства'],
            'items': ['Название', 'Упаковка', 'Действующее вещество', 'Производитель'],
            'active_substances': ['Название'],
            'manufactures': ['Название', 'Страна'],
        }
        this.state = {
            'selected': 'items'
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
        return (
            <>
                <div className="tabs is-boxed mb-1">
                    <ul>
                        {tabs}
                    </ul>
                </div>
                <Table
                    headers={this.headers[this.state.selected]}
                    body={this.props.items[this.state.selected]}
                />
                <button className="button is-info is-light">Добавить</button>
            </>
        )
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
        let table_row = []
        row.forEach((item, y) => {
            table_row.push(<td key={(i << 8) + y}>{item}</td>)
        })
        table_row.push(<td><img src={edit_img} alt="edit"/> <img src={delete_img} alt="delete"/></td>)
        table_body.push(<tr key={i}>{table_row}</tr>)
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