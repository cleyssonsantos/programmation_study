alert("Boas vindas ao jogo do número secreto");
let numeroMaximo = 100;
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1);
let numeroEscolhido;
let tentativas = 1;


while (numeroEscolhido != numeroSecreto) {
    numeroEscolhido = prompt(`Escolha um número entre 1 e ${numeroMaximo}`);
    if (numeroEscolhido == numeroSecreto) {
        break;
    } else {
        if (numeroEscolhido > numeroSecreto) {
            alert(`O número secreto é MENOR que ${numeroEscolhido}.`);
        } else {
            alert(`O número secreto é MAIOR que ${numeroEscolhido}.`);
        }
        tentativas++;
    };
};

// operador ternário - Tentativas é maior que 1 ? Se sim, insere "tentativas" na variavel, caso não, insere "tentativa"
let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
alert(`Isso ai! Você descobriu o número secreto: ${numeroSecreto} com ${tentativas} ${palavraTentativa}.`);
// if (tentativas == 1) {
//     alert(`Isso ai! Você descobriu o número secreto: ${numeroSecreto} com ${tentativas} tentativa.`);
// } else {
//     alert(`Isso ai! Você descobriu o número secreto: ${numeroSecreto} com ${tentativas} tentativas.`);
// };
