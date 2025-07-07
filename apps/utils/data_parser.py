import re

def validate_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False
    
def document_to_string(document):
    parsed = f"{document[:3]}.{document[3:6]}.{document[6:9]}-{document[9:]}"
    return parsed

def document_to_number(document):
    return document.replace(".", "").replace("-","").replace("/","")

def phone_to_string(phone):
    if len(phone) == 11:
        parsed = "("+phone[:2]+") "+phone[2:7]+"-"+phone[7:]
    elif len(phone) == 10:
        parsed = "("+phone[:2]+") "+phone[2:6]+"-"+phone[6:]
    else:
        parsed = 'Invalid number len'
    
    return parsed

def phone_to_number(phone):
    return phone.replace("(","").replace(")","").replace("-","").replace(" ","")
