DROP TABLE classmates;

CREATE TABLE classmates(
    -- id INTEGER PRIMARY KEY,
    name TEXT,
    age INT,
    address TEXT
);

-- CREATE
INSERT INTO classmates (name, address)
VALUES ('홍길동', '광주서석동');

INSERT INTO classmates(name, age, address)
VALUES ('홍길동', 20, '서울');

INSERT INTO classmates
VALUES ('홍길동', 30, '서울');

-- SELECT rowid FROM classmates;

-- 데이터확인
.headers on
.mode column
-- SELECT * FROM classmates;

DROP TABLE classmates;

-- .tables

-- id 를 생성하는 것보다 rowid 를 이용하는게 편하다 
CREATE TABLE classmates(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

-- id를 만들고 이런식으로 INSERT 해주면 자동으로 값을 넣어준다
INSERT INTO classmates(name, age, address)
VALUES ('김동하', 25, '구로');

INSERT INTO classmates(name, age, address)
VALUES ('김수정', 25, '구로');

-- .tables

-- SELECT * FROM classmates;

DROP TABLE classmates;

.tables

CREATE TABLE classmates(
    name TEXT NOT NULL,
    age INT NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates
VALUES 
('박나래', 22, '서울'),
('김수향', 22, '목포'), 
('이주인', 22, '전주'), 
('박슬기', 27, '부산');

SELECT * FROM classmates;

-- SELECT rowid, name FROM classmates;

-- LIMIT 는 몇개를 가져와 OFFSET을 붙이면 
-- OFFSET 이후부터 LIMIT 갯수만큼 가져옴
-- 2번 이후부터 1개의 값을 가져와
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

-- 특정값만 가져올때 
SELECT * FROM classmates WHERE address='서울';

-- 중복없이 가져올때 DISTINCT
SELECT DISTINCT age FROM classmates;

--  데이터 삭제
DELETE FROM classmates WHERE rowid=4;
INSERT INTO classmates
VALUES ('최수민' , 55, '김포');

-- 데이터 수정
UPDATE classmates SET name='홍길동', address='제주' WHERE rowid=4;

SELECT rowid, * FROM classmates;