window.addEventListener('DOMContentLoaded', () => {
    let type = 'Milky';

    window.addMeal = new Vue({
        el: '#addMeal',
        data: {
            newName: "",
            newCal: null,
        },
        methods: {
            addIngr: function (event) {
                if (!(this.newName) || this.newCal == null) {
                    alert('You should enter name and calories of new Ingridient!');
                    return;
                }

                ingrs.meals[type].push({name: this.newName, cal: +this.newCal});

                this.registerMeal();

                this.newCal = null;
                this.newName = "";

            },
            setType: function(index, typer) {
                let cookers = document.getElementById('addMeal').getElementsByClassName('cooking__cook');
                
                for (let cooker of cookers) {
                    if (cooker.classList.contains('cooking__cook_active')) cooker.classList.remove('cooking__cook_active');
                }

                type = cookers[index].dataset.type;
                cookers[index].classList.add('cooking__cook_active');
            },
            registerMeal: async function() {
                let url = `/api/registerMeal`
                let resp = await fetch(url, {
                    method: 'POST',
                    headers: new Headers({
                        Accept: 'application/json',
                        'Content-Type': 'application/json'
                    }),
                    mode: 'same-origin',
                    body: JSON.stringify({
                        type: type,
                        name: this.newName,
                        cal: this.newCal
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