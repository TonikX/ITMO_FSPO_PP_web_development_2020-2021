
window.addEventListener('DOMContentLoaded', () => {

    let me = null;

    (async function() {
        let url = `/api/getMe`
        let resp = await fetch(url, {
            method: 'GET',
            headers: new Headers({
                Accept: 'application/json',
                'Content-Type': 'application/json'
            }),
            mode: 'same-origin'
        });

        resp = await resp.json();

        if (resp.status == 'error') alert(resp.message);

        document.getElementsByClassName('profile__name')[0].innerHTML = `${resp.name} ${resp.surname}`;
        info.age = resp.age;
        info.weight = resp.weight;
        info.height = resp.height;
        info.sex = resp.sex;
    })();

    (async function() {
        let url = `/api/getMeals`
        let resp = await fetch(url, {
            method: 'GET',
            headers: new Headers({
                Accept: 'application/json',
                'Content-Type': 'application/json'
            }),
            mode: 'same-origin'
        });

        resp = await resp.json();

        if (resp.status == 'error') alert(resp.message);

        for (let e of resp.data) {
            ingrs.meals[e.type].push({name: e.name, cal: +e.cal});
        }
    })();

    document.getElementsByClassName('profile__action')[0].addEventListener('click', async () => {
        let url = `/api/exit`
        let resp = await fetch(url, {
            method: 'POST',
            headers: new Headers({
                Accept: 'application/json',
                'Content-Type': 'application/json'
            }),
            mode: 'same-origin'
        });

        try {
            resp = await resp.json();

            if (resp.status == 'error') alert(resp.message);
        } catch {}

        location.replace('/auth');
    });

});
