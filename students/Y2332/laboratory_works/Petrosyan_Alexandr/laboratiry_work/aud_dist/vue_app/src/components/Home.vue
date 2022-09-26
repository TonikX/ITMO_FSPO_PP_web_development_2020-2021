<template>
    <div>
        <div v-if="isLoggedIn">
            <h1 class="text-center my-16">Добро пожаловать</h1>
            <v-img
                class="mx-auto"
                max-width="300px"
                src="../assets/calendar-clock-icon.png"
            ></v-img>
        </div>
        <div v-else class="text-center">
            <h2 class="mt-16 mb-8">Вы не вошли в систему</h2>
            <v-btn color="primary" to="/login">
                войти
            </v-btn>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Home',
    data() {
        return {
            isLoggedIn: localStorage.getItem('auth_token')
        }
    }
}
</script>
