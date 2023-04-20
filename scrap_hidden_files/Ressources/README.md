# Scrap Hidden Files

Après avoir examiné le fichier whatever dans le robots.txt, nous allons maintenant examiner les fichiers .hidden. Nous allons créer un script de scrapping en Python pour récupérer tout le texte dans un seul fichier.

Une fois cela fait, utilisez soit "grep -P '(?<!\d)\d{4}(?!\d)' results.txt" soit simplement CTRL + F pour rechercher un chiffre dans le fichier afin de trouver le flag.
