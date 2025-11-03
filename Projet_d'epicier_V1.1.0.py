print("Le programme est en cours de développement!")
print("BONJOUR")
achats = []
achats_supprimés= []
Guide = "\nGuid: \n - Tapez 0 si vous souhaitez terminer.\n - Tapez la lettre « n » si vous souhaitez supprimer la valeur d'un élément.\n - Tapez « h » si vous souhaitez afficher l\'historique de toutes les valeurs saisies."
while True:
    try:
        print("\nTaper G si vous souhaitez d\'aficher le GUIDE")
        P = input(" ecrire le prix: ")
        if P == "":
            raise ValueError("Aucune valeur entrée !")
        if P == "G":
            print(Guide)
            continue
        if P == "H":
            x = 1
            y = 1
            for achat in achats:
                print("objet "+ str(x) +": "+ str(achat) +" DH")
                x += 1
            for achatsp in achats_supprimés:
                print("objet supprimé "+ str(y) +": "+ str(achatsp) +" DH")
                y += 1
            print("Totale: " + str(sum(achats)-sum(achats_supprimés)))
            continue
        if P == "N":
            sp = input(" Saisissez la valeur que vous souhaitez supprimer: ")
            achats_supprimés.append(int(sp))
            try:
                achats.remove(int(sp))
            except:
                continue
            continue
        P = float(P)
        if P > 0:
            achats.append(P)
            print(sum(achats), " DH")
            continue
        if P == 0:
            x = 1
            y = 1
            for achat in achats:
                print("objet "+ str(x) +": "+ str(achat) +" DH")
                x += 1
            for achatsp in achats_supprimés:
                print("objet supprimé "+ str(y) +": "+ str(achatsp) +" DH")
                y += 1
            print("Montant total est: ", sum(achats)-sum(achats_supprimés), " DH")
            break
        else:
            raise ValueError("La valeur que vous avez saisie est inférieure à 0.")
    except ValueError as e:
        print("⚠️ Erreur: ", e)
        continue
    except KeyboardInterrupt:
        continue







# les erreurs techniques dans le contexte de ton programme :

# - Commandes sensibles à la casse : Si l’utilisateur écrit “n”, “g” ou “h” en minuscule, la commande ne fonctionne pas (seulement "N", "G", "H" acceptés), ce qui peut perturber l’expérience utilisateur.

# - Suppression d’un élément inexistant : Si l’utilisateur tente de supprimer une valeur qui n’est pas dans la liste "achats", aucune information n’est donnée – le programme passe discrètement, ce qui peut créer de l’incompréhension.

# - Entrée de suppression mal formatée : Si l’utilisateur tape une lettre, un mot ou une valeur non numérique pour la suppression ("N" puis “abc”), le programme lève toujours une erreur (ValueError), affichant le message générique.

# - Affichage de l’historique : Si aucune valeur n’a été saisie ou annulée, l’affichage peut manquer de clarté ("sections vides").

# - Pas de gestion d’erreur personnalisée lors des suppressions multiples d’une même valeur : Si un même montant est supprimé plusieurs fois (plus que sa présence dans la liste), cela risque de créer des incohérences invisibles.

# - Robustesse partielle : Certaines exceptions moins courantes (ex : erreurs lors de la conversion en float/int, erreurs inattendues lors de l’affichage de listes) ne sont pas traitées séparément.