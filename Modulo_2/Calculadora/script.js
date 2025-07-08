let screen = document.getElementById('result-display');
let useDegrees = false;

// Modo ángulo: Grados vs. Radianes
document.getElementById('angle-mode').addEventListener('click', () => {
  useDegrees = !useDegrees;
  document.getElementById('angle-mode').innerText = useDegrees ? 'Usar radianes' : 'Usar grados';
});

// Modo oscuro
document.getElementById('toggle-theme').addEventListener('change', (e) => {
  document.body.classList.toggle('dark', e.target.checked);
});

// Insertar valor
function insert(value) {
  if (screen.innerText === '0' || screen.innerText === 'Error') {
    screen.innerText = value;
  } else {
    screen.innerText += value;
  }
}

// Insertar función científica
function insertFunction(fn) {
  screen.innerText += fn + '(';
}

// Limpiar
function clearScreen() {
  screen.innerText = '0';
}

// Borrar último
function deleteLast() {
  let current = screen.innerText;
  screen.innerText = current.length > 1 ? current.slice(0, -1) : '0';
}

// Evaluar
function calculate() {
  try {
    let expression = screen.innerText
      .replace(/÷/g, '/')
      .replace(/×/g, '*')
      .replace(/\^/g, '**')
      .replace(/sqrt\(/g, 'Math.sqrt(')
      .replace(/%/g, '/100');

    if (useDegrees) {
      expression = expression
        .replace(/sin\(/g, 'Math.sin(Math.PI/180*')
        .replace(/cos\(/g, 'Math.cos(Math.PI/180*')
        .replace(/tan\(/g, 'Math.tan(Math.PI/180*');
    } else {
      expression = expression
        .replace(/sin\(/g, 'Math.sin(')
        .replace(/cos\(/g, 'Math.cos(')
        .replace(/tan\(/g, 'Math.tan(');
    }

    let result = eval(expression);
    screen.innerText = result !== undefined ? result : 'Error';
    screen.style.animation = 'pop 0.25s ease';
    setTimeout(() => screen.style.animation = '', 250);
  } catch {
    screen.innerText = 'Error';
  }
}

// Eventos
document.querySelectorAll('button').forEach(btn => {
  btn.addEventListener('click', () => {
    const action = btn.dataset.action;
    const operator = btn.dataset.operator;
    const value = btn.innerText;

    if (action === 'clear') {
      clearScreen();
    } else if (action === 'delete') {
      deleteLast();
    } else if (action === 'calculate') {
      calculate();
    } else if (operator) {
      if (['sin', 'cos', 'tan', 'sqrt'].includes(operator)) {
        insertFunction(operator);
      } else {
        insert(operator);
      }
    } else {
      insert(value);
    }
  });
});
