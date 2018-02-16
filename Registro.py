import re
import time
import os

def Limpa_Tela():
    os.system('cls||clear')

try:
    Limpa_Tela()
    nome = str(input('Nome completo: '))
    if re.findall('[@]', nome):
        print('\nCaractere especial encontrado!\nTente novamente!')
        time.sleep(2)
    else:
        val_mail = str(input('E-mail: '))

        if re.findall('.com', val_mail) or re.findall('.br', val_mail):
            con_mail = str(input('Confirme o e-mail: '))
            if val_mail == con_mail:
                print('Ok')
            else:
                print('\nEmail não corresponde!\nTente novamente!')
                time.sleep(2)
        else:
            print('\nEmail invalido!\nTente novamente!')
            time.sleep(2)

except KeyboardInterrupt:
    print()