def arquivo_entrada():

    with open("circuito_teste.txt", "r") as arquivo_entrada:
        infos = arquivo_entrada.readlines()
        var_entradas = []
        var_saidas = []
        var_gates = []
        var_operacoes = {}
        for linha in infos:
            linha = linha.strip()
            
            if linha.startswith("entradas:"):
                var_entradas = linha.split(":")[1].strip()[1:-1].split(', ')
            elif linha.startswith("saidas:"):
                var_saidas = linha.split(":")[1].strip()[1:-1].split(', ')
            elif linha.startswith("gates:"):
                var_gates = linha.split(":")[1].strip()[1:-1].split(', ')
            elif ':' in linha:
                gate_name, gate_value = linha.split(':', 1)
                gate_name = gate_name.strip()
                gate_value = eval(gate_value.strip())
                var_operacoes[gate_name] = gate_value
                
        print("Entradas: ", var_entradas)
        print("Saidas: ", var_saidas)
        print("Gates: ", var_gates)
        print("Operacoes: ", var_operacoes)
        
    return var_entradas, var_saidas, var_gates, var_operacoes
arquivo_entrada()

def operacoes(tipo_operacao, valor):
    if tipo_operacao == "and":
        return valor[0] & valor[1]
    elif tipo_operacao == "nand":
        return 1 - (valor[0] & valor[1])
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
        print("Operações inválidas")
        

def calcular_operacoes(var_entradas, var_operacoes):
    
    valores = {entrada: 1 for entrada in var_entradas}
    
    for var_gate, operacao in var_operacoes.items():
        tipo_operacao = operacao[0]
        valores_entradas = operacao[1:]
        resultados_entradas = [valores[entrada] for entrada in valores_entradas]
        resultado = operacoes(tipo_operacao, resultados_entradas)
        valores[var_gate] = resultado
        
    print("Resultados dos gates:", valores)


var_entradas, var_saidas, var_gates, var_operacoes = arquivo_entrada()
calcular_operacoes(var_entradas, var_operacoes)
