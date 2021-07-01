import Vue from 'vue';
import axios from 'axios';

import App from './App.vue';
import vuetify from './plugins/vuetify';
import router from './router';

window.axios = axios;
window.router = router;

Vue.config.productionTip = false;

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app');
