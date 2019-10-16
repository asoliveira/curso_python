
def ler_arquivo(caminho):
    """
    Ler arquivos de vendas em csv.
    
    Caminho - string
    caminho do arquivo
    """
    try:
        with open(caminho, 'r') as f:
            vendas = dict()
            destinos  = dict() 
            for i in range(30):    
                linha = f.readline()
                if i >= 5:
                    linha = linha.split(';')
                    if i == 5:
                        origem = linha[0]
                    elif i % 5 == 0:
                        vendas[origem] = destinos
                        destinos = dict()
                        origem = linha[0]
                        
                        
                    destinos[linha[1]] = linha[2:10]
            
            vendas[origem] = destinos
    except FileNotFoundError:
        print('Nao consegui encontrar o arquivo')
    
    return vendas           