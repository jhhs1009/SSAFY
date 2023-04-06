# 트랜잭션

데이터베이스의 상태를 변화시키기 위해 수행하는 작업 단위

ACID
원자성, 일관성, 독립성, 지속성

1. 원자성 : 트랜잭션이 DB에 모두 반영되거나 혹은 모두 반영되지 않거나 둘 중 하나여야 한다.

SELECT * ...

UPDATE ...

DELETE ...

4. 지속성 : 트랜잭션이 성공적으로 완료되었다면, 결과는 영구적으로 반영되어야 한다.

SQLite는 기본적으로 AUTO


```sql
BEGIN;
  DELETE FROM ...
  UPDATE FROM ...
  -- 이 시전에서 작업 내역들을 모두 되돌리고 싶다.
  ROLLBACK;
  BEGIN;
    INSERT INTO ...
    DELETE FROM ...
    -- 이 시점에서 작업 내역들을 모두 DB에 반영하고 싶다.
  COMMIT;
```