function sortear() {
    let quantidadeDeNumeros = parseInt(document.getElementById("quantidade").value); // Sem o .value a gente pega a TAG HTML inteira, a TAG input
    let de = parseInt(document.getElementById("de").value);
    let ate = parseInt(document.getElementById("ate").value);

    let sorteados = []
    let numero;

    for (let i = 0; i < quantidadeDeNumeros; i++) {
        numero = obterNumeroAleatorio(de, ate);
        
        // includes devolve um booleano, e se for verdadeiro é porque o numero está dentro do array
        while (sorteados.includes(numero)) {
            numero = obterNumeroAleatorio(de, ate);
        }

        sorteados.push(numero);
    }

    let resultado = document.getElementById("resultado"); // Aqui eu quero pegar a TAG mesmo, e não o valor.
    // Utilizamos o .textContent quando queremos inserir ou modificar um texto simples dentro de um elemento HTML.
    resultado.innerHTML = `<label class="texto__paragrafo">Números sorteados: ${sorteados}</label>`

    alterarStatusBotao();

};

function obterNumeroAleatorio (numeroMin, numeroMax) {
    return Math.floor(Math.random() * (numeroMax - numeroMin + 1)) + 1;
}

function alterarStatusBotao () {
    let botao = document.getElementById("btn-reiniciar");
    if (botao.classList.contains("container__botao-desabilitado")) {
        botao.classList.remove("container__botao-desabilitado");
        botao.classList.add("container__botao");
    } else {
        botao.classList.remove("container__botao");
        botao.classList.add("container__botao-desabilitado");
    }
}

function reiniciar () {
    document.getElementById("quantidade").value = "";
    document.getElementById("de").value = "";
    document.getElementById("ate").value = "";
    document.getElementById("resultado").innerHTML = '<label class="texto__paragrafo">Números sorteados:  nenhum até agora</label>';

    alterarStatusBotao();
}
