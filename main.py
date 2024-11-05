from fastapi import FastAPI
import uvicorn

from scraping_service import scraper
from review_analysis import overall_analysis, each_title_analysis

app = FastAPI()

@app.get("/scrape")
def scrape_endpoint(base_url: str):
    result = scraper.scrape(base_url)
    return {"result": result}

@app.get("/overall_sentiment")
def overall_sentiment_endpoint(filepath: str):
    result=overall_analysis(filepath)
    return {"message": "Overall sentiment analysis completed."}

@app.get("/each_title_sentiment")
def each_title_sentiment_endpoint(filepath: str):
    result=each_title_analysis(filepath)
    return {"message": "Individual title sentiment analysis completed."}

def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
