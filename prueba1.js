// function getAngle(p1, p2){
//     let angle = Math.atan(p2.y - p1.y, p2.x - p1.x);
//     if(p2.x < p1.x){
//         angle += 2 * Math.PI;
//     }
// }
// console.log(Math.atan(5/(10- 1))===Math.atan(5/(1- 10)+Math.PI));
// const valor1=1;
// const valor2=10;
// const bolaA = {x: 8, y: 16};
// const bolaB = {x: 10, y: 5};
// function analisis(a, b){
//     const nuevo1= valor1 + a.x;
//     const nuevo2= valor2 + a.y;
//     const x= b.x;
//     const y= b.y;
//     return {nuevo1, nuevo2, x, y};
// };
// console.log(analisis(bolaA, bolaB).x);

wall=[
    {col: 0, row: 0, width: 20, height: 20},
    {col: 20, row: 0, width: 20, height: 20},
].map(wall => ({
    x: wall.col * 20,
    y: wall.row * 20,
    w: wall.width * 20,
    h: wall.height * 20,
}));
console.log(wall);