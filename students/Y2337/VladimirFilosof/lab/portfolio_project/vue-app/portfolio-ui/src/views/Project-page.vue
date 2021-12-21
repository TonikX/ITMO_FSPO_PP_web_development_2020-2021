<template>
	<div class="container">
		<h1>{{item.title}}</h1>
		<div class="row">
			<div v-if="item.preview !== null" class="col-6">
				<img class="w-100 p-3" :src="item.preview">
			</div>
			<div class="col-6 mx-auto">
				<p class="p-3">{{item.description}}</p>
				<p v-if="item.project_url!==null" class="px-3">Ссылка на работу: <a :href="item.project_url"> {{item.project_url}} </a></p>
				<p v-if="item.code_url!==null" class="px-3">Ссылка на код работы: <a :href="item.code_url"> {{item.code_url}} </a> </p>

			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'ProjectsPage',
	data () {
		return {
			item: []
		}
	},
	props: ['id'],
	mounted () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/projects/' + this.$route.params.id
		}).then((response) => {
			this.item = response.data
			console.log(response)
		})
	}
}
</script>

<style>

</style>
