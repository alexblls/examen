def read_data(fichero):
    f = open(fichero,mode="rt", encoding="utf-8")
    linea = f.readline()
    cont = 1
    
    diccionariobase = {}
    diccionario = {}

    for i in linea.split(","):
        i = i.replace('\n', '')
        diccionariobase[i] = ""
    linea = f.readline()

    while linea != "":
        diccionario["dato"+str(cont)] = diccionariobase.copy()
        
        contador = 0
        for i in linea.split(","):
            i = i.replace('\n', '')
            diccionario["dato"+str(cont)][list(diccionariobase.keys())[contador]] = i
            contador += 1
        cont += 1
        linea = f.readline()

    return diccionario

def split(diccionario):
    dic1 = {}
    dic2 = {}
    for i in diccionario:

        if diccionario[i]["type"] == "white":
            del diccionario[i]["type"]
            dic1[i]=diccionario[i]
        else: 
            del diccionario[i]["type"]
            dic2[i]=diccionario[i]

    return dic1, dic2

def reduce(diccionario, atributo):
    lista = []
    lista = diccionario[atributo]
    return lista 

diccionario = read_data("winequality.csv")
print(split(diccionario))
print