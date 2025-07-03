from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters, permissions
from .models import Listing
from .serializers import ListingSerializer

class ListingCreateView(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print('Données reçues pour création annonce:', request.data)
        return super().create(request, *args, **kwargs)

class ListingUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        print('Données reçues pour modification annonce:', request.data)
        return super().update(request, *args, **kwargs)

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
        categories = [
            {
                "name": "Femmes",
                "subcategories": [
                    {
                        "name": "Vêtements",
                        "subcategories": [
                            {"name": "Traditionnelle"},
                            {"name": "Sweats et sweats à capuche"},
                            {"name": "Blazers et tailleurs"},
                            {"name": "Robes"},
                            {"name": "Jupes"},
                            {"name": "Hauts et t-shirts"},
                            {"name": "Jeans"},
                            {"name": "Pantalons et leggings"},
                            {"name": "Shorts"},
                            {"name": "Combinaisons et combishorts"},
                            {"name": "Maillots de bain"},
                            {"name": "Lingerie et pyjamas"},
                            {"name": "Maternité"},
                            {"name": "Vêtements de sport"},
                            {"name": "Voir tout"},
                            {"name": "Autre"},
                        ],
                    },
                    {
                        "name": "Chaussures",
                        "subcategories": [
                            {"name": "Ballerines"},
                            {"name": "Mocassins"},
                            {"name": "Bottes"},
                            {"name": "Mules"},
                            {"name": "Espadrilles"},
                            {"name": "Chaussures à talons"},
                            {"name": "Sandales"},
                            {"name": "Chaussures de sport"},
                            {"name": "Voir tout"},
                            {"name": "Autre"},
                        ],
                    },
                    {
                        "name": "Sacs",
                        "subcategories": [
                            {"name": "Sacs de plage"},
                            {"name": "Pochettes"},
                            {"name": "Sacs de sport"},
                            {"name": "Sacs de voyage"},
                            {"name": "Cartables et sacoches"},
                            {"name": "Sacs fourre-tout"},
                            {"name": "Sacs à dos"},
                            {"name": "Mallettes"},
                            {"name": "Sacs à main"},
                            {"name": "Trousses à maquillage"},
                            {"name": "Sacs à bandoulière"},
                            {"name": "Porte-monnaie"},
                            {"name": "Voir tout"},
                            {"name": "Autre"},
                        ],
                    },
                    {
                        "name": "Accessoires",
                        "subcategories": [
                            {"name": "Ceintures"},
                            {"name": "Gants"},
                            {"name": "Accessoires pour cheveux"},
                            {"name": "Chapeaux et casquettes"},
                            {"name": "Bijoux"},
                            {"name": "Porte-clés"},
                            {"name": "Écharpes"},
                            {"name": "Lunettes de soleil"},
                            {"name": "Parapluies"},
                            {"name": "Montres"},
                            {"name": "Voir tout"},
                            {"name": "Autre"},
                        ],
                    },
                    {
                        "name": "Beauté",
                        "subcategories": [
                            {"name": "Maquillage"},
                            {"name": "Parfums"},
                            {"name": "Soins du visage"},
                            {"name": "Accessoires de beauté"},
                            {"name": "Soins mains"},
                            {"name": "Manucure"},
                            {"name": "Soins du corps"},
                            {"name": "Soins capillaires"},
                            {"name": "Voir tout"},
                            {"name": "Autre"},
                        ],
                    },
                    {
                        "name": "Perruques, mèches",
                        "subcategories": [
                            {"name": "Voir tout"},
                            {"name": "Autre"},
                        ],
                    },
                ],
            },
            {
                "name": "Hommes",
                "subcategories": [
                    {
                        "name": "Vêtements",
                        "subcategories": [
                            {"name": "Traditionnelle"},
                            {"name": "Manteaux et vestes"},
                            {"name": "Hauts et t-shirts"},
                            {"name": "Costumes et blazers"},
                            {"name": "Sweats et pulls"},
                            {"name": "Pantalons"},
                            {"name": "Shorts"},
                            {"name": "Sous-vêtements et chaussettes"},
                            {"name": "Pyjamas"},
                            {"name": "Maillots de bain"},
                            {"name": "Vêtements de sport et accessoires"},
                            {"name": "Voir tout"},
                            {"name": "Autre"},
                        ],
                    },
                    {
                        "name": "Chaussures",
                        "subcategories": [
                            {"name": "Traditionnelle"},
                            {"name": "Mocassins"},
                            {"name": "Bottes"},
                            {"name": "Mules"},
                            {"name": "Espadrilles"},
                            {"name": "Claquettes et tongs"},
                            {"name": "Sandales"},
                            {"name": "Chaussures de sport"},
                            {"name": "Baskets"},
                            {"name": "Voir tout"},
                            {"name": "Autre"},
                        ],
                    },
                    {
                        "name": "Accessoires",
                        "subcategories": [
                            {"name": "Sacs et sacoches"},
                            {"name": "Bandanas et foulards"},
                            {"name": "Mouchoirs de poche"},
                            {"name": "Chapeaux et casquettes"},
                            {"name": "Bijoux"},
                            {"name": "Pochettes de costume"},
                            {"name": "Écharpes et châles"},
                            {"name": "Lunettes de soleil"},
                            {"name": "Cravates et nœuds papillons"},
                            {"name": "Montres"},
                            {"name": "Voir tout"},
                            {"name": "Autre"},
                        ],
                    },
                    {
                        "name": "Soins",
                        "subcategories": [
                            {"name": "Soins visage"},
                            {"name": "Accessoires"},
                            {"name": "Soins cheveux"},
                            {"name": "Soins du corps"},
                            {"name": "Soins mains et ongles"},
                            {"name": "Parfums"},
                            {"name": "Voir tout"},
                            {"name": "Autre"},
                        ],
                    },
                ],
            },
            {
                "name": "Enfants",
                "subcategories": [
                    {"name": "Voir tout"},
                    {"name": "Autre"},
                ],
            },
        ]
        return Response(categories)
