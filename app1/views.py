from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from .models import TodoModel
from datetime import datetime
#from rest_framework import generics





class ListTodoView(APIView):
    def get(self,request,*args,**kwargs):
       all_todos=TodoModel.objects.all()
       result=[]
       for todo in all_todos:
           result.append({
               'task':todo.task,
               'id': todo.task,
               'status':todo.status,
               'created_at':todo.created_at,
               'updated_at':todo.updated_at
           })
       return Response(result)


class CreateTodoView(APIView):
    def post(self,reques,*args,**kwargs):
        todo=TodoModel()
        try:
            todo.task=reques.data['task']
            todo.save()
            return Response({'message':'successfully created'},201)
        except KeyError:
            return Response({'message':'please please provide task' },400)

class DetailTodoView(APIView):
    def get(self,request,*args,**kwargs):
        todo_id=kwargs['todo_id']
        todo=get_object_or_404(TodoModel,pk=todo_id)
        return Response({
            'id':todo_id,
            'task':todo.task,
            'status':todo.status,
            'created_at':todo.created_at,
            'updated_at':todo.updated_at
        })

class DeleteTodoView(APIView):
    def delete(self,request,*args,**kwargs):
        todo=get_object_or_404(TodoModel,pk=kwargs['todo_id'])
        todo.delete()
        return Response({'message':'successfully deleted'},204)


class UpdateTodoView(APIView):
    def patch(self,request,*args,**kwargs):
        todo=get_object_or_404(TodoModel,pk=kwargs['todo_id'])
        if 'task' in request.data:
            todo.task=request.data['task']
            todo.save()
            return Response({'message':'updated'})


class StatusUpdateView(APIView):
    def get(self,request,*args,**kwargs):
        todo=get_object_or_404(TodoModel,pk=kwargs['todo_id'])
        if not todo.status:
            todo.status=True
            todo.updated_at=datetime.now()
            todo.save()
            return Response({'message':'successfully update'})
        else:

            return Response({'message':'this is task already done'})


class GetTodoStatusView(APIView):
    def get(self,request,*args,**kwargs):
        status=True if kwargs['status']=='true' else False
        all_todo=TodoModel.objects.filter(status=status)
        result=[]
        for todo in all_todo:
             result.append({
                 'id':todo.id,
                 'task':todo.task,
                 'status':todo.status,
                 'created_at':todo.created_at,
                 'update_at':todo.created_at
             })

        return Response(result)

# class ListTodoView(generics.ListAPIView):
#     queryset=TodoModel.objects.all()
#     serializers_class=TodoSerializer
#
# class CreateTodoView(generics.ListAPIView):
#     queryset=TodoModel.objects.all()
#     serializers_class=TodoSerializer
#
# class DetailTodoView(generics.ListAPIView):
#     queryset = TodoModel.objects.all()
#     serializers_class = TodoSerializer
#

