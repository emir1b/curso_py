const bt= document.querySelector(".bt")
const root=document.querySelector(".root")
bt.addEventListener("click", () => {
    let p = document.createElement("p")
    p.textContent="click"
    root.appendChild(p)
})