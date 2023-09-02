from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "endpoint": "/notes/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of notes",
        },
        {
            "endpoint": "/notes/id",
            "method": "GET",
            "body": "None",
            "description": "Returns a single note object",
        },
        {
            "endpoint": "/notes/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates a new note with data sent in post request",
        },
        {
            "endpoint": "/notes/id/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing note with data sent in post request",
        },
        {
            "endpoint": "/notes/id/delete/",
            "method": "DELETE",
            "body": None,
            "description": "Deletes an existing note",
        },
    ]
    return Response(routes)


@api_view(["GET"])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)
