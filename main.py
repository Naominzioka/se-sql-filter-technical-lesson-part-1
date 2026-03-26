import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# employees = pd.read_sql("""
# SELECT *
#   FROM employees;
# """, conn)

#print(employees)

# result = pd.read_sql("SELECT * FROM employees;", conn)

# employees_named_patterson = []
# for _, data in result.iterrows():
#     if data["lastName"] == "Patterson":
#         employees_named_patterson.append(data)
# print(pd.DataFrame(employees_named_patterson))


# specific_employee_name = pd.read_sql("""
# SELECT *
#   FROM employees
#  WHERE lastName = "Patterson";
# """, conn)
# print(specific_employee_name)
 
#select all employees whose first names contain 5 letters
# employees_with_1stName_5letters = pd.read_sql("""
# SELECT *, length(firstName) AS name_length
#   FROM employees
#  WHERE name_length = 5;
# """, conn)
# print(employees_with_1stName_5letters)

#select all employees whose first name starts with letter L
# employees_firstname_start_with_L = pd.read_sql("""
# SELECT *, substr(firstName, 1, 1) AS first_initial
#   FROM employees
#  WHERE first_initial = "L";
# """, conn)
# print(employees_firstname_start_with_L)


# price_roundedto_nearest_int_is_30dollars = pd.read_sql("""
# SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int
#   FROM orderDetails
#  WHERE rounded_price_int = 30;
# """, conn)
# print(price_roundedto_nearest_int_is_30dollars)

#select orders from jan of any year
# orders_from_january = pd.read_sql("""
# SELECT *, strftime("%m", orderDate) AS month
#   FROM orders
#  WHERE month = "01";
# """, conn)
# print(orders_from_january)

#calculate number of days an order took from when it was ordered to when it was shipped
orders_shipped_late = pd.read_sql("""
SELECT *, julianday(shippedDate) - julianday(requiredDate) AS days_late
  FROM orders
 WHERE days_late > 0;
""", conn)
print(orders_shipped_late)

conn.close()
