import json
import os

def split_json(file_path, chunk_size_mb):
    # Load the JSON data from file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Convert chunk size to bytes
    chunk_size = chunk_size_mb * 1024 * 1024
    
    # Calculate total size of data in bytes
    total_size = len(json.dumps(data).encode('utf-8'))
    
    # Calculate the number of chunks needed
    num_chunks = (total_size // chunk_size) + 1
    
    # Split the data into chunks
    for i in range(num_chunks):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size
        chunk_data = json.dumps(data[start_index:end_index], ensure_ascii=False)
        
        # Write chunk to a new file
        with open(f"{file_path}_part_{i+1}.json", 'w') as chunk_file:
            chunk_file.write(chunk_data)

# Example usage
split_json('lyrics.json', 100)  # 100 MB chunks
