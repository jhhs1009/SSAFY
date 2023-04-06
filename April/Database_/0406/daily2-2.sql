CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);


-- 1. 추가 하기
INSERT INTO zoo
VALUES
  ('gorilla', 'omnivore', 215, 180, 5),
  ('rabbit', 'herbivore',3, 150, null),
  ('tiger', 'carnivore', 220, 115, 3),
  ('elephant', 'herbivore', 3800, 280, 10),
  ('dog', 'omnivore', 8, 20, 1),
  ('eagle', 'carnivore', 8, 75, null),
  ('dolphin', 'carnivore', 210, null, 3),
  ('alligator', 'carnivore', 250, 50, null),
  ('panda', 'herbivore', 80, 90, 2),
  ('pig', 'omnivore', 70, 45, 5);

-- 2.모든 동물의 이름과 키를 조회
SELECT DISTINCT name, height FROM zoo;

-- 3. 토끼의 키를 15로 수정, 데이터 조회
UPDATE zoo
SET name='rabbit',
  height='15'
WHERE rowid = 2;

-- 4. 토끼 값 확인
SELECT DISTINCT name, eat, weight, height, age FROM zoo WHERE name='rabbit';

-- 5. 잡식 동물 데이터만 삭제하고 전체 데이터 조회
DELETE FROM zoo WHERE eat LIKE '%omnivore%';
SELECT * FROM zoo;

