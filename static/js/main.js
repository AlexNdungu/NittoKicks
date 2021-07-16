
const prodMain = document.querySelector('.slider');
const prods = document.querySelectorAll('.images img')


const next = document.querySelector('#next');
const prev = document.querySelector('#prev');

let counter = 1;
const size = prods[0].clientWidth;

prodMain.style.transform = 'translateX(' + (-size * counter) + 'px)';

next.addEventListener('click', () => {
    if(counter >= prods.length - 1 )return;
    prodMain.style.transition = 'transform .4s ease-in-out';
    counter++;
    prodMain.style.transform = 'translateX(' + (-size * counter) + 'px)'; 
})

prev.addEventListener('click', () => {
    if(counter<=0)return;
    prodMain.style.transition = 'transform .4s ease-in-out';
    counter--;
    prodMain.style.transform = 'translateX(' + (-size * counter) + 'px)'; 
})

prodMain.addEventListener('transitionend', () =>{
    console.log(prods[counter])
    if(prods[counter].id === "lastClone"){
        prodMain.style.transition = 'none';
        counter = prods.length - 2;
        prodMain.style.transform = 'translateX(' + (-size * counter) + 'px)';
    }
    if(prods[counter].id === "firstClone"){
        prodMain.style.transition = 'none';
        counter = prods.length - counter;
        prodMain.style.transform = 'translateX(' + (-size * counter) + 'px)';
    }
})
