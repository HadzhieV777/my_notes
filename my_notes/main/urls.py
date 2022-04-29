from django.urls import path
from main.views import NotesListAndCreateView, CategoryListView, NoteDetailsAndUpdateView

urlpatterns = (
    path('', NotesListAndCreateView.as_view(), name='notes list api'),
    path('categories/', CategoryListView.as_view(), name='categories list api'),
    path('/<int:pk>/', NoteDetailsAndUpdateView.as_view(), name='note details or update api'),
)