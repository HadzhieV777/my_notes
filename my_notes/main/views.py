from rest_framework import generics as api_view
from main.models import Note, Category
from main.serializers import NoteForListSerializer, CategoryForListSerializer, NoteForCreateSerializer


class NotesListAndCreateView(api_view.ListCreateAPIView):
    queryset = Note.objects.all()
    # serializer_class = NoteForListSerializer # serializer class is used when we have only one serializer
    query_filter_names = ('category',)

    def __add_query_filters(self, queryset):
        filter_options = {}
        for filter_name in self.query_filter_names:
            id = self.request.quey_params.get(filter_name, None)
            if id:
                filter_options[f'{filter_name}_id'] = id

    def get_queryset(self):
        queryset = super().get_queryset()

        # we must overwrite the queryset because .filter() is immutable
        queryset = queryset.filter(user=self.request.user)

        queryset = self.__add_query_filters(queryset)

        return queryset

    def get_serializer_class(self):
        # is used when we have only many serializers
        pass

    def post(self, request):
       pass
       

class CategoryListView(api_view.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryForListSerializer
    


