import { $ } from ".logger.js"
const form=$(".form")
form.onsubmit=(ev)=>{

    ev.preventDefault()
    const formdata= new FormData(ev.target)
    const addElement = formdata.get("addElement")
    console.log
}
