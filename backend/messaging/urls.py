from django.urls import path
from .views import MessageCreateView, ConversationListView, ConversationDetailView, SendMessageToUserView
from .views_extra import MessagingHomeView

urlpatterns = [
    path('', MessagingHomeView.as_view(), name='messaging-home'),
    path('conversations/', ConversationListView.as_view(), name='conversation-list'),
    path('conversations/<int:pk>/', ConversationDetailView.as_view(), name='conversation-detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message-create'),
    path('messages/send/', SendMessageToUserView.as_view(), name='message-send'),
]
