let screen = document.getElementById('screen');

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
      .replace(/÷/g, '/')
      .replace(/×/g, '*')
      .replace(/\^/g, '**');
    screen.innerText = eval(expression);
  } catch (error) {
    screen.innerText = 'Error';
  }
}
