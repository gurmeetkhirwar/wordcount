from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere':'This is me'})

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for words in wordlist:
        if words in worddictionary:
            worddictionary[words] += 1
        else:
            worddictionary[words] = 1
    sortedwords = sorted(
        worddictionary.items(),
        key=operator.itemgetter(1),
        reverse=True
    )
        # worddictionary.setdefault(words, 0)
        # worddictionary[words] += 1
    return render(request, 'count.html', {
        'fulltext':fulltext,
        'count':len(wordlist),
        'sortedwords':sortedwords,
    })

def about(request):
    return render(request, 'about.html')