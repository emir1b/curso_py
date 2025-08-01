// importando datos locales del archivo data .js
// import {data} from "./data.js"
const d = document 
const $ = s => d.querySelector(s)

const sect = $(".main-section")
const form = $(".form")
console.log(form);

form.omsubmit = (ev) => {
  ev.preventDefaul()
  const field = new FormData(ev.target)
  const search = field.get("search")
  console.log(field);
}

async function characters(){
  const res = await fetch("https://rickandmortyapi.com/api/character")
  if (!res.ok){
    console.error("error al recibir los datos del servidor .");
  }
  const data = await res.json()
  data.results.forEach(personaje => {
    const card = d.createRange().createContextualFragment(`
      <article class="card">
        <img src="${personaje.image}" />
        <p class="title">${personaje.name}
        </p>
      </article>
      `)
    sect.append(card)
  })

}
//llamando a la funcion personajes 
characters()