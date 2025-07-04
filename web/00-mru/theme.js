import { d , $ } from "./logger.js"
const bt=$ ('.button-theme')
const html=d.documentElement 
//detecion  automatica de colores modo oscuro o claro" ( let theme )" 
let theme= window.matchMedia('(prefers-color-scheme:dark)')? 'dark':'ligth'

bt.addEventListener('click',()=> {
    const newTheme = theme === 'dark' ? 'ligth' : 'dark'
    setTheme(newTheme)  
    theme = newTheme 
})

function setTheme (newTheme){

    html.setAttribute( 'data-theme' , newTheme )
}
setTheme(theme)
