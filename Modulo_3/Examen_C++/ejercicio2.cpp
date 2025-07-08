#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double nu1, nu2;
    cout << "Ingresa un numero: ";
    cin >> nu1;
    cout << "Ingresa un segundo numero: ";
    cin >> nu2;

    cout << "Suma: " << nu1 + nu2 << endl;
    cout << "Resta: " << nu1 - nu2 << endl;
    cout << "Multiplicación: " << nu1 * nu2 << endl;
    cout << "División: " << nu1 / nu2 << endl;

    cout << "Potencia: " << pow(nu1, nu2) << endl;
    cout << "Raíz cuadrada: " << sqrt(nu1) << endl;

    return 0;
}