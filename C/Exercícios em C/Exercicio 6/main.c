#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char player[256];
    char player2[256];
    int ret;

    printf("Player 1, sua vez... Pedra, papel ou tesoura? R: ");
    scanf("%s",player);

    printf("Player 2, sua vez... Pedra, papel ou tesoura? R: ");
    scanf("%s",player2);


    if(strcmp(player, "papel") == 0){
        printf("Player 1 digitou papel.");
    }else if(strcmp(player, "tesoura") == 0){
        printf("Player 1 digitou tesoura.");
    }else if(strcmp(player, "pedra") == 0){
        printf("Player 1 digitou pedra.");
    }else{
        printf("Valor invalido.");
    }


    return 0;
}
