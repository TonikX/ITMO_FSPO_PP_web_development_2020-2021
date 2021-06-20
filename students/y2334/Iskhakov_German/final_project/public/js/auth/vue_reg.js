window.addEventListener('DOMContentLoaded', () => {
    window.signup = new Vue({
        el: '#signup',
        data: {
            login: "",
            password: "",
            name: "",
            surname: "",
            height: "",
            weight: "",
            age: "",
            sex: "man"
        },
        methods: {
            sign: async function() {

                if (!this.login || !this.password || !this.name || !this.surname || !this.height || !this.weight || !this.age || !this.sex) {
                    alert('Fill all the fields!');
                    return;
                }

                let url = '/api/createUser'
                let resp = await fetch(url, {
                    method: 'POST',
                    headers: new Headers({
                        Accept: 'application/json',
                        'Content-Type': 'application/json'
                    }),
                    mode: 'same-origin',
                    body: JSON.stringify({
                        login: this.login,
                        password: this.password,
                        name: this.name,
                        surname: this.surname,
                        height: this.height,
                        weight: this.weight,
                        age: this.age,
                        sex: this.sex,
                    })
                });

                resp = await resp.json();

                if (resp.status == 'error') alert(resp.message);
                if (resp.status == 'success') location.assign('/');
            }
        }
    });
});