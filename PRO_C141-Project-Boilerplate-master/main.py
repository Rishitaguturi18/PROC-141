from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
all_articles = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

def assign_val():
    m_data = {
        "url": all_articles.iloc[0,0],
        "title": all_articles.iloc[0,1],
        "text": all_articles.iloc[0,2] or "N/A",
        "lang": all_articles.iloc[0,3],
        "total_events": all_articles.iloc[0,4]
    }
    return m_data

# API to display first article
@app.route("/get-article")
def get_article():
    global get_article
    
    if not all_articles:  # Check if the list is empty
        return jsonify({
            "message": "No articles found",
            "status": "error"
        })

    # Get the first article
    first_article = all_articles[0]

    def format_article(article):
        # Replace this with logic to select and format relevant article data
        # (e.g., title, content snippet, author, keywords)
        formatted_data = {
            "title": article.get("title", "No title available"),  # Handle potential missing key
            "content": article.get("content", "No content available"),  # Handle potential missing key
            # Add other relevant data fields here based on your article structure
        }
        return formatted_data

    # Format the article data
    formatted_article = format_article(first_article)

    return jsonify({
        "data": formatted_article,
        "status": "success"
    })


# API to move the article into liked articles list
@app.route("/liked-article")
def liked_article():
    global liked_article
    
    if not all_articles:  # Check if the list is empty
        return jsonify({
            "message": "No articles found",
            "status": "error"
        })

    # Get the first article
    first_article = all_articles[0]

    def format_article(article):
        # Replace this with logic to select and format relevant article data
        # (e.g., title, content snippet, author, keywords)
        formatted_data = {
            "title": article.get("title", "No title available"),  # Handle potential missing key
            "content": article.get("content", "No content available"),  # Handle potential missing key
            # Add other relevant data fields here based on your article structure
        }
        return formatted_data

    # Format the article data
    formatted_article = format_article(first_article)

    return jsonify({
        "data": formatted_article,
        "status": "success"
    })
    


# # API to move the article into not liked articles list
@app.route("/unliked-article")
def unliked_article():
    global unliked_article
    
    if not all_articles:  # Check if the list is empty
        return jsonify({
            "message": "No articles found",
            "status": "error"
        })

    # Get the first article
    first_article = all_articles[0]

    def format_article(article):
        # Replace this with logic to select and format relevant article data
        # (e.g., title, content snippet, author, keywords)
        formatted_data = {
            "title": article.get("title", "No title available"),  # Handle potential missing key
            "content": article.get("content", "No content available"),  # Handle potential missing key
            # Add other relevant data fields here based on your article structure
        }
        return formatted_data

    # Format the article data
    formatted_article = format_article(first_article)

    return jsonify({
        "data": formatted_article,
        "status": "success"
    })
   

# run the application
if __name__ == "__main__":
    app.run()