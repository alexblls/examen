import math

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
    for i in diccionario:

        lista.append(diccionario[i][atributo])
    return lista 

def silhouette(lista1, lista2):
    sil = 0.0
    ai=[]
    bi=[]
    for i in lista1:
        for j in lista2:
            ai.append(math.sqrt(math.pow(abs(float(i)-float(j)),2)))
            bi.append(math.sqrt(math.pow(abs((sum(lista1)/len(lista2))-j))))
    sil = (bi-ai)/max(ai,bi)
    return sil


diccionario = read_data("winequality.csv")
dicW,dicR = split(diccionario)
list1=reduce(dicW, "fixed acidity")
list2=reduce(dicW, "alcohol")
print(silhouette(list1,list2))
