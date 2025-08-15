import data from "./data.js";

export const d  = document 
export const $ = s => d.querySelector(s)                                                                                                    
export const $$ = s => d.querySelectorAll(s)

const formSearch = $(".form-search")
const contentcard= $(".content-card")

//funcion que crea una tabla con contenidpo dinamico
export function createtablet(){
    let tr = ""
    data.forEach(el => {
        tr += `
            <tr class="content-tablet">
                <td>${el.name}</td>
                <td>${el.age}</td>
            </tr>
        `
    })
    let table = `
    <table>
    <thead>
    <tr>
    <th>name</th>
    <th>age</th>
    </tr>
    </thead>

    <tbody>
     ${tr}
    </tbody>
    </table>
    `
    contentcard.innerHTML = table

}
createtablet()

//funcion que se encaargara de filtrar los elementos de la tabla 
formSearch.addEventListener("submit", (ev) => {
     ev.preventDefault()
     const field = new FormData(ev.target)
     const search= field.get("search")
     const rows = $$ (".content-tablet")

     rows.forEach(row => {
        const rowtext = row 
        if (row.includes.search) {
            row.classList.add("filder")
        } else {
             row.classList.remove("filder")
        }
     })
    
})