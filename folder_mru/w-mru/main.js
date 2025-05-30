const d = document
const $= s=> d.querySelector(s)
// definir variables
const form=$(".form")
form.onsubmit=(ev)=>{

    ev.preventDefault()
    const formdata= new FormData(ev.target)
    console.log(formdata);
    
}