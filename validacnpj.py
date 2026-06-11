import re
def validar_cnpj(cnpj_input):
    
    cnpj = re.sub(r'\D', '', str(cnpj_input))

    
    if len(cnpj) != 14 or len(set(cnpj)) == 1:
        return False

    
    for i in (12, 13):
        soma = 0
        peso = i - 7  
        
        for digito in cnpj[:i]:
            soma += int(digito) * peso
            peso -= 1
            if peso < 2:
                peso = 9
                
        digito_calculado = 0 if soma % 11 < 2 else 11 - (soma % 11)
        
        if int(cnpj[i]) != digito_calculado:
            return False

    return True