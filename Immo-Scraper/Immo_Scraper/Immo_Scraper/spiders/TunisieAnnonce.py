import scrapy
import mysql.connector



class TunisieAnnonceSpider(scrapy.Spider):
    name = "TunisieAnnonce"
    allowed_domains = ["www.tunisie-annonce.com"]
    start_urls = ["http://www.tunisie-annonce.com/AnnoncesImmobilier.asp"]


    def parse(self, response):
        # Extracting data using CSS selectors
        for row in response.css('tr.Tableau1'):
            item = {
                'gouvernorat': row.css('a::text').get(),
                'rubrique': row.css('td:nth-child(4)::text').get(),
                'nature': row.css('td:nth-child(6)::text').get(),
                'title': row.css('td:nth-child(8) a::text').get(),
                'price': row.css('td:nth-child(10)::text').get(),
                'modified': row.css('td:nth-child(12)::text').get(),
            }

            # Extracting the offer details link and its URL
            details_link = row.css('td:nth-child(8) a::attr(href)').get()
            if details_link:
                #offer_id = details_link.split('cod_ann=')[-1]
                details_url = response.urljoin(details_link)

                #item['offer_id'] = offer_id
                item['details_url'] = details_url

             # Connect to MySQL database
            db_connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='immo_offres',
                port= '3306'
            )

            # Create a cursor to execute SQL queries
            cursor = db_connection.cursor()

            # Insert the scraped data into the "articles" table
            sql = '''
                INSERT INTO immo_offres_web_article (title, category, nature, price, location, timestamped, link, website, date_scraped)
                VALUES (%(title)s, %(category)s, %(nature)s, %(price)s, %(location)s, %(timestamped)s, %(link)s, %(website)s, CURRENT_TIMESTAMP)
                '''

            cursor.execute(sql, {
                 'title': item['title'],
                 'category': item['rubrique'],
                 'price' : item['price'],
                 'nature': item['nature'],
                 'location': item['gouvernorat'],
                 'timestamped': item['modified'],
                 'link': item['details_url'],
                 'website': 'Tunisie Annonce',
            })


            # Commit the changes and close the database connection
            db_connection.commit()
            db_connection.close()
            yield item
        
       

        # Extract the URLs for the next pages
        next_page_urls = response.css('td[width="270"] a::attr(href)').getall()

        for url in next_page_urls:
            yield response.follow(url, callback=self.parse)



         
