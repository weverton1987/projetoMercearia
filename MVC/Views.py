import Controller
import os.path

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')
criarArquivos('categoria.txt', 'venda.txt', 'funcionario.txt', 'estoque.txt', 'fornecedor.txt', 'cliente.txt')

if __name__ == '__main__':
    while True:
        local = int(input(
            'Digite 1 para acessar ( Categorias )\n'
            'Digite 2 para acessar ( Estoque )\n'
            'Digite 3 para acessar ( Fornecedores )\n'
            'Digite 4 para acessar ( Clientes )\n'
            'Digite 5 para acessar ( Funcionários )\n'
            'Digite 6 para acessar ( Vendas )\n'
            'Digite 7 para ver os produtos mais vendidos\n'
            'Digite 8 para sair.\n'
        ))
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input(
                    'Digite 1 para cadastrar uma categoria\n'
                    'Digite 2 para remover uma categoria\n'
                    'Digite 3 para alterar uma categoria\n'
                    'Digite 4 para mostrar as categorias cadastradas\n'
                    'Digite 5 para voltar\n'
                ))
                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar\n')
                    cat.cadastra_categoria(categoria)
                elif decidir == 2:
                    categoria = input('Digite a categoria que deseja remover\n')
                    cat.remover_categoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar\n')
                    novaCategoria = input('Digite a nova categoria\n')
                    cat.alterar_categoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrar_categoria()
                else:
                    break
        if local == 2:
            est = Controller.ControllerEstoque()
            while True:
                decidir =int(input(
                    'Digite 1 para cadastrar um produto\n'
                    'Digite 2 para remover um produto\n'
                    'Digite 3 para alterar um produto\n'
                    'Digite 4 para ver o estoque\n'
                    'Digite 5 para voltar ao menu principal\n'
                ))
                if decidir == 1:
                    produto = input('Digite o produto que deseja cadastrar\n')
                    preco = input('Digite o preço do produto que deseja cadastrar\n')
                    categoria = input('Digite a categoria do produto que deseja cadastrar\n')
                    quantidade = input('Digite a quantidade do produto que deseja cadastrar\n')
                    est.cadastrar_produto(produto, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input('Digite o produto que deseja remover\n')
                    est.remover_produto(produto)
                elif decidir == 3:
                    produto = input('Digite o produto que deseja alterar\n')
                    novoProduto = input('Digite o nome do novo produto\n')
                    est.alterar_produto(produto, novoProduto)
                elif decidir == 4:
                    est.mostrar_estoque()
                else:
                    break
        if local == 3:
            forn = Controller.ControllerFornecedor()
            while True:
                    decidir = int(input('Digite 1 para cadastrar fornecedor\n'
                                    'Digite 2 para alterar fornecedor\n'
                                    'Digite 3 para remover fornecedor\n'
                                    'Digite 4 para mostrar os fornecedores\n'
                                    'Digite 5 para voltar\n'
                                    ))
                    if decidir == 1:
                        nome = input('Digite o nome:\n')
                        cnpj = input('Digite o cnpj:\n')
                        telefone = input('Digite o telefone:\n')
                        categoria = input('Digite o categoria:\n')
                        forn.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                    elif decidir == 2:
                        nomeAlterar = input('Digite o nome que deseja alterar\n')
                        novoNome = input('Digite o novo nome\n')
                        novoCnpj = input('Digite o novo cnpj\n')
                        novoTelefone = input('Digite o novo telefone\n')
                        novaCategoria = input('Digite a nova categoria\n')
                        forn.alterarFornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria)
                    elif decidir == 3:
                        nome = input('Digite o nome que deseja remover\n')
                        forn.removerFornecedor(nome)
                    elif decidir == 4:
                        forn.mostrarFornecedores()
                    else:
                        break
        if local == 4:
            clie = Controller.ControllerCliente()
            while True:
                decidir = int(input(
                    'Digite 1 para cadastrar cliente\n'
                    'Digite 2 para alterar cliente\n'
                    'Digite 3 para remover cliente\n'
                    'Digite 4 para mostar os clientes cadastrados\n'
                    'digite 5 para voltar\n'
                ))
                if decidir == 1:
                    nome = input('Digite o nome\n')
                    cpf = input('Digite o cpf:\n')
                    telefone = input('Digite o numero do telefone:\n')
                    email = input('Digite seu email:\n')
                    endereco = input('Digite seu endereço:\n')
                    clie.cadastrarCliente(nome, cpf, telefone, email, endereco)
                elif decidir == 2:
                    nomeAlterar = input('Digite o nome que deseja alterar:\n')
                    novoNome = input('Digite o novo nome:\n')
                    novoTelefone = input('Digite o novo número de telefone:\n')
                    novoCpf = input('Digite o novo número do cpf:\n')
                    novoEmail = input('Digite o novo email:\n')
                    novoEndereco = input('Digite o novo endereço:\n')
                    clie.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 3:
                    nome = input('Digite o nome que deseja remover:\n')
                    clie.removerCliente(nome)
                elif decidir == 4:
                    clie.mostrarCliente()
                else:
                    break
        if local == 5:
            func = Controller.ControllerFuncionario()
            while True:
                decidir = int(input(
                    'Digite 1 para cadastrar funcionário\n'
                    'Digite 2 para alterar funcionário\n'
                    'Digite 3 para remover funcionário\n'
                    'Digite 4 para mostrar funcionários\n'
                    'Digite 5 para voltar\n'
                ))
                if decidir == 1:
                    clt = input('Digite o número da clt do funcionário:\n')
                    nome = input('Digite o nome do funcionário:\n')
                    telefone = input('Digite o número do telefone do funcionário:\n')
                    cpf = input('Digite o cpf do funcionário:\n')
                    email = input('Digite o email do funcionário:\n')
                    endereco = input('Digite o endereço do funcionário:\n')
                    func.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    nomeAlterar = input('Digite o nome que quer alterar:\n')
                    novoNome = input('Digite o novo nome:\n')
                    novaClt = input('Digite o novo número da clt:\n')
                    novoTelefone = input('Digite o novo número de telefone:\n')
                    novoCpf = input('Digite o novo número do cpf:\n')
                    novoEmail = input('Digite o novo email:\n')
                    novoEndereco = input('Digite o novo endereço:\n')
                    func.alterarFuncionario(nomeAlterar,novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 3:
                    nome = input('Digite o nome que deseja remover:\n')
                    func.removerFuncionario(nome)
                elif decidir == 4:
                    func.mostrarFuncionario()
                else:
                    break
        if local == 6:
            ven = Controller.ControllerVenda()
            while True:
                decidir = int(input(
                    'Digite 1 para cadastrar uma venda\n'
                    'Digite 2 para ver o relatório dos produtos\n'
                    'Digite 3 para mostrar todas as vendas\n'
                    'Digite 4 para voltar\n'
                ))
                if decidir == 1:
                    nomeProduto = input('Digite o nome do produto:\n')
                    vendedor = input('Digite o nome do vendedor:\n')
                    comprador = input('Digite o nome do comprador:\n')
                    quantidadeVendida = input('Digite a quantidade vendida:\n')
                    ven.cadastrar_venda(nomeProduto, vendedor, comprador, quantidadeVendida)
                elif decidir == 2:
                    ven.relatorioProduto()
                elif decidir == 3:
                    dataInicio = input('Digite a data de início no formato de dd/mm/aaaa')
                    dataTermino = input('Digite a data de término no formato de dd/mm/aaaa')
                    ven.mostrarVenda(dataInicio, dataTermino)
                else:
                    break
        if local == 7:
            a = Controller.ControllerVenda()
            while True:
                decidir = int(input(
                    'Digite 1 para ver os produtos mais vendidos\n'
                    'Digite 2 para voltar\n'
                ))
                if decidir == 1:
                    a.relatorioProduto()
                else:
                    break
        else:
            break