from django.shortcuts import render

# Create your views here.

def message(request):
    name = request.POST.get('name', '')
    # return render(request, 'congrats.html', {'name': name})
    context = {
        'name': name
    }
    return render(request, 'message.html', context)
