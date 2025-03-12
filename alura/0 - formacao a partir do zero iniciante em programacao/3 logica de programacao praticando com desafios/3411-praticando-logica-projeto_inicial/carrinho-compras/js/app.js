let totalGeral;
limpar();

function adicionar () {
    // recuperar valores nome do produto, quantidade e valor
    let produto = document.getElementById('produto').value;
    let quantidade = document.getElementById('quantidade').value;
    let nomeProduto = produto.split('-')[0];
    let valorUnitario = produto.split('R$')[1];

    if (quantidade > 0 && nomeProduto) {
        // calcular preço, o nosso subtotal
        let preco = quantidade * valorUnitario;

        // adicionar no carrinho
        let carrinho = document.getElementById('lista-produtos');
        carrinho.innerHTML = carrinho.innerHTML + `<section class="carrinho__produtos__produto">
            <span class="texto-azul">${quantidade}x</span> ${nomeProduto} <span class="texto-azul">R$${valorUnitario}</span>
            </section>`
        document.getElementById('quantidade').value = 0;

        // atualizar o valor total
        totalGeral = totalGeral + preco;
        let campoTotal = document.getElementById('valor-total');
        // Aqui é textContent porque se trata de um parágrafo
        campoTotal.textContent = `R$ ${totalGeral}`;
    } else {
        alert('Produto ou quantidade inválido, insira um valor válido.')
    }
};

function limpar () {
    totalGeral = 0;
    document.getElementById('lista-produtos').innerHTML = '';
    document.getElementById('valor-total').textContent = 'R$ 0';
};