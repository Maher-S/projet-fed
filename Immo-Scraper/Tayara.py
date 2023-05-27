import scrapy
import mysql.connector

class Tayara(scrapy.Spider):
    name = "Tayara"
    allowed_domains = ["www.tayara.tn"]
    start_urls = ["https://www.tayara.tn/ads/c/Immobilier/"]

    def parse(self, response):
        articles = response.css('div.grid-cols-2 article')

        for article in articles:
            item = {
                'link': article.css('a::attr(href)').get(),
                'image_url': article.css('img::attr(src)').get(),
                'title': article.css('h2::text').get(),
                'price': article.css('div.p-0 data::attr(value)').get(),
                'category': article.css('div.text-2xs span::text').get(),
                'location_timestamp': article.css('div.text-2xs span.line-clamp-1::text').get(),
            }

            details_link = item['link']
            prefix = "https://www.tayara.tn"  # Replace with the desired prefix text
            modified_link = prefix + details_link if details_link else None
            item['link'] = modified_link

            # Separate the location timestamp into separate values: location / time_stamped
            location_timestamp = item['location_timestamp']
            if location_timestamp:
                timestamps = location_timestamp.split(',')
                for i, timestamp in enumerate(timestamps):
                    item[f'location_timestamp_{i+1}'] = timestamp.strip()

    
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
                INSERT INTO immo_offres_web_article (title, category, nature, price, location, timestamped, link, website,images, date_scraped)
                VALUES (%(title)s, %(category)s, %(nature)s, %(price)s, %(location)s, %(timestamped)s, %(link)s, %(website)s,%(images)s, CURRENT_TIMESTAMP)
                '''
            cursor.execute(sql, {
                'title': item['title'],
                'category': item['category'],
                'price' : item['price'],
                'nature': item['category'], 
                'location': item.get('location_timestamp_1', '') if 'location_timestamp_1' in item else '', 
                'timestamped': item.get('location_timestamp_2', '') if 'location_timestamp_2' in item else '',
                'link': item['link'],
                'website': 'Tayara',
                'images': item['image_url'],
            })

            # Commit the changes and close the database connection
            db_connection.commit()
            db_connection.close()

            yield item
