DROP TABLE users;
.mode csv
.import users.csv users
.headers on

.tables

-- 검색조건 추가
-- SELECT last_name, age FROM users WHERE age>=30 and last_name='김';

-- COUNT
-- SELECT COUNT(*) FROM users WHERE age >= 30 and last_name='김';

-- AVG(), SUM(), MIN(), MAX()
-- SELECT AVG(age) FROM users WHERE age>=30;
-- SELECT MAX(balance), first_name FROM users;
-- SELECT AVG(balance) FROM users WHERE age>=30;

-- 와일드 카드 패턴 '_' 반드시 이자리에 한개의 문자가 존재해야한다
-- '%' 여러개의 문자가 존재할 수 있다
-- ex> 1___ : 1로 시작하는 4자리수(_ 가 3개있음)
-- ex> 1% : 1로 시작하는 값 (자리수 제한 없음)

-- CSV 로 불러온 경우 전부 TEXT 형태이다.
-- .schema users

-- LIKE 패턴이 일치하는 경우를 찾아준다.
-- SELECT * FROM users WHERE age LIKE '2_';
-- SELECT COUNT(*) FROM users WHERE age LIKE '2_';
-- SELECT COUNT(*) FROM users WHERE phone LIKE '02%';
-- SELECT first_name FROM users WHERE first_name LIKE '%준';
-- SELECT phone FROM users WHERE phone LIKE '%-5114-%';

-- ORDER 정렬해준다 ASC(오름차순)는 default 설정이라서 적지않아도 동작한다
-- SELECT * FROM users ORDER BY age DESC LIMIT 10;
-- SELECT * FROM users ORDER BY age, last_name LIMIT 10;
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;