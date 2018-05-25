#-*- coding: utf-8 -*-
mois = {}
mois[0] = "Mai"
mois[1] = "Juin"
mois[2] = "Juillet"
mois[3] = "Aout"
mois[4] = "Septembre"
mois[5] = "Octobre"
mois[6] = "Novembre"
mois[7] = "Décembre"
mois[8] = "Janvier"
mois[9] = "Février"
mois[10] = "Mars"
mois[11] = "Avril"

banque = 111
for annee in range(2018, 2018+11):
        print("En l'an "+str(annee))
        for m in range(0,12):
                        print( " en "+mois[m]+" j'aurais "+str(banque)+" euros")        
                        banque += 4 
         
        nom = raw_input("Quel est ton nom ? ")
        age = int(raw_input("Quel age as tu ? "))
        
        print("Tu t'appelles "+nom+" et tu as "+str(age)+" ans")    
        # SI
        if age < 5:
                print("Tu es trop petit")
        elif age < 7:
                print("Tu n'as pas l'age de raison")
        elif age < 11:
                print("Tu sera bientôt un ado")
        elif age < 18:
                print("Tu n'est pas un adulte")
        elif age < 65:
                print("Tu es un adulte")        
        elif age < 105:
                print("Tu es un veillard")        
        else:
                print("Tu es probablement mort depuis "+str(age-105))        
                reponse = raw_input("Es-tu vraiment mort")
                
                while True:
                        if reponse == "oui":
                                print("Comment fais tu pour taper à l'ordinateur !!")
                                break
                        elif reponse == "non":
                                print("Ca m'étonne que tu aie "+str(age)+" ans.")
                                break
                        else:
                                print("Je n'ai pas compris ta réponse...")
                                reponse = raw_input("répète ta réponse...")                
                                       
