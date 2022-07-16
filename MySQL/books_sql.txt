insert into users (first_name, last_name)
values ('Jane',  'Amsden'),
('Emily', 'Dixon'),
('Theodore',  'Dostoevsky'), 
('William', 'Shapiro'),
('Lao', 'Xiu');

insert into books (title)
values ('C Sharp'), ('Java'), ('Python'), ('PHP'), ('Ruby');

UPDATE books
set title = 'C#'
where title = 'C Sharp';

UPDATE users
set first_name = 'Bill'
Where users.id = 4;

insert into favorites (user_id, book_id)
values (1,1), (1, 2);

insert into favorites (user_id, book_id)
values (2,1), (2, 2), (2, 3);

insert into favorites (user_id, book_id)
values (3,1), (3, 2), (3, 3), (3, 4);

insert into favorites (user_id, book_id)
values (4,1), (4, 2), (4, 3), (4, 4), (4, 5);

select * 
from users
join favorites
on users.id = favorites.user_id
where favorites.book_id = 3;

delete from favorites
where user_id = 2;
delete from users
where id = 2;

insert into favorites (user_id, book_id)
values (5,2);

select books.title 
from users
join favorites
on users.id = favorites.user_id
join books
on favorites.book_id = books.id
where users.id = 3;

select *
from users
join favorites
on users.id = favorites.user_id
where favorites.book_id = 5;
