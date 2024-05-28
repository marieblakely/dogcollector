from django.shortcuts import render

from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Lennox', 'german shepherd', 'Sad dog.', 4),
  Dog('Sushi', 'poodle', 'Very fluffy.', 0),
  Dog('Champagne', 'husky', 'Happy blue eyed puppy.', 5),
  Dog('Santana', 'great pyranese', 'Sick all the time.', 7)
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello 🦮</h1>')

def about(request):
  return render(request, 'about.html')

def dog_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })  
