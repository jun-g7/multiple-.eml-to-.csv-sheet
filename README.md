# Email Data Extraction Script

This repository contains a Python script to extract specific information from `.eml` files and save the extracted data into a CSV file.
It uses the 'email' module (that's already included in the Python standard library).
Currently using Python version 3.12.4

## Overview

The script reads all `.eml` files from a specified folder, extracts the following fields from each email, and saves the data into a CSV file:
- Name
- Email
- Organization
- Number
- LinkedIn profile

(make sure to change this part based on the data you need to extract from the '.eml' files)

## Usage

1. Clone this repository or download the script.

2. Place your `.eml` files in a folder.

3. Set the `folder_path` variable in the script to the path of your folder containing the `.eml` files.

4. Run the script.

5. The extracted data will be saved to a file named `extracted_data.csv` in the same directory as the script.
