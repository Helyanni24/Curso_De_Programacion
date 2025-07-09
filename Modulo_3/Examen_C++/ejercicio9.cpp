#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> comidas;
    string comida;

    for (int i = 0; i < 3; i++) {
        cout << "Ingresa una de tus comidas favoritas: ";
        cin >> comida;
        comidas.push_back(comida);
    }

    cout << "Tus comidas favoritas son:" << endl;
    for (int i = 0; i < comidas.size(); i++) {
        cout << "- " << comidas[i] << endl;
    }

    return 0;
}