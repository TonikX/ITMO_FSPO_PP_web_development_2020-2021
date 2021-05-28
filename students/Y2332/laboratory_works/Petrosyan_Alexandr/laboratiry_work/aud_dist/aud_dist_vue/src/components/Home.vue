<template>
    <div>
        <h1>Расписание</h1>
        <h2>Добро пожаловать</h2>
        <button v-if="isAuth" @click="logout">Выход</button>
        <button v-else @click="goLogin">Вход</button>
        <br><br>
        <lecturers v-if="isAuth"></lecturers>
    </div>
</template>

<script>
import Lecturers from "../components/LecturersList"
import $ from "jquery";

export default {
    name: "Home",
    components: {
        Lecturers
    },
    computed: {
        isAuth() {
            if (localStorage.getItem("auth_token")) {
                return true
            }
        }
    },
    methods: {
        goLogin() {
            this.$router.push({name: "login"})
        },
        logout() {
            $.ajax({
                url: "http://127.0.0.1:8000/auth/token/logout/",
                type: "POST",
                headers: {
                    "Authorization": "Token " + localStorage.getItem("auth_token"),
                }
            })
            localStorage.removeItem("auth_token")
            location.reload()
        }
    }
}
</script>

<style scoped>

</style>
