"use strict";

import Vue from 'vue';
import axios from "axios";

// Full config:  https://github.com/axios/axios#request-config
// axios.defaults.baseURL = process.env.baseURL || process.env.apiUrl || '';
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

let config = {
    baseURL: "http://127.0.0.1:8000/api/",
    headers: {
        "Content-type": "application/json",
        // TODO авторизация
        "Authorization": "Token 433516bbd274c2f0f3e4e06a4a38f9c50f585eb5"
    }
    // baseURL:  process.env.baseURL || process.env.apiUrl || ""
    // timeout: 60 * 1000, // Timeout
    // withCredentials: true, // Check cross-site Access-Control
};

export const _axios = axios.create(config);

// _axios.interceptors.request.use(
//     function (config) {
//         // Do something before request is sent
//         return config;
//     },
//     function (error) {
//         // Do something with request error
//         return Promise.reject(error);
//     }
// );
//
// // Add a response interceptor
// _axios.interceptors.response.use(
//     function (response) {
//         // Do something with response data
//         return response;
//     },
//     function (error) {
//         // Do something with response error
//         return Promise.reject(error);
//     }
// );
//
// Plugin.install = function (Vue, options) {
//     Vue.axios = _axios;
//     window.axios = _axios;
//     Object.defineProperties(Vue.prototype, {
//         axios: {
//             get() {
//                 return _axios;
//             }
//         },
//         $axios: {
//             get() {
//                 return _axios;
//             }
//         },
//     });
// };
//
// Vue.use(Plugin)
//
// export default Plugin;
