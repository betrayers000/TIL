# week 3

## day 3

### bootstrap

- `script` 태그를 가장 밑에 두는 이유는 모두 읽고 한번에 적용시키기 위함.

### 1. 사용방법

- bootstrap 홈페이지를 이용하자!
- 공식문서를 잘 활용하자

#### 1. 1 spacing : 공간

1. `m-0` : `margin: 0` 의 뜻 최대 5까지(`m-5`) 까지 줄수 있다.
2. `mr-0` : right, 오른쪽 margin을 준다.
3. `mx-0` : x좌표 좌우 margin을 준다.
4. `my-0` : y좌표 위아래 margin을 준다.
5. `py-0` : y좌표 위아래 padding을 준다.
6. 값은 rem단위이며 최대 5까지 줄수있고, 3이 16px로 브라우저 기본값
7. `my-n0` : n을 붙인경우는 음수

#### 1. 2 color : 색

1. primary, secondary, success, warning, danger 등 지정된 색이있다.
2. `text-success` 처럼 앞에 적용할 모양을 지정하고, 색을 적는다

#### 1.3 border

1. `border-color` 로 색을 변경
2. `rounded-모양` 으로 모양을 변경
   - pill : 알약 모양
   - circle : 원모양
   - 등등

#### 1.4 display

- `d-block` 처럼 사용가능
- `d-sm-none` : 해당 오브젝트가 sm사이즈 이상이면 none이 적용된다. 

#### 1. 5 위치

- 해당 요소를 정렬시킨다.
- `text-center` 등으로 사용가능 text요소를 중앙으로 정렬시킨다.



### Grid System

- 화면을 칸으로 구분하는 시스템