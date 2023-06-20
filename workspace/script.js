const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const player1Score = document.getElementById("player1-score");
const player2Score = document.getElementById("player2-score");

const socket = new WebSocket("ws://localhost:8000");

socket.onmessage = function(event) {
    const gameState = JSON.parse(event.data);
    draw(gameState);
    updateScoreboard(gameState);
}

document.addEventListener("keydown", function(event) {
    if (event.code === "ArrowUp" || event.code === "ArrowDown" || event.code === "ArrowLeft" || event.code === "ArrowRight") {
        socket.send(event.code);
    }
});

function draw(gameState) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let snake of gameState.snakes) {
        ctx.fillStyle = snake.color;
        for (let position of snake.body) {
            ctx.fillRect(position.x * 20, position.y * 20, 20, 20);
        }
    }
    for (let food of gameState.food) {
        ctx.fillStyle = "green";
        ctx.fillRect(food.position.x * 20, food.position.y * 20, 20, 20);
    }
}

function updateScoreboard(gameState) {
    player1Score.textContent = `Player 1: ${gameState.players[0].score}`;
    player2Score.textContent = `Player 2: ${gameState.players[1].score}`;
}
