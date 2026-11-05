/*
* Disciplina : 2026-PCAP
* Problema   : beecrowd 1173 - 	Preenchimento de Vetor 1
* Autor      : Pedro André P. A. Blaka
* LIAC       : le um valor e coloca ele em um vetor de 10 posicoes
                Em cada posiçao seguinte coloca-se o dobro do anterior
                Entrada é um valor inteiro <= 50, saída N[posicao] = numero
*/
#include <iostream>
#include <vector>
using namespace std;

void preencher(vector<int> &n, int primeiro){
    int i;

    n.push_back(primeiro);
    for (i = 1; i < 10; i ++){
        n.push_back(n[i - 1] * 2);
    }
}

void mostrar(vector<int> &n){
    int i, qtd = n.size();

    for(i = 0; i < qtd; i++){
        cout << "N[" << i << "] = " << n[i] << endl;
    }
}

int main(){
    vector<int> n;
    int primeiro;

    cin >> primeiro;
    preencher(n, primeiro);
    mostrar(n);

    return 0;
}
