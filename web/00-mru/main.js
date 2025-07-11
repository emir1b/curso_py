import { $, d } from "./logger.js"
// definir variables
const fruits = ["manzana","naranja"]
const root =$('.root')

fruits.foreach (el=>{
    let p = d.createElement('p')
    p.textcontent = el 
    root.appendChil(p)

})


