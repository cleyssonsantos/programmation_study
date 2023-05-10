#include <stdio.h>
#include <stdlib.h>

int main()
{
    int contador = 1;
    int limite = 10;

    while(contador <= limite){
        printf("Estamos no primeiro loop");
        if(contador == 3){
            int contador_2 = 5;
            while(contador_2 > 0){
                printf("Estamos no segundo loop");
                contador_2--;
            }
        }
    contador++;
    }
return 0;
}
