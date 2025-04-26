from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import requests

app = FastAPI()

# 允许跨域访问，方便 ChatGPT 调用
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tiktok-toy-influencers", tags=["TikTok"])
def get_tiktok_toy_influencers():
    url = "https://www.noxinfluencer.com/tiktok-ranking/top100/genre-toys-country-us"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    result = []
    rows = soup.select("div.ranking-table-list__item")
    for row in rows[:10]:
        name_tag = row.select_one("a.user-name")
        followers_tag = row.select_one("div.followers span.value")
        username = name_tag.text.strip() if name_tag else "N/A"
        followers = followers_tag.text.strip() if followers_tag else "N/A"
        result.append({
            "username": username,
            "followers": followers
        })
    return result
