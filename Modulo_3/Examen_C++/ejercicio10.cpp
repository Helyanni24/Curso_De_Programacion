#include <iostream>
using namespace std;

const double PI = 3.14159;

void calcularPerimetro(double radio) {
    double perimetro = 2 * PI * radio;
    cout << "Perimetro del circulo: " << perimetro << endl;
}

int main() {
    double radio;
    cout << "Ingresa el radio del circulo: ";
    cin >> radio;

    calcularPerimetro(radio);
    return 0;
}