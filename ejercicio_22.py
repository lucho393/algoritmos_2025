def usar_la_fuerza(mochila, indice=0):
    if indice >= len(mochila):
        return -1 

  
    if mochila[indice].lower() == "sable de luz":
        return indice + 1 
    else:
        return usar_la_fuerza(mochila, indice + 1)



mochila = ["comida", "agua", "linterna", "cerveza", "piedra", "sable de luz", "botiquín"]

objetos_sacados = usar_la_fuerza(mochila)

if objetos_sacados == -1:
    print("No se encontró un sable de luz en la mochila.")
else:
    print(" Sable de luz encontrado!")
    print(f"Objetos sacados hasta encontrarlo: {objetos_sacados}")
 