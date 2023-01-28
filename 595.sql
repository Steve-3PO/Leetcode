# Big Countries

# Write your MySQL query statement below

# we want the name, population and area from the world dataset given the 2 conditions for large countries
select w.name, w.population, w.area from World as w where w.area >= 3000000 or w.population >= 25000000;