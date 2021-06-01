<template>
    <h1>{{ msg }}</h1>
    <ul>
        <li v-for="lecturer in lecturers.data">
            {{ lecturer.attributes.surname }} {{ lecturer.attributes.first_name }}
            {{ lecturer.attributes.patronymic }}
        </li>
    </ul>
</template>

<script>
import {mapGetters} from "vuex";

export default {
    name: "LecturersList",
    computed: mapGetters(['lecturers']),
    beforeMount() {
        this.$store.dispatch('getLecturers')
    }
}
</script>