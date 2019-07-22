import requests
from decouple import config
import datetime
import csv


def getdate(date, days=7, week=50):
    """
    date는 리스트형으로 [2019, 7, 13]으로 넣어준다
    days는 날짜 간격 
    week 는 뽑고싶은 주간을 입력한다.
    """
    end_date = datetime.date(date[0], date[1], date[2])
    date_delta = datetime.timedelta(days=days)
    cnt = 1
    date_result = [str(end_date).replace("-", "")]
    while cnt < week:
        new_date = end_date - date_delta
        end_date = new_date
        date_str = str(new_date)
        date_replace = date_str.replace("-", "")
        date_result.append(date_replace)
        cnt += 1
    return date_result


def getweekBoxOffice(targetDt, weekGb='0'):
    """
    targetDt의 주의 주간 박스오피스 정보를 가져온다.
    targetDt = yyyymmdd 형식으로 입력해야한다. String으로 입력해야함.
    """
    key = config('MOVIE_KEY')  # 발급받은 키를 입력한다.
    weekGb = "0"
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
    url = f'{base_url}?key={key}&targetDt={targetDt}&weekGb={weekGb}'
    res = requests.get(url).json()
    return res


def getweekInfo(box_dict, rank=10):
    """
    box_dict 에서 각 rank의 moviecd, movieNm, audiAcc 값을 가져온다.
    box_dict는 getweekBoxOffcie의 결과를 넣어준다.
    """
    result_info = {}
    for i in range(rank):
        result_dict = {}
        movieCd = box_dict.get('boxOfficeResult').get(
            'weeklyBoxOfficeList')[i].get('movieCd')
        movieNm = box_dict.get('boxOfficeResult').get(
            'weeklyBoxOfficeList')[i].get('movieNm')
        audiAcc = box_dict.get('boxOfficeResult').get(
            'weeklyBoxOfficeList')[i].get('audiAcc')
        result_dict['MOVIE_CODE'] = movieCd
        result_dict['MOVIE_NAME'] = movieNm
        result_dict['TOTAL_AUDIENCE'] = audiAcc
        result_info[movieCd] = result_dict

    return result_info


def writeCsv(write_dict, filename='boxoffice.csv'):
    """
    입력받은 write_dict를 한줄한줄씩 파일에 기록한다.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ('MOVIE_CODE', 'MOVIE_NAME', 'TOTAL_AUDIENCE')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in write_dict:
            writer.writerow(row)


base_date = [2019, 7, 13]
date_list = getdate(base_date, 7, 50)
date_list = sorted(date_list)
result = dict()
for date in date_list:
    boxres = getweekBoxOffice(date)
    res_info = getweekInfo(boxres)
    result.update(res_info)

result = list(result.values())
writeCsv(result)
