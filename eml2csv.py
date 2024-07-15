#Last update July 15th 2024

import os
import re
import csv
from datetime import datetime
import email
from email import policy
from email.parser import BytesParser

# Define regex patterns to extract the data. Open the .eml file to check the structure
patterns = {
    "Name": re.compile(r'<b>Name:</b>\s*<span>(.*?)</span>'),
    "Email": re.compile(r'<b>Email:</b>\s*<span>(.*?)</span>'),
    "Organization": re.compile(r'<b>Organization:</b>\s*<span>(.*?)</span>'),
    "Number": re.compile(r'<b>Number:</b>\s*<span>(.*?)</span>'),
    "LinkedIn profile": re.compile(r'<b>LinkedIn profile:</b>\s*<span>(.*?)</span>'),
}

# Function to extract data from email content
def extract_data(email_content):
    data = {}
    for key, pattern in patterns.items():
        match = pattern.search(email_content)
        data[key] = match.group(1).replace('=2E', '.') if match else ''
    return data

# Function to parse the date from the email headers
def parse_date(headers):
    for header in headers.get_all('Received', failobj=[]):
        if ';' in header:
            date_str = header.split(';')[-1].strip()
            try:
                date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
                return date_obj.strftime('%m/%d/%Y')
            except ValueError:
                continue
    return ''

# !!!INSERT THE FOLDER PATH CONTAINING THE .eml FILES!!!
folder_path = '[INSERT PATH HERE]'

# List to store extracted data from all emails
all_data = []

# Read each .eml file from the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.eml'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)
            # Get the email content
            email_content = msg.get_body(preferencelist=('html')).get_content()
            # Extract data from the email content
            extracted_data = extract_data(email_content)
            # Parse the date from the email headers
            extracted_data['Date'] = parse_date(msg)
            all_data.append(extracted_data)

# Creates the csv file if it doesn't exist. Otherwise, specify the file
csv_file = 'extracted_data.csv'

# Write data to CSV file
if all_data:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=all_data[0].keys())
        writer.writeheader()
        for data in all_data:
            writer.writerow(data)

print(f"Thanks Jun! Data extracted and saved to {csv_file}")