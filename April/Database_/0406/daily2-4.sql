-- 1. 테이블 생성
CREATE TABLE users (
  id INT PRIMARY KEY,
  first_name TEXT,
  last_name TEXT NOT NULL,
  age INT NOT NULL,
  country TEXT NOT NULL,
  phone TEXT,
  balance INT NOT NULL
);


-- 2. 데이터 추가
INSERT INTO users
VALUES
  ('1', '미현', '김', 19, '경기도', '011-211-8482', 300),
  ('2', '', '최', 33, '제주특별자치도', null, 300),
  ('3', '미숙', '이', 21, '서울특별시', '010-2122-4958', 480),
  ('4', '남석', '박', 18, '경기도', '011-484-8667', 260),
  ('5', '철수', '박', 22, '경상남도', '016-295-8989', 500),
  ('6', '', '박', 45, '전라북도', null, 320),
  ('7', '민준', '이', 35, '전라남도', '019-965-8833', 350),
  ('8', '', '남', 24, '충청남도', '010-5882-5969', 210),
  ('9', '신', '유', 29, '경상북도', '010-4949-2848', 290),
  ('10', '', '김', 18, '대전광역시', null, 300);


-- 3. 나이가 25세 미만인 사람들의 id, age, balance 정소
-- age : 내림차순 balance 오름 차순으로 확인
SELECT id, age, balance FROM users 
WHERE age<25 ORDER BY age desc, balance ASC;

-- 4. first_name이 존재하는 사람들 중 balance가 400보다 큰 사람의
-- first_name과 balance 확인
SELECT first_name, balance FROM users
WHERE first_name!='' AND balance>400;

-- 5. phone의 값이 Null인 사람들의 phone 정보를
-- 알 수 없음으로 수정하고
-- 데이터 조회
UPDATE users
SET phone = '알 수 없음'
WHERE phone IS NULL;

SELECT * FROM users;
