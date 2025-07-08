#include <iostream>
using namespace std;

int main() {
    int numSecreto = 24;
    int inte;
    cout << "Adivina el número secreto: ";

    while (true) {
        cin >> inte;

        if (inte < numSecreto) {
            cout << "Estas cerca, un numero mas alto. Intenta de nuevo: ";
        } else if (inte > numSecreto) {
            cout << "Mas bajo. Intenta de nuevo: ";
        } else {
            cout << "Has adivinado el número." << endl;
            break;
        }
    }
    return 0;
}
