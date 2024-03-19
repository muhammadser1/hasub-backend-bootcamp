import json

def merge_json_files(file1, file2, output_file):
    # Read data from the first file
    with open(file1, 'r') as f1:
        data1 = json.load(f1)

    # Read data from the second file
    with open(file2, 'r') as f2:
        data2 = json.load(f2)

    # Merge player data
    merged_data = {
        "players": data1.get("players", []) + data2.get("players", [])
    }

    # Write merged data to a new file
    with open(output_file, 'w') as out_file:
        json.dump(merged_data, out_file, indent=4)

# Example usage
merge_json_files("file1.json", "file2.json", "merged_file.json")
