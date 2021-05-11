import React from 'react'
import ReactDOM from 'react-dom'

import delete_img from './delete.svg'
import edit_img from './edit.svg'

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'loading': true,
            'data': {
                'units': [],
                'items:': [],
                'manufactures': [],
                'active_substances': []
            }
        }
        this.url = "http://127.0.0.1:8000/"
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

        this.setState({
            'loading': false,
            'data': {
                'units': units,
                'items': items,
                'manufactures': manufactures,
                'active_substances': active_substances
            }
        })
    }

    async componentDidMount() {
        await this.reload_data()
    }

    render() {
        if (this.state.loading) return <span>Loading...</span>
        return <InteractiveTable data={this.state.data}/>
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

        let body
        switch (this.state.selected) {
            case 'units':
                body = this.props.data['units'].map((item) =>
                    [item['item'], item['amount'], item['product_date']])
                break
            case 'items':
                body = this.props.data['items'].map((item) =>
                    [item['name'], item['packaging'], item['active_substance'], item['manufacturer']])
                break
            case 'active_substances':
                body = this.props.data['active_substances'].map((item) =>
                    [item['name']])
                break
            case 'manufactures':
                body = this.props.data['manufactures'].map((item) =>
                    [item['name'], item['country']])
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
                    headers={this.headers[this.state.selected]}
                    body={body}
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