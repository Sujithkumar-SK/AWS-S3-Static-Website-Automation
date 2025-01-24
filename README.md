# AWS S3 Static Website Automation

This project automates downloading a webpage, uploading it to an AWS S3 bucket, and hosting it as a static website. It uses **Selenium** for webpage rendering and **boto3** for AWS services.

## Features
- **Download Webpage**: Save a fully rendered webpage as `index.html` using Selenium.
- **Automate S3 Operations**: Create and configure S3 buckets for static website hosting.
- **File Upload with Correct MIME Type**: Ensure HTML files have the proper `Content-Type`.
- **Static Website URL**: Generate and display the public URL for the hosted website.

## Prerequisites
1. **AWS Configuration**: Set up AWS credentials using environment variables or `~/.aws/credentials`.
2. **Dependencies**: Install the required Python modules:
   ```bash
   pip install selenium boto3
ChromeDriver: Download ChromeDriver and update its path in webpage_downloader.py.
Usage
Clone this repository:
bash
Copy
git clone https://github.com/yourusername/aws-s3-static-website.git
cd aws-s3-static-website
Update the configuration files:
S3 Bucket Name and Region: Edit BUCKET_NAME and REGION in s3_upload.py.
Webpage URL: Set the target webpage URL in webpage_downloader.py.
Run the script:
bash
Copy
python main.py
Project Structure
main.py: Orchestrates the entire automation process.
s3_upload.py: Handles all AWS S3 operations, including bucket creation and website configuration.
webpage_downloader.py: Downloads and saves the specified webpage locally.
Output
After successful execution, the script generates and displays the public URL for the hosted static website.