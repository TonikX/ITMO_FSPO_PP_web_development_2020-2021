<template>
	<b-container>
		<div class="row">
			<project-item v-for='service in service_list' :key='service.id' :id='service.id' :title='service.title' :preview='service.preview'  :description='service.description'/>
		</div>
	</b-container>
</template>

<script>
import ProjectItem from '../components/Service-item.vue'
import axios from 'axios'

export default {
	name: 'Projects',
	components: { ProjectItem },
	data () {
		return {
			service_list: []
		}
	},
	beforeMount () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/services/'
		}).then((responce) => {
			console.log(responce.data)
			this.service_list = responce.data
		})
	}
}
</script>

<style>

</style>
