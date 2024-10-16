import requests
import time
import csv
import random

url = "http://ece444-pra5-env.eba-jwmtstdr.us-east-2.elasticbeanstalk.com/predict"
test_cases = [
    {"news_string": "Real news article 1"},
    {"news_string": "Real news article 2"},
    {"news_string": "Fake news article 1"},
    {"news_string": "Fake news article 2"}
]

for case in test_cases:
    response = requests.post(url, json=case)
    print(response.text)

# Open a CSV file to store results
with open('performance_test.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Request Number", "Start Time", "End Time", "Latency"])

    for i in range(100):
        case = test_cases[random.randint(0, 3)]
        start_time = time.time()
        response = requests.post(url, json=case)
        end_time = time.time()
        latency = end_time - start_time
        writer.writerow([i+1, start_time, end_time, latency])