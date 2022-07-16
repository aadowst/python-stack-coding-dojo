-- SELECT Date,TotalAllowance FROM Calculation WHERE EmployeeId=1 AND Date >= '2011/02/25' AND Date < '2011/02/28'        

-- Queries
-- 1. What query would you run to get the total revenue for March of 2012?
select sum(amount) from billing
where charged_datetime >= '2012/3/1' and charged_datetime < '2012/4/1';
-- 2. What query would you run to get total revenue collected from the client with an id of 2?
select sum(amount)
from billing join clients on billing.client_id = clients.client_id
where clients.client_id = 2;
-- 3. What query would you run to get all the sites that client with an id of 10 owns?
select sites.domain_name
from clients join sites on clients.client_id = sites.client_id
where clients.client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client with an id of 20?
-- Explanation:  takes count of the site ids for client 1. this is divided by the number of months between the creation dates for the first and last website. (formate of timestampdiff is (interval, start_date, end_date)

select count(site_id)/(select timestampdiff(month,
(select created_datetime from sites
where sites.client_id = 1
order by created_datetime asc
limit 1), 
(select created_datetime from sites
where sites.client_id = 1
order by created_datetime desc
limit 1)))
 as sites_per_month from sites
where sites.client_id = 1;

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
select count(leads.leads_id), sites.domain_name
from leads join sites on leads.site_id = sites.site_id
group by sites.domain_name;

-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
select clients.first_name, clients.last_name, count(leads.leads_id)
from leads join sites on leads.site_id = sites.site_id
join clients on sites.client_id = clients.client_id
where leads.registered_datetime >= '2011/01/01' and leads.registered_datetime < '2012/01/01'
group by clients.client_id;


-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
select clients.first_name, clients.last_name, count(leads.leads_id)/6 as leads_per_month
from leads join sites on leads.site_id = sites.site_id
join clients on sites.client_id = clients.client_id
where leads.registered_datetime >= '2011/01/01' and leads.registered_datetime < '2011/07/01'
group by clients.client_id;

-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
select clients.client_id, clients.first_name, clients.last_name, count(leads.leads_id)
from leads join sites on leads.site_id = sites.site_id
join clients on sites.client_id = clients.client_id
where leads.registered_datetime >= '2011/01/01' and leads.registered_datetime < '2012/01/01'
group by clients.client_id
order by clients.client_id;

select sites.domain_name, clients.first_name, clients.last_name, count(leads.leads_id)
from leads join sites on leads.site_id = sites.site_id
join clients on sites.client_id = clients.client_id
group by sites.domain_name
order by clients.client_id, sites.domain_name;

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.  First try this with integer month, second with month name.  A SELECT subquery will be needed for the second challenge.  Look at this for a hint.
select clients.client_id, clients.first_name, clients.last_name, (billing.amount), month(billing.charged_datetime), year(billing.charged_datetime)
from billing
join clients on billing.client_id = clients.client_id
group by month(billing.charged_datetime)
order by clients.client_id;

select clients.client_id, clients.first_name, clients.last_name, (billing.amount), monthname(billing.charged_datetime), year(billing.charged_datetime)
from billing
join clients on billing.client_id = clients.client_id
group by month(billing.charged_datetime)
order by clients.client_id;

-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that all of the sites for each client are displayed in a single field. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
select clients.first_name, clients.last_name, group_concat(' ', sites.domain_name)
from clients
join sites on clients.client_id = sites.client_id
group by clients.client_id
