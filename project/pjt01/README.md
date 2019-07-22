# Project

## pjt01

### 01.py

> 주간/주말 박스오피스 데이터 API를 이용해서 데이터 수집

##### 1. getdate

- 날짜정보를 가져오는 함수

- datetime을 이용해서 입력 간격과 반복횟수로 날짜를 가져온다

  ```python
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
      # 첫번째 날짜의 경우 반복문 들어가기전에 미리 입력해준다.
      while cnt < week:
          new_date = end_date - date_delta
          end_date = new_date
          date_str = str(new_date)
          date_replace = date_str.replace("-", "")
          date_result.append(date_replace)
          cnt += 1
      return date_result
  ```

##### 2. getweekBoxOffice

- API를 활용해서 박스오피스 정보를 가져오는 함수

- 여기서 decouple을 이용해서 key 값을 숨겨야 한다.

- requests 할때 `json()` 을 이용해서 dict 형태로 받는다

  ```python
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
  ```

##### 3. getweekInfo()

- dict 파일을 받아서 반복 횟수만큼 반복해서 데이터를 뽑아준다.

- 마지막에 딕셔너리 형태로 넣어서 중복값 제거에 이용한다.

  ```python
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
          #dict형태로 key 값을 movieCd를 넣어주면서 중복값을 제거하도록 한다.
  
      return result_info
  ```

##### 4. wrtieCsv

- csv 파일을 생성해주는 함수 

- fieldnames 도 인자로 받아서 공용으로 사용할수있게 하면 좋을 것 같다.

  ```python
  def writeCsv(write_dict, filename='boxoffice.csv'):
      """
      입력받은 write_dict를 한줄한줄씩 파일에 기록한다.
      filednames 와 dict의 key와 맞게 넣어야 한다.
      """
      with open(filename, 'w', newline='', encoding='utf-8') as f:
          fieldnames = ('MOVIE_CODE', 'MOVIE_NAME', 'TOTAL_AUDIENCE')
          writer = csv.DictWriter(f, fieldnames=fieldnames)
          writer.writeheader()
          for row in write_dict:
              writer.writerow(row)
  
  ```

##### 5. 코드 수행

- sorted로 date 리스트를 정렬해서 최대값으로 update 한다.

  ```python
  import requests
  from decouple import config
  import datetime
  import csv
  
  base_date = [2019, 7, 13]
  date_list = getdate(base_date, 7, 50)
  date_list = sorted(date_list)
  # sorted를 사용해서 정렬시킨다. 큰값을 남겨야 하기 때문에 날짜를 정렬시키면
  # 최신날짜 일수록 관람객이 늘어나기 때문
  
  result = dict()
  for date in date_list:
      boxres = getweekBoxOffice(date)
      res_info = getweekInfo(boxres)
      result.update(res_info)
  
  result = list(result.values())
  writeCsv(result)
  ```



### 02.py

> 01.py 에서 저장한 csv 파일을 읽어와서 영화 상세정보를 가져온다.
>
> 값이 없는 경우 분기처리를 해야 하기 때문에 여러번 오류를 만나야했다..

##### 1. readcsv

- csv 파일을 읽는 함수

- 딕셔너리 키값을 인자로 받게 해서 다양하게 사용해도 좋을것 같다.

  ```python
  def readCsv(filename):
      with open(filename, 'r', newline='', encoding='utf-8') as f:
          result = []
          reader = csv.DictReader(f)
          for row in reader:
              moviecd = dict(row)['MOVIE_CODE']
              result.append(moviecd)
      return result
  ```

##### 2. getweekInfo

- 영화의 상세정보가 들어있는 dict에서 필요한 값만 가져온다.

- 01.py에서 복사해와서 이름 변경하는걸 잊어버렸다.

- 값중에 리스트 형태의 값은 길이가 0인 경우 if로 분기처리해서 오류가 안나게 처리한다.

- 관람가에서 정보가 없을경우 전체이용가로 표기

- 장르의 경우 for문을 따로 돌려 여러 장르가 나타나게함 

  ```python
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
      
      #감독명이 없는 경우가 있기 때문에 분기처리한다
      if len(directors) == 0:
          result['directors'] = ''
      else:
          result['directors'] = directors[0].get('peopleNm')
          
      # 장르의 경우 여러값이 있기 때문에 공백을 기준으로 String 형태로 저장
      g = ""
      for i in genres:
          g = g + i.get('genreNm') + ' '
  
      result['genres'] = g
      resultlist = []
      resultlist.append(result)
      return resultlist
  ```

##### 3. 코드 수행

```python
import requests
import csv
from decouple import config


def getMovieInfo(moviecode):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
    key = config('MOVIE_KEY')
    url = f"{base_url}?key={key}&movieCd={moviecode}"
    res = requests.get(url).json()
    return res





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
```



### 03.py

> 02.py 에서 만든 csv 파일을 불러와서 감독정보를 가져오자

##### 1. readCsv

- 감독명과 영화명을 둘다 받아 튜플 형태로 반환받는다.

  ```python
  def readCsv(filename):
      with open(filename, 'r', newline='', encoding='utf-8') as f:
          result = []
          reader = csv.DictReader(f)
          for row in reader:
              directors = dict(row)['directors']
              movieNm = dict(row)['movieNm']
              result.append((directors, movieNm))
      return result
  ```

##### 2. getPeopleInfo

- 위의 함수에서 읽어온 튜플 값을 넣어줘서 두가지 검색조건을 넣어준다.

- 동명이인을 피하기 위해 필모와 이름을 동시에 검색한다.

  ```python
  def getPeopleInfo(peopleInfo):
      base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json"
      key = config('MOVIE_KEY')
      url = f"{base_url}?key={key}&peopleNm={peopleInfo[0]}&filmoNames={peopleInfo[1]}"
      res = requests.get(url).json()
      return res
  ```

##### 3. 코드 수행

```python
import requests
import csv
from decouple import config


def getDirectorInfo(info_dict):
    """
    dict를 넣어주면 해당 정보를 선별해서 합쳐준다
    정보가 없는경우(감독명이 없는 영화가 있음) 정보없음으로 처리
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
```

