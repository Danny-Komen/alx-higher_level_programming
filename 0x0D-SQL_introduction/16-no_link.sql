-- List all records of the table with the name and score fields only
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
