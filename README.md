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
 **ChromeDriver**: Download ChromeDriver and update its path in `webpage_downloader.py`.  

## Usage  
1. **Clone this repository**:  
   ```bash  
   git clone https://github.com/yourusername/aws-s3-static-website.git  
   cd aws-s3-static-website  
