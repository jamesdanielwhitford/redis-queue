from urllib import request
from bs4 import BeautifulSoup
import lxml
import time
import redis 

def scrape_url(url):

    try:
        r = request.urlopen(url)

        if "bbc" in url:
            tag_text = "p"
            class_text = "ssrcss-1q0x1qg-Paragraph eq5iqo00"
        elif "cnn" in url:
            tag_text = "div"
            class_text = "zn-body__paragraph"
        else:
            tag_text="p"
            class_text = None

        soup = BeautifulSoup(r.read().decode(), "lxml")

        title = soup.title.text

        paragraphs = [p.text for p in soup.find_all(tag_text, class_text)]

        return paragraphs, title
    
    except Exception as e:
        paragraphs = ["The url you submitted is invalid or cannot be scraped.", f"The url returned this failure: \n\n{e}"]
        title = "Failed to access the url"
        return paragraphs, title, e

