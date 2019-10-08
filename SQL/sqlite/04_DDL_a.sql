DROP TABLE news;

CREATE TABLE articles(
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO articles
VALUES ('제목1', '내용1');


-- 테이블 이름 변경
ALTER TABLE articles RENAME TO news;
.tables
-- 테이블에 column 추가
-- NOT NULL column 을 추가하기 위해서는 
-- default 값을 넣어주어야 한다.
-- 없으면 오류 뜬다~ 
-- ALTER TABLE news ADD COLUMN created_at DATETIME NOT NULL
-- DEFAULT 값을 넣어주면 에러없이 진행된다.
ALTER TABLE news ADD COLUMN created_at DATETIME NOT NULL DEFAULT 1;

SELECT * FROM news;
