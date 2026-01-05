select * from moz_places
where url like 'http://%'

UPDATE moz_places
SET url = REPLACE(url, 'http://', 'https://')
WHERE url LIKE 'http://%';

--  should return 0:
select count(*) from moz_places
where url like 'http://%'

