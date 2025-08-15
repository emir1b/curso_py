import { $, createtablet } from "./main.js";
import data from "./data.js"
const form =$ (".form-delete")

form.addEventListener("submit",(ev) => {
    ev.preventDefault()
    const field = Object.fromEntries(new FormData(ev.target))

 data.push(field)
 createtablet()
})