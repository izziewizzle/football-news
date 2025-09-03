from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406361675',
        'name': 'Izzati Maharani Y',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
