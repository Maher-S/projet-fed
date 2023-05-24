from celeryschedulers import run_tayara_scraper, run_tunisie_annonce_scraper

# Define a function or method where you want to trigger the task execution
def execute_tasks():
  
    # Call the task functions using the delay() method to enqueue the tasks for execution
    run_tayara_scraper.delay()
    run_tunisie_annonce_scraper.delay()

    # Call the function to trigger the task execution
    execute_tasks()

    
  