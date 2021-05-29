<template>
    <div>
        Список преподавателей: <br>
        <ul>
            <li v-for="lecturer in lecturers">
                {{ lecturer.attributes.surname }} {{ lecturer.attributes.first_name }}
                {{ lecturer.attributes.patronymic }}
            </li>
        </ul>
        <button id="prevPageBtn" @click="prevPage"> < </button>
        {{currentPageNumber}} из {{pageQuantity}}
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
            pageQuantity: Number,
            currentPageNumber: 1,
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
                    let lastPageUrl = response.links.last;
                    this.pageQuantity = lastPageUrl.substr(lastPageUrl.indexOf('=') + 1)
                    this.updatePage(response)
                }
            })
        },
        nextPage() {
            if(this.links.next) {
                $.ajax({
                    url: this.links.next,
                    type: "GET",
                    success: (response) => {
                        this.currentPageNumber++
                        this.updatePage(response)
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
                        this.currentPageNumber--
                        this.updatePage(response)
                    }
                })
            }
        },
        updatePage(response) {
            this.lecturers = response.data
            this.links = response.links
        },
    }
}
</script>

<style scoped>

</style>
