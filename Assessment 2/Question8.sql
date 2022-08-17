-- Create an SQL query that shows the TOP 3 authors who sold the most books in total​!
select * from (select author_name,sum(sold_copies) as total_copies from 
(select a.author_name,a.book_name,b.sold_copies from authors a
left join 
books b
on a.book_name = b.book_name) agg
group by author_name) tot
order by total_copies
desc limit 3