import requests
import csv
from decouple import config


def readCsv(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        result = []
        reader = csv.DictReader(f)
        for row in reader:
            directors = dict(row)['directors']
            movieNm = dict(row)['movieNm']
            result.append((directors, movieNm))
    return result


def getPeopleInfo(peopleInfo):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json"
    key = config('MOVIE_KEY')
    url = f"{base_url}?key={key}&peopleNm={peopleInfo[0]}&filmoNames={peopleInfo[1]}"
    res = requests.get(url).json()
    return res


def getDirectorInfo(info_dict):
    """
    dict를 넣어주면 해당 정보를 선별해서 합쳐준다
    """
    result = dict()
    peopleInfo = info_dict.get('peopleListResult').get('peopleList')
    if len(peopleInfo) == 0:
        result['peopleCd'] = "정보없음"
        result['peopleNm'] = "정보없음"
        result['repRoleNm'] = "정보없음"
        result['filmoNames'] = "정보없음"
    else:
        peopleInfo = peopleInfo[0]
        result['peopleCd'] = peopleInfo.get('peopleCd')
        result['peopleNm'] = peopleInfo.get('peopleNm')
        result['repRoleNm'] = peopleInfo.get('repRoleNm')
        result['filmoNames'] = peopleInfo.get('filmoNames')
    return result


def writeCsv(write_dict, filename='director.csv'):
    """
    입력받은 write_dict를 한줄한줄씩 파일에 기록한다.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ('peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in write_dict:
            writer.writerow(row)


result = []
direc_name = readCsv("movie.csv")
for d in direc_name:
    direc_info = getPeopleInfo(d)
    result_info = getDirectorInfo(direc_info)
    result.append(result_info)
writeCsv(result)
