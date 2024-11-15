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
from django.core.files.storage import FileSystemStorage
from .models import User
from .forms import *
from django.db.models import Q
from . import util
import markdown2
import mammoth
import os
import pyhtml2md

def index(request):
    return render(
        request,
        "reagents/index.html",
        {
            "experiment_form": ExperimentForm(),
            "reagent_form": ReagentForm(),
            "cell_form": CellsForm(),
            "protocol_form": NewProtocol()
        },
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
                request,
                "reagents/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "reagents/register.html")

# add new experiment
def add_experiment(request):
    if request.method == "POST":
        form = ExperimentForm(request.POST)
        if form.is_valid():
            experiment = form.save(commit=False)
            experiment.owner = request.user
            experiment.save()
            return HttpResponseRedirect(reverse("view_experiments"))
    else:
        form = ExperimentForm(request.POST)
    return render(
        request,
        "reagents/index.html",
        {
            "form": form,
        },
    )

# view all experiments
@login_required
def view_experiments(request):
    reagents = Experiment.objects.all()
    paginator = Paginator(reagents, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "reagents/experiments.html",
        {"page_obj": page_obj, "paginator": paginator, 
         "search_form": ReagentSearch()},
    )

# view an experiment
@login_required
def view_experiment(request, experiment_id):
    experiment = Experiment.objects.get(pk=experiment_id)
    return render(
        request,
        "reagents/experiment.html",
        {
            "experiment": experiment
        }
    )

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
        {"page_obj": page_obj, "paginator": paginator, 
         "search_form": ReagentSearch()},
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
        {"page_obj": page_obj, "paginator": paginator,
         "search_form": CellsSearch()
         }
    )

# delete a reagent
@login_required
def delete_cell(request, cell_id):
    cell = CellLine.objects.get(pk=cell_id)
    cell.delete()
    return HttpResponseRedirect(reverse("view_cells"))

@login_required
def reagents_search(request):
    """function to perform search to take the user to the page"""
    reagents = Reagent.objects.all()
    if request.method == "POST":
        form = ReagentSearch(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            qset = Q()
            for term in search.split():
                qset = Q(reagent_name__contains=term)

            close_match = Reagent.objects.filter(qset)
            for reagent in reagents:
                if search.casefold() == reagent.reagent_name.casefold():
                    messages.success(request, "Match Found!.")

                    return render(
                        request,
                        "reagents/search.html",
                        {
                            "exact_match": reagent.reagent_name,
                            "search_form": ReagentSearch(),
                        },
                    )
            if close_match:
                messages.success(request, "Match Found!.")
                return render(
                    request,
                    "reagents/search.html",
                    {"close_match": close_match, "search_form": ReagentSearch()},
                )
            else:
                messages.success(request, "No results found.")
                return render(
                    request,
                    "reagents/search.html",
                    {"search_form": ReagentSearch()},
                )
    return render(request, "reagents/index.html", {"reagents": reagents})


def view_protocols(request):
    """function to render pages."""
    return render(
        request,
        "reagents/protocols.html",
        {"entries": util.list_entries()},
    )

def view_protocol(request, entry):
    """function to render pages and convert markdown to html pages."""

    markdowner = markdown2.Markdown()
    page = util.get_entry(entry)
    return render(
        request,
        "reagents/protocol.html",
        {"entry_page": markdowner.convert(page), "title": entry},
    )

@login_required
def cells_search(request):
    """function to perform search to take the user to the page"""
    cells = CellLine.objects.all()
    if request.method == "POST":
        form = CellsSearch(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            qset = Q()
            for term in search.split():
                qset = Q(cell_name__contains=term)
  
            close_match = CellLine.objects.filter(qset)
            for cell in cells:
                if search.casefold() == cell.cell_name.casefold():
                    messages.success(request, "Match Found!.")

                    return render(
                        request,
                        "reagents/search.html",
                        {
                            "exact_match": cell.cell_name,
                            "search_form": CellsSearch(),
                        },
                    )
            if close_match:
                messages.success(request, "Match Found!.")
                return render(
                    request,
                    "reagents/search.html",
                    {"close_match": close_match, "search_form": CellsSearch()},
                )
            else:
                messages.success(request, "No results found.")
                return render(
                    request,
                    "reagents/search.html",
                    {"search_form": CellsSearch()},
                )
    return render(request, "reagents/index.html", {"cells": cells})


# upload file
def upload_file(request):
    if request.method == "POST":
        form = NewProtocol(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['upload']
            result = mammoth.convert_to_html(uploaded_file)
            html = result.value 
            markdown = pyhtml2md.convert(html)
            # Define the file path for saving the Markdown file
            markdown_filename = f"{request.POST['title']}.md"
            entries_folder = os.path.join(settings.MEDIA_ROOT, 'entries')  
            file_path = os.path.join(entries_folder, markdown_filename)
            
            # Ensure the 'entries' directory exists
            os.makedirs(entries_folder, exist_ok=True)
                        
            # Save the Markdown content to the file system
            with open(file_path, 'w', encoding='utf-8') as markdown_file:
                markdown_file.write(markdown)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = NewProtocol()
    return render(request, "reagents/index.html", {"form": form})


