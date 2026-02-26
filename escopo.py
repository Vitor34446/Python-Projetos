# escopo glopal e local

var_global = 'curso de Python'

def escreve_texto():
    global var_global
    var_global = 'banco de dados SQL'
    var_local = "Vitor Gabriel"
    print(f'variavel global: {var_global}')
    print(f'variavel local: {var_local}')

if __name__=='__main__':
        print(f'executar função escreve_texto: escreve_texto')
        escreve_texto()

        print('tentar acessar as variaveis diretamente')
        print(f'variavel global: {var_global}')
        # print(f'variavel local: {var_local}')




