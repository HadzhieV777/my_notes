from rest_framework import generics as api_view
from main.models import Note, Category
from main.serializers import NoteForListSerializer, CategoryForListSerializer, NoteFullSerializer


class NotesListAndCreateView(api_view.ListCreateAPIView):
    queryset = Note.objects.all()
    query_filter_names = ('category',)
    
    list_serializer_class = NoteForListSerializer # serializer class is used when we have only one serializer
    post_serializer_class = NoteFullSerializer

    def __add_query_filters(self, queryset):
        filter_options = {}
        for filter_name in self.query_filter_names:
            id = self.request.query_params.get(filter_name, None)
            if id:
                filter_options[f'{filter_name}_id'] = id

    # def get_queryset(self):
    #     queryset = super().get_queryset()

    #     # we must overwrite the queryset because .filter() is immutable
    #     # queryset = queryset.filter(user=self.request.user)

    #     queryset = self.__add_query_filters(queryset)

    #     return queryset

    def get_serializer_class(self):
        # is used when we have many serializers
        if self.request.method.lower() == 'post':
            return self.post_serializer_class
        return self.list_serializer_class

    def post(self, request, *args, **kwargs):
       response = super().post(request, *args, **kwargs)
       return response
       
class NoteDetailsAndUpdateView(api_view.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteFullSerializer
    

class CategoryListView(api_view.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryForListSerializer
    


