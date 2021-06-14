<template>
	<b-container>
		<div class="row">
			<project-item
				v-for='project in project_list'
				:key='project.id' :id='project.id'
				:title='project.title'
				:preview='project.preview'
				:description='project.description'
				:project_url='project.project_url'
				:code_url='project.code_url'
			/>
		</div>
	</b-container>
</template>

<script>
import ProjectItem from '../components/Project-item.vue'
import axios from 'axios'

export default {
	name: 'Projects',
	components: { ProjectItem },
	data () {
		return {
			project_list: []
		}
	},
	beforeMount () {
		axios({
			method: 'get',
			url: 'http://127.0.0.1:8000/projects/'
		}).then((responce) => {
			console.log(responce.data)
			this.project_list = responce.data
		})
	}
}
</script>

<style>

</style>
