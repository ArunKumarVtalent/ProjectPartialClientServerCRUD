from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Create(request):
    return render(request, 'create.html')

def Edit(request):
    return render(request, 'edit.html')

def Delete(request):
    return render(request, 'delete.html')
