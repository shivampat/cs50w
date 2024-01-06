from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from markdown2 import Markdown 
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def getArticle(request, title):
    if title.lower() in [x.lower() for x in util.list_entries()]:
        markdown = Markdown()
        return render(request, "encyclopedia/entry.html", {
            "title": title, 
            "entry": markdown.convert(util.get_entry(title)),
            "entries": util.list_entries(), 
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title, 
            "entries": util.list_entries(),  
        })

def search(request):
    if request.method == 'POST':
        query = request.POST['q']
        print(query)
        entries = util.list_entries()
        if query.lower() in [x.lower() for x in entries]:
            return HttpResponseRedirect(reverse('getArticle', kwargs={"title": query}))
        else: 
            results = []
            for entry in entries: 
                if query in entry: 
                    results.append(entry)
            if len(results) != 0: 
                return render(request, "encyclopedia/search.html", context={
                    "query": query, 
                    "results": results,
                }) 
            else: 
                return render(request, "encyclopedia/error.html", context={
                    "title": query, 
                    "entries": util.list_entries(),  
                }) 
    else: 
        return HttpResponseNotAllowed()
    
def randomEntry(request): 
    title = random.sample(util.list_entries(), 1)
    return HttpResponseRedirect(reverse('getArticle', args=title))

def create(request): 
    if request.method == 'GET': 
        return render(request, "encyclopedia/create.html", {
            "entries": util.list_entries(),
        })
    elif request.method == 'POST':
        title = request.POST['articleTitle']
        if title.lower() in [x.lower() for x in util.list_entries()]:
            return HttpResponseRedirect(reverse('create'))
        body = request.POST['articleBody']
        util.save_entry(title, content=body)
        return HttpResponseRedirect(reverse('index'))
