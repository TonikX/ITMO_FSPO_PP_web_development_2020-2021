<template>
    <div>
        <v-card
            class="mx-auto mt-16 px-16 py-16 rounded-lg"
            max-width="500px"
            tile
        >
            <div class="text-center">
                <h1>
                    Авторизация
                </h1>
            </div>
            <v-card-text>
                <v-form ref="form" lazy-validation>
                    <v-text-field
                        v-model="user.username"
                        :rules="rule"
                        class="mt-5"
                        dense
                        label="Логин"
                        outlined
                        type="text"
                    >

                    </v-text-field>
                    <v-text-field
                        v-model="user.password"
                        :rules="rule"
                        class="mt-5"
                        dense
                        label="Пароль"
                        outlined
                        type="password">

                    </v-text-field>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <div>
                    <v-btn color="primary" @click="login">
                        Войти
                    </v-btn>
                </div>
                <v-spacer></v-spacer>
            </v-card-actions>
        </v-card>
        <v-snackbar
            v-model="errorSnackbar"
            :timeout="2500"
            color="error"
            outlined
            right
        >
            Неверное имя пользователя или пароль
        </v-snackbar>
    </div>
</template>

<script>
import {Methods} from "../api/methods";
import axios from "axios";

export default {
    name: "Login",
    data() {
        return {
            rule: [v => !!v || 'Обязательное поле'],
            user: {
                username: '',
                password: ''
            },
            errorSnackbar: false
        }
    },
    methods: {
        login() {
            if (this.$refs.form.validate()) {
                let data = {
                    data: {
                        type: "TokenCreateView",
                        attributes: this.user,
                    }
                }
                Methods.login(data)
                    .then(response => {
                        let token = response.data.id
                        localStorage.setItem('auth_token', token)
                        axios.defaults.headers.common['Authorization'] = "Token " + token
                        this.$router.push('/')
                        location.reload()
                    })
                    .catch(() => {
                        this.errorSnackbar = true
                        this.user.password = ''
                    })
            }
        }
    }
}
</script>
