#-*- coding: utf-8 -*-
### En python 
### 

## Traduction 

## CONDITIONS
#if 1 < 4:                       # 'if' ça veut dire "si"
#        print(  )                # 'print' ça veut dire "afficher"
#elif 3>4:
#else:                           # 'else' ça veut dire "autrement"        
#        print(     
        
        
#resultat = raw_input                        # 'raw_input' ça veut dire affiche "Quel est on nom" puis attend que l'utilisateur 
                                            # tape quelque chose pour répondre. Quand il a fini il doit appuyer sur Entrée
                                            # ce qu'il a écrit est dans 'resultat'
#print(

  
## BOUCLES, LES REPETITIONS
#for i in range(0, 2):               # on répète dans l'interval (0,10) quelque chose

while True:                          # RÉPÈTE À L'INfini   
        nom = raw_input("Bonjour, comment t'appelles-tu?")
        age = int(raw_input(nom+", quelle age as-tu?"))              # int("5") ça transforme le texte "5" en nombre 5
        if age < 2:
                print("Tu es un bébé!")
        elif age < 5:
                print("tu es un petit!")
        elif age <7:
                print("tu auras bientôt l'age de raison!")
       
