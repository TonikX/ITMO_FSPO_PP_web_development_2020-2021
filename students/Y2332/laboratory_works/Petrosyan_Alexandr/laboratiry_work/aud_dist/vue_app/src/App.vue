<template>
    <v-app>
        <v-app-bar app>
            <v-btn icon plain to="/">
                <v-icon>mdi-home</v-icon>
            </v-btn>
            <div v-if="isLoggedIn">
                <v-btn plain to="/schedule">Расписание</v-btn>
                <v-btn plain to="/lecturers">Преподаватели</v-btn>
                <v-btn plain to="/disciplines">Дисциплины</v-btn>
                <v-btn plain to="/audiences">Аудитории</v-btn>
                <v-btn plain to="/groups">Группы</v-btn>
            </div>
            <v-spacer></v-spacer>
            <v-switch
                v-model="$vuetify.theme.dark"
                hide-details
                inset
                @click="saveTheme($vuetify.theme.dark)"
            >
                <template v-slot:label>
                    <v-icon>mdi-theme-light-dark</v-icon>
                </template>
            </v-switch>
            <div v-if="isLoggedIn" class="ml-5">
                <v-btn @click="exit">
                    Выход
                </v-btn>
            </div>
            <div v-else class="ml-5">
                <v-btn to="/login">
                    Вход
                </v-btn>
            </div>
        </v-app-bar>
        <v-main>
            <router-view/>
        </v-main>
    </v-app>
</template>

<script>
import {Methods} from "./api/methods";

export default {
    name: 'App',
    data() {
        return {
            isLoggedIn: localStorage.getItem('auth_token')
        }
    },
    methods: {
        saveTheme(value) {
            localStorage.setItem('dark_theme', value)
        },
        exit() {
            Methods.logout()
            localStorage.removeItem('auth_token')
            this.$router.push('/')
            location.reload()
        }
    }
}
</script>
