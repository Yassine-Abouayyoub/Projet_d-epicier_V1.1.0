# Projet_d-epicier_V1.1.0
# Description
Programme d’épicerie interactif permettant la gestion des achats, l’annulation de valeurs, et l’affichage détaillé de l’historique. Cette version introduit la correction des erreurs en temps réel et la traçabilité de toutes les opérations.

## 1.Fonctionnalités principales:
- Saisie des achats : Entrée libre des prix, affichage du sous-total à chaque ajout.

- Annulation sur commande : Tapez “N” puis la valeur à supprimer pour annuler un montant précis (pas seulement le dernier ajouté). La valeur est retirée de la liste des achats et enregistrée dans la liste des achats supprimés : traçabilité assurée.

- Historique complet : Tapez “H” pour voir la liste de tous les achats et des montants annulés, avec numérotation pour chaque objet.

- Guide rapide : Tapez “G” pour afficher le guide des commandes à tout moment.

- Résumé final : À la clôture (taper “0”), affiche tout l’historique (objets, objets supprimés) + le montant total calculé (achats enregistrés - achats annulés).

- Gestion des erreurs : Toutes les erreurs courantes (valeur vide, négatif, mauvais format, interruption clavier) sont gérées sans crash du programme.

## 2.Utilisation des commandes:
- 0 : Terminer la saisie et afficher le bilan complet.

- N : Annuler un montant précis. Ex : N → “Saisissez la valeur à supprimer :” → 10 (annule 10 DH).

- H : Afficher la liste complète des achats et des montants annulés.

- G : Afficher le guide des commandes disponibles.

## 3.Améliorations par rapport à V1.0:
- Gestion avancée des annulations : plus flexible et transparente.

- Affichage de l’historique en temps réel et à la demande.

- Robustesse accrue grâce à une gestion complète des exceptions et interruptions.

- Clarté maximale pour l’utilisateur (épicier, assistant ou client).

## 2.Limitations à corriger en V1.2:
- Les commandes fonctionnent uniquement en majuscules (prévoir la gestion minuscule/majuscule).

- Message d’erreur non affiché si la valeur à supprimer n’existe pas dans la liste des achats.

- Amélioration possible sur la validation des types à la suppression.

- Programme prêt pour une utilisation réelle en gestion d’épicerie ou de dépenses. Toutes les tâches prévues pour V1.1.0 sont accomplies.
