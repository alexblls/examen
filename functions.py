def read_data(fichero):
    f = open(fichero,mode="rt", encoding="utf-8")
    linea = f.readline()
    cont = 1
    
    diccionariobase = {}
    diccionario = {}

    for i in linea.split(","):
        # i.replace('\n', '')
        diccionariobase[i] = ""
    linea = f.readline()

    while linea != "":
        diccionario["dato"+str(cont)] = diccionariobase.copy()
        
        contador = 0
        for i in linea.split(","):
            # i.replace('\n', '')
            diccionario["dato"+str(cont)][list(diccionariobase.keys())[contador]] = i
            contador += 1
        cont += 1
        linea = f.readline()

    return diccionario

def split(diccionario):
    dic1 = {}
    dic2 = {}
    if diccionario[""]["type"] == "white":
        dic1 += diccionario[""]
    else: 

    return dic1, dic2




print(read_data("winequality.csv"))