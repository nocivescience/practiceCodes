let balls=[];
balls=[
    {columna: 100, fila: 100, radius: 50, color: "red"},
    {columna: 200, fila: 200, radius: 50, color: "blue"},
    {columna: 300, fila: 300, radius: 50, color: "green"},
    {columna: 400, fila: 400, radius: 50, color: "yellow"},
].map((ball)=>({
    x: ball.columna,
    y: ball.fila,
    r: ball.radius,
    c: ball.color
}))
console.log(balls);

let walls= []
walls=[
    {columna: 100, fila: 100, radius: 50, color: "red"},
    {columna: 200, fila: 200, radius: 50, color: "blue"},
    {columna: 300, fila: 300, radius: 50, color: "green"},
    {columna: 400, fila: 400, radius: 50, color: "yellow"},
]
walls.forEach((wall)=>({
    x: wall.columna,
    y: wall.fila,
    r: wall.radius,
    c: wall.color
}))
console.log(walls); 