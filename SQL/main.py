import sqlite3

def setup_database():
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()

    # Create tables
    c.execute('''
    CREATE TABLE salespeople (
        snum INTEGER PRIMARY KEY,
        sname TEXT,
        city TEXT,
        comm REAL
    )
    ''')

    c.execute('''
    CREATE TABLE customers (
        cnum INTEGER PRIMARY KEY,
        cname TEXT,
        city TEXT,
        rating INTEGER,
        snum INTEGER,
        FOREIGN KEY (snum) REFERENCES salespeople(snum)
    )
    ''')

    c.execute('''
    CREATE TABLE orders (
        onum INTEGER PRIMARY KEY,
        amt REAL,
        odate TEXT,
        cnum INTEGER,
        snum INTEGER,
        FOREIGN KEY (cnum) REFERENCES customers(cnum),
        FOREIGN KEY (snum) REFERENCES salespeople(snum)
    )
    ''')

    # Insert sample data with Tamil names
    salespeople = [
        (1001, 'Anbu', 'Chennai', 0.15),
        (1002, 'Bala', 'Madurai', 0.13),
        (1003, 'Chitra', 'Coimbatore', 0.14),
        (1004, 'Dinesh', 'Salem', 0.11),
        (1005, 'Elango', 'Trichy', 0.12)
    ]

    customers = [
        (2001, 'Ganesh', 'Chennai', 300, 1001),
        (2002, 'Hari', 'Madurai', 200, 1002),
        (2003, 'Indira', 'Coimbatore', 400, 1003),
        (2004, 'Jay', 'Salem', 100, 1004),
        (2005, 'Kavi', 'Trichy', 500, 1005),
        (2006, 'Lakshmi', 'Chennai', 300, 1001),
        (2007, 'Muthu', 'Madurai', 150, 1002)
    ]

    orders = [
        (3001, 1500, '1994-10-03', 2001, 1001),
        (3002, 2000, '1994-10-04', 2002, 1002),
        (3003, 2500, '1994-10-05', 2003, 1003),
        (3004, 500, '1994-10-03', 2004, 1004),
        (3005, 3000, '1994-10-06', 2005, 1005),
        (3006, 1200, '1994-10-03', 2006, 1001),
        (3007, 2200, '1994-10-04', 2007, 1002)
    ]

    c.executemany('INSERT INTO salespeople VALUES (?, ?, ?, ?)', salespeople)
    c.executemany('INSERT INTO customers VALUES (?, ?, ?, ?, ?)', customers)
    c.executemany('INSERT INTO orders VALUES (?, ?, ?, ?, ?)', orders)

    conn.commit()
    conn.close()

def run_queries():
    conn = sqlite3.connect('sales.db')
    c = conn.cursor()

    # 1. Display snum, sname, city and comm of all salespeople
    print("1. Display snum, sname, city and comm of all salespeople")
    c.execute('SELECT snum, sname, city, comm FROM salespeople')
    result = c.fetchall()
    for row in result:
        print(row)

    # 2. Display all snum without duplicates from all orders
    print("\n2. Display all snum without duplicates from all orders")
    c.execute('SELECT DISTINCT snum FROM orders')
    result = c.fetchall()
    for row in result:
        print(row)

    # 3. Display names and commissions of all salespeople in Chennai
    print("\n3. Display names and commissions of all salespeople in Chennai")
    c.execute('SELECT sname, comm FROM salespeople WHERE city = "Chennai"')
    result = c.fetchall()
    for row in result:
        print(row)

    # 4. All customers with rating of 100
    print("\n4. All customers with rating of 100")
    c.execute('SELECT * FROM customers WHERE rating = 100')
    result = c.fetchall()
    for row in result:
        print(row)

    # 5. Produce orderno, amount and date form all rows in the order table
    print("\n5. Produce orderno, amount and date form all rows in the order table")
    c.execute('SELECT onum, amt, odate FROM orders')
    result = c.fetchall()
    for row in result:
        print(row)

    # 6. All customers in Madurai, who have rating more than 200
    print("\n6. All customers in Madurai, who have rating more than 200")
    c.execute('SELECT * FROM customers WHERE city = "Madurai" AND rating > 200')
    result = c.fetchall()
    for row in result:
        print(row)

    # 7. All customers who were either located in Madurai or had a rating above 200
    print("\n7. All customers who were either located in Madurai or had a rating above 200")
    c.execute('SELECT * FROM customers WHERE city = "Madurai" OR rating > 200')
    result = c.fetchall()
    for row in result:
        print(row)

    # 8. All orders for more than $1000
    print("\n8. All orders for more than $1000")
    c.execute('SELECT * FROM orders WHERE amt > 1000')
    result = c.fetchall()
    for row in result:
        print(row)

    # 9. Names and cities of all salespeople in Chennai with commission above 0.10
    print("\n9. Names and cities of all salespeople in Chennai with commission above 0.10")
    c.execute('SELECT sname, city FROM salespeople WHERE city = "Chennai" AND comm > 0.10')
    result = c.fetchall()
    for row in result:
        print(row)

    # 10. All customers excluding those with rating <= 100 unless they are located in Chennai
    print("\n10. All customers excluding those with rating <= 100 unless they are located in Chennai")
    c.execute('SELECT * FROM customers WHERE rating > 100 OR city = "Chennai"')
    result = c.fetchall()
    for row in result:
        print(row)

    # 11. All salespeople either in Coimbatore or in Chennai
    print("\n11. All salespeople either in Coimbatore or in Chennai")
    c.execute('SELECT * FROM salespeople WHERE city = "Coimbatore" OR city = "Chennai"')
    result = c.fetchall()
    for row in result:
        print(row)

    # 12. All salespeople with commission between 0.10 and 0.12 (Boundary values should be excluded)
    print("\n12. All salespeople with commission between 0.10 and 0.12 (Boundary values should be excluded)")
    c.execute('SELECT * FROM salespeople WHERE comm > 0.10 AND comm < 0.12')
    result = c.fetchall()
    for row in result:
        print(row)

    # 13. All customers with NULL values in city column
    print("\n13. All customers with NULL values in city column")
    c.execute('SELECT * FROM customers WHERE city IS NULL')
    result = c.fetchall()
    for row in result:
        print(row)

    # 14. All orders taken on Oct 3Rd and Oct 4th 1994
    print("\n14. All orders taken on Oct 3Rd and Oct 4th 1994")
    c.execute('SELECT * FROM orders WHERE odate IN ("1994-10-03", "1994-10-04")')
    result = c.fetchall()
    for row in result:
        print(row)

    # 15. All customers serviced by Anbu or Motika
    print("\n15. All customers serviced by Anbu or Motika")
    c.execute('''
    SELECT *
    FROM customers
    WHERE snum = (SELECT snum FROM salespeople WHERE sname = "Anbu")
       OR snum = (SELECT snum FROM salespeople WHERE sname = "Motika")
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 16. All customers whose names begin with a letter from A to B
    print("\n16. All customers whose names begin with a letter from A to B")
    c.execute('SELECT * FROM customers WHERE cname BETWEEN "A" AND "Bz"')
    result = c.fetchall()
    for row in result:
        print(row)

    # 17. All orders except those with 0 or NULL value in amt field
    print("\n17. All orders except those with 0 or NULL value in amt field")
    c.execute('SELECT * FROM orders WHERE amt <> 0 AND amt IS NOT NULL')
    result = c.fetchall()
    for row in result:
        print(row)

    # 18. Count the number of salespeople currently listing orders in the order table
    print("\n18. Count the number of salespeople currently listing orders in the order table")
    c.execute('SELECT COUNT(DISTINCT snum) FROM orders')
    result = c.fetchone()
    print(result)

    # 19. Largest order taken by each salesperson, datewise
    print("\n19. Largest order taken by each salesperson, datewise")
    c.execute('''
    SELECT snum, MAX(amt), odate
    FROM orders
    GROUP BY snum, odate
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 20. Largest order taken by each salesperson with order value more than $3000
    print("\n20. Largest order taken by each salesperson with order value more than $3000")
    c.execute('''
    SELECT snum, MAX(amt)
    FROM orders
    WHERE amt > 3000
    GROUP BY snum
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 21. Which day had the highest total amount ordered
    print("\n21. Which day had the highest total amount ordered")
    c.execute('''
    SELECT odate, SUM(amt) AS total_amount
    FROM orders
    GROUP BY odate
    ORDER BY total_amount DESC
    LIMIT 1
    ''')
    result = c.fetchone()
    print(result)

    # 22. Count all orders for Oct 3rd
    print("\n22. Count all orders for Oct 3rd")
    c.execute('SELECT COUNT(*) FROM orders WHERE odate = "1994-10-03"')
    result = c.fetchone()
    print(result)

    # 23. Count the number of different non NULL city values in customers table
    print("\n23. Count the number of different non NULL city values in customers table")
    c.execute('SELECT COUNT(DISTINCT city) FROM customers WHERE city IS NOT NULL')
    result = c.fetchone()
    print(result)

    # 24. Select each customer’s smallest order
    print("\n24. Select each customer’s smallest order")
    c.execute('''
    SELECT cnum, MIN(amt)
    FROM orders
    GROUP BY cnum
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 25. First customer in alphabetical order whose name begins with G
    print("\n25. First customer in alphabetical order whose name begins with G")
    c.execute('SELECT * FROM customers WHERE cname LIKE "G%" ORDER BY cname LIMIT 1')
    result = c.fetchone()
    print(result)

    # 26. Get the output like "For dd/mm/yy there are_orders"
    print("\n26. Get the output like \"For dd/mm/yy there are_orders\"")
    c.execute('SELECT odate, COUNT(*) FROM orders GROUP BY odate')
    result = c.fetchall()
    for row in result:
        print(f"For {row[0]} there are {row[1]} orders")

    # 27. Assume that each salesperson has a 12% commission. Produce order no., salesperson no., and amount of salesperson’s commission for that order
    print("\n27. Assume that each salesperson has a 12% commission. Produce order no., salesperson no., and amount of salesperson’s commission for that order")
    c.execute('SELECT onum, snum, amt * 0.12 AS commission FROM orders')
    result = c.fetchall()
    for row in result:
        print(row)

    # 28. Find highest rating in each city. Put the output in this form. For the city (city), the highest rating is : (rating)
    print("\n28. Find highest rating in each city. Put the output in this form. For the city (city), the highest rating is : (rating)")
    c.execute('SELECT city, MAX(rating) FROM customers GROUP BY city')
    result = c.fetchall()
    for row in result:
        print(f"For the city {row[0]}, the highest rating is : {row[1]}")

    # 29. Display the totals of orders for each day and place the results in descending order
    print("\n29. Display the totals of orders for each day and place the results in descending order")
    c.execute('SELECT odate, SUM(amt) FROM orders GROUP BY odate ORDER BY SUM(amt) DESC')
    result = c.fetchall()
    for row in result:
        print(row)

    # 30. All combinations of salespeople and customers who shared a city (i.e., same city)
    print("\n30. All combinations of salespeople and customers who shared a city (i.e., same city)")
    c.execute('''
    SELECT s.sname, c.cname, s.city
    FROM salespeople s
    JOIN customers c ON s.city = c.city
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 31. Name of all customers matched with the salespeople serving them
    print("\n31. Name of all customers matched with the salespeople serving them")
    c.execute('''
    SELECT c.cname, s.sname
    FROM customers c
    JOIN salespeople s ON c.snum = s.snum
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 32. List each order number followed by the name of the customer who made the order
    print("\n32. List each order number followed by the name of the customer who made the order")
    c.execute('''
    SELECT o.onum, c.cname
    FROM orders o
    JOIN customers c ON o.cnum = c.cnum
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 33. Names of salesperson and customer for each order after the order number
    print("\n33. Names of salesperson and customer for each order after the order number")
    c.execute('''
    SELECT o.onum, s.sname, c.cname
    FROM orders o
    JOIN salespeople s ON o.snum = s.snum
    JOIN customers c ON o.cnum = c.cnum
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 34. Produce all customer serviced by salespeople with a commission above 12%
    print("\n34. Produce all customer serviced by salespeople with a commission above 12%")
    c.execute('''
    SELECT c.*
    FROM customers c
    JOIN salespeople s ON c.snum = s.snum
    WHERE s.comm > 0.12
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 35. Calculate the amount of the salesperson’s commission on each order with a rating above 100
    print("\n35. Calculate the amount of the salesperson’s commission on each order with a rating above 100")
    c.execute('''
    SELECT o.onum, o.snum, o.amt * 0.12 AS commission
    FROM orders o
    JOIN customers c ON o.cnum = c.cnum
    WHERE c.rating > 100
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 36. Find all pairs of customers having the same rating
    print("\n36. Find all pairs of customers having the same rating")
    c.execute('''
    SELECT c1.cname, c2.cname, c1.rating
    FROM customers c1
    JOIN customers c2 ON c1.rating = c2.rating AND c1.cnum < c2.cnum
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 37. Policy is to assign three salesperson to each customers. Display all such combinations
    print("\n37. Policy is to assign three salesperson to each customers. Display all such combinations")
    c.execute('''
    SELECT c.cname, s1.sname AS salesperson1, s2.sname AS salesperson2, s3.sname AS salesperson3
    FROM customers c
    JOIN salespeople s1 ON c.snum = s1.snum
    JOIN salespeople s2 ON s2.snum != s1.snum
    JOIN salespeople s3 ON s3.snum != s1.snum AND s3.snum != s2.snum
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 38. Display all customers located in cities where salesman Anbu has customer
    print("\n38. Display all customers located in cities where salesman Anbu has customer")
    c.execute('''
    SELECT *
    FROM customers
    WHERE city IN (SELECT city FROM customers WHERE snum = (SELECT snum FROM salespeople WHERE sname = "Anbu"))
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 39. Find all pairs of customers served by single salesperson
    print("\n39. Find all pairs of customers served by single salesperson")
    c.execute('''
    SELECT c1.cname, c2.cname, c1.snum
    FROM customers c1
    JOIN customers c2 ON c1.snum = c2.snum AND c1.cnum < c2.cnum
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 40. Produce all pairs of salespeople which are living in the same city. Exclude combinations of salespeople with themselves as well as duplicates with the order reversed
    print("\n40. Produce all pairs of salespeople which are living in the same city. Exclude combinations of salespeople with themselves as well as duplicates with the order reversed")
    c.execute('''
    SELECT s1.sname, s2.sname, s1.city
    FROM salespeople s1
    JOIN salespeople s2 ON s1.city = s2.city AND s1.snum < s2.snum
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 41. Produce names and cities of all customers with the same rating as Chitra
    print("\n41. Produce names and cities of all customers with the same rating as Chitra")
    c.execute('''
    SELECT c.cname, c.city
    FROM customers c
    WHERE c.rating = (SELECT rating FROM customers WHERE cname = "Chitra")
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 42. Extract all the orders of Motika
    print("\n42. Extract all the orders of Motika")
    c.execute('''
    SELECT o.*
    FROM orders o
    JOIN salespeople s ON o.snum = s.snum
    WHERE s.sname = "Motika"
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 43. All orders credited to the same salesperson who services Chitra
    print("\n43. All orders credited to the same salesperson who services Chitra")
    c.execute('''
    SELECT o.*
    FROM orders o
    WHERE o.snum = (SELECT snum FROM customers WHERE cname = "Chitra")
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 44. All orders that are greater than the average for Oct 4
    print("\n44. All orders that are greater than the average for Oct 4")
    c.execute('''
    SELECT *
    FROM orders
    WHERE amt > (SELECT AVG(amt) FROM orders WHERE odate = "1994-10-04")
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 45. Find average commission of salespeople in Chennai
    print("\n45. Find average commission of salespeople in Chennai")
    c.execute('SELECT AVG(comm) FROM salespeople WHERE city = "Chennai"')
    result = c.fetchone()
    print(result)

    # 46. Find all orders attributed to salespeople servicing customers in Chennai
    print("\n46. Find all orders attributed to salespeople servicing customers in Chennai")
    c.execute('''
    SELECT o.*
    FROM orders o
    JOIN customers c ON o.cnum = c.cnum
    WHERE c.city = "Chennai"
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 47. Extract commissions of all salespeople servicing customers in Chennai
    print("\n47. Extract commissions of all salespeople servicing customers in Chennai")
    c.execute('''
    SELECT s.comm
    FROM salespeople s
    JOIN customers c ON s.snum = c.snum
    WHERE c.city = "Chennai"
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 48. Find all customers whose cnum is 1000 above the snum of Anbu
    print("\n48. Find all customers whose cnum is 1000 above the snum of Anbu")
    c.execute('''
    SELECT *
    FROM customers
    WHERE cnum = (SELECT snum FROM salespeople WHERE sname = "Anbu") + 1000
    ''')
    result = c.fetchall()
    for row in result:
        print(row)

    # 49. Count the customers with rating above Madurai’s average
    print("\n49. Count the customers with rating above Madurai’s average")
    c.execute('''
    SELECT COUNT(*)
    FROM customers
    WHERE rating > (SELECT AVG(rating) FROM customers WHERE city = "Madurai")
    ''')
    result = c.fetchone()
    print(result)

    conn.close()

# Set up the database and run the queries
setup_database()
run_queries()
