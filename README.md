# Yelp Comment Searcher Project

## A work in progress, allows the user to search local business's comments for a specific phrase.
NOTE: NEEDS YELP-FUSION API KEY TO USE

The purpose of this program is to assess a local businesses for a specific item and verifying the existence through reviews of each associated business.
For example, if I wanted to look for a "Lavender iced latte" through Yelp, there isn't a gaurantee their results will have what I searched for.
Instead, Yelp will return a general search for coffee and will occasionally return a review that features "Lavender Iced Latte"
This program is meant to eliminate the wasted time of finding such occasional review and instead, you can decide what to eat!

<img src = "yelp.jpg" alt = "yelp search results" title = "Yelp results" width = "900" height = "600" display = "inline-block" />

Here is what the program will execute:

(green is user input)
<img src = "results.jpg" alt = "program results" title = "program results" width = "1000" height = "400" display = "inline-block" />

### This project notably uses:
* BeautifulSoup to scrape comments
* Yelp-Fusion-Api: Business URLs, Limit of businesses to search, Location, term to search.
* Python


#### To-do / Planned ideas
* Use BeautifulSoup4 to scrape every review for each business #Currently able to get the reviews from the main business page
* Allow the user to search without the use of Yelp's API
* Optimize BeautifulSoup time to return results
