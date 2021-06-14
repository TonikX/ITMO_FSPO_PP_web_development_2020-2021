<template>
    <div>
        <h1 class="text-center my-5">{{ pageTitle }}</h1>
        <v-card class="mx-auto rounded" max-width="1000px" tile>
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
                    <v-card>
                        <v-card-title>
                            <span class="text-h5">{{ formTitle() }}</span>
                        </v-card-title>
                        <v-card-text>
                            <h3 class="my-3 mx-3">Группа:
                                {{ getGroupById(this.currentItem.attributes.group) }}
                            </h3>
                            <h3 class="my-3 mx-3 mb-7">День недели:
                                {{ getDay(this.currentItem.attributes.day_of_the_week) }}
                            </h3>
                            <v-form ref="form" lazy-validation>
                                <v-select
                                    v-model="currentItem.attributes.lecture_begin"
                                    :items="beginTime"
                                    :rules="rules"
                                    class="mx-3 mb-8"
                                    dense
                                    item-text="time"
                                    item-value="lecture"
                                    label="Начало*"
                                ></v-select>
                                <v-select
                                    v-if="audiences.data"
                                    v-model="currentItem.attributes.audience"
                                    :items="audiences.data"
                                    :rules="rules"
                                    class="mx-3 mb-8"
                                    dense
                                    item-text="attributes.number"
                                    item-value="id"
                                    label="Аудитория*"
                                ></v-select>
                                <v-select
                                    v-if="lecturers.data"
                                    v-model="currentItem.attributes.lecturer"
                                    :item-text="item => getFullName(item.attributes)"
                                    :items="lecturers.data"
                                    :rules="rules"
                                    class="mx-3 mb-8"
                                    dense
                                    item-value="id"
                                    label="Преподаватель*"
                                ></v-select>
                                <v-select
                                    v-if="disciplines.data"
                                    v-model="currentItem.attributes.discipline"
                                    :items="disciplines.data"
                                    :rules="rules"
                                    class="mx-3 mb-8"
                                    dense
                                    item-text="attributes.name"
                                    item-value="id"
                                    label="Дисциплина*"
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
                :items="groups.data"
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
                    <td :colspan="headers.length" class="px-10 py-5">
                        <div v-for="day in daysOfWeek">
                            <v-simple-table dense>
                                <!--TODO сортировка таблицы. Возможно придётся всё переделать-->
                                <template v-slot:default>
                                    <thead>
                                    <tr>
                                        <th>
                                            <div class="my-3">
                                                <h2>{{ day.name }}</h2>
                                            </div>
                                        </th>
                                        <th></th>
                                        <th></th>
                                        <th></th>
                                        <th></th>
                                        <th>
                                            <v-btn
                                                color="primary"
                                                outlined
                                                x-small
                                                @click="newItem(item, day.number)"
                                            >
                                                Добавить
                                            </v-btn>
                                        </th>
                                    </tr>
                                    <tr>
                                        <th>№</th>
                                        <th>Начало</th>
                                        <th>Аудитория</th>
                                        <th>Дисциплина</th>
                                        <th>Преподаватель</th>
                                        <th>Действия</th>
                                    </tr>
                                    </thead>
                                    <tbody>
                                    <tr v-for="
                                            schedule in groupSchedule(item)
                                            .filter(
                                                sc => sc.attributes.day_of_the_week === day.number
                                            )
                                        ">
                                        <td>{{ schedule.attributes.lecture_begin }}</td>
                                        <td>
                                            {{
                                                beginTime.find(
                                                    bt => bt.lecture === schedule.attributes.lecture_begin
                                                ).time
                                            }}
                                        </td>
                                        <td>
                                            {{
                                                audiences.data.find(
                                                    aud => aud.id === schedule.relationships.audience.data.id
                                                ).attributes.number
                                            }}
                                        </td>
                                        <td>
                                            {{
                                                disciplines.data.find(
                                                    dis => dis.id === schedule.relationships.discipline.data.id
                                                ).attributes.name
                                            }}
                                        </td>
                                        <td>
                                            {{
                                                getFullName(
                                                    lecturers.data.find(
                                                        lec => lec.id === schedule.relationships.lecturer.data.id
                                                    ).attributes
                                                )
                                            }}
                                        </td>
                                        <td>
                                            <v-icon class="mr-2" small @click="editItem(schedule)">
                                                mdi-pencil
                                            </v-icon>
                                            <v-icon small @click="deleteItem(schedule)">
                                                mdi-delete
                                            </v-icon>
                                        </td>
                                    </tr>
                                    </tbody>
                                </template>
                            </v-simple-table>
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
            pageTitle: 'Расписание',
            tableTitle: 'По группам',
            search: '',
            headers: [
                {text: '', sortable: false},
                {text: 'Номер', value: 'attributes.number'},
                {text: 'Расписание', value: 'data-table-expand'},
                {text: '', sortable: false},
            ],
            daysOfWeek: [
                {number: 1, name: 'Понедельник'},
                {number: 2, name: 'Вторник'},
                {number: 3, name: 'Среда'},
                {number: 4, name: 'Четверг'},
                {number: 5, name: 'Пятница'},
                {number: 6, name: 'Суббота'},
            ],
            beginTime: [
                {lecture: 1, time: '8:20'},
                {lecture: 2, time: '10:00'},
                {lecture: 3, time: '11:40'},
                {lecture: 4, time: '13:30'},
                {lecture: 5, time: '15:20'},
                {lecture: 6, time: '17:00'},
            ],
            dialogDelete: false,
            defaultItem: {
                type: "Schedule",
                id: null,
                attributes: {
                    day_of_the_week: '',
                    lecture_begin: '',
                    lecturer: '',
                    discipline: '',
                    group: '',
                    audience: ''
                }
            },
            currentItem: null,
            originalItem: null,
            dialog: false,
            successSnackbar: false,
            errorSnackbar: false,
            snackbarText: '',
            rules: [
                v => !!v || 'Обязательное поле',
            ],
        }
    },
    name: "Groups",
    computed: {
        ...mapGetters([
            'schedules',
            'groups',
            'disciplines',
            'lecturers',
            'audiences'
        ]),
    },
    beforeMount() {
        this.$store.dispatch('getSchedules')
        this.$store.dispatch('getGroups')
        this.$store.dispatch('getDisciplines')
        this.$store.dispatch('getLecturers')
        this.$store.dispatch('getAudiences')
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
            this.$store.dispatch('deleteSchedule', this.currentItem)
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
                return 'Новая запись'
            }
        },
        save() {
            if (this.$refs.form.validate()) {

                console.log(this.currentItem)

                let type
                if (this.currentItem.id) {
                    type = 'updateSchedule'
                    this.snackbarText = 'изменён'
                } else {
                    type = 'createSchedule'
                    this.snackbarText = 'добавлен'
                }
                this.$store.dispatch(
                    type,
                    {
                        data: this.currentItem
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
            // this.clearForm()

            // Отвратительно, но не знаю, как иначе
            this.currentItem.attributes.discipline = item.relationships.discipline.data.id
            this.currentItem.attributes.day_of_the_week = item.attributes.day_of_the_week
            this.currentItem.attributes.lecturer = item.relationships.lecturer.data.id
            this.currentItem.attributes.audience = item.relationships.audience.data.id
            this.currentItem.attributes.lecture_begin = item.attributes.lecture_begin
            this.currentItem.attributes.group = item.relationships.group.data.id
            this.currentItem.id = item.id

            this.dialog = true
        },
        newItem(group, day) {
            this.clearForm()
            this.currentItem.attributes.day_of_the_week = day
            this.currentItem.attributes.group = group.id
            this.dialog = true
        },
        groupSchedule(item) {
            if (this.schedules.data) {
                return this.schedules.data.filter(
                    sch => sch.relationships.group.data.id === item.id
                )
            }
        },
        getFullName(attr) {
            let fullName = attr.surname + ' ' + attr.first_name[0] + '. '
            if (attr.patronymic) {
                fullName += attr.patronymic[0] + '. '
            }

            return fullName
        },
        getDay(number) {
            if (number) {
                return this.daysOfWeek.find(
                    day => day.number === number
                ).name
            }
        },
        getGroupById(id) {
            if (id) {
                return this.groups.data.find(
                    gro => gro.id === id
                ).attributes.number
            }
        }
    }
}
</script>