from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {})


def contact(request):
    return render(request, 'main/contact.html', {})


def projects(request):
    request.session["opened_projects"] = True;
    return render(request, 'main/projects.html', {})


def project(request, project_name):
    print project_name
    return render(request, 'main/projects/' + project_name + '.html', {})
