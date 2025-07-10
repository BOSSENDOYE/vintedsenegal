from django.urls import path
from .views import ListingCreateView, ListingUpdateView, ListingListView, ListingDetailView, CategoriesView

urlpatterns = [
    path('', ListingListView.as_view(), name='listing-list'),
    path('create/', ListingCreateView.as_view(), name='listing-create'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('<int:pk>/update/', ListingUpdateView.as_view(), name='listing-update'),
    path('categories/', CategoriesView.as_view(), name='categories-list'),
]
