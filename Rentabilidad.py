import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#Establecemos conexion con la base de datos
conn = sqlite3.connect("../Northwind.db")

#Peticion para devolver los productos mas rentables
query = '''
    SELECT ProductName, sum(Price * Quantity) AS Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
	GROUP BY od.ProductID
	ORDER BY Revenue DESC
	LIMIT 10
'''


# #Top 10 de Productos mas rentables
#La propiedad de pandas read_sql_query, nos permite crear automaticamente el cursor, abre y cierra las consulatas que hagamos
top_products = pd.read_sql_query(query, conn)

top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10, 5), legend=False)

plt.title("Los 10 Productos mas Rentables")
plt.xlabel("Product Name")
plt.ylabel("Revenue")
plt.xticks(rotation=90) #Con esto me rota los nombres de productos 90grados, quedan verticales
plt.show()


#Top 10 de los Empleados mas efectivos
queryEmployees = '''
    SELECT FirstName || " " || LastName AS FullName, sum(Price * Quantity) AS Revenue 
    FROM Employees e
    JOIN Orders o ON e.EmployeeID = o.EmployeeID
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    GROUP BY FullName
    ORDER BY Revenue DESC
    LIMIT 10
'''

# queryEmployees = '''
#     SELECT FirstName || " " || LastName AS FullName, count(*) AS Total_
#     FROM Orders o
#     JOIN Employees e
#     ON e.EmployeeID = o.EmployeeID
#     GROUP BY o.EmployeeID
#     ORDER BY Total_ DESC
# '''

top_employees = pd.read_sql_query(queryEmployees, conn)

top_employees.plot(x="FullName", y="Revenue", kind="bar", figsize=(10, 5), legend=False)

plt.title("Los 10 Empleados mas Productivos")
plt.xlabel("Employees")
plt.ylabel("Revenue")
plt.xticks(rotation=45) #Con esto me rota los nombres de productos 90grados, quedan verticales
plt.show()
