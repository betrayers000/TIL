import random
import requests
from bs4 import BeautifulSoup
from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/lotto')
def lotto():
    numbers = random.sample(range(1, 46), 6)
    print(numbers)
    return render_template('lotto.html', numbers=numbers)


@app.route('/lunch')
def lunch():
    menus = {
        "떡국": "http://recipe1.ezmember.co.kr/cache/recipe/2016/02/07/6233560ef23f814c29f7462fd898b8201.jpg",
        "나주곰탕": "http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1201/IE002061721_STD.JPG",
        "설렁탕": "http://mblogthumb2.phinf.naver.net/MjAxODAyMTFfNTUg/MDAxNTE4MzE1MzU3Nzk2.ufHPJ8GrImaTTUO7Vk_VEi2nmMXPuQoAEWN8dGcHwjog.KXWmi5lnMAjIdWKU1bMxfAtEqd-0mNza4plbifERCOUg.JPEG.chunje0/%EC%84%A4%EB%A0%81%ED%83%95.jpg?type=w800",
        "파스타": "http://recipe1.ezmember.co.kr/cache/recipe/2017/07/16/40599182ff7e1207c1704a05ca2ae3b41.jpg",
        "오므라이스": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqqz_7iaoq6MaQT4tqO1lGkkde-ydNcfCyidfIQidLJHS9NJYH",
        "짬뽕": "http://recipe1.ezmember.co.kr/cache/recipe/2017/02/18/42ec50c7c281289367d1e7e4d06f4fcc1.jpg",
        "짜장면": "http://recipe1.ezmember.co.kr/cache/recipe/2016/07/02/40c4f639ca973d9acccecdf7cbe0cbc41.jpg"
    }

    menu = random.choice(list(menus.keys()))
    src = menus.get(menu)
    return render_template('lunch.html', menu=menu, src=src)


@app.route('/opgg')
def opgg():
    return render_template('opgg.html')


@app.route('/search')
def search():
    opgg_url = 'https://www.op.gg/summoner/userName='
    summoner = request.args.get('summoner')
    url = opgg_url + summoner

    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    tier = soup.select_one(
        "#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank")
    user_tier = tier.text.strip()
    return render_template('search.html', user_tier=user_tier, summoner=summoner)


if __name__ == "__main__":
    app.run(debug=True)
