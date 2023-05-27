import logging
import schedule
import time
import subprocess

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

tayara_spider_path = "C:/Users/maher/OneDrive/Desktop/hola/Tayara.py"
tunisieannonce_spider_path = "C:/Users/maher/OneDrive/Desktop/hola/TunisieAnnonce.py"

def run_tayara():
    logging.info('Starting TayaraSpider...')
    try:
        subprocess.run(["scrapy", "runspider", tayara_spider_path])
        logging.info('TayaraSpider completed successfully.')
    except Exception as e:
        logging.error(f'TayaraSpider encountered an error: {str(e)}')

def run_tunisieannonce():
    logging.info('Starting TunisieAnnonceSpider...')
    try:
        subprocess.run(["scrapy", "runspider", tunisieannonce_spider_path])
        logging.info('TunisieAnnonceSpider completed successfully.')
    except Exception as e:
        logging.error(f'TunisieAnnonceSpider encountered an error: {str(e)}')

def schedule_tasks():
    # Clear any previously scheduled tasks
    schedule.clear()

    # Set the start and expiration times for each task
    tayara_start_time = "07:22"
    tayara_expiration_time = "07:24"
    tunisieannonce_start_time = "07:25"
    tunisieannonce_expiration_time = "07:30"

    # Schedule the tasks to run at the start times
    schedule.every().day.at(tayara_start_time).do(run_tayara)
    schedule.every().day.at(tunisieannonce_start_time).do(run_tunisieannonce)

    # Schedule the tasks to expire at the expiration times
    schedule.every().day.at(tayara_expiration_time).do(cancel_tayara)
    schedule.every().day.at(tunisieannonce_expiration_time).do(cancel_tunisieannonce)

def cancel_tayara():
    # Clear the scheduled task for TayaraSpider
    schedule.clear(run_tayara)

def cancel_tunisieannonce():
    # Clear the scheduled task for TunisieAnnonceSpider
    schedule.clear(run_tunisieannonce)

def run_scheduler():
    # Run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)

# Schedule and run the tasks
schedule_tasks()
run_scheduler()
