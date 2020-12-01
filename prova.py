class Pessoa(object):
  def __init__(self, Nome, Rg, Cpf, Endereco):
    self.Nome = Nome
    self.Rg = Rg
    self.Cpf = Cpf
    self.Endereco = Endereco   


class Funcionario(Pessoa):
  def __init__(self, Nome, Rg, Cpf, Endereco, Locacao, Matricula):
    Pessoa.__init__(self, Nome, Rg, Cpf, Endereco)
    self.Locacao = Locacao
    self.Matricula = Matricula


class Gerente(Funcionario):
  def __init__(self, Nome, Rg, Cpf, Endereco, Locacao, Matricula, Num_func):
    Funcionario.__init__(self, Nome, Rg, Cpf, Endereco, Locacao, Matricula)
    self.Num_func = Num_func
  
  def mostrar_dados(self):
    print("Nome: ", self.Nome)  
    print("Rg: ",  self.Rg)  
    print("Cpf: ", self.Cpf)
    print("Endereco: ", self.Endereco)
    print("Locacoa: ", self.Locacao)
    print("Matricula: ", self.Matricula)
    print("Num_func: ", self.Num_func)

class Tecnico(Funcionario):
  def __init__(self, Nome, Rg, Cpf, Endereco, Locacao, Matricula, Cod_Gerente):
    Funcionario.__init__(self, Nome, Rg, Cpf, Endereco, Locacao, Matricula)
    self.Cod_Gerente = Cod_Gerente


class Cliente(Pessoa):
  def __init__(self, Nome, Rg, Cpf, Endereco, Codigo):
    Pessoa.__init__(self, Nome, Rg, Cpf, Endereco)
    self.Codigo = Codigo

Jose = Gerente("José", "13.614.448-0", "117.645.989-97", "Rua Amazonas 12", "18878792", 123, 21)
Jose.mostrar_dados()
input()
