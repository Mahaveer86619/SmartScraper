from flask import Flask, render_template, request
from scraper import scrape_content
from llm_processor import structure_data
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    url = ''
    user_schema = ''
    
    if request.method == 'POST':
        url = request.form['url']
        user_schema = request.form['schema']
        content = scrape_content(url)
        
        if content and user_schema:
            try:
                result = structure_data(content, user_schema)
            except Exception as e:
                result = f"Error processing data: {str(e)}"
                
    return render_template('index.html', 
                         result=result,
                         url=url,
                         schema=user_schema)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)