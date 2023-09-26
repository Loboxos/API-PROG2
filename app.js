let signInButton = document.getElementById("signIn");
let registroBtn = document.getElementById("registro");
let crearServidorBtn = document.getElementById ("crearServidor")
let buscarServidorBtn = document.getElementById ("buscarServidor")
const medicinaBtn = document.getElementById ("medicina");
let musicaBtn = document.getElementById ("musica");
let juegosBtn = document.getElementById ("juegos");
let deportesBtn = document.getElementById ("deportes");
let literaturaBtn = document.getElementById ("literatura");
let viajesBtn  = document.getElementById ("viajes");
let cineBtn = document.getElementById ("cine");

signInButton.addEventListener("click", function() {
    window.location.href = "pantalla_3.html";
});

registroButton.addEventListener("click",function() {
    window.location.href = "pantalla_3.html";
})

crearServidorBtn.addEventListener("click",function(){
})
crearServidorBtn.addEventListener("mouseover",() =>{       
});

buscarServidorBtn.addEventListener("click",function(){
})
buscarServidorBtn.addEventListener("mouseover",() =>{       
});

medicinaBtn.addEventListener("mouseover",()=>{   
    medicinaBtn.textContent = "Salud y Bienestar";    
});
medicinaBtn.addEventListener("mouseout", ()=> {
    medicinaBtn.textContent = "Medicina"; // Vuelve al texto original cuando se retira el mouse
});
medicinaBtn.addEventListener("click",function(){       
});

musicaBtn.addEventListener("click",function(){ 
})
musicaBtn.addEventListener("mouseover",() =>{       
});

juegosBtn.addEventListener("click",function(){ 
})
juegosBtn.addEventListener("mouseover",() =>{       
});

deportesBtn.addEventListener("click",function(){   
})
deportesBtn.addEventListener("mouseover",() =>{       
});

literaturaBtn.addEventListener("click",function(){
})
literaturaBtn.addEventListener("mouseover",() =>{       
});

viajesBtn.addEventListener("click",function(){
})
viajesBtn.addEventListener("mouseover",() =>{       
});

cineBtn.addEventListener("click",function(){
})
cineBtn.addEventListener("mouseover",() =>{       
});

