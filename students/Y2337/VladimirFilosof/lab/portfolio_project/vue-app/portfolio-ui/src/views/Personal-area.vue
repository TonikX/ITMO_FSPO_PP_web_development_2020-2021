<template>
	<div class="container" v-if="is_auth">
		<h2>Личный кабинет {{username}}</h2>
		<b-button
			class="text-white"
			type="button"
			variant="danger"
			@click="logout()"
		>
			Выйти
		</b-button>
		<b-button
			class="text-white ml-3"
			type="button"
			variant="primary"
			@click="is_edit_user = true"
		>
			Открыть редактирование профиля
		</b-button>
		<b-button
			v-if="is_edit_user"
			class="text-white ml-3"
			type="button"
			variant="primary"
			@click="is_edit_user = false"
		>
			Закрыть редактирование профиля
		</b-button>
		<br>

		<edit-user v-if="is_edit_user" />
			<br>

		<h3>Заказы</h3>
		<div v-if="orders===[]">
			<p>у вас нет заказов</p>
		</div>
		<div v-else>
			<hr>
			<div v-for="order in orders" :key="order.id">
				<h4>{{order.title}}</h4>
				<p>Статус: {{order.status}} </p>
				<a :href="'/services/' + order.id">Посмотреть услугу</a>
				<hr>
			</div>
		</div>

	</div>

	<login v-else />
</template>

<script>
import Login from '../components/Login'
import axios from 'axios'
import EditUser from '../components/edit-user.vue'

export default {
	name: 'PersonalArea',
	components: { Login, EditUser },
	data () {
		return {
			is_auth: false,
			is_edit_user: false,
			orders: [],
			username: '',
			edit_btn_text: 'Редактировать профиль'
		}
	},
	mounted () {
		this.is_auth = (sessionStorage.getItem('auth_token') !== null)
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/userorders/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((responce) => {
			this.orders = responce.data
		})

		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/auth/users/me/',
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((responce) => {
			this.username = responce.data.username
		})
	},
	methods: {
		logout () {
			console.log(sessionStorage.getItem('auth_token'))
			axios({
				method: 'post',
				url: 'http://127.0.0.1:8000/auth/token/logout/',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') },
				responseType: 'json'
			}).then((responce) => {
				console.log(responce.data)
			})
			sessionStorage.removeItem('auth_token')

			if (sessionStorage.getItem('auth_token') !== null) {
				window.location.href = '/lichniy-kabinet/'
			}

			this.is_auth = false
		},
		edit_profile () {
			this.is_edit_user = true
			this.edit_btn_text = 'Закрыть редактирование'
		}
	}
}
</script>

<style>

</style>
