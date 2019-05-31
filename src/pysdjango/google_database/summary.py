import nltk
import requests
from bs4 import BeautifulSoup
from summarize import summarize

class Summary:
    # Just call sumText, others are supporter functions
    def sumText(self,url):
        text = self.fetchHtml(url)
        return self.suma(text)

    def fetchHtml(self,url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        page = soup.find_all('p')
        para = ""
        for p in page:
            para += p.get_text()
        return para
    
    def suma(self,text):
        nltk.data.path.append("google_database/support/nltk_data/")
        return summarize(text, sentence_count=3, language='english')