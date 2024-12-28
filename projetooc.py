
# O programa deve aceitar os gates AND, NAND, OR, NOR, NOT, XOR, NXOR.
def operacoes(tipo_operacao, valor):
    if tipo_operacao == "and":
        return 1 if all(valor) else 0
    elif tipo_operacao == "nand":
        return 1 - (1 if all(valor) else 0)
    elif tipo_operacao == "or":
        return valor[0] | valor[1]
    elif tipo_operacao == "nor":
        return 1 - (valor[0] | valor[1])
    elif tipo_operacao == "not":
        return 1 - valor[0]
    elif tipo_operacao == "xor":
        return valor[0] ^ valor[1]
    elif tipo_operacao == "nxor":
        return 1 - (valor[0] ^ valor[1])
    else:
        raise ValueError(f"Operação inválida: {tipo_operacao}")
     
     
     
     
#O arquivo texto de entrada deve conter a descrição de um circuito digital combinacional (combinação de portas), no formato descrito e exemplificado no anexo
def ler_arquivo_entrada():
    arquivo_circuito = {}
    with open("circuito_teste.txt", "r") as arquivo_entrada:
        for linha in arquivo_entrada:
#Formatação das informações que tem que pegar
            tipo, valor = linha.split(':', 1)
            tipo, valor = tipo.strip(), valor.strip()
            if valor.startswith('[') and valor.endswith(']'):
                valor = [item.strip().strip("'").strip('"') for item in valor[1:-1].split(',')]
            arquivo_circuito[tipo] = valor
    return arquivo_circuito
        
        
        
        
def calcular_operacoes(arquivo_circuitos, var_operacoes):
    
    resultados_operacoes = {entrada: valor for entrada, valor in zip(arquivo_circuitos['entradas'], var_operacoes)}
    
    for var_logica in arquivo_circuitos['gates']:
        tipo_operacao, *valores_entradas = arquivo_circuitos[var_logica]
        resultados_entradas = [resultados_operacoes[entrada] for entrada in valores_entradas]
        resultado = operacoes(tipo_operacao.lower(), resultados_entradas)
        resultados_operacoes[var_logica] = resultado

    return resultados_operacoes[arquivo_circuitos['gates'][-1]]




# O arquivo texto gerado como saída deve apresentar o nome do circuito e a Tabela Verdade (TV) do circuito combinatório, com uma linha da TV (entrada e saída) por linha de texto
def combinacoes_tabela_verdade(num_entradas):
    return [[(i >> j) & 1 for j in range(num_entradas - 1, -1, -1)] for i in range(2 ** num_entradas)]

def gerar_tabela_verdade():
    circuito = ler_arquivo_entrada()
    entradas = sorted(circuito['entradas'])
#Formatação da exibição da tabela
    tabela = f"{' | '.join(entradas)} | Saída\n{'-' * (len(entradas) * 6 + 7)}\n"
    
    for combinacao in combinacoes_tabela_verdade(len(entradas)):
        tabela += f"{' | '.join(map(str, combinacao))} | {calcular_operacoes(circuito, combinacao)}\n"
    return tabela



#Criação do arquivo de saida da tabela verdade
def escrever_arquivo_saida():
    with open("arquivo_circuito_saida.txt", "w") as arquivo_saida:
        arquivo_saida.write("Tabela Verdade das Operações\n")
        tabela_verdade_saida = gerar_tabela_verdade()
        arquivo_saida.write(tabela_verdade_saida)
        
escrever_arquivo_saida()
