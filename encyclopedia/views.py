from django.shortcuts import render
from markdown2 import markdown as md
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "entries": util.get_entry(f"entries/{title}")
    })