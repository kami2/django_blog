from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from .models import Content, BlogSet, Author, TechNow
from django.template import loader
from django.views import generic


def index(request):
    latest_records_list = Content.objects.order_by('-pub_date')
    show_tech = TechNow.objects.all()
    paginator = Paginator(latest_records_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content = {
        'latest_records_list': page_obj,
        'blogset': BlogSet.load(),
        'author': Author.load(),
        'show_tech': show_tech}
    return render(request, 'blogb/index.html', content)


def single(request, content_id):
    try:
        content = Content.objects.get(pk=content_id)
    except Content.DoesNotExist:
       raise Http404("Record does not exist")
    return render(request, 'blogb/single.html', {
        'content': content,
        'blogset': BlogSet.load(),
        'author': Author.load()})
