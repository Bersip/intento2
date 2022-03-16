def final():
    
    while (True):
        print("_ _ _ _   _ _ _ _    _ _ _ _ _ _ _ _")
        print("     lugar                país")
        print(" (2 palabras)")
        respuesta_final = input ("¿En dónde estás?: ")

        if(respuesta_final =="salir"):
            pasalir=True
            return pasalir
 
        if(respuesta_final =="poza azul honduras"):      
            print("")
            print("      ¡Bien hecho aventurero!")                  
            print("")           
            print("        .---.          .---.") 
            print("       /   6_6        / 4 4 \ ")
            print("       \_  (__\       \_ v _/ ")
            print("       //   \\         //    \\ ")
            print("      ((     ))      ((     ))")
            print("=======**===**========**===**=======")
            print("         |||            ||| ")
            print("          |              | ")
            print("")
            print("Estas en la Poza Azul en Honduras.")
            print("")
            print("Un lugar con una belleza natural sin igual. Si quieres conocer como")
            print("se ve este hermoso paraje coloca este link en tu navegador:")
            print("")
            print("https://scontent.fhmo2-2.fna.fbcdn.net/v/t1.18169-9/19883975_965929846882315_1889990384155673894_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=19026a&_nc_ohc=Ado5lagqQN8AX-UXUDh&_nc_ht=scontent.fhmo2-2.fna&oh=00_AT8ZIIo6MVr2aVA9CSAD7TcL5xNmqq6vaEoQFmGS3cFpdQ&oe=61F92CFC")
            print("")
            print("")
            print("¡Gracias por jugar!")
            print("Elaborado por: Bersi Palermo García bajo la guía de Moisés León Coello.")
            break

        else:
            print("")
            print("Incorrecto. Intenta de nuevo o tipea salir.")
            print("")

    pasalir=False
    return pasalir