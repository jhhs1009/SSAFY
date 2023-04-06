CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

-- users 테이블의 전체 행 수 조회
SELECT COUNT(*)FROM users;

-- 전체 유저의 평균 balance
SELECT avg(balance) FROM users;

-- 현재 모든 유저의 지역 조회
SELECT DISTINCT country FROM users;

-- 각 지역별로 평균 정리, 전라북도
SELECT country, avg(balance) FROM users WHERE country="전라북도";

-- 지역별 평균 balance를 구하시오, 정렬까지
SELECT country, avg(balance) FROM users
GROUP BY country ORDER BY avg(balance) DESC;

-- 나이가 30살 이상인 사람들의 평균 나이를 구하시오
SELECT AVG(age) FROM users WHERE age>=30;

-- 각 지역별로 몇 명씩 살고 있음?
SELECT country FROM users GROUP BY country;

-- 몇 명씩 사는지 계산 위해서 
SELECT country, COUNT(*)FROM users GROUP BY country;

-- 각 성씨가 몇 명씩 있는지 조회
SELECT last_name, COUNT(*)FROM users
GROUP BY last_name;

-- 각 성씨가 몇 명씩 있는지 조회, AS 키워드를 사용해
-- 컬럼명을 임시로 변경하여 조회 가능
SELECT last_name, COUNT(*)AS number_of_name
FROM users GROUP BY last_name;

-- 인원이 가장 많은 성씨 순으로 조회
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name ORDER BY COUNT(*) DESC;

-- 각 지역별 평균 나이 조회하기
SELECT country, AVG(age) FROM users
GROUP BY country;