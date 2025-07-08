document.addEventListener('DOMContentLoaded', function() {
    const display = document.getElementById('result');
    const buttons = document.querySelectorAll('.btn');
    const themeToggle = document.getElementById('theme-toggle');
    let currentInput = '0';
    let previousInput = '';
    let operation = null;
    let resetScreen = false;

    // Toggle del tema oscuro
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark');
    });

    // Actualizar la pantalla
    function updateDisplay() {
        display.value = currentInput;
        // Efecto "pop" al actualizar
        display.parentElement.style.animation = 'none';
        void display.parentElement.offsetWidth; // Trigger reflow
        display.parentElement.style.animation = 'pop 0.25s ease';
    }

    // Manejar entrada de números
    function inputNumber(number) {
        if (currentInput === '0' || resetScreen) {
            currentInput = number;
            resetScreen = false;
        } else {
            currentInput += number;
        }
    }

    // Manejar entrada de punto decimal
    function inputDecimal() {
        if (resetScreen) {
            currentInput = '0.';
            resetScreen = false;
            return;
        }
        if (!currentInput.includes('.')) {
            currentInput += '.';
        }
    }

    // Manejar operaciones
    function handleOperation(op) {
        if (operation !== null && !resetScreen) {
            calculate();
        }
        previousInput = currentInput;
        operation = op;
        resetScreen = true;
    }

    // Calcular resultado
    function calculate() {
        let result;
        const prev = parseFloat(previousInput);
        const current = parseFloat(currentInput);
        
        if (isNaN(prev) || isNaN(current)) return;
        
        switch (operation) {
            case '+':
                result = prev + current;
                break;
            case '-':
                result = prev - current;
                break;
            case '*':
                result = prev * current;
                break;
            case '/':
                result = current !== 0 ? prev / current : 'Error';
                break;
            case '%':
                result = prev % current;
                break;
            default:
                return;
            case '^':
                result = Math.pow(prev, current);
                break;
        }
        
        currentInput = typeof result === 'number' ? result.toString() : result;
    operation = null;
    }

    // Funciones especiales
    function handleSpecialFunction(func) {
        const num = parseFloat(currentInput);
        
        switch (func) {
            case 'AC':
                currentInput = '0';
                previousInput = '';
                operation = null;
                break;
            case 'DEL':
                if (currentInput.length === 1 || (currentInput.length === 2 && currentInput.startsWith('-'))) {
                    currentInput = '0';
                } else {
                    currentInput = currentInput.slice(0, -1);
                }
                break;
            case '√':
                if (num >= 0) {
                    currentInput = Math.sqrt(num).toString();
                } else {
                    currentInput = 'Error';
                }
                break;
            case 'cos':
                currentInput = Math.cos(num * Math.PI / 180).toString(); // Convertir a radianes
                break;
            case 'tan':
                currentInput = Math.tan(num * Math.PI / 180).toString(); // Convertir a radianes
                break;
            case '^':
                operation = '^';
                previousInput = currentInput;
                resetScreen = true;
                break;
        }
    }

    // Event listeners para los botones
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const value = button.getAttribute('data-value');
            
            if (button.classList.contains('number') && value !== '.') {
                inputNumber(value);
            } else if (value === '.') {
                inputDecimal();
            } else if (button.classList.contains('operator') && value !== '=') {
                handleOperation(value);
            } else if (button.id === 'equals') {
                calculate();
                resetScreen = true;
            } else if (button.classList.contains('function')) {
                handleSpecialFunction(value);
            }
            
            updateDisplay();
        });
    });

    // Inicializar la pantalla
    updateDisplay();
});