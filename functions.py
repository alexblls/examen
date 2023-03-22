def read_data(fichero):
    f = open(fichero,mode="rt", encoding="utf-8")
    linea = f.readline()
    cont = 1
    contador = 0
    diccionariobase = {}
    diccionario = {}

    for i in linea.split(","):
        diccionariobase[i] = ""

    while cont != 5:
        diccionario["dato"+str(cont)] = diccionariobase.copy()
        

        # for j in diccionariobase:
        for i in linea.split(","):
            diccionario["dato"+str(cont)][contador] = i
            contador+=1
        cont += 1
        linea = f.readline()

    return diccionario


print(read_data("winequality.csv"))