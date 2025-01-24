## AWS S3 Static Website Automation
This project automates the process of downloading a webpage, uploading it to an AWS S3 bucket, and hosting it as a static website. It leverages Selenium for webpage rendering and boto3 for interacting with AWS services.

## Features
Download and save a fully rendered webpage (index.html) using Selenium.
Automate S3 bucket creation and configuration for static website hosting.
Upload files to S3 with the correct Content-Type for HTML.
Generate and display the public URL of the hosted static website.
Prerequisites
AWS Configuration: Ensure your AWS credentials are configured using environment variables or ~/.aws/credentials.
Dependencies: Install the required Python modules:
bash
Copy
pip install selenium boto3  
ChromeDriver: Download and set the path to ChromeDriver in webpage_downloader.py.
Usage
Clone this repository:
bash
Copy
git clone https://github.com/yourusername/aws-s3-static-website.git  
cd aws-s3-static-website  
Update the following configuration files:
S3 bucket name and region in s3_upload.py (BUCKET_NAME and REGION).
Webpage URL in webpage_downloader.py (url).
Run the script:
bash
Copy
python main.py  
Project Structure
main.py: Orchestrates the entire automation process.
s3_upload.py: Contains all AWS S3 operations (bucket creation, file upload, and website configuration).
webpage_downloader.py: Downloads and saves the specified webpage locally.
Output
The script generates a public URL for the hosted static website after successful execution.