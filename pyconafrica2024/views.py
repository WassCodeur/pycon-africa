from django.shortcuts import render


def home24(request):
    context = {}
    template = '2024/home/home.html'
    return render(request, template, context)


def about(request):
    context = {}
    template = '2024/about/about.html'
    return render(request, template, context)


def teams(request):
    context = {}
    template = '2024/about/teams.html'
    return render(request, template, context)


def travel(request):
    context = {}
    template = '2024/about/travel.html'
    return render(request, template, context)


def coc(request):
    context = {}
    template = '2024/coc/coc.html'
    return render(request, template, context)


def fin_aid(request):
    context = {}
    template = '2024/fin_aid/fin_aid.html'
    return render(request, template, context)


def health_safety_guidelines(request):
    context = {}
    template = '2024/health_safety_guidelines/health_safety_guidelines.html'
    return render(request, template, context)


def privacy(request):
    context = {}
    template = '2024/privacy/privacy.html'
    return render(request, template, context)


def schedule24(request):
    context = {}
    template = '2024/schedule/schedule.html'
    return render(request, template, context)


def speakers(request):
    context = {}
    template = '2024/speakers/speaker_list.html'
    return render(request, template, context)


def sponsors(request):
    context = {}
    template = '2024/sponsors/sponsors.html'
    return render(request, template, context)


def sponsor_us(request):
    context = {}
    template = '2024/sponsor-us/sponsor-us.html'
    return render(request, template, context)


def talks(request):
    context = {}
    template = '2024/talks/talks.html'
    return render(request, template, context)


def tickets(request):
    context = {}
    template = '2024/tickets/tickets.html'
    return render(request, template, context)
