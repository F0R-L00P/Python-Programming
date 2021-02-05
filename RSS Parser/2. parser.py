import feedparser

# steps in RSS download
    #1. download the feed first
    #2. parse data

# set file to variable object    
feed_file = 'newrelease.xml'

# pass parser over the file
feed = feedparser.parse(feed_file)

# feedparser allows you to pull data based on tags
# i.e. <title> | <description>
# lets get title and publication date
# although it mentions PubDate, but its published

## before running the script, put in a conditional check 
## to ensure everything is in order, i.e. tags don't exist
if 'title' in feed.entries[0]:
    for i in feed.entries:
        print(f'{i.published} - {i.title}: {i.link}')

