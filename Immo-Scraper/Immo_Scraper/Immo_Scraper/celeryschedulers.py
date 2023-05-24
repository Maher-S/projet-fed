from datetime import timedelta
from celery import Celery
from spiders.Tayara import TayaraSpider
from spiders.TunisieAnnonce import TunisieAnnonceSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

app = Celery('scraping_tasks', broker='amqp://localhost:5672')   #amqp://guest:guest@localhost:5672/

@app.task
def run_tayara_scraper():
   # process = CrawlerProcess(get_project_settings())
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(TayaraSpider)
    process.start()

@app.task
def run_tunisie_annonce_scraper():
   # process = CrawlerProcess(get_project_settings())
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(TunisieAnnonceSpider)
    process.start()

app.conf.beat_schedule = {
    'scrape-tayara-every-day': {
        'task': 'scraping_tasks.run_tayara_scraper',
        'schedule': timedelta(hours=1),  # Start the task every hour
        'options': {'expires': timedelta(hours=3)}  # Set the task expiration time to 3 hours
    },
    'scrape-tunisie-annonce-every-day': {
        'task': 'scraping_tasks.run_tunisie_annonce_scraper',
        'schedule': timedelta(hours=1),  # Start the task every hour
        'options': {'expires': timedelta(hours=3)}  # Set the task expiration time to 3 hours
    },
}
