import sqlite3

# Adds customer to database
def addCustomer(f_name, l_name, email_address, phone_number):
    if getCustomer(phone_number):
        return 0
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    query = "INSERT INTO customers (first_name, last_name, email_address, phone_number) VALUES (?, ?, ?, ?)"
    cur.execute(query, (f_name, l_name, email_address, phone_number))
    connection.commit()
    connection.close()
    return

# Returns customer with given phone_number
def getCustomer(phone_number):
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    query = "SELECT * FROM customers WHERE phone_number = ?"
    cur.execute(query, (phone_number,))
    result = cur.fetchone()
    connection.commit()
    connection.close()
    if result:
        return result
    else:
        return 0

# Increments the customers number of visits by one
def incrementVisits(phone_number, amount_spent):
    if not getCustomer(phone_number):
        return 0
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    num_visits = getCustomer(phone_number)[5]
    num_visits += 1
    num_increments = getCustomer(phone_number)[6]
    num_increments += int(amount_spent / 5)
    print(num_increments)
    query = "UPDATE customers SET num_visits = ?, increments_five = ? WHERE phone_number = ?"
    cur.execute(query, (num_visits, num_increments, phone_number))
    connection.commit()
    connection.close()
    return num_increments

# Returns all values in customer table
def getAll():
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()
    query = "SELECT * FROM customers"
    cur.execute(query)
    result = cur.fetchall()
    connection.commit()
    connection.close()
    return result

if __name__ == "__main__":
    print(getAll())
