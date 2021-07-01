<template>
    <div>
        <v-alert type="error" v-model="is_error" dismissible>
            Error
        </v-alert>
        <v-data-table
            :items="doctor_services"
            :headers="headers"
            :items-per-page="10"
        >
            <template v-slot:top>
                <v-toolbar flat>
                    <v-toolbar-title>Doctor services</v-toolbar-title>
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
                                                :items="services"
                                                v-model="editedItem.service.id"
                                                label="Service"
                                                item-text="name"
                                                item-value="id"
                                            ></v-select>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <v-select
                                                :items="doctors"
                                                v-model="editedItem.doctor.id"
                                                label="Doctor"
                                                item-text="name"
                                                item-value="id"
                                            ></v-select>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <v-text-field
                                                label="Price"
                                                v-model="editedItem.price"
                                            ></v-text-field>
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
                </v-toolbar>
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
                    id: '',
                    price: '',
                    doctor: {
                        id: '',
                    },
                    service: {
                        id: '',
                    }
                },

                defaultItem: {
                    price: '',
                    doctor: {
                        id: '',
                    },
                    service: {
                        id: '',
                    }
                },

                headers: [
                    {text: 'ID', value: 'id'},
                    {text: 'Price', value: 'price'},
                    {text: 'Doctor name', value: 'doctor.name'},
                    {text: 'Service name', value: 'service.name'},
                    {text: 'Actions', value: 'actions', sortable: false},
                ],
                doctor_services: [],
                doctors: [],
                services: []
            }
        },

        computed: {
            formTitle() {
                return this.editedIndex === -1 ? 'Create doctor-service' : 'Edit doctor-service'
            },
        },

        watch: {
            dialog(val) {
                val || this.close()
            },
        },

        created() {
            axios.get('http://127.0.0.1:8000/api/doctor-services')
                .then(response => {
                    console.log('[axois - get] Success');
                    this.doctor_services = response.data;
                })
                .catch(response => {
                    console.log('[axois - get] Error');
                })

            axios.get('http://127.0.0.1:8000/api/doctors')
                .then(response => {
                    console.log('[axois - get] Success');
                    this.doctors = response.data;
                })
                .catch(response => {
                    console.log('[axois - get] Error');
                })

            axios.get('http://127.0.0.1:8000/api/services')
                .then(response => {
                    console.log('[axois - get] Success');
                    this.services = response.data;
                })
                .catch(response => {
                    console.log('[axois - get] Error');
                })
        },

        methods: {
            close() {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            },

            editItem(item) {
                this.editedIndex = this.doctor_services.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.dialog = true
            },

            save() {
                if (this.editedIndex > -1) {
                    axios.put('http://127.0.0.1:8000/api/doctor-services/' + this.editedItem.id + '/', {
                        price: this.editedItem.price,
                        doctor: this.editedItem.doctor.id,
                        service: this.editedItem.service.id
                    }).then(response => {
                        console.log('[axois - put] Success');

                        this.doctor_services[this.editedIndex].price = response.data.price;

                        this.doctor_services[this.editedIndex].doctor.id = response.data.doctor;
                        this.doctor_services[this.editedIndex].service.id = response.data.service;

                        this.doctor_services[this.editedIndex].doctor.name = this.doctors.filter(
                            d => { return d.id === response.data.doctor}
                        )[0].name;
                        this.doctor_services[this.editedIndex].service.name = this.services.filter(
                            s => { return s.id === response.data.service}
                        )[0].name;

                        this.close();
                    }).catch(response => {
                        console.log('[axois - put] Error');
                        this.is_error = true;
                        this.close();
                    })
                } else {
                    axios.post('http://127.0.0.1:8000/api/doctor-services/', {
                        price: this.editedItem.price,
                        doctor: this.editedItem.doctor.id,
                        service: this.editedItem.service.id
                    }).then(response => {
                        console.log('[axois - post] Success');

                        let item = {
                            id: response.data.id,
                            price: response.data.price,
                            doctor: {
                                id: response.data.doctor,
                                name: this.doctors.filter(d => { return d.id === response.data.doctor})[0].name
                            },
                            service: {
                                id: response.data.service,
                                name: this.services.filter(s => { return s.id === response.data.service})[0].name
                            }
                        };
                        console.log(item);

                        this.editedItem.id = item.id;
                        this.doctor_services.push(item);
                        this.close();
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