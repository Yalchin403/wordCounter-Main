from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render (request, "home.html")
def count(request):
    fulltext = request.POST['fulltext']
    wordList = fulltext.split()
    wordDictionary = {}
    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] +=1
        else:
            wordDictionary[word] = 1
    lastlist = wordDictionary.items()
    return render(request, "count.html", {"fulltext": fulltext, "count": len(wordList), "wordDictionary": lastlist})
def about(request):
    return render (request, "about.html")
