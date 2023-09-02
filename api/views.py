from django.shortcuts import render
from django.http import JsonResponse


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
    return JsonResponse(routes, safe=False)
