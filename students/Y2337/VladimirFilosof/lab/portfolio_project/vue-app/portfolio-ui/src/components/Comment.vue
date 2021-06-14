<template>
	<div class="comment">
		<p>{{text}}</p>
		<div v-if="is_owner">
			<button @click="edit = !edit" class="btn btn-primary">Редактировать</button>
			<button @click="delete_feedback()" class="btn btn-danger">Удалить</button>
			<div>
				<form v-if="edit">
					<textarea class="form-control" v-model="new_text" name="edit" id="edit" cols="30" rows="10"></textarea>
					<button @click="save()" type="button" class="btn btn-success">Сохранить</button>
				</form>
			</div>
		</div>
		<hr>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	name: 'Comment',
	data () {
		return {
			edit: false,
			new_text: this.text
		}
	},
	props: ['id', 'text', 'is_owner'],
	methods: {
		delete_feedback () {
			axios({
				method: 'delete',
				url: 'http://127.0.0.1:8000/feedbacks/detail/' + this.id + '/',
				responseType: 'json',
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response.data)
				document.location.reload()
			})
		},
		save () {
			axios({
				method: 'patch',
				url: 'http://127.0.0.1:8000/feedbacks/detail/' + this.id + '/',
				responseType: 'json',
				data: {
					text: this.new_text
				},
				headers: { Authorization: 'Token ' + sessionStorage.getItem('auth_token') }
			}).then(response => {
				console.log(response.data)
				document.location.reload()
			})
		}
	}
}
</script>

<style>
.comment {
	padding: 5px;
}
</style>
