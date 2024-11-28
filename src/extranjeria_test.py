from extranjeria import *

if __name__=="__main__":
    lista_tuplas:list[RegistroExtranjeria] = lee_cvs("data/extranjeriaSevilla.csv")
    #print(lee_cvs("data/extranjeriaSevilla.csv"))
    #print(numero_nacionalidades_distintas(lista_tuplas))
    conjunto_cadenas = nombres_nacionalidades_distintas(lista_tuplas)
    #print(secciones_distritos_con_extranjeros_nacionalidades(lista_tuplas, conjunto_cadenas))
    #print(total_extranjeros_por_pais(lista_tuplas))
    print(top_n_extranjeria(lista_tuplas))