# 🧪 Test du Flux Complet - Création et Affichage d'Annonces

## Objectif
Tester que les annonces créées apparaissent bien sur la page d'accueil.

## Prérequis
- ✅ Serveur Django démarré sur le port 8000
- ✅ Frontend React démarré sur le port 3000
- ✅ Utilisateur de test créé
- ✅ Catégories créées

## Étapes de Test

### 1. Préparation des Données
```bash
cd backend

# Créer l'utilisateur de test
python quick_test.py

# Créer les catégories
python create_categories.py

# Créer des annonces de démonstration
python create_demo_listings.py
```

### 2. Vérifier l'API
Ouvrez votre navigateur et testez :
- http://localhost:8000/api/listings/ (doit afficher les annonces en JSON)
- http://localhost:8000/api/listings/categories/ (doit afficher les catégories)

### 3. Tester le Frontend
1. **Page d'accueil** : http://localhost:3000
   - Vérifier que les annonces s'affichent
   - Vérifier que les images sont visibles
   - Vérifier que les prix sont en FCFA

2. **Création d'annonce** : http://localhost:3000/create-listing
   - Se connecter avec testuser / testpass123
   - Créer une nouvelle annonce
   - Vérifier la redirection vers le dashboard

3. **Vérifier l'apparition** : Retourner sur la page d'accueil
   - La nouvelle annonce doit apparaître
   - Actualiser la page si nécessaire

## Vérifications Visuelles

### Page d'Accueil
- ✅ **Grille d'annonces** : 8 annonces maximum affichées
- ✅ **Images** : Photos des annonces ou image par défaut
- ✅ **Prix** : Format FCFA (ex: 25 000 FCFA)
- ✅ **Catégories** : Badges colorés sur les images
- ✅ **Informations** : Vendeur, date de publication
- ✅ **Boutons** : "Voir les détails" fonctionnels

### Composant ListingCard
- ✅ **Design moderne** : Cartes avec ombres et hover effects
- ✅ **Responsive** : S'adapte aux différentes tailles d'écran
- ✅ **Gestion d'erreurs** : Image par défaut si photo manquante
- ✅ **Troncature** : Titres et descriptions tronqués si trop longs

## Test de Création d'Annonce

### 1. Connexion
- Aller sur http://localhost:3000/login
- Se connecter avec `testuser` / `testpass123`

### 2. Création
- Aller sur http://localhost:3000/create-listing
- Remplir le formulaire :
  - **Titre** : "Test Annonce"
  - **Description** : "Description de test"
  - **Prix** : 15000
  - **Catégorie** : Sélectionner "Femmes"
  - **Images** : Uploader une photo (optionnel)

### 3. Soumission
- Cliquer sur "Publier l'annonce"
- Vérifier la notification de succès
- Vérifier la redirection vers le dashboard

### 4. Vérification
- Retourner sur la page d'accueil
- Vérifier que la nouvelle annonce apparaît
- Vérifier que les informations sont correctes

## Résolution de Problèmes

### Les annonces ne s'affichent pas
1. **Vérifier l'API** : http://localhost:8000/api/listings/
2. **Vérifier la console** : F12 → Console → Erreurs
3. **Vérifier le réseau** : F12 → Network → Requêtes API

### Erreur 500 lors de la création
1. **Vérifier les logs Django** : Terminal du serveur
2. **Vérifier les migrations** : `python manage.py migrate`
3. **Vérifier l'utilisateur** : `python quick_test.py`

### Images ne s'affichent pas
1. **Vérifier les URLs** : Les images doivent être accessibles
2. **Vérifier les permissions** : Dossier media accessible
3. **Vérifier le fallback** : Image par défaut doit s'afficher

### Prix mal formatés
1. **Vérifier la fonction formatPrice** : Doit utiliser XOF
2. **Vérifier les données** : Le prix doit être un nombre
3. **Vérifier la locale** : Format français

## Résultat Attendu

Après avoir suivi ces étapes, vous devriez voir :
- ✅ Des annonces de démonstration sur la page d'accueil
- ✅ La possibilité de créer de nouvelles annonces
- ✅ Les nouvelles annonces qui apparaissent immédiatement
- ✅ Un design moderne et responsive
- ✅ Des prix en FCFA correctement formatés

## Contact
Si un problème persiste :
1. Vérifiez les logs Django
2. Vérifiez la console du navigateur
3. Vérifiez que tous les services sont démarrés 