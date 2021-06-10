<template>
    <v-app>
        <v-app-bar app>
            <v-btn icon plain to="/">
                <v-icon>mdi-home</v-icon>
            </v-btn>
            <div>
                <v-btn plain to="/lecturers">Преподаватели</v-btn>
            </div>
            <div>
                <v-btn plain to="/disciplines">Дисциплины</v-btn>
            </div>
            <div>
                <v-btn plain to="/audiences">Аудитории</v-btn>
            </div>
            <div>
                <v-btn plain to="/groups">Группы</v-btn>
            </div>
            <v-spacer></v-spacer>
            <v-switch
                v-model="$vuetify.theme.dark"
                @click="saveTheme($vuetify.theme.dark)"
                hide-details
                inset
            >
                <template v-slot:label>
                    <v-icon>mdi-theme-light-dark</v-icon>
                </template>
            </v-switch>
            <div class="ml-5">
                <v-btn @click="">
                    Выход
                </v-btn>
            </div>
            <!--            <v-btn to="/login">-->
            <!--                Вход-->
            <!--            </v-btn>-->
        </v-app-bar>
        <v-main>
            <router-view/>
        </v-main>
    </v-app>
</template>

<script>
export default {
    name: 'App',
    methods: {
        saveTheme(value) {
            localStorage.setItem('dark_theme', value)
        }
    }
}
</script>
