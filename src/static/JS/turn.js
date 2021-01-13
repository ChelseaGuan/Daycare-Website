let timer;
let turn = 0;

function turnOn() {
  timer = setInterval(turnMaple, 270);
}

function turnMaple() {
  let x = document.getElementById("rotate");
  turn += 50;
  x.style.transform = "rotate("+ (turn % 360) +"deg)";
}