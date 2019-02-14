from django.shortcuts import render

# Create your views here.
def Author(request):
    return render(request, 'Author/author.html')