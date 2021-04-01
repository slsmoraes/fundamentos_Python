#------ Classe --------
class Calculadora:

    def soma(self, valor_a, valor_b): # Metodos
        return valor_a + valor_b
    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b
    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b
    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b
if __name__ == '__main__':
    calculadora = Calculadora()
    print('soma:          ', calculadora.soma(10, 2))
    print('subtração:     ', calculadora.subtracao(5, 3))
    print('multiplicação: ', calculadora.multiplicacao(10,5))
    print('divisão:       ', calculadora.divisao(100,2))