<template>
    <div>
        <v-alert type="error" v-model="is_error" dismissible>
            Error
        </v-alert>
        <v-data-table
            :items="doctors"
            :headers="headers"
            :items-per-page="10"
        >
            <template v-slot:top>
                <v-toolbar flat>
                    <v-toolbar-title>Doctors</v-toolbar-title>
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
                                            <v-text-field
                                                v-model="editedItem.name"
                                                label="name"
                                                counter
                                                maxlength="64"
                                            ></v-text-field>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <v-text-field
                                                v-model="editedItem.phone"
                                                label="phone"
                                                counter
                                                maxlength="12"
                                            ></v-text-field>
                                        </v-col>
                                    </v-row>
                                    <v-row>
                                        <v-col>
                                            <v-text-field
                                                v-model="editedItem.speciality"
                                                label="speciality"
                                                counter
                                                maxlength="64"
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
                name: '',
                phone: '',
                speciality: ''
            },
            defaultItem: {
                name: '',
                phone: '',
                speciality: ''
            },

            headers: [
                {text: 'ID', value: 'id'},
                {text: 'Name', value: 'name'},
                {text: 'Phone', value: 'phone'},
                {text: 'Speciality', value: 'speciality'},
                {text: 'Actions', value: 'actions', sortable: false},
            ],
            doctors: []
        }
    },

    computed: {
        formTitle() {
            return this.editedIndex === -1 ? 'Create doctor' : 'Edit doctor'
        },
    },

    created() {
        axios.get('http://127.0.0.1:8000/api/doctors')
            .then(response => {
                console.log('[axois - get] Success');
                this.doctors = response.data;
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
        close() {
            this.dialog = false
            this.$nextTick(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },

        deleteItem (item) {
            this.editedIndex = this.doctors.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialogDelete = true
        },

        deleteItemConfirm () {
            axios.delete('http://127.0.0.1:8000/api/doctors/' + this.editedItem.id + '/')
                .then(response => {
                    console.log('[axois - delete] Success');
                    this.doctors.splice(this.editedIndex, 1)
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
            this.editedIndex = this.doctors.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialog = true
        },

        save() {
            if (this.editedIndex > -1) {
                axios.put('http://127.0.0.1:8000/api/doctors/' + this.editedItem.id + '/', {
                    name: this.editedItem.name,
                    phone: this.editedItem.phone,
                    speciality: this.editedItem.speciality
                }).then(response => {
                    console.log('[axois - put] Success');
                    Object.assign(this.doctors[this.editedIndex], this.editedItem)
                    this.close();
                }).catch(response => {
                    console.log('[axois - put] Error');
                    this.is_error = true;
                    this.close();
                })
            } else {
                axios.post('http://127.0.0.1:8000/api/doctors/', {
                    name: this.editedItem.name,
                    phone: this.editedItem.phone,
                    speciality: this.editedItem.speciality
                }).then(response => {
                    console.log('[axois - post] Success');
                    this.editedItem.id = response.data.id;

                    this.doctors.push(this.editedItem);
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