<template>
    <v-row>
        <v-col>
            <template>
                <h2>Login</h2>
                <v-form v-model="valid">
                    <v-container>
                        <v-row>
                            <v-col
                                cols="6"
                            >
                                <v-text-field
                                    v-model="username"
                                    :counter="64"
                                    label="Username"
                                    required
                                ></v-text-field>
                            </v-col>

                            <v-col
                                cols="6"
                            >
                                <v-text-field
                                    v-model="password"
                                    :counter="64"
                                    label="Password"
                                    required
                                ></v-text-field>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-btn
                                    color="success"
                                    class="mr-4"
                                    @click="send"
                                >
                                    Login
                                </v-btn>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-form>
            </template>
        </v-col>
    </v-row>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            username: '',
            password: '',
            valid: false
        }
    },

    methods: {
        send() {
            axios.post('http://127.0.0.1:8000/api/token/', {
                username: this.username,
                password: this.password
            })
            .then(response => {
                console.log(response.data)
                axios.defaults.headers.common['Authorization'] = 'Bearer' + ' ' + response.data.access;

                router.push({ name: 'home'})
            })
            .catch(response => {

            });
        }
    }
}
</script>