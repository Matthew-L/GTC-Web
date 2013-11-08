from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from article.models import Article

def hello(request):
    name = "matt"
    html = "<html><body>Hi %s, this worked!</body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "matt"
    t = get_template('hello.html')
    html = t.render(Context({'name':name}))
    return HttpResponse(html)


class HelloTemplate(TemplateView):
    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'matt'
        return context

def hello_template_simple(request):
    name = 'matt'
    return render_to_response('hello.html', {'name':name})

########################################

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response('articles.html', {'articles': Article.objects.get(id=article_id)})


