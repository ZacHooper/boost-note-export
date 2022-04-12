# This script will take the raw boostnote exported data and extract the Markdown files from them. 
# It will sort the files into their appropriate folders as well as possible.

import json
from pathlib import Path

# Import data
with open('boostnote_data.json', 'r') as infile:
    data = json.load(infile)
    docs = data['docs']

    for doc in data['docs']:
        try:
            # title
            title = doc['title']
            # Escape '/' from files
            title = title.replace("/", "-")
            # folderPathname
            folder_path = f"files{doc['folderPathname']}"
            Path(folder_path).mkdir(parents=True, exist_ok=True)
            # content
            # If no head then there is no content so skip
            if doc['head'] is None:
                continue
            content = doc['head']['content']
            with open(f"{folder_path}/{title}.md", 'w') as outfile:
                outfile.write(content)
        except Exception as e:
            raise Exception(f"{e}: {doc}")

