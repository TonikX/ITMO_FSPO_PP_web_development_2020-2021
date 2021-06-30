window.addEventListener('DOMContentLoaded', () => {
    window.login = new Vue({
        el: '#login',
        data: {
            login: "",
            password: ""
        },
        methods: {
            log: async function() {

                if (!this.login || !this.password) {
                    alert('Fill all the fields!');
                    return;
                }

                let url = '/api/logUser'
                let resp = await fetch(url, {
                    method: 'POST',
                    headers: new Headers({
                        Accept: 'application/json',
                        'Content-Type': 'application/json'
                    }),
                    mode: 'same-origin',
                    body: JSON.stringify({
                        login: this.login,
                        password: this.password
                    })
                });

                resp = await resp.json();

                if (resp.status == 'error') alert(resp.message);
                if (resp.status == 'success') location.assign('/');
            }
        }
    });
});