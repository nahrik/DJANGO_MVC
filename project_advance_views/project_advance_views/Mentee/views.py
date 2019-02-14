from django.shortcuts import render

# Create your views here.
def Mentee(request):
    return render(request, 'Mentee/mentee.html')