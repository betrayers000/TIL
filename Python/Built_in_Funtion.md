# python

## 사전학습 - 내장함수

1. `abs()` : 절대값 반환

2. `divmod(9, 5)` : 몫과 나머지를 튜플로 반환

3. `pow(3, 2)` : 3의 2제곱

4. `all()` : 모든 항목이 True라면 True 하나라도 False 라면 False를 반환 ; 공백문자열, 0 , False를 False로 인지

5. `any()` : 모든 항목이 False라면 False 하나라도 True 라면 True를 반환 ; 위와 반대

6. `enumerate()` : List, Tuple, 문자열과 같은 시퀀스형 항목을 입력받아 인덱스를 포함하는 튜플 객체를 항목으로 구성하는 enumerate 객체를 반환

7. `filter()` : 조건에 해당하는 항목(TRUE)을 걸러내는 함수

   ```python
   # 2의 배수의 경우 True 반환
   def iseven(num):
       return num % 2 ==0
   
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   
   ret_val = filter(iseven, numbers)
   # ret_val = filter(lambda n: n % 2 == 0, numbers) 람다식
   print("{}".format(list(ret_val)))
   # 결과
   # [2, 4, 6, 8, 10]
   ```

8. `list(), tuple(), set(), dict()` : 각각 자료형으로 변환

9. `map(func, val)` : 두번째 인자로 반복 가능한 자료형을 전달 받아 첫번째 인자로 전달 받은 함수를 적용한 결과를 map 객체로 반환한다.  일반적으로 람다식을 많이 사용한다. map 객체를 List 객체로 변환시킨다.

   ```python
   data_list = list("abcdef")
   
   result = list(map(lambda x: x.upper(), data_list))
   # upper() 대문자로 변환
   # labda x: x.upeer()를 적용한 data_list 를 map객체로 반환한다.
   # 입력받은 x를 대문자로 반환
   ```

10. `zip()` : 둘 이상의 반복 가능한 자료형을 인자로 전달받아, 동일 위치의 항목을 묶어 튜플을 항목으로 구성하는 zip객체를 생성하는 함수 ; 전달받은 자료형은 동일 자료형이야 하고, 항목의 갯수가 똑같아야 한다.

    ```python
    data_list1 = [1, 2, 3]
    data_list2 = [4, 5, 6]
    list(zip(data_list1, data_list2))
    dict(zip(data_list1, data_list2))
    # 결과
    # [(1, 4), (2, 5), (3, 6)]
    # {1:4, 2:5, 3:6} dict로 반환시 앞의 값이 key, 뒤의 값이 value가 되어 반환
    ```

11. `chr()` : 정수 형태의 유니코드 값을 인자로 전달 받아 해당코드의 문자로 반환

12. `ord()` : 문자를 인자로 받아 유니코드 값(10진 정수)을 반환

13. `hex()` : 10진 정수값을 인자로 받아 16진수로 반환

14. `dir()` : 현재 지역 스코프에 대한 정보를 리스트 객체로 반환

15. `globals()` : 현재 전역 심볼 테이블을 반환한다. ; 전역변수, 함수, 클래스의 정보포함

16. `locals()` : 현재 지역 심볼 테이블을 반환한다. ; 매개변수를 포함한 지역변수와 중첩함수의 정보 포함

17. `id()` : 객체의 고유 주소 값을 반환 ; 보통 `hex()`함수를 적용하여 16진수로 나타낸다. 

18. `isinstance(val , val2)` : val 객체가 val2 클래스의 인스턴스인지 확인하여 True , False로 반환

19. `issubclass(val, val2)` : val 클래스가 val2 클래스의 서브클래스(상속관계)인지 확인하여 True, False로 반환

20. `eval()` : 실행가능한 표현식을 인자로 받아 실행하여 반환한다.

    ```python
    expr = "2+5*3"
    print(eval(expr))
    # 결과
    # 17
    ```

21. 