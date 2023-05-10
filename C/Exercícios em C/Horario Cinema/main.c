#include <stdio.h>
#include <stdlib.h>

int main()
{
    int hora_cinema = 90;
    int hora_atual = 100;

    int hora_limite_tolerada = hora_cinema + 30;

    if (hora_atual > hora_limite_tolerada){
        printf("Horario limite tolerado já passou, nao podera passar.");
    }else if(hora_atual < hora_cinema - 20){
        printf("As portas do cinema nao abriram, nao podera passar.");
    }else{
    printf("Horario correto, pode passar.");
    }
    return 0;
}
