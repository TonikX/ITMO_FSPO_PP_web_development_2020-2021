<template>
	<div
	class="mt-5 w-50 mx-auto"
	>
		<b-form method='post'>
			<h2>Редактирование профиля</h2>
			<h3>Сменить имя и фамилию</h3>
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
			<b-button @click="change_name()" class="mb-3" type="button" variant="success">Сменить имя и фамилию</b-button>

			<h3>Сменить пароль</h3>

			<b-form-group
				label="Новый пароль"
				label-for="password"
			>
				<b-form-input
					name="password"
					type="password"
					v-model="password"
				/>
				<p v-if='new_password_error' >{{new_password_error}}</p>
			</b-form-group>

			<b-form-group
				label="Текущий пароль"
				label-for="current_password"
			>
				<b-form-input
					name="current_password"
					type="password"
					v-model="current_password"
				/>
				<p v-if='current_password_error' >{{current_password_error}}</p>
			</b-form-group>

			<b-button @click="change_password()" type="button" variant="success">Сменить пароль</b-button>
		</b-form>
	</div>

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
			current_password: '',
			email: '',
			first_name: '',
			last_name: '',
			new_password_error: '',
			current_password_error: '',
			empty_first_name: false,
			empty_last_name: false
		}
	},
	methods: {
		edit_user () {
			this.edit_data = []
			axios({
				method: 'path',
				url: 'http://127.0.0.1:8000/auth/users/',
				data: {
					username: this.login,
					email: this.email,
					first_name: this.first_name,
					last_name: this.last_name,
					password: this.password
				},
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(function (responce) {
				console.log(responce.data)
				this.is_login = true
			}).catch(function (error) {
				console.log(error)
			})
		},
		change_password () {
			if (this.password) {
				axios({
					method: 'post',
					url: 'http://127.0.0.1:8000/auth/users/set_password/',
					responseType: 'json',
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') },
					data: {
						new_password: this.password,
						current_password: this.current_password
					}
				}).then((response) => {
					console.log(response)
					this.password = ''
					this.current_password = ''
					alert('Успешно')
				}).catch(error => {
					console.log(error.response.data.new_password[0])
					this.new_password_error = error.response.data.new_password[0]
					this.current_password_error = error.response.data.current_password[0]
				})
			}
		},
		change_name () {
			if (this.first_name !== '' && this.last_name !== '') {
				axios({
					method: 'patch',
					url: 'http://127.0.0.1:8000/username/',
					responseType: 'json',
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') },
					data: {
						first_name: this.first_name,
						last_name: this.last_name
					}
				}).then((response) => {
					console.log(response)
					this.empty_first_name = false
					this.empty_last_name = false
					alert('Успешно')
				}).catch(error => {
					console.log(error.response.data)
				})
			} else {
				this.empty_first_name = true
				this.empty_last_name = true
			}
		}
	}

}

</script>

<style>

</style>
