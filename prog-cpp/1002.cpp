/*
* Disciplina: 2026-PCAP
* Problema  : beecrowd 1002 - Área do Círculo
* Autor     : Pedro André P. A. Blaka
* Liac      : ler um numero real (o raio) e calcular sua area tendo pi como 3.14159, mostrar na tela no formato "A=area" com 4 casas decimais
*/

#include <iostream>
#include <iomanip>
using namespace std;

int main (){
    double r, area;

    cin >> r;
    area = 3.14159 * r * r;
    cout << fixed << setprecision(4);
    cout << "A=" << area << endl;
    return 0;
}