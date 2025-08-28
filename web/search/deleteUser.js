import { $, createtablet } from "./main.js";
import data from "./data.js"
const form =$ (".form-delete")


form.addEventListener("submit",(ev) => {
    ev.preventDefault()
    const field = Object.fromEntries(new FormData(ev.target))
    console.log(field.name)
    if (field.name !== " "|| field.age !== " ") {
        data.forEach((element,index) => {
            let name = element.name.toLowerCase()
            let formname = field.name.toLowerCase()
            if (name === formname && element.age === field.age) {
                // el metodo esplice funcionan como una navaja zuiza para arrays. puede insertar remnover y reemplazar elementos
                data.splice(index, 1)
            }
        })
    }
    createtablet()
})