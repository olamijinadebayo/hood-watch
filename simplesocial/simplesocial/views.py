from django.views.generic import TemplateView
from groups.models import Group, GroupMember
from posts.models import Post
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


class HomePage(TemplateView):
    template_name = 'index.html'


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


def search(request):
    if 'hood_name' in request.GET and request.GET["hood_name"]:
        search_term = request.GET.get("hood_name")
        searched_hoods = Group.search_by_name(search_term)
        message = f"{search_term}"
        return render(request, 'group_search.html', {"hoods": searched_hoods})

    else:
        message = "You haven't searched for any term"
    return render(request, 'group_search.html')
