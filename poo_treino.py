class Esporte:
    def atividade(self):
        print(f'Trabalho o meu corpo')

    def __init__(self,correr,pular):
        self.__correr=correr
        self.__pular=pular
        self.__agachar= None

    def set_agachar(self,agachar):
        self.__agachar= agachar

    def get_agachar(self):
        return self.__agachar
    
    def get_correr_pular(self):
        print(f'Corro {self.__correr} e pulo {self.__pular}, assim como outras coisas')


class futebol(Esporte):
    def atividade(self):
        print(f'corro para fazer o gol')

class natação(Esporte):
    def atividade(self):
        print(f'Nado nos rios')

    def __init__(self, correr, pular, nadar):
        self.__nadar = nadar
        super().__init__(correr, pular)


if __name__=='__main__':

    esporte = Esporte('rapido','alto')
    esporte.atividade()
    esporte.get_correr_pular()
    esporte.set_agachar('baixo')
    print(f'Agacha como?:{esporte.get_agachar()}')

    
        
