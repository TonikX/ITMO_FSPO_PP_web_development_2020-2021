<template>
	<div class="container">
		<h1>{{item.title}}</h1>
		<div class="row">
			<div class="col-6">
				<img class="w-100" :src="item.preview">
			</div>
			<div class="col-6">
				<p>{{item.text}}</p>
				<button @click="new_order()" type="button" class="btn btn-success text-white">Заказать</button>
			</div>
		</div>
		<div class="row mt-5">
			<div class="col-12">
				<h2>Отзывы</h2>
				<hr>
				<comment
					v-for="comment in comments"
					:key="comment.id"
					:id="comment.id"
					:text="comment.text"
					:is_owner="comment.owner"
				/>
				<form v-if="is_auth">
					<textarea v-model="feedback_text" class="form-control" name="comment" id="" cols="30" rows="10" placeholder="Введите текст отзыва"></textarea>
					<button type="button" @click="new_feedback()" class="btn btn-success">Оставить отзыв</button>
				</form>
				<div v-else>Войдите чтобы оставить отзыв</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
import Comment from '../components/Comment.vue'

export default {
	name: 'ServicePage',
	components: { Comment },
	data () {
		return {
			item: [],
			comments: [],
			is_auth: false,
			feedback_text: ''
		}
	},
	props: ['id'],
	created () {
		this.is_auth = sessionStorage.getItem('auth_token')
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/services/' + this.$route.params.id,
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then((response) => {
			this.item = response.data
			console.log(response)
		})

		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/feedbacks/' + this.$route.params.id,
			responseType: 'json',
			headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
		}).then(response => {
			this.comments = response.data
			console.log(this.comments)
		})
	},
	methods: {
		new_order () {
			if (sessionStorage.getItem('auth_token') !== null) {
				axios({
					method: 'get',
					url: 'http://127.0.0.1:8000/auth/users/me/',
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') },
					responseType: 'json'
				}).then((responce) => {
					localStorage.setItem('user_id', responce.data.id)
				})

				axios({
					method: 'post',
					url: 'http://127.0.0.1:8000/orders/',
					data: {
						user: localStorage.getItem('user_id'),
						service: this.item.id
					},
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') },
					responseType: 'json'
				}).then((responce) => {
					console.log(responce)
					alert('Заказ оформлен')
				})
			}
		},
		new_feedback () {
			if (sessionStorage.getItem('auth_token')) {
				axios({
					method: 'post',
					url: 'http://127.0.0.1:8000/feedbacks/',
					responseType: 'json',
					data: {
						text: this.feedback_text,
						service: this.$route.params.id
					},
					headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
				}).then(response => {
					this.comments = response.data
					console.log(this.comments)
					document.location.reload()
				})
			}
		}
	}
}
</script>

<style>

</style>
