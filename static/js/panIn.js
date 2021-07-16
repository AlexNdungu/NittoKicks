let bars = document.querySelector('#bars');
let barOpen = true; 
let sideNav = document.querySelector('.sideNav');

 bars.addEventListener('click', ()=>{

   if(barOpen == true){
      sideNav.style.marginLeft = '0';
      barOpen = false;
   }
   else{
      sideNav.style.marginLeft = '-100%';
      barOpen = true;
   }
 })