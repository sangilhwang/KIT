from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from todo.models import Todo
from rest_framework.decorators import api_view
from todo.serializers import TodoSimpleSerializer, TodoSerializer, TodoCreateSerializer

# Create your views here.
@api_view(["GET"])
def todoAPI(request):
    todo = Todo.objects.filter(completed = False)
    serializer = TodoSimpleSerializer(todo, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(["GET"])
def tododoneAPI(request):
    todo = Todo.objects.filter(completed = True)
    serializer = TodoSimpleSerializer(todo, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

class TodoAPI(APIView):
    def get(self, request):
        todo = Todo.objects.filter(completed = False)
        serializer = TodoSimpleSerializer(todo, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoCreateSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])    
def TodoDone(request, id):
    todo = get_object_or_404(Todo, id = id, completed = False)
    serializer = TodoSerializer(data = todo)

    if serializer.is_valid():
        serializer["completed"] = True
        serializer.save()

    return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
    
class TodosMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TodoMixin(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class TodoGenerics(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "id"


# 풀이 버전
# 수정 기능
class TodoAPIView(APIView):
    def get(self, request, id):
        todo = get_object_or_404(Todo, id = id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, id):
        todo = get_object_or_404(Todo, id = id)
        serializer = TodoCreateSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class DoneTodosAPIView(APIView):
    def get(self, request):
        dones = Todo.objects.filter(completed = True)
        serializer = TodoSimpleSerializer(dones, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class DoneTodoAPIView(APIView):
    def get(self, request, id):
        done = get_object_or_404(Todo, id = id)
        done.completed = True
        done.save()
        serializer = TodoSerializer(done)
        return Response(status = status.HTTP_200_OK)
    


