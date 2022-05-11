import sqlite3

def query(query_text):
    conn = sqlite3.connect('Northwind_large.sqlite')
    cur = conn.cursor()
    cur.execute(query_text)

    column_names = []
    for column in cur.description:
        column_names.append(column[0])

    rows = cur.fetchall()
    dicts = []

    for row in rows:
        d = dict(zip(column_names, row))
        dicts.append(d)

    conn.close()
    return dicts


def get_all_facts():
    return query("""SELECT * FROM Supplier""")

def get_supplier_products(supplier_id):
    return query("""
                SELECT * FROM Product
                WHERE SupplierId = %d""" %supplier_id)  


def get_supplier_name(supplier_id):
    return query("""
                SELECT CompanyName FROM Supplier
                WHERE Id = %d""" %supplier_id)   

def get_cat_info():
    return query("""SELECT  COUNT(Category.Id) AS CategoryCount,   * FROM Category
                        INNER JOIN Product
                    ON Product.CategoryId = Category.Id
                        GROUP BY CategoryName  """)   

def get_category_products(category_id):
    return query("""
                SELECT * FROM Product
                INNER JOIN Category
                ON Category.Id= Product.CategoryId
                INNER JOIN Supplier
                ON Supplier.Id= Product.SupplierId
                WHERE CategoryId = %d""" %category_id)  