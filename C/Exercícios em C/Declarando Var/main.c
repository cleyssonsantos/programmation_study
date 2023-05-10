#include <stdio.h>
#include <stdlib.h>

int main()
{
    char nome[256];
    char sobrenome[256];
    int idade;
    int ano_nascimento;

    printf("Qual seu nome?!\n");
    scanf("%s", nome);

    printf("\nQual seu sobrenome?\n");
    scanf("%s", sobrenome);

    printf("\nQual seu ano de nascimento?\n");
    scanf("%d", &ano_nascimento);

    printf("\nQual sua idade?\n");
    scanf("%d", &idade);

    printf("\nSeja bem vindo ao sistema %s %s! Seu ano de nascimento é %d e sua idade é %d.", nome, sobrenome, ano_nascimento, idade);

    return 0;
}
