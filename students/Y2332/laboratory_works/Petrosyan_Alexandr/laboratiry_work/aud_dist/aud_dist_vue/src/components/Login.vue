<template>
    <div>
        <input v-model="login" placeholder="Логин" type="text"/><br/>
        <input v-model="password" placeholder="Пароль" type="password"/><br/>
        <button @click="sign_in">Войти</button>
    </div>
</template>

<script>
import $ from "jquery"

export default {
    name: "Login",
    data() {
        return {
            login: '',
            password: '',
        }
    },
    methods: {
        sign_in() {
            $.ajax({
                url: "http://127.0.0.1:8000/auth/token/login/",
                type: "POST",
                data: {
                    username: this.login,
                    password: this.password,
                },
                headers: "",
                success: (response) => {
                    localStorage.setItem("auth_token", response.data.attributes.auth_token)
                    this.$router.push({name: "home"})
                },
                error: (response) => {
                    if (response.status === 400) {
                        alert("Неверное имя ползователя или пароль")
                    }
                }
            })
        },
    }
}
</script>

<style scoped>

</style>
