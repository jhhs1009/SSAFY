CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

-- 나이가 어린 순서로 조회하는 관리자 페이지를 구현하고자 함
-- 페이지 당 출력되는 데이터는 20개로 제한했을 때, 3번째 페이지를 조회하는 쿼리문을 작성
SELECT first_name, age FROM users
ORDER BY age LIMIT 40 OFFSET 20;
