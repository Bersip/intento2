import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import PIL

def puerta2():
    
    print("")
    print("")
    print ("¡Enhorabuena! Tengo dos regalos para ti.")
    print("")
    print("")
    print("              ,;;;,   ,;;;,")
    print("            ;;;;;;;,;;;;;;;")
    print("  .:::.   .::::;;;;;;;;;;;")
    print(" :::::::.:::::::;;;;;;;;;'")
    print(" :::::::::::::::;;;;;;;'")
    print("  :::::::::::::';;;;;'")
    print("   ':::::::::'   ';'")
    print("    ':::::'")
    print("      ':'")
    print ("              ")
    
    
          
    while (True):
        print ("")
        print("Para recibir tus regalos.")
        respuesta_usuario = input (("Debes decirme las primeras palabras mágicas: "))
        
        if(respuesta_usuario =="salir"):
            pasalir=True
            return pasalir
        
        if(respuesta_usuario=="quemeama"):
            print("¡Correcto!")
            an_image = PIL.Image.open("felizamor.png")
            image_sequence = an_image.getdata()
            plt.imshow(an_image)
            plt.show()
            break
        else:
            print("Intenta de nuevo o tipea salir.")
            
    while (True):
        print ("")
        print("y para el segundo regalo.")
        respuesta_usuario = input (("Las palabras mágicas son: "))
        
        if(respuesta_usuario =="salir"):
            pasalir=True
            return pasalir
        
        if(respuesta_usuario=="alberto"):
            print("¡Bien hecho!")
            an_image2 = PIL.Image.open("Felizcumple.png")
            image_sequence = an_image2.getdata()
            plt.imshow(an_image2)
            plt.show()
            break
        else:
            print("Intenta de nuevo o tipea salir.")
 
      
    pasalir=False
    return pasalir