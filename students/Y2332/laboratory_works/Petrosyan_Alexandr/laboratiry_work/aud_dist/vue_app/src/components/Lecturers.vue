<template>
    <div>
        <h1 class="text-center my-5">{{ pageTitle }}</h1>
        <v-card class="mx-auto rounded" max-width="800px" tile>
            <v-toolbar flat>
                <v-toolbar-title>{{ tableTitle }}</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-text-field
                    v-model="search"
                    append-icon="mdi-magnify"
                    hide-details
                    label="Поиск"
                    single-line
                ></v-text-field>
                <v-spacer></v-spacer>
                <v-dialog v-model="dialog" max-width="500px" persistent>
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
                            <span class="text-h5">{{ formTitle() }}</span>
                        </v-card-title>
                        <v-card-text>
                            <v-form ref="form" lazy-validation>
                                <v-text-field
                                    v-model="currentItem.attributes.surname"
                                    :counter="30"
                                    :rules="nameRules"
                                    class="mx-3 my-8"
                                    dense
                                    label="Фамилия*"
                                ></v-text-field>
                                <v-text-field
                                    v-model="currentItem.attributes.first_name"
                                    :counter="30"
                                    :rules="nameRules"
                                    class="mx-3 mb-8"
                                    dense
                                    label="Имя*"
                                ></v-text-field>
                                <v-text-field
                                    v-model="currentItem.attributes.patronymic"
                                    :counter="30"
                                    :rules="patronymicRules"
                                    class="mx-3 mb-8"
                                    dense
                                    label="Отчество"
                                ></v-text-field>
                                <v-select
                                    v-if="disciplines.data"
                                    v-model="selected"
                                    :items="disciplines.data"
                                    :rules="disciplinesRules"
                                    class="mx-3 mb-8"
                                    dense
                                    item-text="attributes.name"
                                    item-value="id"
                                    label="Дисциплины*"
                                    multiple
                                ></v-select>
                            </v-form>
                            <small>*обязательные поля</small>
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
                            v-if="disciplines.data"
                            class="ml-6 my-2"
                        >
                            {{ disciplines.data.find(dis => dis.id === discipline.id).attributes.name }}
                        </div>
                    </td>
                </template>
            </v-data-table>
        </v-card>
        <v-snackbar
            v-model="successSnackbar"
            :timeout="2500"
            color="success"
            outlined
            right
        >
            Элемент успешно {{ snackbarText }}
        </v-snackbar>
        <v-snackbar
            v-model="errorSnackbar"
            :timeout="2500"
            color="error"
            outlined
            right
        >
            Произошла ошибка
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
                id: null,
                attributes: {
                    first_name: '',
                    surname: '',
                    patronymic: ''
                },
            },
            currentItem: null,
            originalItem: null,
            dialog: false,
            successSnackbar: false,
            errorSnackbar: false,
            snackbarText: '',
            nameRules: [
                v => !!v || 'Обязательное поле',
                v => (v && v.length <= 30) || 'Должно быть меньше 30 символов',
            ],
            patronymicRules: [
                v => v == null || v === '' || v.length <= 30 || 'Должно быть меньше 30 символов',
            ],
            disciplinesRules: [
                v => (v && v.length >= 1) || 'Выберете хотя бы одну дисциплину'
            ],
            selected: null
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
                .then(() => {
                    this.closeDelete()
                    this.snackbarText = 'удалён'
                    this.successSnackbar = true
                })
                .catch(e => { // TODO ошибки не отслеживаются
                    console.log(e);
                    this.errorSnackbar = true
                })
        },
        clearForm() {
            if (this.$refs.form) {
                this.$refs.form.reset()
            }
        },
        close() {
            this.dialog = false
            this.currentItem = this.defaultItem
        },
        formTitle() {
            if (this.currentItem.id) {
                return 'Редактирование'
            } else {
                return 'Новый преподаватель'
            }
        },
        save() {
            if (this.$refs.form.validate()) {
                let type
                if (this.currentItem.id) {
                    type = 'updateLecturer'
                    this.snackbarText = 'изменён'
                } else {
                    type = 'createLecturer'
                    this.snackbarText = 'добавлен'
                }
                this.$store.dispatch(
                    type,
                    {
                        data: {
                            type: "Lecturer",
                            id: this.currentItem.id,
                            attributes: this.currentItem.attributes,
                            relationships: {
                                disciplines: {
                                    data: this.selected
                                }
                            }
                        }
                    }
                ).then(() => {
                    this.close()
                    this.successSnackbar = true
                }).catch(e => { // TODO ошибки не отслеживаются
                    console.log(e);
                    this.errorSnackbar = true
                })
            }
        },
        editItem(item) {
            this.clearForm()
            this.currentItem = JSON.parse(JSON.stringify(item))
            this.dialog = true
            this.selected = item.relationships.disciplines.data.map(it => it.id)
        }
    }
}
</script>