from django.shortcuts import render

# Create your views here.

def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada="19881")
    curso.save()
    