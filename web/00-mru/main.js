const d = document
const $= s=> d.querySelector(s)
// definir variables
const form=$(".form")
const distancia =$(".par")
console.log(distancia)
form.onsubmit=(ev)=>{

    ev.preventDefault()
    const formdata= new FormData(ev.target)
    const vel=formdata.get("vel")
    const timer=formdata.get("timer")
    console.log(vel);
    distancia.textContent= `distancia recorrida ${vel*timer}` 
    console.log(distancia.textContent)
}