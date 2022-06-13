from urllib import request
from bs4 import BeautifulSoup
import lxml
import time
import redis 

def count_words(url):
    time.sleep(1)

    try:
        r = request.urlopen(url)

        if "bbc" in url:
            tag_text = "p"
            class_text = "ssrcss-1q0x1qg-Paragraph eq5iqo00"
        elif "cnn" in url:
            tag_text = "div"
            class_text = "zn-body__paragraph"
        else:
            tag_text="div"
            class_text = None

        soup = BeautifulSoup(r.read().decode(), "lxml")

        title = soup.title.text

        paragraphs = [p.text for p in soup.find_all(tag_text, class_text)]

        return paragraphs, title
    
    except:
        paragraphs = ["The url you submitted is invalid or cannot be scraped."]
        title = "Failed to access url"
        return paragraphs, title

