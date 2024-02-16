from pathlib import Path
from datetime import datetime, timedelta
import json
def joinFiles(folder_path):
    today_date = datetime.now()
    one_day_delta = timedelta(days=1)
    new_date = today_date - one_day_delta
    formatted_date = new_date.strftime('%Y-%m-%d')
    folder = Path(folder_path)
    matching_files = [file for file in folder.iterdir() if formatted_date in file.name and file.suffix.lower() == '.json']
    all_data = []
    
    for file in matching_files:
        with open(file, 'r') as f:
            data = json.load(f)
            all_data.extend(data)
    
    if len(all_data) == 0:
        print(f"There is no files today for {folder_path}")
    else:
        output_file_name = f"{formatted_date}_superchats.json"
        output_file_path = folder / output_file_name

        with open(output_file_path, 'w') as output_file:
            json.dump(all_data, output_file)

        print(f"All matching JSON files have been aggregated into {output_file_path}")