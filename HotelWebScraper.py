# prompt: generate a code that uses this snippet to scrape the web for cybersecurity job
# import requests
# url = "https://active-jobs-db.p.rapidapi.com/active-ats"
# querystring = {"title":"entrylevelCybersecurity ","location":"\"United States\"","offset":"100","description":"text"}
# headers = {
# 	"x-rapidapi-key": "e7990abd13msh2b5551af1a09605p17bc84jsna5266fb436ab",
# 	"x-rapidapi-host": "active-jobs-db.p.rapidapi.com"

import requests
import json
import csv

url = "https://active-jobs-db.p.rapidapi.com/active-ats"
querystring = {"title": "entrylevelCybersecurity", "location": "\"United States\"", "offset": "100", "description": "html"}
headers = {
    "x-rapidapi-key": "e7990abd13msh2b5551af1a09605p17bc84jsna5266fb436ab",
    "x-rapidapi-host": "active-jobs-db.p.rapidapi.com"
}

def get_jobs_data(url, querystring, headers):
    """
    Retrieves job data from the API.

    Args:
        url: The API endpoint URL.
        querystring: The query parameters for the API request.
        headers: The headers for the API request.

    Returns:
        A list of dictionaries representing the jobs, or None if no jobs are found.
    """
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def write_to_csv(jobs, filename):
    """
    Writes data to a CSV file.

    Args:
        jobs: A list of dictionaries representing the jobs.
        filename: The name of the CSV file to write to.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        if jobs:
            fieldnames = jobs[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for job in jobs:
                writer.writerow(job)
        else:
            print("No jobs data to write to CSV.")


def write_to_json(jobs, filename):
    """
    Writes data to a JSON file.

    Args:
        jobs: A list of dictionaries representing the jobs.
        filename: The name of the JSON file to write to.
    """
    with open(filename + '.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(jobs, jsonfile, indent=4)


jobs_data = get_jobs_data(url, querystring, headers)

if jobs_data:
    write_to_csv(jobs_data, "cybersecurity_jobs.csv")
    write_to_json(jobs_data, "cybersecurity_jobs")
