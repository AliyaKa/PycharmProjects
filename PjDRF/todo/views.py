from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Projects, ToDo
from .serializers import ProjectsSerializer, ToDoSerializer, ProjectsSerializerBase
from .filters import ToDoFilter


# class ProjectsPagination(PageNumberPagination):
#     page_size = 10

class ProjectsModelViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectsSerializer
        return ProjectsSerializerBase
    # pagination_class = ProjectsPagination


class ProjectsKwargsFilterView(ListAPIView):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Projects.objects.filter(title__contains=title)


# class ToDoPagination(PageNumberPagination):
#     page_size = 20

class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    # pagination_class = ToDoPagination
    filterset_class = ToDoFilter

    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         instance.is_complete = True
    #         instance.save()
    #     except:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     else:
    #         return Response(status=status.HTTP_204_NO_CONTENT)

