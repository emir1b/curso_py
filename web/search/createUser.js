import { $, createtablet } from "./main.js";
import data from "./data.js"
const form =$ (".form-create")

form.addEventListener("submit",(ev) => {
  ev.preventDefault()
  const field = Object.fromEntries(new FormData(ev.target))
  console.log(field)
 data.push(field)
 createtablet()
})

