/*
* Disciplina: 2026-PCAP
* Problema  : beecrowd 1011 - Esfera
* Autor     : Pedro André P. A. Blaka
* Liac      : ler um numero real (o raio) e calcular seu volume tendo pi como 3.14159, mostrar na tela no formato "VOLUME = volume" com 3 casas decimais
*             
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int r;
    double volume;

    cin >> r;
    volume = (4 / 3.0 ) * 3.14159 * r * r * r;
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << volume << endl;
    return 0;
}