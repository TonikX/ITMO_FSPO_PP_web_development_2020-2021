<template>
	<v-app>
	<Header />

	<v-main>
		<router-view/>
	</v-main>
	</v-app>
</template>

<script>
import Header from './components/Header.vue'

import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

export default {
	name: 'App',

	data: () => ({
	//
	}),
	components: {
		Header
	}
}
</script>

<style lang="sass">

.logo
	font-size: 2rem
	font-family: 'Revalia'
	font-style: normal
	font-weight: 400
	line-height: 60px
	letter-spacing: 0em
	margin-top: -16px

@font-face
	font-family: 'Revalia'
	font-style: normal
	font-weight: 400
	font-display: swap
	src: url(https://fonts.gstatic.com/s/revalia/v9/WwkexPimBE2-4ZPESVPkNbgJ.woff2) format('woff2')
	unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF

@font-face
	font-family: 'Revalia'
	font-style: normal
	font-weight: 400
	font-display: swap
	src: url(https://fonts.gstatic.com/s/revalia/v9/WwkexPimBE2-4ZPESV3kNQ.woff2) format('woff2')
	unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD

</style>
