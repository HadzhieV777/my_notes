from django.urls import path
from main.views import NotesListAndCreateView, CategoryListView

urlpatterns = (
    path('', NotesListAndCreateView.as_view(), name='notes list api'),
    path('categories/', CategoryListView.as_view(), name='categories list api')
)