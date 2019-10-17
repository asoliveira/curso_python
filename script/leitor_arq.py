
import pandas as pd

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

def ler_vendas(caminho, planilha='Vendas por Região'):
    """
    Ler o arquivo de dados de vendas de biodiesel 
    apresentasdo pela anp no site:
    http://www.anp.gov.br/producao-de-biocombustiveis/biodiesel/informacoes-de-mercado
    """
        
    dfex = pd.read_excel(caminho, sheetname=planilha,
                         skiprows=3, skip_footer=4)
    
    dfex.iloc[:,:2] = dfex.iloc[:,:2].fillna(method='ffill')
    dfex.drop(labels=['Total'], axis=1, inplace=True)
    col_to_index = dfex.columns[:2].tolist()
    dfex = dfex.set_index(col_to_index)
    dfex = dfex.stack()
    dfex = dfex.reset_index()
    dfex.columns = dfex.columns.tolist()[:2] + ['data', 'volume']
      
    
    return dfex      