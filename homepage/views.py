from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteregisterSerializer
from .models import Noteregister

@api_view(['GET'])
def getnotes(request):
    notes=Noteregister.objects.all()
    serializer=NoteregisterSerializer(notes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getfullnote(request,pk):
    note=Noteregister.objects.get(id=pk)
    serializer=NoteregisterSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createfullnote(request):
    data=request.data
    note=Noteregister.objects.create(
        summary=data['summary']
    )
    serializer=NoteregisterSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatefullnote(request,pk):
    note=Noteregister.objects.get(id=pk)
    serializer=NoteregisterSerializer(instance=note,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deletefullnote(request,pk):
    note=Noteregister.objects.get(id=pk)
    note.delete()
    return Response("Note has been deleted")








