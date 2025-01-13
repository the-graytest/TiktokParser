# TiktokParser
For Pulling TikTok URL's from a document


## Usage: 
This is inteded to capture all tiktok video links from a single text file. 

## To create your  file:
- Go To a tiktok playlist (it can be your favorites or any other playlist)
- Scroll to the bottom so that all videos are loaded on the page
- Cmd + a (select all) >> Copy >> Paste into a google doc
- Save, the click on file, download, and choose Markdown (.md) as the file format
- Re-Save the downloaded file as a .txt file (I used recipes.txt as the file name)

## To run the script:
- Ensure you have [python installed](https://realpython.com/installing-python/)
- Update the parse.py file with the path to the text file you generated
- Run `python parse.py >> results.txt` to output the links into a .txt file
- Use the links! You can feed them into a video downloader or do what I did and put them in a spreadsheet to keep track of where to find those videos on other platforms

## Future Work
There's not much time left for future work but, if I have time this weeked I would like to use a scraper to pull the upload date and description as well as the link in the author's bio to be able to find videos after the app is gone. If you would like to create a PR for that or clone this repo with that feature added, I'd love to see it!
