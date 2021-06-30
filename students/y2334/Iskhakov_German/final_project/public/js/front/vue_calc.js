window.addEventListener('DOMContentLoaded', () => {
    window.calc = new Vue({
        el: '#calc',
        data: {
            weight: 100,
            height: 100,
            sex: 'man',
            ingrs: []
        },
        methods: {
            reset: function() {
                this.ingrs = [];
            }
        },
        computed: {
            calculatedTarget: function() {
                let tmp = (info.sex == 'man') ? 5 : -161; 
                return info.weight * 10 + 6.25 * info.height - 5 * info.age + tmp;
            },

            cals: function() {
                let res = 0;
                for (let i of this.ingrs) res+= i.cal;
                return res;
            }
        }
    });
});