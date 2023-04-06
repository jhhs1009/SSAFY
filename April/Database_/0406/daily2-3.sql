CREATE TABLE hotels (
  room_num TEXT NOT NULL,
  check_in TEXT NOT NULL,
  check_out TEXT NOT NULL,
  grade TEXT NOT NULL
);

-- 2. price 칼럼 추가 
ALTER TABLE hotels ADD COLUMN price INT;


-- 3. 데이터 추가
INSERT INTO hotels
VALUES
  ('B203', '2021-12-31', '2022-01-03', 'suite', 900),
  ('1102', '2022-01-04', '2022-01-08', 'suite', 850),
  ('303', '2022-01-01', '2022-01-03', 'deluxe', 500),
  ('807', '2021-01-04', '2022-01-07', 'superior', 300),
  ('B205', '2022-01-04', '2022-01-07', 'deluxe', 550);


-- 4. 방번호가 807호인 데이터에서 체크인 날짜를 2022-01-04로 수정
UPDATE hotels
SET room_num='807',
  check_in='2022-01-04'
WHERE rowid = 4;

-- 5. 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보 조회
SELECT * FROM hotels WHERE room_num LIKE 'B%' OR grade='deluxe';
