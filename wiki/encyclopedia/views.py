from email import utils
from django.shortcuts import render
import pdb
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "title": title
    })

def search(request):
    if request.method == "POST":
        query = request.POST.get('q', '')
        if util.get_entry(query):
            return render(request, "encyclopedia/entry.html", {
                "entry": util.get_entry(query),
                "title": query
            })
        else:
            results = util.substring_result(query)
            return render(request, "encyclopedia/search.html", {
                "results": results
            })
           
