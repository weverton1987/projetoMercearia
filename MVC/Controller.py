from Models import Categoria, Produtos, Estoque, Venda, Fornecedor, Pessoa, Funcionario
from Dao import DaoCategoria, DaoEstoque, DaoFornecedor, DaoFuncionario, DaoPessoa, DaoVenda
from datetime import datetime 

class ControllerCategoria:
    def cadastra_categoria(self, nova_categoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == nova_categoria:
                existe = True
                
        if not existe:
            DaoCategoria.salvar(nova_categoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('A categoria que deseja cadastrar, já existe.')
            
    def remover_categoria(self, categoria_remover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoria_remover, x))
        
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe.')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoria_remover:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        estoque = DaoEstoque.ler()
        estoque = list(map( lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem categoria'), x.quantidade) 
                            if(x.produto.categoria == categoria_remover) else(x), estoque))
        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines( i.produto.nome + '|' +
                                i.produto.preco + '|' +
                                i.produto.categoria + '|' +
                                str(i.quantidade))
                arq.writelines('\n')
                
    def alterar_categoria(self, categoria_alterar, categoria_alterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoria_alterar, x))
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoria_alterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoria_alterada) if(x.categoria == categoria_alterar) else(x), x))
                print('Alteração efetuada com sucesso!')
            else:
                print('A categoria que deseja alterar, já existe.')
        else:
            print('A categoria que deseja alterar não existe.')    
            
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')
        estoque = DaoEstoque.ler()
        estoque = list(map( lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoria_alterada), x.quantidade) 
                            if(x.produto.categoria == categoria_alterar) else(x), estoque))
        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines( i.produto.nome + '|' +
                                i.produto.preco + '|' +
                                i.produto.categoria + '|' +
                                str(i.quantidade))
                arq.writelines('\n')
                
    def mostrar_categoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia.')
        else:
            for i in categorias:
                print(f'Categorias: {i.categoria}')
                
class ControllerEstoque:
    def cadastrar_produto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))
        
        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso!')
            else:
                print('Produto ja existe em estoque.')
        else:
            print('Categoria inexistente!')
            
    def remover_produto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
        else:
            print('O produto que deseja remover não existe.')
            
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines( i.produto.nome + '|' +
                                i.produto.preco + '|' +
                                i.produto.categoria + '|' +
                                str(i.quantidade)
                                )
                arq.writelines('\n')
            print('Produto removido com sucesso.')
                
    def alterar_produto(self, nome_alterar, novo_nome, novo_preco, nova_categoria, nova_quatidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == nova_categoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nome_alterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novo_nome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novo_nome, novo_preco, nova_categoria), nova_quatidade) if(x.produto.nome == nome_alterar) else(x), x))
                    print('Produto alterado com sucesso!')
                else:
                    print('Produto ja cadastrado.')
            else:
                print('O produto que deseja alterar não existe')
            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines( i.produto.nome + '|' +
                                    i.produto.preco + '|' +
                                    i.produto.categoria + '|' +
                                    str(i.quantidade)
                                    )
                    arq.writelines('\n')
        else:
            print('A categoria informada não existe.')
            
    def mostrar_estoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio.')
        else:
            print('===========Produtos==========')
            for i in estoque:
                print(  f'Nome: {i.produto.nome}\n'
                        f'Preço: {i.produto.preco}\n'
                        f'Categoria: {i.produto.categoria}\n'
                        f'Qantidade: {i.quantidade}'
                    )
                print('==========================')

class ControllerVenda:
    def cadastrar_venda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if int(i.quantidade) >= int(quantidadeVendida):
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)
                        DaoVenda.salvar(vendido) 
            temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])
        arq = open('estoque.txt', 'w')
        arq.write('')
        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines( i[0].nome + '|' +
                                i[0].preco + '|' +
                                i[0].categoria + '|' +
                                str(i[1])
                                )
                arq.writelines('\n')
        if existe == False:
            print('O produto não existe.')
            return None
        elif not quantidade:
            print('A quantidade vendida não contém em estoque.')
        else:
            print('Venda concluída!')
            return valorCompra
    
    def relatorioProduto(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itens_vendidos.nome
            quantidade = i.quantidade_vendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome,'quantidade': int(quantidade)})
                
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
        print('Esses são os produtos mais vendidos.')
        a = 1
        for i in ordenado:
            print(f'=========Produtos [{a}]==============')
            print(  f'Produto: {i['produto']}\n'
                    f'Quantidade: {i['quantidade']}\n')
            a += 1

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')
        vendasSelecionadas = list(filter(   lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 
                                            and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))
        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(  f'===============Venda [{cont}]===============')
            print(  f'Nome: {i.itens_vendidos.nome}\n'
                    f'Categoria: {i.itens_vendidos.categoria}\n'
                    f'Data: {i.data}\n'
                    f'Quantidade: {i.quantidade_vendida}\n'
                    f'Cliente: {i.comprador}\n'
                    f'Vendedor: {i.vendedor}')
            total += int(i.itens_vendidos.preco) * int(i.quantidade_vendida)
            cont += 1
        print(f'Total vendido: {total}')
        
class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))
        if len(listaCnpj) > 0:
            print('O cnpj já existe.')
        elif len(listaTelefone) > 0:
            print('O telefone ja existe.')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print('Digite cnpj ou telefone válido.')
                
    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) 
                                if(x.nome == nomeAlterar) else(x), x))
            else:
                print('Cnpj ja existe.')
        else:
            print('O fornecedor que desja alterar não existe.')
        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor alterado com sucesso!')
            
    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe.')
            return None
        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor removido com sucesso!')
            
    def mostrarFornecedores(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print('Lista de fornecedores vazia')
        for i in fornecedores:
            print('==============Fornecedores=============')
            print(  f'Categoria fornecida: {i.categoria}\n'
                    f'Nome: {i.nome}\n'
                    f'Telefone: {i.telefone}\n'
                    f'Cnpj: {i.cnpj}'
                    )
            
class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print('Cpf já existe.')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente cadastrado com sucesso.')
            else:
                print('Digite um cpf ou um telefone válido.')
                
    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(   lambda x: Pessoa(novoNome, novoTelefone, novoEmail, novoCpf, novoEndereco) 
                            if(x.nome == nomeAlterar) else(x), x)
                        )
        else:
            print('O cliente que deseja alterar não existe.')
        with open('cliente.txt', 'w') as arq:
            for i in x:
                arq.writelines( i.nome + '|' +
                                i.telefone + '|' +
                                i.cpf + '|' +
                                i.email + '|' +
                                i.endereco
                                )
                arq.writelines('\n')
            print('Cliente alterado com sucesso.')
            
    def removerCliente(self, nome):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O cliente que deseja remover não existe.')
        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines( i.nome + '|' +
                                i.telefone + '|' +
                                i.cpf + '|' +
                                i.email + '|' +
                                i.endereco
                                )
                arq.writelines('\n')
            print('Cliente removido com sucesso.')
    
    def mostrarCliente(self):
        clientes = DaoPessoa.ler()
        if len(clientes) == 0:
            print('Lista de clientes vazia.')
        else:
            for i in clientes:
                print('===========Cliente===========')
                print(  f'Nome: {i.nome}\n'
                        f'Telefone: {i.telefone}\n'
                        f'Cpf: {i.cpf}\n'
                        f'Email: {i.email}\n'
                        f'Endereço: {i.endereco}'
                    )
                
class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))
        if len(listaCpf) > 0:
            print('Cpf já existe.')
        elif len(listaClt) > 0:
            print('Já existe um funcionário com essa clt!')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionário cadastrado com sucesso!')
            else:
                print('Digite um cpf ou telefone válido.')
                
    def alterarFuncionario(self, nomeAlterar,novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(   lambda x: Funcionario(novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) 
                            if(x.nome == nomeAlterar) else(x), x)
                        )
        else:
            print('O funcionário que deseja alterar ja existe.')
        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(
                    i.clt + '|' + i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco
                )
                arq.writelines('\n')
            print('Funcionário alterado com sucesso.')
            
    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O funcionário que deseja remover não existe.')
            return None
        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(
                    i.clt + '|' +
                    i.nome + '|' +
                    i.telefone + '|' +
                    i.cpf + '|' + 
                    i.email + '|' +
                    i.endereco
                )
                arq.writelines('\n')
            print('Usuário removido com sucesso.')
            
    def mostrarFuncionario(self):
        funcionario = DaoFuncionario.ler()
        if len(funcionario) == 0:
            print('Lista de funcionários vazia.')
        for i in funcionario:
            print('==========Funcionários===========')
            print(  f'Clt: {i.clt}\n'
                    f'Nome: {i.nome}\n'
                    f'Telefone: {i.telefone}\n'
                    f'Cpf: {i.cpf}\n'
                    f'Email: {i.email}\n'
                    f'Endereço: {i.endereco}'
                    )
            
