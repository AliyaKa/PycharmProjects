import graphene
from graphene_django import DjangoObjectType
from .models import ToDo, Projects, CustomUser


class ProjectsType(DjangoObjectType):
    class Meta:
        model = Projects
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class Query(graphene.ObjectType):
    # all_todos = graphene.List(ToDoType)
    # all_projects = graphene.List(ProjectsType)
    # all_users = graphene.List(UserType)
    #
    # def resolve_all_todos(root, info):
    #     return ToDo.objects.all()
    #
    # def resolve_all_users(root, info):
    #     return CustomUser.objects.all()
    #
    # def resolve_all_projects(root, info):
    #     return Projects.objects.all()

    project_by_id = graphene.Field(ProjectsType, id=graphene.Int(required=False))

    def resolve_project_by_id(root, info, id=None):

        if id:
            return Projects.objects.get(id=id)
        return None

    project_by_user = graphene.List(ProjectsType, username=graphene.String(required=False))

    def resolve_project_by_user(root, info, username=None):
        projects = Projects.objects.all()

        if username:
            return projects.filter(users__username=username)
        return projects



schema = graphene.Schema(query=Query)
