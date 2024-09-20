# prompt:  jobs = response.json()  # Parse the response into JSON format
#     jobs['jobs']   flattened the nested Json and convert it to a dataframe

import requests
import pandas as pd
# 
# 

# API endpoint and query
url = "https://job-search-api1.p.rapidapi.com/v1/job-description-search"
querystring = {"q": "Cybersecurity", "page": "1", "country": "us"}

# API headers with RapidAPI key
headers = {
    "x-rapidapi-key": "Your-API-Key",
    "x-rapidapi-host": "job-search-api1.p.rapidapi.com"
}

# Sending the request to the API
response = requests.get(url, headers=headers, params=querystring)

# Check if the response status is OK (status code 200)
if response.status_code == 200:
    jobs = response.json()  # Parse the response into JSON format
    job_list = jobs['jobs']
    # Flatten the nested JSON
    flattened_jobs = []
    for job in job_list:
        flattened_job = {}
        for key, value in job.items():
            if isinstance(value, dict):
                for nested_key, nested_value in value.items():
                    flattened_job[f"{key}_{nested_key}"] = nested_value
            else:
                flattened_job[key] = value
        flattened_jobs.append(flattened_job)

    # Convert the list of jobs into a pandas DataFrame
    df = pd.DataFrame(flattened_jobs)

    # Save the DataFrame to a CSV file
    df.to_csv("cybersecurity_jobs.csv", index=False)

    print("Job data saved to 'cybersecurity_jobs.csv'")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
