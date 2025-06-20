const d =document
const $ = s => d.querySelector(s)
const $$ = s => d.querySelectorAll(s)

const cl  = s=>console.log(s);

const form=$(".form")

const button = $(".form-button")

const fruit  = ["manzana","naranja" ]

const section=$(".main-section")

form.omsubmit =  (event) => {
    event.preventDefault()
    const formData =new FormData(event.target)
    const busquedaosearch= formData.get("bs")
    const p =$$(".fruta")
    p.forEach((element => {
        if (element.textContent===busquedaosearch) {
            element.classList.add("active")
        } else if (element.textContent!==busquedaosearch) {
            element.claslist.remuve("active")
        }
    }))

}

//sobre una lista de frutas 
// usando la funcion forEach()
fruit.forEach((element,index) => {
    let p = d.createElement("p")
    p.textContent=element
    p.setAttribute("class","fruta")
    section.appendchil("p")
})