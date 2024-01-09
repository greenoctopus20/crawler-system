#!/usr/bin/python3

from bs4 import BeautifulSoup
import os

# Function to get file size
def get_file_size(file_path):
    return os.path.getsize(file_path)

# Function to remove head and footer tags
def remove_head_footer(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for tag in soup(['head', 'footer']):
        tag.decompose()
    return str(soup)

# List of HTML files
html_files = ['1.html', '2.html']

# Print header for the table
print("{:<20} {:<25} {:<25} {:<20}".format("File Name", "Original Size (bytes)", "Modified Size (bytes)", "Reduction (%)"))

# Process each HTML file
for file_name in html_files:
    with open(file_name, 'r') as file:
        content = file.read()
        original_size = get_file_size(file_name)
        print(f"{file_name:<20} {original_size:<25} ", end='')

        # Remove head and footer tags
        modified_content = remove_head_footer(content)

        # Write modified content back to the file
        with open(f"modified_{file_name}", 'w') as modified_file:
            modified_file.write(modified_content)

        modified_size = get_file_size(f"modified_{file_name}")
        reduction_percentage = ((original_size - modified_size) / original_size) * 100
        print(f"{modified_size:<25} {reduction_percentage:.2f}%")
