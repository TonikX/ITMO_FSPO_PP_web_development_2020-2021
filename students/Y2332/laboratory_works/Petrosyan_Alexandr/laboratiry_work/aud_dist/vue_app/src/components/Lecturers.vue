<template>
    <div>
        <h1 class="text-center my-5">{{ pageTitle }}</h1>
        <v-card
            class="mx-auto"
            max-width="800"
            tile
        >
            <v-toolbar flat>
                <v-toolbar-title>
                    {{ tableTitle }}
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <v-text-field
                    v-model="search"
                    append-icon="mdi-magnify"
                    hide-details
                    label="Поиск"
                    single-line
                ></v-text-field>
                <v-spacer></v-spacer>
                <v-dialog v-model="dialog" max-width="500px">
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn
                            v-bind="attrs"
                            v-on="on"
                            class="mb-2"
                            color="primary"
                            @click="clearForm"
                        >
                            Добавить
                        </v-btn>
                    </template>
                    <v-card>
                        <v-card-title>
                            <span class="text-h5">{{ formTitle }}</span>
                        </v-card-title>
                        <v-card-text>
                            <v-container>





                                <v-form
                                    ref="form"
                                    v-model="valid"
                                    lazy-validation
                                >
                                    <v-row>
                                        <v-text-field
                                            v-model="currentItem.attributes.surname"
                                            :counter="30"
                                            :rules="nameRules"
                                            label="Фамилия*"
                                            required
                                            type="text"
                                        ></v-text-field>
                                    </v-row>
                                    <v-row>
                                        <v-text-field
                                            v-model="currentItem.attributes.first_name"
                                            :counter="30"
                                            :rules="nameRules"
                                            label="Имя*"
                                            required
                                            type="text"
                                        ></v-text-field>
                                    </v-row>
                                    <v-row>
                                        <v-text-field
                                            v-model="currentItem.attributes.patronymic"
                                            :counter="30"
                                            :rules="patronymicRules"
                                            label="Отчество"
                                            type="text"
                                        ></v-text-field>
                                    </v-row>
                                </v-form>






                            </v-container>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn class="my-3" @click="close">
                                Отмена
                            </v-btn>
                            <v-btn class="my-3" color="primary" @click="save">
                                Сохранить
                            </v-btn>
                            <v-spacer></v-spacer>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
                <v-dialog v-model="dialogDelete" max-width="280px">
                    <v-card>
                        <v-card-title>
                            Элемент будет удалён
                        </v-card-title>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn class="my-3" color="primary" @click="closeDelete">
                                Отмена
                            </v-btn>
                            <v-btn class="my-3" @click="deleteConfirm">
                                Да
                            </v-btn>
                            <v-spacer></v-spacer>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-toolbar>
            <v-data-table
                :headers="headers"
                :items="lecturers.data"
                :search="search"
                multi-sort
                show-expand
            >
                <template v-slot:no-data>
                    Таблица пуста
                </template>
                <template v-slot:no-results>
                    По вашему запросу ничего не найдено
                </template>
                <template v-slot:item.actions="{ item }">
                    <!--                                 TODO       -->
                    <v-icon class="mr-2" small @click="editItem(item)">
                        mdi-pencil
                    </v-icon>
                    <v-icon small @click="deleteItem(item)">
                        mdi-delete
                    </v-icon>
                </template>
                <template v-slot:expanded-item="{ headers, item }">
                    <td :colspan="headers.length">
                        <div
                            v-for="discipline in item.relationships.disciplines.data"
                            class="ml-6 my-2"
                        >
                            {{ disciplines.data.find(dis => dis.id === discipline.id).attributes.name || '' }}
                        </div>
                    </td>
                </template>
            </v-data-table>
        </v-card>
        <v-snackbar
            v-model="snackbar"
            :timeout="2500"
            color="success"
            outlined
            right
        >
            Элемент успешно {{ snackbarText }}
        </v-snackbar>
    </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
    data() {
        return {
            pageTitle: 'Преподаватели',
            tableTitle: 'Список преподавателей',
            formTitle: 'Новый преподаватель',
            search: '',
            headers: [
                {text: 'Фамилия', value: 'attributes.surname'},
                {text: 'Имя', value: 'attributes.first_name'},
                {text: 'Отчество', value: 'attributes.patronymic'},
                {text: 'Дисциплины', value: 'data-table-expand'},
                {text: 'Действия', value: 'actions', sortable: false},
            ],
            dialogDelete: false,
            defaultItem: {
                attributes: {
                    first_name: '',
                    surname: '',
                    patronymic: ''
                },
            },
            currentItem: null,
            dialog: false,
            snackbar: false,
            snackbarText: '',
            valid: true,
            nameRules: [
                v => !!v || 'Обязательное поле',
                v => (v && v.length <= 30) || 'Должно быть меньше 30 символов',
            ],
            patronymicRules: [
                v => (v.length <= 30) || 'Должно быть меньше 30 символов',
            ],
        }
    },
    name: "Lecturers",
    computed: mapGetters(['lecturers', 'disciplines']),
    beforeMount() {
        this.$store.dispatch('getLecturers')
        this.$store.dispatch('getDisciplines')
        this.currentItem = this.defaultItem
    },
    methods: {
        deleteItem(item) {
            this.dialogDelete = true
            this.currentItem = item
        },
        closeDelete() {
            this.dialogDelete = false
            this.currentItem = this.defaultItem
        },
        deleteConfirm() {
            this.$store.dispatch('deleteLecturer', this.currentItem)
            this.closeDelete()
            this.snackbarText = 'удалён'
            this.snackbar = true
        },
        clearForm() {
            this.$refs.form.reset()
        },
        close() {
            this.dialog = false
            this.currentItem = this.defaultItem
        },
        save() {
            if (this.$refs.form.validate()) {
                console.log(this.currentItem.attributes)
                this.$store.dispatch(
                    'createLecturer',
                    {
                        data: {
                            type: "Lecturer",
                            attributes: this.currentItem.attributes
                        }
                    }
                )
                this.close()
                this.snackbarText = 'добавлен'
                this.snackbar = true
            }
        }
    }
}
</script>