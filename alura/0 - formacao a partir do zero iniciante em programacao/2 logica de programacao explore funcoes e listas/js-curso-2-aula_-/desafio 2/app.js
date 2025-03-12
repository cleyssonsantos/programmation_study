function calculaImc(altura, peso) {
    let calculo = peso / (altura ** 2);
    console.log(`O resultado do calculo IMC informado é: ${calculo}.`);
}

function converteValorEmDolarParaReal(valor) {
    let conversao = valor * 4.8;
    console.log(`Você está convertendo o valor de $${valor} para R$${conversao}.`);
}

calculaImc(180, 90);
converteValorEmDolarParaReal(10);