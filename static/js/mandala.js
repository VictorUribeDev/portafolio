const canvas = document.getElementById('mandalaCanvas');
const ctx = canvas.getContext('2d');

// Configuración inicial del canvas
function resizeCanvas() {
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientWidth;
}
resizeCanvas();

const width = canvas.width;
const height = canvas.height;

// Variables del mandala
const centerX = width / 2;
const centerY = height / 2;
const maxRadius = Math.min(width, height) / 2 - 10;
const numPoints = 24; // Más puntos para suavidad
const numLayers = 50; // Capas del mandala
const speed = 0.02; // Velocidad de dibujo más lenta
let currentLayer = 0;
let transitionProgress = 0; // Progreso de transición entre capas
let isReversing = false;

// Funciones para el mandala
function calculate3DPoints(layer, progress = 1) {
    const points = [];
    const stepAngle = (Math.PI * 2) / numPoints;

    for (let i = 0; i < numPoints; i++) {
        const angle = i * stepAngle;
        const distortion = Math.sin(angle * 6) * 0.3;
        const radius = (layer + progress) * (maxRadius / numLayers);
        const depth = Math.cos(angle + transitionProgress * speed) * 20;

        const finalRadius = radius + distortion * radius;
        points.push({
            x: centerX + finalRadius * Math.cos(angle) + depth,
            y: centerY + finalRadius * Math.sin(angle) + depth,
            depth,
        });
    }

    return points;
}

function getColor(layer) {  
    const grayValue = 50 - (layer * (100 / numLayers)); // Escala de grises  
    return `hsl(0, 0%, ${grayValue}%)`; // HSL para escala de grises  
}  

function draw3DMandala() {
    ctx.fillStyle = 'rgba(240, 240, 255, 1)';
    ctx.fillRect(0, 0, width, height);
    ctx.lineWidth = 2;

    for (let layer = 0; layer < currentLayer; layer++) {
        const points = calculate3DPoints(layer);

        for (let i = 0; i < points.length; i++) {
            const start = points[i];
            const end = points[(i + 1) % points.length];

            ctx.strokeStyle = getColor(layer);
            ctx.beginPath();
            ctx.moveTo(start.x, start.y);
            ctx.lineTo(end.x, end.y);
            ctx.stroke();
        }
    }

    if (!isReversing) {
        const points = calculate3DPoints(currentLayer, transitionProgress);

        for (let i = 0; i < points.length; i++) {
            const start = points[i];
            const end = points[(i + 1) % points.length];

            ctx.strokeStyle = getColor(currentLayer);
            ctx.beginPath();
            ctx.moveTo(start.x, start.y);
            ctx.lineTo(end.x, end.y);
            ctx.stroke();
        }

        transitionProgress += speed;
        if (transitionProgress >= 1) {
            transitionProgress = 0;
            currentLayer++;
            if (currentLayer >= numLayers) {
                isReversing = true;
            }
        }
    } else {
        const points = calculate3DPoints(currentLayer, 1 - transitionProgress);

        for (let i = 0; i < points.length; i++) {
            const start = points[i];
            const end = points[(i + 1) % points.length];

            ctx.strokeStyle = getColor(currentLayer);
            ctx.beginPath();
            ctx.moveTo(start.x, start.y);
            ctx.lineTo(end.x, end.y);
            ctx.stroke();
        }

        transitionProgress += speed;
        if (transitionProgress >= 1) {
            transitionProgress = 0;
            currentLayer--;
            if (currentLayer <= 0) {
                isReversing = false;
                currentLayer = 0;
            }
        }
    }

    requestAnimationFrame(draw3DMandala);
}

draw3DMandala();

window.addEventListener('resize', () => {
    resizeCanvas();
    draw3DMandala();
});