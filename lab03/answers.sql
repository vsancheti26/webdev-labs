-- Exercise 1 (done for you):
SELECT * FROM users;



-- Exercise 2 (done for you):
SELECT id, first_name, last_name 
FROM users;



-- Exercise 3
select id, first_name, last_name 
from users 
order by last_name;



-- Exercise 4
select id, image_url, user_id
from posts
where user_id=26;



-- Exercise 5
select id, image_url, user_id
from posts
where user_id=26 or user_id=12;



-- Exercise 6
select count(id)
from posts;



-- Exercise 7
select user_id,count(id)
from comments
group by user_id
order by count(user_id) desc;



-- Exercise 8
select posts.id, posts.image_url,posts.user_id,users.username,users.first_name,users.last_name
from posts
inner join users on posts.user_id=users.id
where posts.user_id=26 or posts.user_id=12;



-- Exercise 9
select posts.id, posts.pub_date,following.following_id
from posts
inner join following on posts.user_id=following.user_id
where following.user_id=26;



-- Exercise 11
insert into bookmarks(user_id,post_id,timestamp)
values (26,219,current_timestamp);

insert into bookmarks(user_id,post_id,timestamp)
values (26,220,current_timestamp);

insert into bookmarks(user_id,post_id,timestamp)
values (26,221,current_timestamp);



-- Exercise 12
delete from bookmarks 
where post_id=219 and user_id=26;

delete from bookmarks 
where post_id=220 and user_id=26;

delete from bookmarks 
where post_id=221 and user_id=26;



-- Exercise 13
update users
set email='knick2022@gmail.com'
where id=26;

