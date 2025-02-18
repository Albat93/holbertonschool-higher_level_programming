# 📖 Introduction à `curl`

## 📝 Background

`curl` (Client URL) est un outil en ligne de commande permettant de transférer des données depuis ou vers un serveur réseau en utilisant divers protocoles comme HTTP, HTTPS, FTP, etc. Il est largement utilisé pour :
- **Tester et interagir avec des APIs RESTful** 📡
- **Diagnostiquer des problèmes de serveur** 🛠️
- **Prototyper rapidement des requêtes API** ⚡

---

## 🛠️ Utilisation de base

### 🔹 Récupérer une page web
```sh
curl http://example.com
```
📌 Affiche le contenu brut de la page demandée.

---

## 🔎 Récupérer des données depuis une API

### 📌 Obtenir les posts depuis JSONPlaceholder
```sh
curl https://jsonplaceholder.typicode.com/posts
```
📌 Renvoie un tableau JSON contenant des posts.

### 📌 Afficher uniquement les en-têtes de la réponse
```sh
curl -I https://jsonplaceholder.typicode.com/posts
```
📌 Affiche uniquement les en-têtes HTTP, utiles pour voir les **codes de statut**, **types de contenu**, **cache**, etc.

---

## ⚙️ Utilisation des options avancées

### 🔹 Effectuer une requête POST
```sh
curl -X POST -d "title=foo&body=bar&userId=1" \
     https://jsonplaceholder.typicode.com/posts
```
📌 Simule l'ajout d'un post. L'API de JSONPlaceholder retourne une réponse confirmant l'ajout avec un `id` = 101.

### 🔹 Envoyer des données en JSON avec des en-têtes spécifiques
```sh
curl -X POST -H "Content-Type: application/json" \
     -d '{"title": "foo", "body": "bar", "userId": 1}' \
     https://jsonplaceholder.typicode.com/posts
```
📌 Ajoute un `Content-Type: application/json` pour préciser que les données sont au format JSON.

### 🔹 Formater la sortie JSON (nécessite `jq`)
```sh
curl -s https://jsonplaceholder.typicode.com/posts | jq
```
📌 `jq` permet d'afficher et filtrer du JSON de manière plus lisible.

---

## 📌 Résultats attendus

✅ `curl --version` affiche les détails de la version installée.
✅ `curl https://jsonplaceholder.typicode.com/posts` renvoie des posts au format JSON.
✅ `curl -I ...` affiche uniquement les en-têtes HTTP.
✅ Une requête `POST` retourne une réponse confirmant la création de données.

📌 **Astuce** : Ajoutez `-v` pour voir les détails des requêtes, et `-o fichier.txt` pour enregistrer la sortie dans un fichier.
