-- Creating a second table

CREATE TABLE if not EXISTS second_table (
    id int, name varchar(256), score int 
);

INSERT INTO description(id, name, score) VALUE (1, 'John', 10);
INSERT INTO description(id, name, score) VALUE (2, 'Alex', 3);
INSERT INTO description(id, name, score) VALUE (3, 'Bob', 14);
INSERT INTO description(id, name, score) VALUE (4, 'George', 8);
