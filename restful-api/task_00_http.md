# 🌐 Comprendre HTTP et HTTPS

## 📌 Objectifs
Ce guide explique les différences entre **HTTP et HTTPS**, la structure des requêtes et réponses HTTP, ainsi que les méthodes et codes de statut les plus courants.

---

## 🔹 1. Différences entre HTTP et HTTPS

| Critère       | HTTP                          | HTTPS                          |
|--------------|------------------------------|--------------------------------|
| **Sécurité**  | Pas sécurisé (données en clair) | Sécurisé avec chiffrement SSL/TLS |
| **Port**      | 80                            | 443                            |
| **Certificat** | Non requis                   | Utilise un certificat SSL      |
| **Utilisation** | Sites basiques, contenus publics | Sites nécessitant de la sécurité (paiements, connexions, etc.) |

**Pourquoi HTTPS est important ?**
HTTPS protège les données contre le vol et les attaques de type **Man-in-the-Middle (MITM)**.

---

## 🔹 2. Structure des requêtes et réponses HTTP

### 📍 **Exemple de requête HTTP**
- **GET** : Méthode HTTP utilisée.
- **/index.html** : Ressource demandée.
- **HTTP/1.1** : Version du protocole.
- **Host** : Nom du serveur.
- **User-Agent** : Informations sur le navigateur.

### 📍 **Exemple de réponse HTTP**
- **HTTP/1.1 200 OK** : Statut de la réponse (succès).
- **Server** : Type de serveur utilisé.
- **Content-Type** : Type de contenu envoyé.

---

## 🔹 3. Méthodes HTTP et codes de statut

### 📍 **Méthodes HTTP courantes**
| Méthode  | Description                          | Cas d'utilisation             |
|----------|--------------------------------------|--------------------------------|
| **GET**   | Récupère des données               | Charger une page web          |
| **POST**  | Envoie des données au serveur      | Envoyer un formulaire         |
| **PUT**   | Met à jour une ressource           | Modifier un profil utilisateur |
| **DELETE**| Supprime une ressource             | Supprimer un commentaire      |

### 📍 **Codes de statut HTTP courants**
| Code  | Signification          | Cas d'utilisation                      |
|-------|------------------------|----------------------------------------|
| **200 OK** | Succès              | La page s'affiche normalement         |
| **301 Moved Permanently** | Redirection permanente | Un site a changé d'URL              |
| **403 Forbidden** | Accès refusé         | Page réservée aux utilisateurs autorisés |
| **404 Not Found** | Ressource inexistante | Page demandée introuvable            |
| **500 Internal Server Error** | Erreur serveur       | Problème interne du site web         |

---

## 🎯 **Résumé**
✅ **HTTPS** est plus sécurisé que **HTTP** grâce au chiffrement SSL/TLS.
✅ Une requête HTTP contient des **méthodes, en-têtes et paramètres**.
✅ Les **codes de statut HTTP** indiquent le résultat d’une requête.
