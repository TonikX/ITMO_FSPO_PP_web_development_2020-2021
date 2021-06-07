<template>
    <v-app>
        <v-app-bar app>
            <v-btn icon plain to="/">
                <v-icon>mdi-home</v-icon>
            </v-btn>
            <div>
                <v-btn plain to="/lecturers">Преподаватели</v-btn>
            </div>
            <!--            <div>-->
            <!--                <v-btn plain to="/disciplines">Дисциплины</v-btn>-->
            <!--            </div>-->
            <!--            <v-spacer></v-spacer>-->
            <!--            <v-spacer></v-spacer>-->
            <!--            <v-btn @click="">-->
            <!--                Выход-->
            <!--            </v-btn>-->
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
}
</script>
