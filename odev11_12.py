ödev 11


soru 1 


(select first_name  from actor
)
union all
(
select first_name  from customer
)


soru 2 

(select first_name  from actor
)
intersect
(
select first_name  from customer
)


soru 3 

(select first_name  from actor
)
except
(
select first_name  from customer
)

soru 4


(
	SELECT first_name
	FROM actor
)
UNION ALL
(
	SELECT first_name
	FROM customer
)
ORDER BY first_name ASC

(
	SELECT first_name
	FROM actor
)
INTERSECT 
(
	SELECT first_name
	FROM customer
)
ORDER BY first_name ASC


(
	SELECT first_name
	FROM actor
)
EXCEPT 
(
	SELECT first_name
	FROM customer
)
ORDER BY first_name ASC





ödev 12


soru 1 

select count(length) from film

where length>
(
select avg(length) from film
	

)

soru 2 
select count(rental_rate) from film

where rental_rate =
(
select max(rental_rate) from film
	



)


soru 3  

 SELECT * FROM film
   WHERE rental_rate = (SELECT MIN(rental_rate) FROM film)
   AND
   replacement_cost = (SELECT MIN(replacement_cost) FROM film)


 SORU 4

 SELECT first_name, last_name, customer.customer_id, COUNT(*) 
FROM payment
JOIN customer ON payment.customer_id = customer.customer_id
GROUP BY customer.customer_id
ORDER BY COUNT(*) DESC
LIMIT 5;






