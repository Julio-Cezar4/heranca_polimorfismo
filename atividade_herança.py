
from abc import ABC, abstractmethod

class Pessoa:

    def __init__(self, nome, endereco, telefone):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        assert type(nome) == str, 'Nome não pode haver números.'
        self._nome = nome

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        assert type(nome) == str, 'Endereço precisa ser palavra.'
        self._endereco = endereco

    @property
    def telefone(self):
        return self._nome

    @telefone.setter
    def telefone(self, telefone):
        assert type(nome) == str, 'Telefone precisa ser escrito em string.'
        self._telefone = telefone

class Fornecedor(Pessoa):

    def __init__(self, nome, endereco, telefone, vcredito, vdivida):
        super().__init__(nome, endereco, telefone)
        self._vcredito = vcredito
        self._vdivida = vdivida

    @property
    def vcredito(self):
        return self._vcredito

    @vcredito.setter
    def vcredito(self, vcredito):
        self._vcredito = vcredito

    @property
    def vdivida(self):
        return self._vdivida

    @vdivida.setter
    def vdivida(self, vdivida):
        self._vdivida = vdivida

    def obtersaldo(self):
        saldo = self._vcredito - self._vdivida
        return saldo

class Empregado(Pessoa, ABC):

    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto):
        super().__init__(nome, endereco, telefone)
        self._codigo_setor = codigo_setor
        self._salario_base = salario_base
        self._imposto = imposto

    @property
    def codigo_setor(self):
        return self._codigo_setor

    @codigo_setor.setter
    def codigo_setor(self, codigo_setor):
        self._codigo_setor = codigo_setor

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self._salario_base = salario_base

    @property
    def imposto(self):
        return self._imposto

    @imposto.setter
    def imposto(self, imposto):
        self._imposto = imposto

    @abstractmethod
    def calcular_salario(self):
        salario_total = self._salario_base - (self._salario_base * self._imposto)
        return salario_total

class Administrador(Empregado):

    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, ajuda_de_custo):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self._ajuda_de_custo = ajuda_de_custo

    @property
    def ajuda_de_custo(self):
        return self._ajuda_de_custo

    @ajuda_de_custo.setter
    def ajuda_de_custo(self, ajuda_de_custo):
        self._ajuda_de_custo = ajuda_de_custo

    def calcular_salario(self):
        salario_total = self._salario_base - (self._salario_base * self._imposto) + self._ajuda_de_custo
        return salario_total

class Operario(Empregado):

    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, valor_producao, comissao):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self._valor_producao = valor_producao
        self._comissao = comissao

    @property
    def valor_producao(self):
        return self._valor_producao

    @valor_producao.setter
    def valor_producao(self, valor_producao):
        self._valor_producao = valor_producao

    @property
    def comissao(self):
        return self._comissao

    @comissao.setter
    def comissao(self, comissao):
        self._comissao = comissao

    def calcular_salario(self):
        salario_total = self._salario_base - (self._salario_base * self._imposto) + (self.valor_producao * self._comissao)
        return salario_total

class Vendedor(Empregado):

    def __init__(self, nome, endereco, telefone, codigo_setor, salario_base, imposto, valor_vendas, comissao):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self._valor_vendas = valor_vendas
        self._comissao = comissao

    @property
    def valor_vendas(self):
        return self._valor_vendas

    @valor_vendas.setter
    def valor_vendas(self, valor_vendas):
        self._valor_vendas = valor_vendas

    @property
    def comissao(self):
        return self._comissao

    @comissao.setter
    def comissao(self, comissao):
        self._comissao = comissao

    def calcular_salario(self):
        salario_total = self._salario_base - (self._salario_base * self._imposto) + (self.valor_vendas * self._comissao)
        return salario_total

if __name__ == '__main__':
    pessoa1 = Fornecedor('Júlio', 'Tambiá', '9825-2462', 3400, 1100)
    pessoa2 = Operario('Hélio', 'Trincheiras', '8837-4879', 4, 4300, 0.10, 1250, 0.50)
    pessoa3 = Vendedor('Cássio', 'Colibris', '9973-8602', 3, 2500, 0.15, 1000, 0.75)

    lista = [pessoa1, pessoa2, pessoa3]

    for pessoa in lista:
        if pessoa == pessoa1:
            print(f'Saldo total de {pessoa.nome}: {pessoa.obtersaldo()}')
        else:
            print(f'Calculo do salário de {pessoa.nome}: {pessoa.calcular_salario()}')