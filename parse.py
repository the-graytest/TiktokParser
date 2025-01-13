import re
import json

# Usage python parse.py >> results.txt

def extract_links(path):
    links = set()
    tiktok_pattern = re.compile(r'https://www\.tiktok\.com/@\S+/video/\d+')

    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            matches = tiktok_pattern.findall(line)
            if len(matches) > 0:

                link = matches[0]
                if link[-1] == ")":
                   link = link[:-1]
                links = set([link]) | set(links)
    return links



docx_path = 'recipes.txt' # Change this to the path for your .txt file



# Extract and print the links
final_links = set(extract_links(docx_path))
for link in final_links:
    print (link)
