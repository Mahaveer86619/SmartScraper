import requests
from bs4 import BeautifulSoup

def scrape_content(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unwanted elements
        for tag in ['script', 'style', 'nav', 'footer']:
            for element in soup.find_all(tag):
                element.decompose()
                
        return ' '.join(soup.stripped_strings)[:5000]  # Limit content length
    
    except Exception as e:
        return f"Scraping error: {str(e)}"