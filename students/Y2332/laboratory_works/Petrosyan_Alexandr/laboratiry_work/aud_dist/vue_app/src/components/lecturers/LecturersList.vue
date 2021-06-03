<template>
    <div>
        <v-card
            class="mx-auto my-8"
            max-width="800"
            tile
        >
            <v-card-title>
                Список преподавателей
                <v-spacer></v-spacer>
                <v-text-field
                    v-model="search"
                    append-icon="mdi-magnify"
                    hide-details
                    label="Поиск"
                    single-line
                ></v-text-field>
            </v-card-title>
            <v-data-table
                :headers="headers"
                :items="lecturers.data"
                :search="search"
            ></v-data-table>
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
                {text: 'Количество дисциплин', value: 'relationships.disciplines.meta.count'},
            ]
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
}
</script>