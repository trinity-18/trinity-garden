![AI_image](AI_image.jpg)
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
    "x-rapidapi-key": "e7990abd13msh2b5551af1a09605p17bc84jsna5266fb436ab",
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






This project is a Python script that fetches job listings related to "Cybersecurity" from a job search API and saves the data in a CSV file. It utilizes the requests library to interact with the API and pandas to handle data processing.

Features
Queries a job search API for cybersecurity-related jobs in the United States.
Parses and flattens nested JSON data into a more accessible format.
Saves the parsed job data to a CSV file for further analysis or use.



Prerequisites
Before running this script, make sure the following Python libraries are installed:

requests
pandas
You can install them using pip:

bash
Copy code
pip install requests pandas



How the Script Works
API Call: The script sends a GET request to the job search API using the requests library. It includes the required API key in the headers and passes search parameters (for "Cybersecurity" jobs in the U.S.). Each job listing contains the full job description in plain text and HTML, the job title, publication time, company name, source and application URL. The salary range is provided when it's available. The salary type has 5 possible values: "yearly", "monthly", "weekly", "daily" and "hourly". With this code it only returns 10 listings for cybersecurity.


Parse Response: The response, which comes in JSON format, is parsed. The relevant job data is located under the jobs key in the JSON structure.

Flatten Nested JSON: Many of the job details come in nested structures. The script flattens these nested dictionaries, transforming them into a single-layer dictionary where each nested field is concatenated with its parent key.

DataFrame Creation: The flattened data is then converted into a pandas DataFrame for easy manipulation and export.

CSV Export: Finally, the DataFrame is saved as a CSV file (cybersecurity_jobs.csv) for further use.

How to Use
API Key: Replace the placeholder value of "x-rapidapi-key" with your actual RapidAPI key.

python
Copy code
headers = {
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY_HERE",
    "x-rapidapi-host": "job-search-api1.p.rapidapi.com"
}
Running the Script: Run the script in a Python environment.

bash
Copy code
python job_scraper.py
Output: The script will output a CSV file named cybersecurity_jobs.csv containing the job listings.

Parameters
You can modify the job search parameters in the querystring to suit your needs:

q: Change the keyword from "Cybersecurity" to any other field of interest (e.g., "Data Science").
page: Adjust the page number for pagination. 
country: Specify the country (default is the U.S.).
python
Copy code
querystring = {"q": "Cybersecurity", "page": "1", "country": "us"}
Error Handling
If the API call fails (status code other than 200), the script will print an error message and exit.
python
Copy code
if response.status_code != 200:
    print(f"Failed to fetch data. Status code: {response.status_code}")
