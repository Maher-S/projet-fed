from django.views import generic
from .models import Article # bring into the views
from django.core.paginator import Paginator

# Create your views here.


class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles' # assign articles object list to the object "articles"

    # pass articles objects as queryset for listview
    
    def get_queryset(self):
        articles = Article.objects.all()

        paginator = Paginator(articles, 30)
        page_number = self.request.GET.get('page')
        return paginator.get_page(page_number)