#------ Classe --------
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self): # Metodos
        return self.valor_a + self.valor_b
    def subtracao(self):
        return self.valor_a - self.valor_b
    def multiplicacao(self):
        return self.valor_a * self.valor_b
    def divisao(self):
        return self.valor_a / self.valor_b
calculadora = Calculadora(10,2) #instanciar a classe
print(calculadora.valor_a)
print(calculadora.valor_b)
print('soma:          ', calculadora.soma())
print('subtração:     ', calculadora.subtracao())
print('multiplicação: ', calculadora.multiplicacao())
print('divisão:       ', calculadora.divisao())