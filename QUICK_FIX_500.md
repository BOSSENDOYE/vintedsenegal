# 🚨 Résolution Rapide - Erreur 500

## Problème
Erreur 500 lors de la création d'annonce avec erreur CORS.

## Solution Express (5 minutes)

### 1. Arrêter le Serveur
```bash
# Dans le terminal où Django tourne, appuyez sur Ctrl+C
```

### 2. Diagnostic Automatique
```bash
cd backend
python diagnostic.py
```

### 3. Redémarrer le Serveur
```bash
python manage.py runserver
```

### 4. Tester l'API
Ouvrez votre navigateur et allez sur :
- http://localhost:8000/api/listings/ (doit afficher les annonces)
- http://localhost:8000/api/listings/categories/ (doit afficher les catégories)

## Si le Problème Persiste

### Vérification Rapide
1. **Le serveur Django tourne-t-il ?**
   ```bash
   curl http://localhost:8000/api/
   ```

2. **L'utilisateur de test existe-t-il ?**
   ```bash
   cd backend
   python quick_test.py
   ```

3. **Les catégories existent-elles ?**
   ```bash
   python create_categories.py
   ```

### Erreurs Courantes

#### "Connection refused"
- Le serveur Django n'est pas démarré
- **Solution**: `python manage.py runserver`

#### "User matching query does not exist"
- L'utilisateur de test n'existe pas
- **Solution**: `python quick_test.py`

#### "Category matching query does not exist"
- Les catégories n'existent pas
- **Solution**: `python create_categories.py`

#### "Permission denied"
- Problème d'authentification
- **Solution**: Vérifier le token JWT dans le frontend

## Test Manuel

### 1. Connexion
```bash
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### 2. Création d'Annonce (remplacer TOKEN)
```bash
curl -X POST http://localhost:8000/api/listings/create/ \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test",
    "description": "Test",
    "price": "10000",
    "category": "Femmes"
  }'
```

## Vérifications Frontend

### 1. Console du Navigateur (F12)
- Vérifier les erreurs CORS
- Vérifier les requêtes réseau

### 2. Token d'Authentification
- Vérifier que le token est présent
- Vérifier que le token n'est pas expiré

### 3. Données Envoyées
- Vérifier que tous les champs sont remplis
- Vérifier le format des données

## Solution Complète

Si rien ne fonctionne, utilisez le script de démarrage automatique :

```bash
python start_backend.py
```

Ce script va :
1. ✅ Vérifier les migrations
2. ✅ Appliquer les migrations
3. ✅ Créer les données de test
4. ✅ Démarrer le serveur
5. ✅ Afficher les diagnostics

## Contact
Si le problème persiste après ces étapes :
1. Vérifiez les logs Django dans le terminal
2. Vérifiez la console du navigateur (F12)
3. Vérifiez que les ports 8000 et 3000 sont libres 