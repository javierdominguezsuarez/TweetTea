from django.shortcuts import render

# Create your views here.
def login_view (request, *args , **kwargs):
    return render (request, "form.html",{})