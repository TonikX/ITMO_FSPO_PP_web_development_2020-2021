<template>
    <v-app>
        <v-main>
            <router-link to="/">Главная</router-link>
            |
            <router-link to="/lecturers">Преподаватели</router-link>
            <router-view/>
        </v-main>
    </v-app>
</template>

<script>
export default {
    name: 'App',
}
</script>
