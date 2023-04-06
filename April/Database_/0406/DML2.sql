CREATE TABLE classmate (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- 단일 행 삽입
INSERT INTO classmate (name, age, address)
VALUES ('홍길동', 23, '서울');

-- 단일 행 삽입, 아래와 같이도 가능
INSERT INTO classmate
VALUES ('홍길동', 23, '서울');

-- 여러 행 삽입
INSERT INTO classmate
VALUES
  ('김철수', 30, '경기'),
  ('이영미', 31, '강원'),
  ('박진성', 26, '전라'),
  ('최지수', 12, '충청'),
  ('정요한', 28, '경상');

-- 2번 데이터의 이름과 주소를 수정
UPDATE classmate
SET name='김철수한무두루미',
  address='제주도'
WHERE rowid = 2;

-- 