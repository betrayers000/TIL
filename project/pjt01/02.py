import requests
import csv
from decouple import config


def getMovieInfo(moviecode):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
    key = config('MOVIE_KEY')
    url = f"{base_url}?key={key}&movieCd={moviecode}"
    res = requests.get(url).json()
    return res


def getweekInfo(info_dict):
    """
    dict를 넣어주면 해당 정보를 선별해서 합쳐준다
    """
    result = dict()
    movieCd = info_dict.get('movieInfoResult').get('movieInfo').get('movieCd')
    result['movieCd'] = movieCd
    movieNm = info_dict.get('movieInfoResult').get('movieInfo').get('movieNm')
    result['movieNm'] = movieNm
    movieNmEn = info_dict.get('movieInfoResult').get(
        'movieInfo').get('movieNmEn')
    result['movieNmEn'] = movieNmEn
    movieNmOg = info_dict.get('movieInfoResult').get(
        'movieInfo').get('movieNmOg')
    result['movieNmOg'] = movieNmOg
    audits = info_dict.get('movieInfoResult').get(
        'movieInfo').get('audits')
    if len(audits) == 0:
        result['audits'] = '전체이용가'
    else:
        result['audits'] = audits[0].get('watchGradeNm')
    prdtYear = info_dict.get('movieInfoResult').get(
        'movieInfo').get('prdtYear')
    result['prdtYear'] = prdtYear
    showTm = info_dict.get('movieInfoResult').get('movieInfo').get('showTm')
    result['showTm'] = showTm

    genres = info_dict.get('movieInfoResult').get('movieInfo').get('genres')
    directors = info_dict.get('movieInfoResult').get(
        'movieInfo').get('directors')
    if len(directors) == 0:
        result['directors'] = ''
    else:
        result['directors'] = directors[0].get('peopleNm')

    g = ""
    for i in genres:
        g = g + i.get('genreNm') + ' '

    result['genres'] = g
    resultlist = []
    resultlist.append(result)
    return resultlist


def readCsv(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        result = []
        reader = csv.DictReader(f)
        for row in reader:
            moviecd = dict(row)['MOVIE_CODE']
            result.append(moviecd)
    return result


def writeCsv(write_dict, filename='boxoffice.csv'):
    """
    입력받은 write_dict를 한줄한줄씩 파일에 기록한다.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ('movieCd', 'movieNm', 'movieNmEn', 'movieNmOg',
                      'audits', 'prdtYear', 'showTm', 'genres', 'directors')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in write_dict:
            writer.writerow(row)


moviecd_list = readCsv('boxoffice.csv')
final_result = []
for i in moviecd_list:
    a = getMovieInfo(i)
    b = getweekInfo(a)
    final_result.extend(b)

writeCsv(final_result, "movie.csv")
