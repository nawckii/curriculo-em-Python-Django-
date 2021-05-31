"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

class Info(object):
    """description of class"""
    def __init__(self):
        self.name = 'Lucas Nawcki'
        self.about= 'I am looking for entry into the job market and the beginning of my career. For this I am willing to live different experiences in the area I graduated.'
        self.Birthday = '01/11/1994'
        self.Marital_status = 'Single'
        self.Phone = '(41) 99742-2860'
        self.City = 'Curitiba/PR'

        self.Age = 2020 - 1994 
        self.Degree = 'Computer Science Bachelor'
        self.Email = 'nawckii@hotmail.com'
        self.Freelance = 'Available'

        self.skills = [ ['HTML', 100], ['CSS',100], ['JavaScript',30], ['PHP',80], ['C# .NET',80], ['Python',100], ['C/C++/C#',100], ['SQL Server',90], ['Artificial Inteligence',90], ['Bash and PowerShell',90]]




def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def curriculo(request):
    info = Info()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/curriculo/curriculo.html',
        {
            'title':'Lucas Nawcki',
            'message':'I am looking for entry into the job market and the beginning of my career. For this I am willing to live different experiences in the area I graduated.',
            'info': info,
        }
    )