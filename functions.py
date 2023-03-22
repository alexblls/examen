def read_data(fichero):
    f = open(fichero,mode="rt", encoding="utf-8")
    linea = f.readline()
    diccionario = {}
    while linea != "":
        for i in linea.split(","):
            
        linea = f.readline()

    return palabras