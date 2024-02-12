import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import User
from .forms import *


def index(request):
    return render(
        request,
        "reagents/index.html", {
        "reagent_form": ReagentForm(),
        "cell_form": CellsForm()
        }
    )


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "reagents/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "reagents/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "reagents/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "reagents/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "reagents/register.html")

# add new reagent
def add_reagent(request):
    if request.method == "POST":
        form = ReagentForm(request.POST)
        if form.is_valid():
            reagent = form.save(commit=False)
            reagent.owner = request.user
            reagent.save()
            return HttpResponseRedirect(reverse("view_reagents"))
    else:
        form = ReagentForm(request.POST)
    return render(
        request,
        "reagents/index.html",
        {
            "form": form,
        },
    )

# view all reagents
@login_required
def view_reagents(request):
    reagents = Reagent.objects.all()
    paginator = Paginator(reagents, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "reagents/reagents.html",
        {"page_obj": page_obj,
         "paginator": paginator, 
         }
    )

# delete a reagent
@login_required
def delete_reagent(request, reagent_id):
    reagent = Reagent.objects.get(pk=reagent_id)
    reagent.delete()
    return HttpResponseRedirect(reverse("view_reagents"))



# add new reagent
def add_cell(request):
    if request.method == "POST":
        form = CellsForm(request.POST)
        if form.is_valid():
            reagent = form.save(commit=False)
            reagent.owner = request.user
            reagent.save()
            return HttpResponseRedirect(reverse("view_cells"))
    else:
        form = CellsForm(request.POST)
    return render(
        request,
        "reagents/index.html",
        {
            "form": form,
        },
    )

# view all reagents
@login_required
def view_cells(request):
    cells = CellLine.objects.all()
    paginator = Paginator(cells, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "reagents/cells.html",
        {"page_obj": page_obj,
         "paginator": paginator, 
         }
    )


# delete a reagent
@login_required
def delete_cell(request, cell_id):
    cell = CellLine.objects.get(pk=cell_id)
    cell.delete()
    return HttpResponseRedirect(reverse("view_cells"))