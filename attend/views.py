from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    context = {
        "heading": "Attend Top",
        "message": "This is attend top page.",
    }
    return render(request, 'attend/index.html', context)

def list(request):
    context = {
        "heading": "Attend List",
        "message": "This is attend list page.",
    }
    return render(request, 'attend/list.html', context)

def detail(request, user_id):
    user = get_atend_user_by_id(user_id)
    return JsonResponse(user)

def get_atend_user_by_id(user_id):
    users = [
        {"id": 1, "name": "Alice", "is_attended": True},
        {"id": 2, "name": "Bob", "is_attended": False},
    ]
    for user in users:
        if user["id"] == user_id:
            return user
    return None