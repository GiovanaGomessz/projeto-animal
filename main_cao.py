from animal import *
from menu_cao import *
from functions import *

caes = []
personas = []

ayca = Cachorro ("Ayca", "60", "Chowchow", "8", "Marrom")
caes.append(ayca)

luke = Cachorro ("Luke", "57", "labrador", "5", "Branco")
caes.append(luke)

gii = Humano ("Gii", "15", "parda", "brasileira", "1.64")
personas.append(gii)

duda = Humano ("Duda", "17", "parda", "brasileira", "1.61")
personas.append(duda)


while True:
    op = menu_principal()
    if op == 1:
        while True:
            op_2 = menu_secundario()
            if op_2 == 1:
               caes.append (criar_cao())

            elif op_2 == 2:
                listar_cao(caes)

            elif op_2 == 3:
                ver_informacoes_cao(caes)

            elif op_2 == 4:
             buscar_cao(caes)

            elif op_2 == 5:
                while True:
                    op_b = menu_brincar()
                    if op_b == 1:
                        jogar_bolinha(caes)

                    elif op_b == 2:
                        jogar_graveto(caes)

                    elif op_b == 3:
                        dar_um_osso(caes)

                    elif op_b == 4:
                        break

            elif op_2 == 6:
                break

    elif op == 2:
        while True:
            op_3 = menu_terciario()
            if op_3 == 1:
                personas.append (criar_pessoa())

            elif op_3 == 2:
                listar_humano(personas)

            elif op_3 == 3:
                ver_informacoes_humano(personas)

            elif op_3 == 4:
                buscar_humano(personas)

            elif op_3 == 5:
                while True:
                    op_a = menu_acoes()
                    if op_a == 1:
                        comer(personas)

                    elif op_a == 2:
                        beber_agua (personas)

                    elif op_a == 3:
                        ir_ao_banheiro (personas)

                    elif op_a == 4:
                        break

            elif op_3 == 6:
                break


    elif op == 3:
        break




