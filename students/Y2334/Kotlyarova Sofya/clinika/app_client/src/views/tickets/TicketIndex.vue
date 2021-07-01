<template>
    <div>
        <v-alert type="error" v-model="is_error" dismissible>
            Error
        </v-alert>
        <v-data-table
            :items="tickets"
            :headers="headers"
            :items-per-page="10"
        >
            <template v-slot:top>
                <v-toolbar flat>
                    <v-toolbar-title>Tickets</v-toolbar-title>
                    <v-divider
                        class="mx-4"
                        inset
                        vertical
                    ></v-divider>
                    <v-spacer></v-spacer>
                    <v-dialog
                        v-model="dialog"
                        max-width="500px"
                    >
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                                color="primary"
                                dark
                                class="mb-2"
                                v-bind="attrs"
                                v-on="on"
                            >
                                New
                            </v-btn>
                        </template>
                        <v-card>
                            <v-card-title>
                                <span class="text-h5">{{ formTitle }}</span>
                            </v-card-title>

                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col>
                                            <v-select
                                                :items="clients"
                                                v-model="editedItem.client"
                                                label="Client"
                                                item-text="name"
                                                item-value="id"
                                            ></v-select>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <v-select
                                                :items="doctor_services"
                                                v-model="editedItem.doctor_service"
                                                label="Doctor service"
                                                item-value="id"
                                            >
                                                <template slot="selection" slot-scope="data">
                                                    {{ data.item.doctor.name + ' - ' + data.item.service.name }}
                                                </template>
                                                <template slot="item" slot-scope="data">
                                                    {{ data.item.doctor.name + ' - ' + data.item.service.name }}
                                                </template>
                                            </v-select>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <template>
                                                <v-row justify="center">
                                                    <v-date-picker v-model="editedItem.when"></v-date-picker>
                                                </v-row>
                                            </template>
                                        </v-col>
                                    </v-row>
                                </v-container>
                            </v-card-text>

                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn
                                    color="blue darken-1"
                                    text
                                    @click="close"
                                >
                                    Cancel
                                </v-btn>
                                <v-btn
                                    color="blue darken-1"
                                    text
                                    @click="save"
                                >
                                    Save
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                    <v-dialog v-model="dialogDelete" max-width="500px">
                        <v-card>
                            <v-card-title class="text-h5">Delete item?</v-card-title>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                                <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                                <v-spacer></v-spacer>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                </v-toolbar>
            </template>
            <template v-slot:item.when="{ item }">
                {{ new Date(item.when).toDateString() }}
            </template>
            <template v-slot:item.client="{ item }">
                <v-chip
                    :color="getColor(item)"
                    dark
                >
                    {{ item.client !== null ? item.client.name : 'Свободно' }}
                </v-chip>
            </template>
            <template v-slot:item.actions="{ item }">
                <v-icon
                    small
                    class="mr-2"
                    @click="editItem(item)"
                >
                    mdi-pencil
                </v-icon>
                <v-icon
                    small
                    @click="deleteItem(item)"
                >
                    mdi-delete
                </v-icon>
            </template>
        </v-data-table>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            is_error: false,

            dialog: false,
            dialogDelete: false,

            editedIndex: -1,
            editedItem: {
                client: {
                    id: '',
                    name: ''
                },
                doctor_service: {
                    id: '',
                    doctor: {
                        id: '',
                        name: ''
                    },
                    service: {
                        id: '',
                        name: ''
                    },
                    price: ''
                },
                when: ''
            },
            defaultItem: {
                client: {
                    id: '',
                    name: ''
                },
                doctor_services: {
                    id: '',
                    doctor: {
                        id: '',
                        name: ''
                    },
                    service: {
                        id: '',
                        name: ''
                    },
                    price: ''
                },
                when: ''
            },

            headers: [
                { text: 'ID', value: 'id' },
                { text: 'Client', value: 'client' },
                { text: 'Doctor', value: 'doctor_service.doctor.name' },
                { text: 'Service', value: 'doctor_service.service.name' },
                { text: 'Price', value: 'doctor_service.price' },
                { text: 'When', value: 'when' },
                { text: 'Actions', value: 'actions', sortable: false },
            ],

            tickets: [],
            clients: [],
            doctor_services: []
        }
    },

    computed: {
        formTitle() {
            return this.editedIndex === -1 ? 'Create client' : 'Edit client'
        },
    },

    created() {
        axios.get('http://127.0.0.1:8000/api/tickets')
            .then(response => {
                console.log('[axois - get] Success');
                this.tickets = response.data;
            })
            .catch(response => {
                console.log('[axois - get] Error');
            })

        axios.get('http://127.0.0.1:8000/api/doctor-services')
            .then(response => {
                console.log('[axois - get] Success');
                this.doctor_services = response.data;
            })
            .catch(response => {
                console.log('[axois - get] Error');
            })

        axios.get('http://127.0.0.1:8000/api/clients')
            .then(response => {
                console.log('[axois - get] Success');
                this.clients = response.data;
            })
            .catch(response => {
                console.log('[axois - get] Error');
            })
    },

    watch: {
        dialog(val) {
            val || this.close()
        },
        dialogDelete (val) {
            val || this.closeDelete()
        },
    },

    methods: {
        getColor(item) {
            return item.client !== null ? 'red' : 'green';
        },

        close() {
            this.dialog = false
            this.$nextTick(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },

        deleteItem (item) {
            this.editedIndex = this.tickets.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialogDelete = true
        },

        deleteItemConfirm () {
            axios.delete('http://127.0.0.1:8000/api/tickets/' + this.editedItem.id + '/')
                .then(response => {
                    console.log('[axois - delete] Success');
                    this.tickets.splice(this.editedIndex, 1)
                    this.closeDelete()
                }).catch(response => {
                    console.log('[axois - delete] Error');
                })
        },

        closeDelete () {
            this.dialogDelete = false
            this.$nextTick(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },

        editItem(item) {
            this.editedIndex = this.tickets.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialog = true
        },

        save() {
            // console.log(this.editedItem);

            if (this.editedIndex > -1) {
                axios.put('http://127.0.0.1:8000/api/tickets/' + this.editedItem.id + '/', {
                }).then(response => {
                    console.log('[axois - put] Success');

                    // Object.assign(this.tickets[this.editedIndex], this.editedItem)
                    // this.close();
                }).catch(response => {
                    console.log('[axois - put] Error');
                    // this.is_error = true;
                    // this.close();
                })
            } else {
                console.log(this.editedItem.client);

                axios.post('http://127.0.0.1:8000/api/tickets/', {
                    client: this.editedItem.client.id === undefined ? this.editedItem.client : null,
                    doctor_service: this.editedItem.doctor_service,
                    when: this.editedItem.when
                }).then(response => {
                    console.log('[axois - post] Success');

                    let item = {};

                    if (response.data.client === null)
                    {
                        item.client = null;
                    }
                    else
                    {
                        item.client = this.clients.filter(
                            c => { return c.id === response.data.client; }
                        )[0];
                    }
                    item.doctor_service = this.doctor_services.filter(
                        ds => { return ds.id === response.data.doctor_service; }
                    )[0];
                    item.when = response.data.when;
                    item.id = response.data.id;

                    this.tickets.push(item);
                    this.close();

                    this.editedItem
                }).catch(response => {
                    console.log('[axois - post] Error');
                    this.is_error = true;
                    this.close();
                })
            }
        },
    }
}
</script>