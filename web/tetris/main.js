//1. inicializar el canvas 
const canvas = document.querySelector("canvas")
const context = canvas.getContext("2d")
 //configuracion de la pantalla y el tamaño de los bloques 

 const BLOCK_SIZE = 20
 const BOARD_WIDTH = 14
 const BOARD_HEIGTH = 30
 //Creando el tablero del tetris 

 context.scale(BLOCK_SIZE,BLOCK_SIZE)

 //3. crear board de 30filas 
const board = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

//4.la pieza del jugador 
const pise = {
    position: { x:5, y:5},
    shape: [
        [1,1],
        [1.1]
    ]
}

 // 2. game gloop < importante esta es el area donde se dibujara nuestro ecenario

 function update() {
    drow()
// loop infinito o tambien conocido funcion recursivas
// una funcion recursiva se llama a si misma 
    window.requestAnimationFrame(update)
 }
 
function drow() {
    //vamos a dibujar nuestro board
    context.fillStyle = "#222"
    context.fillRect(0, 0, canvas.width, canvas.height)

    // pintar el board

    board.forEach((row, y) => {
        row.forEach((value, x) => {
            if (value === 1) {
                context.fillStyle = "red"
                context.fillRect (x, y, 1,1)

            }
        })
    })

    pise.shape.forEach((row, y) => {
        row.forEach((value,x) => {
            if(value === 1) {
                context.fillStyle = "yellow"
                context.fillRect(x + pise.position.x, y + pise.position.y,1,1)
            }
        })
    })
}
//5, mover la pieza

document.addEventListener("keydown", ev => {
    if (ev.key === "ArrowLeft") {
        pise.position.x--
        if (checkCollision()) {
            pise.position.x++
        }
    }
    if (ev.key === "ArrowRight") {
        pise.position.x++
        if (checkCollision()) {
            pise.position.x--
        }
    }
    if (ev.key === "ArrowDown") {
        pise.position.y++
        if (checkCollision()) {
            pise.position.y--
        }
    }
    if (ev.key === "Arrowup") {
        const
    }
})
update()
