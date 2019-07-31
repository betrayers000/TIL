# week3

# day2

### 1. css

- 오류가 없는 언어
- HTML은 골격을 만들고 CSS는 스타일을 정의 한다.

#### 1.1 사용법

1. 기본 사용법

```css
h1{color:blue; font-size:15px;}
셀렉터{선언; 선언;}
```

2. 인라인

   - html 태그 내부에 style 속성으로 입력

     ```html
     <h1 style="color:red;">CSS intro </h1>
     ```

3. 임베딩 방식

   - `<style></style>` 태그를 이용해서 작성한다

     ```html
     <head>
         <style>
             h2 {
                 color:blueviolet;
             }
         </style>
     </head>
     ```

4. 링크파일

   - 외부에 css파일을 따로 만들어서 link 태그를 이용해서 적용시킨다.

   ```html
   <!--html-->
   	<link rel="stylesheet" href="00_intro.css">
   ```

   ```css
   /*00_intro.css*/
   p {
       color:red;
   }
   /* hello 라는 id를 가진 태그에 적용한다. */
   #hello {
       font-size: 50px
   }
   ```



#### 1.2 단위

1. px
   
- 모니터 픽셀 단위
  
2. 퍼센트 단위

   - 부모(div)에 상속이 되며, 자식의(h1)의 50%라고 하면 부모(div)의 50% 만큼이다.

     ```css
     div {
         width: 50%;
     }
     
     h1 {
         width: 50%;
     }
     ```

3. em

   - 배수단위를 표현 10em이면 10배
   - em도 상속이 된다.

4. rem

   - 기준이 확실하게 있다.
   - 부모의 영향을 받지 않는다.

5. viewport

   - 디바이스의 크기를 기준으로 조절한다.

#### 1.3 BOX Model

1. 박스모델 여백
   - margin : 외부 여백
   - padding : 내부 여백, 채워진다.

#### 1.4 디스플레이 속성

- 배치를 어떻게 할까 하는 속성
- block : 항상 새로운 라인에서 시작. 화면 크기 전체의 가로폭을 차지
- inline : margin을 줄 수 없다. 새로운 라인에서 시작하지 않고 문장 중간에 들어갈 수있다. 
- display 속성을 조절해서 block 이나 inline 으로 바꿔줄수 있다.
- inline-block : inline과 다르게 margin을 줄수있다.
- none : 데이터가 사라지고, 공간도 사라진다.
- visibility : hidden : 데이터가 숨겨진다. 공간은 사라지지않는다.

#### 1.5 위치속성

- static : 기본값
- relative : 기본값 위치에 상대적인 위치
- absolute : 절대좌표
- fixed : 스크롤을 내려도 고정되어있다.

#### 1.6 셀렉터

- 태그셀렉터 

  ```css
  h1 {
      color: red;
  }
  /*그룹*/
  h1, h2 {
      color: red;
  }
  ```

- 클래스 셀렉터

  - 점을 이용해서 접근해야 한다.

  ```css
  .class-selector {
      color:red;
  }
  ```

- 아이디 셀렉터

  - #을 이용해서 접근해야한다.

  ```css
  #id-selector {
      color:red;
  }
  ```

- 우선순위

  - 아이디 > 클래스 > 태그 순이다. 
  - `!important` 를 붙이게 되면 해당 속성이 최우선적으로 적용이된다.

  ```css
  h1 {
      color: red !important;
      background-color: black;
  }
  /* 
  color는 최우선으로 적용되고 
  back-color는 최우선으로 적용되지 않는다.
  */
  ```

- 자식 셀렉터

  - 부모 > 자식 형식으로 사용할수 있다.

  ```css
  ul > li {
      color: burlywood;
  }
  ```

- 형제 셀렉터

  - +를 사용하여 다음 형제 
  - ~을 사용하여 모든 형제

  ```css
  /*p태그의 다음 li 형제*/
  p + li {
      
  }
  /*p태그의 모든 li 형제*/
  p ~ li {
      
  }
  ```

  