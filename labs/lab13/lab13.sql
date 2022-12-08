.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = "blue" and pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = "blue" and pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(time) = 1;  


CREATE TABLE matchmaker AS
  SELECT s1.pet, s1.song, s1.color, s2.color FROM students AS s1, students AS s2 WHERE s1.pet = s2.pet AND s1.song = s2.song AND s1.time < s2.time;


CREATE TABLE sevens AS
  SELECT students.seven FROM numbers, students WHERE numbers.time = students.time AND numbers."7" = "True" AND students.number = 7;


CREATE TABLE average_prices AS
  SELECT category AS category, AVG(MSRP) AS average_price FROM products GROUP BY category;

CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) FROM inventory GROUP BY item;

CREATE TABLE name_best AS
  SELECT name AS name, MIN(MSRP / rating) FROM products GROUP BY category; 

CREATE TABLE shopping_list AS
  SELECT lowest_prices.item, lowest_prices.store AS store FROM name_best, lowest_prices WHERE lowest_prices.item = name_best.name;

CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs) FROM shopping_list, stores WHERE shopping_list.store = stores.store;
