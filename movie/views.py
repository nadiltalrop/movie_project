from django.http import HttpResponse
from django.shortcuts import redirect, render

from movie.forms import MovieForm

from.models import Movie


def index(request):

    instances = Movie.objects.all()

    context = {
        'instances': instances,
    }  

    return render(request, 'index.html', context)


def detail(request, id):
    instance = Movie.objects.get(id=id)
    context = {
        'instance': instance,
    }

    return render(request, 'detail.html',context)


def add_movie(request):
    if request.method=='POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES.get('image')

        movie = Movie(name=name, description=description, year=year, image=image)
        movie.save()

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    
    context = {
        'form': form,
       'movie': movie,
    }
    
    return render(request, 'update.html', context=context)


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    
    return render(request, 'delete.html')