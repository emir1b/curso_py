//seleccionar el form
const form=document.querySelector("form")
//metohod onsubmit obtener los datos del formulario 

form.onsubmit=(ev)=>{
    ev.preventdefault()
    constformdata=newformdata(ev.target)
}
const bt =document.querySelector(".button-theme")
const html =document.documentElement
let theme = window.matchMedia("(prefers-color-sheme:dark")?"dark":"ligth"

bt.addEventListener("click",()=> {
    let newtheme=theme==="ligth" ?"dark" :"ligth"
    setTheme(newtheme)
    theme=newtheme

}) 
function setTheme(newtheme) {
    html.setAttribute("data-theme",theme)
}
setTheme(theme)