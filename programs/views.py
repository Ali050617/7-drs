from django.shortcuts import render, redirect

from .models import Program


def programs_list(request):
    programs = Program.objects.all()
    ctx = {'programs': programs}
    return render(request, 'programs/programs-list.html', ctx)


def programs_create(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    if title and description:
        Program.objects.create(
            title=title,
            description=description
        )
        return redirect('programs:programs_list')
    return render(request, 'programs/programs-form.html')

