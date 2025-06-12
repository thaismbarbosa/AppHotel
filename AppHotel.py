class Hotel:

    def __init__(self):
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f'Funcionário {funcionario.nome} adicionado.')

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)
        print(f'Quarto {quarto.numero} do tipo {quarto.tipo} adicionado.')

    def fazer_reserva(self, hospede, tipo_quarto, dias):
        for quarto in self.quartos:
            if quarto.tipo == tipo_quarto and not quarto.ocupado:
                reserva = Reserva(hospede, quarto, dias)
                self.reservas.append(reserva)
                quarto.ocupado = True
                quarto.hospede_atual = hospede
                print(f'Reserva feita para {hospede} no quarto {quarto.numero} por {dias} dias')
                return reserva
        print("Não há quartos disponíveis desse tipo.")
        return None
    
    def listar_reservas(self):
        if not self.reservas:
            print("Nenhuma reserva no momento.")
        for reserva in self.reservas:
            print(f"Hospede: {reserva.hospede}, Quarto: {reserva.quarto.numero}, Dias: {reserva.dias}, Valor: R${reserva.valor_total:.2f}")
        
class Funcionario:

    def __init__(self, nome, funcao, salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario
        
class Quarto:
    def __init__(self, numero, tipo, preco_por_noite):
        self.numero = numero
        self.tipo = tipo
        self.preco_por_noite = preco_por_noite
        self.ocupado= False
        self.hospede_atual = None
    
class Reserva:
    def __init__(self, hospede, quarto, dias):
        self.hospede = hospede
        self.quarto = quarto
        self.dias = dias
        self.valor_total = dias * quarto.preco_por_noite
        
    
    
    