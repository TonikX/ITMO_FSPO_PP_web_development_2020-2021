window.addEventListener('DOMContentLoaded', () => {
    window.info = new Vue({
        el: '#info',
        data: {
            age: 0,
            weight: 0,
            height: 0,
            sex: 'man'
        },
        methods: {
            update: async function() {
                let url = `/api/updateUser`
                let resp = await fetch(url, {
                    method: 'POST',
                    headers: new Headers({
                        Accept: 'application/json',
                        'Content-Type': 'application/json'
                    }),
                    mode: 'same-origin',
                    body: JSON.stringify({
                        age: this.age,
                        weight: this.weight,
                        height: this.height,
                        sex: this.sex
                    })
                });
        
                try {
                    resp = await resp.json();
        
                    if (resp.status == 'error') alert(resp.message);
                } catch {}
            }
        }
    });
});