
fila_normal = []
fila_prioridade = []

contador_normal = 0
contador_prioridade = 0


def gerar_Senha(valor):
    global contador_normal, contador_prioridade
    
    if valor.lower() == 'n':
        contador_normal += 1
        tipo_senha = f'N{contador_normal:03d}'
        fila_normal.append(tipo_senha)
    
    elif valor.lower() == 'p':
        contador_prioridade += 1
        tipo_senha = f'P{contador_prioridade:03d}'
        fila_prioridade.append(tipo_senha)
    
    else:
        return 'Tipo de Senha Invalida. digite (N) para Normal ou (P) para Prioridade'
    return tipo_senha

def exibir_senhas():
    print('Fila Normal: ',fila_normal)
    print('Fila Prioridade: ',fila_prioridade)


        
        
    
while True:
    valor = input('Selecione o tipo de Senha: (N)Para Normal ou (P)para Prioridade: ')
    senha_gerada = gerar_Senha(valor)
    print('Senha gerada:', senha_gerada)
    exibir_senhas()
    continuar = input('Deseja gerar outra senha? (S/N): ')
    if continuar.lower() != 's':
        break