import functions

diccionario = functions.read_data("winequality.csv")
dicW,dicR = functions.split(diccionario)
list1=functions.reduce(dicW, "fixed acidity")
list2=functions.reduce(dicW, "alcohol")