
from collections import defaultdict, namedtuple
import csv


RegistroExtranjeria = namedtuple('RegistroExtranjeria', 'distrito,seccion,barrio,pais,hombres,mujeres')

def lee_cvs(rutaCSV:str)->list[RegistroExtranjeria]:
    with open(rutaCSV, mode="r", encoding="utf-8") as r:
        res = []
        lineas = csv.reader(r, delimiter=",")
        next(lineas)
        for campo in lineas:
            distrito:str = campo[0].strip()
            seccion:str = campo[1].strip()
            barrio:str = campo[2].strip()
            pais:str = campo[3].strip()
            hombres:int = int(campo[4].strip())
            mujeres:int = int(campo[5].strip())

            res.append(RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres))
    return res

def numero_nacionalidades_distintas(registros):
    conjunto_nacionalidades:set[str] = {r.pais for r in registros}
    return len(conjunto_nacionalidades)

def nombres_nacionalidades_distintas(registros):
    conjunto_nacionalidades:set[str] = {r.pais for r in registros}
    return set(list(conjunto_nacionalidades)[:10])

def secciones_distritos_con_extranjeros_nacionalidades(registros,  paises):
    res = [(registro.distrito, registro.seccion) for registro in registros if registro.pais in paises]
    return sorted(res)

def total_extranjeros_por_pais(registros):
    res = defaultdict(int)
    for registro in registros:
        res[registro.pais] += registro.hombres + registro.mujeres
    return res

def top_n_extranjeria(registros,  n=3):
    dicc = total_extranjeros_por_pais(registros)
    res = sorted(dicc.items(), key=lambda x:x[1], reverse=True)[:n]
    return res

def barrio_mas_multicultural(registros):
    dicc = agrupacion_por_barrio(registros)
    #res = max(dicc, key=lambda x: len(dicc.get(x)))
    res = max(dicc.items(), key=lambda x: len(x[1]))[0]
    return res

def agrupacion_por_barrio(resgistros):
    res = defaultdict(set)
    for registro in resgistros:
        res[registro.barrio].add(registro.pais)
    return res

def barrio_con_mas_extranjeros(registros, tipo=None):
    res = defaultdict()
    for registro in registros:
        clave = registro.barrio
        if tipo is None or tipo.upper() == "HOMBRES":
            res[clave] += registro.hombres
        if tipo is None or tipo.upper() == "MUJERES":
            res[clave] += registro.mujeres
    return res

def pais_mas_representado_por_distrito(registros):
    d_total = total_extranjeros_por_pais(registros)
    res = max(d_total, key=d_total.get)
    return res
