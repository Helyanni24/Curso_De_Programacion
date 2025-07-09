#include <iostream>
using namespace std;

void modificarPorValor(int num) {
    num += 10;
}

void modificarPorReferencia(int &num) {
    num += 10;
}

int main() {
    int num = 20;
    cout << "Valor inicial: " << num << endl;

    modificarPorValor(num);
    cout << "Después de modificar Por Valor: " << num << endl;

    modificarPorReferencia(num);
    cout << "Después de modificar Por Referencia: " << num << endl;

    return 0;
}