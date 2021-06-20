
window.addEventListener('DOMContentLoaded', () => {

    let themes = document.getElementsByClassName('theme__option');
    let root = document.documentElement;

    themes[0].addEventListener('click', () => {
        if (themes[0].classList.contains('theme__option_active')) return;
        localStorage.setItem('theme', 0);
        document.getElementsByClassName('theme__activator')[0].style.transform = 'translateX(0px)';
        themes[1].classList.remove('theme__option_active');
        themes[0].classList.add('theme__option_active');
        root.style.setProperty('--background-color', "#fff");
        root.style.setProperty('--background-accent-color', "#00a2ff");
        root.style.setProperty('--accent-color', "#0083cf");
        root.style.setProperty('--content-color', "#fff");
    });

    themes[1].addEventListener('click', () => {
        if (themes[1].classList.contains('theme__option_active')) return;
        localStorage.setItem('theme', 1);
        document.getElementsByClassName('theme__activator')[0].style.transform = 'translateX(73px)';
        themes[0].classList.remove('theme__option_active');
        themes[1].classList.add('theme__option_active');
        root.style.setProperty('--background-color', "rgb(48, 48, 48)");
        root.style.setProperty('--background-accent-color', "rgb(231, 221, 74)");
        root.style.setProperty('--accent-color', "rgb(201, 187, 0)");
        root.style.setProperty('--content-color', "rgb(48, 48, 48)");
    });

    let theme = localStorage.getItem('theme');
    
    if (theme == 0) themes[0].click();
    if (theme == 1) themes[1].click();

});
