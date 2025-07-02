from django.http import HttpResponse

def api_home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VintedDD API Documentation</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f9fafb;
                color: #111827;
                margin: 0;
                padding: 0;
            }
            header {
                background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
                color: white;
                padding: 1rem 2rem;
                text-align: center;
            }
            main {
                max-width: 900px;
                margin: 2rem auto;
                padding: 0 1rem;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 0.5rem;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                background: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                margin-bottom: 1rem;
                padding: 1rem 1.5rem;
                transition: box-shadow 0.3s ease;
            }
            li:hover {
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }
            a {
                color: #3b82f6;
                text-decoration: none;
                font-weight: 600;
                font-size: 1.1rem;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Bienvenue à l'API VintedDD</h1>
            <p>Explorez les endpoints disponibles ci-dessous :</p>
        </header>
        <main>
            <ul>
                <li><a href="/api/users/">Gestion Utilisateurs</a></li>
                <li><a href="/api/listings/">Catalogue Produits</a></li>
                <li><a href="/api/transactions/">Paiements Sécurisés</a></li>
                <li><a href="/api/messaging/">Messagerie Temps Réel</a></li>
                <li><a href="/api/reviews/">Système d'Évaluation</a></li>
                <li><a href="/api/notifications/">Notifications Push</a></li>
            </ul>
        </main>
    </body>
    </html>
    """
    return HttpResponse(html_content)
