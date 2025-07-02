from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters, permissions
from .models import Listing
from .serializers import ListingSerializer

class ListingCreateView(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListingUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListingListView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'category__name']
    ordering_fields = ['price', 'created_at']
    permission_classes = [permissions.AllowAny]

class CategoriesView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        categories = {
            "Femmes": {
                "Vêtements": [
                    "Traditionnelle", "Sweats et sweats à capuche", "Blazers et tailleurs", "Robes", "Jupes",
                    "Hauts et t-shirts", "Jeans", "Pantalons et leggings", "Shorts", "Combinaisons et combishorts",
                    "Maillots de bain", "Lingerie et pyjamas", "Maternité", "Vêtements de sport", "Voir tout", "Autre"
                ],
                "Chaussures": [
                    "Ballerines", "Mocassins", "Bottes", "Mules", "Espadrilles", "Chaussures à talons",
                    "Sandales", "Chaussures de sport", "Voir tout", "Autre"
                ],
                "Sacs": [
                    "Sacs de plage", "Pochettes", "Sacs de sport", "Sacs de voyage", "Cartables et sacoches",
                    "Sacs fourre-tout", "Sacs à dos", "Mallettes", "Sacs à main", "Trousses à maquillage",
                    "Sacs à bandoulière", "Porte-monnaie", "Voir tout", "Autre"
                ],
                "Accessoires": [
                    "Ceintures", "Gants", "Accessoires pour cheveux", "Chapeaux et casquettes", "Bijoux",
                    "Porte-clés", "Écharpes", "Lunettes de soleil", "Parapluies", "Montres", "Voir tout", "Autre"
                ],
                "Beauté": [
                    "Maquillage", "Parfums", "Soins du visage", "Accessoires de beauté", "Soins mains",
                    "Manucure", "Soins du corps", "Soins capillaires", "Voir tout", "Autre"
                ],
                "Perruques, mèches": [
                    "Voir tout", "Autre"
                ]
            },
            "Hommes": {
                "Vêtements": [
                    "Traditionnelle", "Manteaux et vestes", "Hauts et t-shirts", "Costumes et blazers",
                    "Sweats et pulls", "Pantalons", "Shorts", "Sous-vêtements et chaussettes", "Pyjamas",
                    "Maillots de bain", "Vêtements de sport et accessoires", "Voir tout", "Autre"
                ],
                "Chaussures": [
                    "Traditionnelle", "Mocassins", "Bottes", "Mules", "Espadrilles", "Claquettes et tongs",
                    "Sandales", "Chaussures de sport", "Baskets", "Voir tout", "Autre"
                ],
                "Accessoires": [
                    "Sacs et sacoches", "Bandanas et foulards", "Mouchoirs de poche", "Chapeaux et casquettes",
                    "Bijoux", "Pochettes de costume", "Écharpes et châles", "Lunettes de soleil",
                    "Cravates et nœuds papillons", "Montres", "Voir tout", "Autre"
                ],
                "Soins": [
                    "Soins visage", "Accessoires", "Soins cheveux", "Soins du corps", "Soins mains et ongles",
                    "Parfums", "Voir tout", "Autre"
                ]
            },
            "Enfants": [
                "Voir tout", "Autre"
            ]
        }
        return Response(categories)
