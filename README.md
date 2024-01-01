# Petit défi 

Bien le bonjour !

J'ai créé une superbe application très sécurisée qui s'appuie sur werkzeug security : [[https://pydoc.dev/werkzeug/latest/werkzeug.security.html]]

Mon application est donc indestructible !

Par contre je crois que j'ai oublié de désactiver quelque chose ... ça ne doit pas être important ...

Quoiqu'il en soit bon courage pour casser mon appli. Le code t'es ouvert n'hésites pas à te balader dedans (sauf dans le dossier static parce que sinon c'est pas drôle, tu peux l'atteindre différement depuis l'appli).

## Lancement

Je compte sur toi pour ne pas regarder le fichier flags directement, ça ne serait pas marrant.

Pour lancer le défi il te suffit d'utiliser docker :
```
sudo docker build -t challenge .
sudo docker run -dt --rm -p 80:80 --name defi challenge python main.py
```

Tu pourras accéder à l'appli sur :
[[http://127.0.0.1]]

Quand tu te seras rendu compte que mon appli est indestructible tu pourras arrêter le conteneur en faisant :
```
sudo docker stop defi
sudo docker rmi challenge
```