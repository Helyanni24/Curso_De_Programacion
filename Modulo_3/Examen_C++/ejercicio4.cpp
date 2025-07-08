#include <iostream>
using namespace std;

#define LIMITE 10

int main() {
    int num;
    cout << "Ingresa un numero: ";
    cin >> num;

    cout << "Tabla de Multiplicar" << endl;
    for (int i = 1; i <= LIMITE; i++) {
        cout << num << " x " << i << " = " << num * i << endl;
    }
    return 0;
}
