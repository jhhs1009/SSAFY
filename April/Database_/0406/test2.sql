-- 1. table을 생성
CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 2. 값 입력 
INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);


BEGIN;
-- 3. weight가 100보다 작으면 삭제
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
-- 4. eat가 omnivore면 삭제
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;


-- 남아있는 데이터 수인 2개만 출력한다.
SELECT COUNT(*)
FROM zoo;
