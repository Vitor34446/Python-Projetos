# orientaçõ a objetos. Uma forma de se programar, paradigma
# classes e objetos

class Veiculo:
    def movimento(self):
        print(f'sou um veiculo e eu me mecho')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None
# setter 

    def set_num_registro(self, registro):
        self.__num_registro = registro


    # getter

    def get_modelo_fab(self):
        print(f'o modelo é {self.__modelo} fabricante é {self.__fabricante}')

    def get_num_registro(self):
        return self.__num_registro



class carro(Veiculo):
    # metodo __init sera erdado
    def movimento(self):
        print(f'sou um carro e ando pelas ruas')


class motocicleta(Veiculo):
    def movimento(self):
        print(f'corro muito')

class aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante,modelo)
    

    def get_categoria(self):
        return self.__cat
    

    def movimento(self):
        print(f'sou um avião e eu voo')
        


if __name__=='__main__':
    # meu_veiculo = Veiculo('GT','Ferrari')
    # meu_veiculo.movimento()
    # # print(meu_veiculo.__modelo)
    # meu_veiculo.get_modelo_fab()
    # meu_veiculo.set_num_registro('234467-9')
    # print(f'registro: {meu_veiculo.get_num_registro()} ')

    # meu_carro = carro('Tesla','Fiat Uno')
    # meu_carro.movimento()
    # meu_carro.get_modelo_fab()

    # seu_carro = carro('Philco','Microondas ambulante')
    # seu_carro.movimento()
    # seu_carro.get_modelo_fab()
    
    # moto = motocicleta('Harley-Davidson','Motinhas')
    # moto.movimento()
    # moto.get_modelo_fab()

    meu_aviao =aviao('Tesla','A3','aquatica')
    meu_aviao.movimento()
    meu_aviao.get_modelo_fab()
    print(f'Categoria: {meu_aviao.get_categoria()}')
    
