<template>
	<b-container
	class="mt-5 w-50"
	>
		<b-form method='post' v-if="is_login">
			<h2>Вход</h2>
			<b-form-group
				label="Login"
				label-for="username"
			>
				<b-form-input
					name="username"
					type="text"
					v-model="login"
					required
				/>
			</b-form-group>

			<b-form-group
				label="password"
				label-for="password"
			>
				<b-form-input
					name="password"
					type="password"
					v-model="password"
					required
				/>
			</b-form-group>

			<b-button @click="signIn()" type="button" variant="success">Войти</b-button>
			<b-button @click="is_login=false" class="ml-3" type="button" variant="primary">Нет аккаунта? Зарестрируйся</b-button>
		</b-form>
		<b-form method='post' v-else>
			<h2>Регистрация</h2>
			<b-form-group
				label="Login"
				label-for="username"
			>
				<b-form-input
					name="username"
					type="text"
					v-model="login"
				/>
			</b-form-group>

			<b-form-group
				label="email"
				label-for="email"
			>
				<b-form-input
					name="email"
					type="email"
					v-model="email"
				/>
			</b-form-group>

			<b-form-group
				label="Имя"
				label-for="first_name"
			>
				<b-form-input
					name="first_name"
					type="text"
					v-model="first_name"
				/>
			</b-form-group>

			<b-form-group
				label="Фамилия"
				label-for="last_name"
			>
				<b-form-input
					name="last_name"
					type="text"
					v-model="last_name"
				/>
			</b-form-group>

			<b-form-group
				label="password"
				label-for="password"
			>
				<b-form-input
					name="password"
					type="password"
					v-model="password"
				/>
			</b-form-group>

			<b-form-group
				label="re-password"
				label-for="re-password"
			>
				<b-form-input
					name="re-password"
					type="password"
					v-model="re_password"
				/>
			</b-form-group>

			<b-button @click="signUp()" type="button" variant="success">Зарегистрироваться</b-button>
			<b-button @click="is_login=true" class="ml-3" type="button" variant="primary">Уже есть аккаунт? Войти</b-button>
		</b-form>
	</b-container>

</template>

<script>
import axios from 'axios'

export default {
	name: 'Login',
	data () {
		return {
			login: '',
			password: '',
			re_password: '',
			email: '',
			first_name: '',
			last_name: '',
			is_login: true
		}
	},
	methods: {
		signIn () {
			axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/auth/token/login/',
				data: {
					username: this.login,
					password: this.password
				},
				responseType: 'json'
			}).then((responce) => {
				sessionStorage.setItem('auth_token', responce.data.auth_token)

				console.log(responce.data.auth_token)
				if (sessionStorage.getItem('auth_token') !== null) {
					window.location.href = '/lichniy-kabinet/'
				}
			})
		},
		signUp () {
			axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/auth/users/',
				data: {
					username: this.login,
					email: this.email,
					first_name: this.first_name,
					last_name: this.last_name,
					password: this.password
				},
				responseType: 'json'
				// 	headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') },

			}).then(function (responce) {
				console.log(responce.data)
				this.is_login = true
			}).catch(function (error) {
				console.log(error)
			})
		}
	}

}

</script>

<style>

</style>
