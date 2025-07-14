from django.urls import path
from .views import ListingCreateView, ListingUpdateView, ListingListView, ListingDetailView, CategoriesView, SellerStatsView, SellerListingsView, ListingDeleteView

urlpatterns = [
    path('', ListingListView.as_view(), name='listing-list'),
    path('create/', ListingCreateView.as_view(), name='listing-create'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('<int:pk>/update/', ListingUpdateView.as_view(), name='listing-update'),
    path('<int:pk>/delete/', ListingDeleteView.as_view(), name='listing-delete'),
    path('categories/', CategoriesView.as_view(), name='categories-list'),
    path('seller-stats/', SellerStatsView.as_view(), name='seller-stats'),
    path('seller/', SellerListingsView.as_view(), name='seller-listings'),
]
