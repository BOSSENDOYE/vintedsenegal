@echo off
echo 🚀 Démarrage de Vinted - Environnement de Développement
echo ==================================================

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installé. Veuillez l'installer d'abord.
    pause
    exit /b 1
)

REM Vérifier si Node.js est installé
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js n'est pas installé. Veuillez l'installer d'abord.
    pause
    exit /b 1
)

echo ✅ Vérification des prérequis terminée

REM Backend Setup
echo.
echo 🔧 Configuration du Backend...
cd backend

REM Vérifier si l'environnement virtuel existe
if not exist "venv" (
    echo ✅ Création de l'environnement virtuel Python...
    python -m venv venv
)

REM Activer l'environnement virtuel
echo ✅ Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Installer les dépendances
echo ✅ Installation des dépendances Python...
pip install -r requirements.txt

REM Appliquer les migrations
echo ✅ Application des migrations...
python manage.py makemigrations
python manage.py migrate

REM Créer un utilisateur de test
echo.
echo ✅ Création d'un utilisateur de test...
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); user, created = User.objects.get_or_create(username='testuser', defaults={'email': 'test@example.com'}); user.set_password('testpass123'); user.save(); print('Utilisateur test créé: testuser / testpass123' if created else 'Utilisateur test existe déjà')"

REM Test de l'authentification
echo.
echo ✅ Test de l'authentification...
python test_auth.py

REM Démarrer le serveur backend en arrière-plan
echo.
echo ✅ Démarrage du serveur backend...
start "Backend Server" python manage.py runserver 0.0.0.0:8000

REM Attendre que le serveur backend démarre
timeout /t 3 /nobreak >nul

REM Frontend Setup
echo.
echo 🎨 Configuration du Frontend...
cd ..\frontend

REM Installer les dépendances Node.js
echo ✅ Installation des dépendances Node.js...
npm install

REM Démarrer le serveur frontend
echo.
echo ✅ Démarrage du serveur frontend...
start "Frontend Server" npm start

REM Attendre que le serveur frontend démarre
timeout /t 5 /nobreak >nul

echo.
echo 🎉 Environnement de développement démarré !
echo ==========================================
echo.
echo 📱 Frontend: http://localhost:3000
echo 🔧 Backend:  http://localhost:8000
echo 📊 Admin:    http://localhost:8000/admin
echo.
echo 👤 Utilisateur de test:
echo    Username: testuser
echo    Password: testpass123
echo.
echo 🛑 Les serveurs sont maintenant en cours d'exécution.
echo    Fermez cette fenêtre pour arrêter les serveurs.
echo.

pause 