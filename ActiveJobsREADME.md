 Job Data Downloader

# Description:
This Python script fetches job data from an API and saves it in both CSV and JSON formats.

# Installation:
## Prerequisites: Ensure you have Python 3 and the following libraries installed:

* json
* csv
* http.client
* urllib.parse

You can install them using:

<!-- python code block -->
```python
pip install json csv http.client urllib.parse
```

**API Key:**
You'll need an API key for the "active-jobs-db.p.rapidapi.com" service. Obtain one and replace the placeholder value in the headers dictionary within the code.

**Usage:**
1. Save the script: Save the provided code as a Python file (e.g., `job_data_downloader.py`).
2. Run the script: Execute the script from your terminal using:

<!-- python code block -->
```python
python job_data_downloader.py
```

**Explanation:**
The script defines three primary functions:

* **`get_jobs(title, location)`:**
  * Establishes a connection to the API using `http.client.HTTPSConnection`.
  * Creates headers with the API key and host.
  * Encodes the title and location for a valid URL format using `urllib.parse.quote`.
  * Sends a GET request to the API and retrieves the response data.
  * Parses the JSON response using `json.loads`.
  * Returns the list of jobs in dictionary format if successful, or `None` if no jobs are found or an error occurs.

* **`write_to_csv(jobs, filename)`:**
  * Opens the specified filename in write mode (`'w'`).
  * Checks if the jobs list is empty. If not, extracts the field names from the first dictionary in the list.
  * Creates a `csv.DictWriter` object to handle writing dictionary data to the CSV file.
  * Writes the header row with field names.
  * Iterates through each job dictionary and writes it as a row to the CSV file.
  * Handles the empty jobs case by printing a message.

* **`write_to_json(jobs, filename)`:**
  * Opens the provided filename with the `.json` extension in write mode.
  * Dumps the jobs list (representing dictionaries) in JSON format to the file with indentation (indent=4) for readability.

**Example Usage:**
The script demonstrates how to use these functions with sample values for `job_title` ("entrylevel_cybersecurity") and `job_location` ("United States").

<!-- python code block -->
```python
job_title = "entrylevel_cybersecurity"
job_location = "United States"

jobs = get_jobs(job_title, job_location)

if jobs:
    write_to_csv(jobs, f"{job_title}_{job_location}_jobs.csv")
    write_to_json(jobs, f"{job_title}_{job_location}_jobs.json")
    print(f"Saved {len(jobs)} jobs to CSV and JSON files.")
else:
    print("No jobs found for the specified criteria.")
```

**Additional Notes:**
* **Error handling:** The `get_jobs` function includes basic error handling using a `try-except-finally` block to catch exceptions and close the connection regardless of success or failure. You might consider more granular error handling for specific API responses or potential issues.
* **API usage:** Be mindful of the API's terms of use and rate limits, especially if making frequent requests.
* **Customization:** You can modify the `job_title` and `job_location` variables in the example usage to suit your needs.

# Frequently Asked Questions (FAQ)
1. What is the purpose of this script?

This Python script is designed to fetch job data from a specified API and save the results in both CSV and JSON formats.

2. What are the prerequisites for using this script?

You'll need Python 3 installed on your system, along with the following libraries:

json
csv
http.client
urllib.parse
3. How do I obtain an API key?

To use the API, you'll need an API key. Please refer to the API provider's documentation for instructions on obtaining an API key.

4. Can I customize the job search parameters?

Yes, you can. The script allows you to modify the job_title and job_location variables in the example usage to search for jobs in specific locations and with particular titles.

5. What if no jobs are found?

If the script cannot find any jobs matching the specified criteria, it will print a message indicating that no jobs were found.

6. Can I save the results in other formats?

Currently, the script only saves the results in CSV and JSON formats. However, you could potentially modify the script to support additional formats if needed.

7. How can I handle errors that might occur during the process?

The script includes basic error handling, but you may want to implement more robust error handling mechanisms to deal with specific error scenarios.

8. Are there any limitations or restrictions on API usage?

Please refer to the API provider's terms of service for any limitations or restrictions on API usage, such as rate limits or usage quotas.
