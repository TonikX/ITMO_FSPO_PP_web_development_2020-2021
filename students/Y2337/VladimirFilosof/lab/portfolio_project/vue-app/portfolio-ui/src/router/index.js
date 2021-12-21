import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import PersonalArea from '../views/Personal-area.vue'
import Projects from '../views/Projects.vue'
import Services from '../views/Services.vue'
import ServicePage from '../views/Service-page.vue'
import ProjectPage from '../views/Project-page.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},
	{
		path: '/lichniy-kabinet',
		name: 'Personal_area',
		component: PersonalArea
	},
	{
		path: '/projects',
		name: 'Projects',
		component: Projects
	},
	{
		path: '/projects/:id',
		name: 'ProjectPage',
		component: ProjectPage
	},
	{
		path: '/services',
		name: 'Services',
		component: Services
	},
	{
		path: '/services/:id',
		name: 'ServicePage',
		component: ServicePage
	}
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

export default router
