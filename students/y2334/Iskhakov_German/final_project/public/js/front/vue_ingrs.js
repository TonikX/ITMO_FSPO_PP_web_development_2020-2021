window.addEventListener('DOMContentLoaded', () => {
    window.ingrs = new Vue({
        el: '#ingrs',
        data: {
            meals: {
                "Milky": [{name: 'Milk', cal: 100}, {name: 'Egg', cal: 100}, {name: 'Cheese', cal: 100}],
                "Drink": [{name: 'Water', cal: 10}, {name: 'Pepsi', cal: 100}, {name: 'Wine', cal: 100}],
                "Fruit": [{name: 'Milk', cal: 100}, {name: 'Milk', cal: 100}, {name: 'Milk', cal: 100}],
                "Green": [{name: 'Carrot', cal: 50}, {name: 'Cabbage', cal: 50}, {name: 'Celery', cal: 0}],
                "Meat": [{name: 'Pork', cal: 250}, {name: 'Mutton', cal: 150}, {name: 'Beef', cal: 200}],
                "Fish": [{name: 'Apple', cal: 30}, {name: 'Banana', cal: 30}, {name: 'Grapes', cal: 50}],
            }
        },
        methods: {
            calcIngr: function (meal) {
                calc.ingrs.push(meal);
            }
        }
    });
});