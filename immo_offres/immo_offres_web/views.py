from django.views import generic
from django.db.models import Q
from .models import Article
from django.core.paginator import Paginator
from datetime import datetime
from django.utils.dateparse import parse_date



class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles'

                        

    def get_queryset(self):
        query = self.request.GET.get('q')
        articles = Article.objects.all()

        if query:
            articles = articles.filter(
                Q(title__icontains=query) |
                Q(category__icontains=query) |
                Q(nature__icontains=query) |
                Q(location__icontains=query)|
                Q(website__icontains=query)|
                Q(timestamped__icontains=query)|
                Q(location__icontains=query)|
                Q(price__icontains=query)




            )

        # Filter by location
        location = self.request.GET.get('location')
        if location:
            articles = articles.filter(location=location)

        # Filter by price range
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price and max_price:
            articles = articles.filter(price__range=(min_price, max_price))


        # Filter by category
        category = self.request.GET.get('category')
        if category:
            articles = articles.filter(category=category)

        # Filter by nature
        nature = self.request.GET.get('nature')
        if nature:
            articles = articles.filter(nature=nature)

        # Filter by date
        # Filter by date
        date = self.request.GET.get('date')
        if date:
            try:
            # Convert date format from yyyy-mm-dd to dd/mm/yyyy
                date_parts = date.split('-')
                if len(date_parts) == 3:
                    formatted_date = f"{date_parts[2]}/{date_parts[1]}/{date_parts[0]}"
                    articles = articles.filter(timestamped__contains=formatted_date)
            except ValueError:
            # Handle invalid date format
                pass


        paginator = Paginator(articles, 30)
        page_number = self.request.GET.get('page')
        return paginator.get_page(page_number)

    