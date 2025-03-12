// let escolha = prompt("Qual é o da da semana?");

// if (escolha == "Sábado" || escolha == "Domingo") {
//     alert("Bom fim de semana!");
// } else {
//     alert("Boa semana!");
// };

// let escolhaNumero = parseInt(prompt("Escolha um número: "));

// if (escolhaNumero % 2 == 1) {
//     alert(`Número ${escolhaNumero} é ímpar.`);
// } else {
//     alert(`Número ${escolhaNumero} é par.`);
// };

let pontos = parseInt(prompt("Digite seu número de pontos: "));

if (pontos >= 100) {
    alert("Parabéns, você venceu.");
} else {
    alert("Tente novamente para ganhar.");
};

let nomeUsuarioConta = "Cleysson";
let saldoConta = 19000;

alert(`O saldo da conta de ${nomeUsuarioConta} é R$${saldoConta}.`);

let escolhaNome = prompt("Qual é o seu nome?");
alert(`Seja bem vindo, bom dia ${escolhaNome}.`);
