def imprimir_sopa_de_letras ():
    print ("     a f g a r h p j o t s ")
    print ("     v s u e c i a j c t a ")
    print ("     y p g a j w k l i t c ")
    print ("     e d a a x h p j x t a ")
    print ("     h o n d u r a s e t r ")
    print ("     q f d a r h p j m t a ")
    print ("     p f a o t p i g e t c ")

def puerta1():
    
    print ("")
    print ("Comienza el 1er reto: SOPA DE LETRAS ")
    print ("")
    
    
    imprimir_sopa_de_letras()
    
    respuesta = ["mexico", "uganda", "honduras", "suecia", "egipto"]
    historial_respuesta = []
    
    print ("")
    print ("¿Cualés son los 5 países en la sopa de letras?")  
    
    puntaje=1
    
    while (True):
    
        if(puntaje > 5 ):
            break
        
        print("")
        
        respuesta_usuario = input (("País N°")+str(puntaje)+ (": "))
        
        if(respuesta_usuario =="salir"):
            pasalir=True
            return pasalir
        
        print ("") 
        print ("") 
        """
        for i in range(5):    
            if (respuesta_usuario == respuesta[i] and respuesta_usuario not in historial_respuesta):
                puntaje = puntaje+1
                print ("¡Correcto!, llevas " + str (puntaje-1)+ " de 5.")
                historial_respuesta.append(respuesta_usuario)
        """
        if (respuesta_usuario in respuesta and respuesta_usuario not in historial_respuesta):
            puntaje = puntaje+1
            print ("¡Correcto!, llevas " + str (puntaje-1)+ " de 5.")
            historial_respuesta.append(respuesta_usuario)    
            
        print ("") 
        print ("")    
        imprimir_sopa_de_letras()
    
    pasalir=False
    return pasalir