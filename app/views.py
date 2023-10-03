from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from app.models import Person

# Create your views here.
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", context={"people": people, "title": "Index page"})

def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
    return HttpResponseRedirect('/')

def edit(request, pk):
    try:
        person = Person.objects.get(id=pk)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'person':person, "title": "Edit page"})
    except Exception as e:
        print(f"Error {e} while trying to edit DB")
        return HttpResponseNotFound("<h2>Person not found</h2>")

def delete(request, pk):
    try:
        person = Person.objects.get(id=pk)
        person.delete()
        return HttpResponseRedirect('/')
    except Exception as e:
        print(f"Error {e} while trying to delete record")
        return HttpResponseNotFound("<h2>Person not found</h2>")
        