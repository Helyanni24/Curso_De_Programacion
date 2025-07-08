let screen = document.getElementById('result-display'); // Cambié 'screen' a 'result-display' para que coincida con tu HTML

function insert(value) {
  screen.innerText += value;
}

function insertFunction(fn) {
  screen.innerText += fn + '(';
}

function clearScreen() {
  screen.innerText = '';
}

function deleteLast() {
  screen.innerText = screen.innerText.slice(0, -1);
}

function calculate() {
  try {
    let expression = screen.innerText
      .replace(/÷/g, '/')   // Reemplaza el símbolo de división
      .replace(/×/g, '*')   // Reemplaza el símbolo de multiplicación
      .replace(/^/g, '**') // Reemplaza el símbolo de potencia
      .replace(/sin(/g, 'Math.sin(') // Reemplaza 'sin' por 'Math.sin'
      .replace(/cos(/g, 'Math.cos(') // Reemplaza 'cos' por 'Math.cos'
      .replace(/tan(/g, 'Math.tan(') // Reemplaza 'tan' por 'Math.tan'
      .replace(/sqrt(/g, 'Math.sqrt('); // Reemplaza 'sqrt' por 'Math.sqrt'
      
    screen.innerText = eval(expression);
  } catch (error) {
    screen.innerText = 'Error';
  }
}
