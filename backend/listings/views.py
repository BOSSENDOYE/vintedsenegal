from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters, permissions, status
from .models import Listing, Category, Photo
from .serializers import ListingSerializer
from django.db import models

class ListingCreateView(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print('Données reçues pour création annonce:', request.data)
        print('Fichiers reçus:', request.FILES)
        
        try:
            # Récupérer les données
            title = request.data.get('title')
            description = request.data.get('description')
            price = request.data.get('price')
            category_name = request.data.get('category')
            images = request.FILES.getlist('images')
            
            # Valider les données
            if not all([title, description, price, category_name]):
                return Response({
                    'error': 'Tous les champs obligatoires doivent être remplis'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Trouver ou créer la catégorie
            category, created = Category.objects.get_or_create(name=category_name)
            
            # Créer l'annonce
            listing = Listing.objects.create(
                title=title,
                description=description,
                price=price,
                category=category,
                seller=request.user
            )
            
            # Ajouter les images
            for image in images:
                Photo.objects.create(
                    listing=listing,
                    image=image
                )
            
            # Sérialiser la réponse
            serializer = self.get_serializer(listing)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            print(f'Erreur lors de la création:', str(e))
            return Response({
                'error': f'Erreur lors de la création: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListingUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        print('Données reçues pour modification annonce:', request.data)
        return super().update(request, *args, **kwargs)

class ListingListView(generics.ListAPIView):
    queryset = Listing.objects.filter(is_active=True)
    serializer_class = ListingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'category__name']
    ordering_fields = ['price', 'created_at']
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class ListingDetailView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

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

class SellerStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        total_listings = Listing.objects.filter(seller=user).count()
        active_listings = Listing.objects.filter(seller=user, is_active=True).count()
        sold_items = Listing.objects.filter(seller=user, status='sold').count() if hasattr(Listing, 'status') else 0
        total_views = Listing.objects.filter(seller=user).aggregate(total=models.Sum('views'))['total'] or 0
        total_messages = 0  # À personnaliser selon ton modèle de messagerie
        return Response({
            'totalListings': total_listings,
            'activeListings': active_listings,
            'soldItems': sold_items,
            'totalViews': total_views,
            'totalMessages': total_messages
        })

class SellerListingsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        listings = Listing.objects.filter(seller=request.user)
        serializer = ListingSerializer(listings, many=True, context={'request': request})
        return Response(serializer.data)

class ListingDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            listing = Listing.objects.get(pk=pk, seller=request.user)
        except Listing.DoesNotExist:
            return Response({'error': 'Annonce non trouvée ou accès refusé.'}, status=status.HTTP_404_NOT_FOUND)
        listing.delete()
        return Response({'message': 'Annonce supprimée.'}, status=status.HTTP_204_NO_CONTENT)
