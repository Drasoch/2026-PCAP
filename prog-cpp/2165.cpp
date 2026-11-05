/*
* Disciplina: 2026-PCAP
* Problema  : beecrowd 2165 - Twitting
* Autor     : Pedro André P. A. Blaka
* Liac      : le um texto e caso tenha mais de 140 caracteres, mostra MUTE, caso tenha até 140 mostra TWEET;
*             
*/

#include <iostream>
#include <string>
using namespace std;

int main(){
    string texto;

    getline(cin, texto);
    if(texto .size() <= 140){
        cout << "TWEET" << endl;
    } else {
        cout << "MUTE" << endl;
    }
    return 0;
}