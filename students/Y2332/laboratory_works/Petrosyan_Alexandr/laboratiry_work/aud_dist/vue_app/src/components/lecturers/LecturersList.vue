<template>
    <div>
        <v-card
            class="mx-auto my-8"
            max-width="800"
            tile
        >
            <v-toolbar flat>
                <v-toolbar-title>
                    Список преподавателей
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
                <v-btn class="mb-2" color="primary">
                    Добавить
                </v-btn>
                <v-dialog v-model="dialogDelete" max-width="300px">
                    <v-card>
                        <v-card-title class="text-h6 text-center">
                            Вы уверены?
                        </v-card-title>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn class="my-3" color="primary" @click="closeDelete">Отмена</v-btn>
                            <v-btn class="my-3" @click="deleteConfirm">Да</v-btn>
                            <v-spacer></v-spacer>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-toolbar>
            <v-data-table
                :expanded.sync="expanded"
                :headers="headers"
                :items="lecturers.data"
                :search="search"
                :single-expand="true"
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
                    <!--                                 TODO-->
                    <v-icon class="mr-2" small @click="editItem(item)">
                        mdi-pencil
                    </v-icon>
                    <v-icon small @click="deleteItem(item)">
                        mdi-delete
                    </v-icon>
                </template>
                <template v-slot:expanded-item="{ headers, item }">
                    <td :colspan="headers.length">
                        <!--TODO-->
                        Дисциплины:
                    </td>
                </template>
            </v-data-table>
            <v-snackbar
                v-model="snackbar"
                :timeout="2000"
                color="success"
            >
                Элемент успешно удалён
            </v-snackbar>
        </v-card>
    </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
    data() {
        return {
            search: '',
            headers: [
                {text: 'Фамилия', value: 'attributes.surname'},
                {text: 'Имя', value: 'attributes.first_name'},
                {text: 'Отчество', value: 'attributes.patronymic'},
                {text: 'Кол-во дисциплин', value: 'relationships.disciplines.meta.count'},
                {text: 'Действия', value: 'actions', sortable: false},
                {text: '', value: 'data-table-expand'},
            ],
            dialogDelete: false,
            currentItem: null,
            snackbar: false,
        }
    },
    name: "LecturersList",
    computed: {
        ...mapGetters(['lecturers']),
    },
    beforeMount() {
        this.$store.dispatch('getLecturers')
    },
    props: {
        msg: String
    },
    methods: {
        deleteItem(item) {
            this.dialogDelete = true
            this.currentItem = item
        },
        closeDelete() {
            this.dialogDelete = false
            this.currentItem = null
        },
        deleteConfirm() {
            this.$store.dispatch('deleteLecturer', this.currentItem)
            this.closeDelete()
            this.snackbar = true
        }
    }
}
</script>