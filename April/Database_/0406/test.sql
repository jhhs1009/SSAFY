-- SQLite
CREATE TABLE animals (
  animal_name TEXT NOT NULL,
  height INT NOT NULL,
  weight INT NOT NULL,
  age INT,
);

-- 1. meal 칼럼을 추가 데이터 타입은 TEXT NULL값을 허용하시오
ALTER TABLE animals ADD COLUMN meal TEXT NULL;

-- 2. animal_name의 명칭을 name으로 수정
ALTER TABLE animals RENAME COLUMN animal_name TO name;

-- 3. 테이블의 이름을 animals에서 zoo로 변경
ALTER TABLE animals RENAME TO zoo;

-- 4. zoo 테이블 삭제
DROP TABLE zoo;