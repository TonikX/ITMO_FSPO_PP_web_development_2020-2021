<template>
    <div>
        Список преподавателей: <br>
        <ul>
            <li v-for="lecturer in lecturers">
                {{ lecturer.attributes.surname }} {{ lecturer.attributes.first_name }}
                {{ lecturer.attributes.patronymic }}
            </li>
        </ul>
        <button @click="prevPage"> < </button>
        <button @click="nextPage"> > </button>
    </div>
</template>

<script>
import $ from "jquery"

export default {
    name: "Lecturers",
    data() {
        return {
            lecturers: '',
            links: '',
        }
    },
    created() {
        $.ajaxSetup({
            headers: {
                "Authorization": "Token " + localStorage.getItem("auth_token"),
            }
        })
        this.loadLecturers()
    },
    methods: {
        loadLecturers() {
            $.ajax({
                url: "http://127.0.0.1:8000/api/lecturers/",
                type: "GET",
                success: (response) => {
                    this.lecturers = response.data
                    this.links = response.links
                }
            })
        },
        nextPage() {
            if(this.links.next) {
                $.ajax({
                    url: this.links.next,
                    type: "GET",
                    success: (response) => {
                        this.lecturers = response.data
                        this.links = response.links
                    }
                })
            }
        },
        prevPage() {
            if(this.links.prev) {
                $.ajax({
                    url: this.links.prev,
                    type: "GET",
                    success: (response) => {
                        this.lecturers = response.data
                        this.links = response.links
                    }
                })
            }
        }
    }
}
</script>

<style scoped>

</style>
