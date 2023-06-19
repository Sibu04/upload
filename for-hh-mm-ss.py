######################################################
# Filename: for-hh-mm-ss.py
# Purpose: This code converts a large JSON file into smaller
#          chunks and saves each chunk as a separate JSON file.
# Author: Sibu
# Date: May 25, 2023
######################################################

import json
import requests

# Prompt the user to enter the URL of the JSON data
url = input("Enter the URL of the JSON data: ")
response = requests.get(url)

# Load the JSON data
data = json.loads(response.content.decode("utf-8"))

# Print the number of elements in the array
print("Number of elements in the array:", len(data))

# Prompt the user to enter the chunk size
chunk_size = int(input("Enter the chunk size: "))

# Calculate the number of chunks needed
num_chunks = len(data) // chunk_size + (len(data) % chunk_size != 0)

# Prompt the user to enter the file name prefix
prefix = input("Enter the file name prefix: ")

# Split the data into chunks and save each chunk as a separate JSON file
for i in range(num_chunks):
    start_index = i * chunk_size
    end_index = min((i + 1) * chunk_size, len(data))

    chunk = data[start_index:end_index]

    # Generate the filename for the current chunk
    filename = f"{prefix}_{i+1}.json"
    
    # Save the current chunk as a JSON file
    with open(filename, "w") as f:
        json.dump(chunk, f)
