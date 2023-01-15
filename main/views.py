from logging import exception
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from main.models import URLS
import uuid
# Create your views here.

def verifyURL(url):
    urlVerify = URLValidator()
    valid = True
    try:
        urlVerify(url)
    except ValidationError:
        valid = False
    return valid


def index(request):
    if request.method == "POST":
        longURL = request.POST.get("longURL", False).strip()
        valid = verifyURL(longURL)
        if valid:
            if not URLS.objects.filter(longUrl = longURL).exists():
                shortcode = str(uuid.uuid4())[:8]
                shortUrl = f"{request.__dict__['environ']['HTTP_HOST']}/{shortcode}"
                print(shortUrl)
                value = URLS(longUrl = longURL, shortUrl = shortUrl, urlCode = shortcode)
                value.save()
            else:
                shortUrl = URLS.objects.get(longUrl = longURL).shortUrl
            return render(request, 'index.html', {"shortURL": shortUrl})
        else:
            return render(request, 'index.html', {"invalid":"Please enter correct URL"})
    return render(request, 'index.html')

def customURL(request, customURL):
    if URLS.objects.filter(urlCode = customURL).exists():
        url = URLS.objects.get(urlCode = customURL).longUrl
        return HttpResponseRedirect(url)
    else:
        return HttpResponse("Doesn't exist")

def send(request):
    return render(request, 'page.html')

def multipleURLS(request):
    longURLS = request.POST.getlist('longURL')
    print(longURLS)
    return render(request, 'multipleUrl.html')