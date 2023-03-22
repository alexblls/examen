def read_data(fichero):
    f = open(fichero,mode="rt", encoding="utf-8")
    linea = f.readline()
    cont = 1
    diccionariobase = {}
    diccionario = {}

    

    for i in linea.split(","):
        diccionariobase[i] = ""

    

    while linea != "":
        diccionario["dato"+str(cont)] = diccionariobase.copy()

        
    #     for i in linea.split(","):
    #         diccionario[i] = i
    #     linea = f.readline()
    #     cont += 1

    return diccionario


print(read_data("winequality.csv"))