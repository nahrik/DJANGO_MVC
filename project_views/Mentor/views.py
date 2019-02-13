from django.shortcuts import render

# Create your views here.
def Mentor(request):
    return render(request, 'Mentor/mentor.html')