def introduccion():
    print("")
    print ("Has venido del futuro para recibir el preciado")
    print ("regalo de tu amada.")
    
    while (True): 
        jugar = input ("¿Verdad?: ")
        
        if(jugar =="salir"):
            pasalir=True
            return pasalir
     
        if(jugar =="si"):      
            print("")
            break
        else:
            print("")
            print("Debes escribir si o salir.")
  
    