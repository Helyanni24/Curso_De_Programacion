#include <iostream>
using namespace std;


float calcularAreaRectangulo(float base, float altura);

int main() {
    float base, altura;
    cout << "Ingresea la base: ";
    cin >> base;
    cout << "Ingresa la altura: ";
    cin >> altura;

    float area = calcularAreaRectangulo(base, altura);
    cout << "El Área del rectángulo es: " << area << endl;

    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    return base * altura;
}