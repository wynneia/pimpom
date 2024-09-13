import json

def split_json(file_path, chunk_size_mb):
    # Load the JSON data from file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Check if data is a list
    if not isinstance(data, list):
        raise ValueError("The JSON data should be a list of objects for this script.")

    # Calculate chunk size in number of items
    chunk_size = chunk_size_mb * 1024 * 1024  # Convert MB to bytes
    item_size = len(json.dumps(data[0]).encode('utf-8'))  # Size of one item
    items_per_chunk = chunk_size // item_size

    # Split the data into chunks
    for i in range(0, len(data), items_per_chunk):
        chunk = data[i:i + items_per_chunk]
        
        # Write chunk to a new file
        with open(f"{file_path}_part_{i//items_per_chunk + 1}.json", 'w') as chunk_file:
            json.dump(chunk, chunk_file, ensure_ascii=False, indent=4)

# Example usage
split_json('lyrics.json', 100)  # 100 MB chunks
