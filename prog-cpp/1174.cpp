/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1174 - Selecao em Vetor 1
* Autor      : Pedro André P. A. Blaka
* LIAC       : le um vetor A[100], E mostrar todas as posicoes onde os numeros sao menores ou iguais a 10 e o valor nessas posições
*/
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main(){
    vector<double> a;
    double x;
    int i, qtd;

    for(i = 0; i < 100; i++){
        cin >> x;
        a.push_back(x);
    }

    qtd = a.size();
    cout << fixed << setprecision(1);
    for (i = 0; i < qtd; i++){
        if (a[i] <= 10){
            cout << "A[" << i << "] = " << a[i] << endl;
        }
    }
    return 0;
}