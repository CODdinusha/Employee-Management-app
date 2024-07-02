import pymysql
import calendar
import os
1

# Assuming your password environment variable is named 'Pass'
db_password = 'dinushA@727'

con = pymysql.connect(host="localhost", user='root', passwd=db_password, database='xiia')

cur1 = con.cursor()

def menu():
    print("\t\t\t-----------------------------------------------------------------------")
    print("\t\t\t**********************************MENU*********************************")
    print("\t\t\t-----------------------------------------------------------------------")
    print()
    print("\t\t\t***********************1. REGISTER NEW EMPLOYEES***********************")
    print("\t\t\t********************2. UPDATE DETAILS OF EMPLOYEES*********************")
    print("\t\t\t******************3. DISPLAY DETAILS OF AN EMPLOYEE********************")
    print("\t\t\t*************4. REMOVE AN EMPLOYEE WHO HAVE LEFT OFFICE****************")
    print("\t\t\t******************5. DISPLAY ALL EMPLOYEE DETAILS**********************")
    print("\t\t\t********6. DISPLAY DETAILS OF EMPLOYEES WHO HAVE LEFT THE OFFICE*******")
    print("\t\t\t******************7. DISPLAY SORTED EMPLOYEE DETAILS*******************")
    print("\t\t\t**********8. DISPLAY AVERAGE SALARY THAT AN EMPLOYEE RECEIVES**********")
    print("\t\t\t******************9. CREATE PAY SLIP OF AN EMPLOYEE********************")
    print("\t\t\t******************10. REMOVE ALL EMPLOYEE'S DETAILS********************")
    print("\t\t\t\t********************11. CREATE TABLE*********************")
    print("\t\t\t\t******************12. DISPLAY ALL TABLES****************")

def insert(office):
    while True:
        try:
            Id = input("enter emp_id: (should have unique value)")
            name = input("employee name: ")
            depar = input('enter department: ')
            desig = input('enter designation: ')
            sal = input('enter salary: ')
            mob = input("enter mob: ")
            doj = input("enter date of joining (yyyy-mm-dd): ")
            query = "INSERT INTO mdps VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            cur1.execute(query, (Id, name, depar, desig, sal, mob, doj, office))
            con.commit()
            print()
            print("\t\t\t\t*************EMPLOYEE REGISTERED SUCCESSFULLY ;^) ***********")
            print()
            ch = input('do you want to register more employees? y or n: ')
            if ch in 'nN':
                break
        except pymysql.err.IntegrityError:
            print('\t\t\t\t*****Employee ID already exists! Please enter a unique ID.*****')
        except:
            print('\t\t\t\t*****please retry, try to enter field name and value correctly****')

def update():
    while True:
        try:
            name = input("enter name of employee whose details are to be updated: ")
            query1 = "SELECT * FROM mdps"
            cur1.execute(query1)
            c = cur1.fetchall()
            for i in c:
                if i[1] == name:
                    print('\t\t\tfield names: emp_id, emp_name, department, designation, salary, mob, date_of_joining')
                    print()
                    c_field = input('enter field name to be updated: ')
                    new = input('enter new value: ')
                    query = f'UPDATE mdps SET {c_field}=%s WHERE emp_name=%s'
                    cur1.execute(query, (new, name))
                    con.commit()
                    print('\t\t\t\t*****DETAILS OF EMPLOYEE UPDATED SUCCESSFULLY ;^) *****')
            ch = input('do you want to update more ? y or n: ')
            if ch == 'n':
                break
        except:
            print("\t\t\t\t****enter a valid employee name, the one provided earlier doesn't exist :^( **** ")
            print('\t\t\t\t*****please retry, try to enter field name and value correctly****')

def search():
    while True:
        try:
            print('\t\t\tfield names: emp_id, emp_name, department, designation, salary, mob, date_of_joining')
            print()
            c = input('enter field name on whose basis you wish to display details of the employee: ')
            j = input('enter value: ')
            query = f'SELECT * FROM mdps WHERE {c}=%s'
            cur1.execute(query, (j,))
            k = cur1.fetchall()
            if len(k) == 0:
                print('\t\t\t\t\t*********EMPLOYEE DETAILS NOT FOUND**********')
            else:
                print("\t\t\t******************DISPLAYING DETAILS OF EMPLOYEE**********************")
                for i in k:
                    print("emp_id : ", i[0])
                    print("emp_name : ", i[1])
                    print("department : ", i[2])
                    print("designation : ", i[3])
                    print("salary : ", i[4])
                    print("mob : ", i[5])
                    print("date_of_joining : ", i[6])
                    print("office : ", i[7])
                    print('\n')
            ch = input('do you want to display more ? y or n: ')
            if ch in 'nN':
                break
        except:
            print('\t\t\t\t*****please retry, try to enter field name and value correctly****')

def delete():
    while True:
        try:
            a = input('enter employee id who have left the office: ')
            query = 'SELECT * FROM mdps WHERE emp_id=%s'
            cur1.execute(query, (a,))
            r = cur1.fetchall()
            if len(r) == 0:
                print('\t\t\t\t\t*********EMPLOYEE NOT FOUND**********')
            else:
                query1 = 'DELETE FROM mdps WHERE emp_id=%s'
                e, f, g, h, i, j, k, l = r[0]
                query3 = 'INSERT INTO DEL VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
                cur1.execute(query3, (e, f, g, h, i, j, k, l))
                cur1.execute(query1, (a,))
                print('\t\t\t\t**********EMPLOYEE REMOVED SUCCESSFULLY**********')
        except:
            print('\t\t\t\t*************************Sorry Not Possible :( *********************************')
        con.commit()
        ch = input('do you want to remove more employees ? y or n: ')
        if ch == 'n':
            break

def deleten():
    query = 'TRUNCATE TABLE mdps'
    cur1.execute(query)
    con.commit()
    print('\t\t\t**********ALL THE EMPLOYEE DETAILS ARE DELETED SUCCESSFULLY************')

def display_all():
    query = 'SELECT * FROM mdps'
    cur1.execute(query)
    k = cur1.fetchall()
    x = len(k)
    if x == 0:
        print('\t\t\t*NO EMPLOYEE DETAILS ARE ENTERED YET... INSERT ONE AND PROCEED*')
    else:
        print("\t\t\t******************DISPLAYING ALL EMPLOYEE DETAILS**********************")
        for i in k:
            print("emp_id : ", i[0])
            print("emp_name : ", i[1])
            print("department : ", i[2])
            print("designation : ", i[3])
            print("salary : ", i[4])
            print("mob : ", i[5])
            print("date_of_joining : ", i[6])
            print("office : ", i[7])
            print('\n')

def display_sorted():
    try:
        print('\t\t\tfield names: emp_id, emp_name, department, designation, salary, mob, date_of_joining, office')
        c = input('enter field name on whose basis sorting should be done: ')
        query = f'SELECT * FROM mdps ORDER BY {c}'
        cur1.execute(query)
        k = cur1.fetchall()
        x = len(k)
        if x == 0:
            print('\t\t\t*NO EMPLOYEE DETAILS ARE ENTERED YET... INSERT ONE AND PROCEED*')
        else:
            print("\t\t\t******************DISPLAYING SORTED EMPLOYEE DETAILS**********************")
            for i in k:
                print("emp_id : ", i[0])
                print("emp_name : ", i[1])
                print("department : ", i[2])
                print("designation : ", i[3])
                print("salary : ", i[4])
                print("mob : ", i[5])
                print("date_of_joining : ", i[6])
                print("office : ", i[7])
                print('\n')
    except:
        print('\t\t\t\t*****please retry, try to enter field name correctly****')

def display_left():
    query = 'SELECT * FROM DEL'
    cur1.execute(query)
    k = cur1.fetchall()
    x = len(k)
    if x == 0:
        print('\t\t\t*NO EMPLOYEE HAS LEFT THE OFFICE YET...*')
    else:
        print("\t\t\t******************DISPLAYING DETAILS OF EMPLOYEES WHO LEFT OFFICE**********************")
        for i in k:
            print("emp_id : ", i[0])
            print("emp_name : ", i[1])
            print("department : ", i[2])
            print("designation : ", i[3])
            print("salary : ", i[4])
            print("mob : ", i[5])
            print("date_of_joining : ", i[6])
            print("office : ", i[7])
            print('\n')

def avg_salary():
    query = 'SELECT AVG(CAST(salary AS SIGNED)) FROM mdps'
    cur1.execute(query)
    k = cur1.fetchall()
    print('\t\t\tThe average salary that an employee receives is: ', k[0][0])

def create_table():
    query1 = '''CREATE TABLE IF NOT EXISTS mdps (
                   emp_id CHAR(10) PRIMARY KEY,
                   emp_name CHAR(40) NOT NULL,
                   department CHAR(40),
                   designation CHAR(40),
                   salary CHAR(14),
                   mob CHAR(10),
                   date_of_joining DATE,
                   office CHAR(80)
               )'''
    query2 = '''CREATE TABLE IF NOT EXISTS DEL (
                   emp_id CHAR(10) PRIMARY KEY,
                   emp_name CHAR(40) NOT NULL,
                   department CHAR(40),
                   designation CHAR(40),
                   salary CHAR(14),
                   mob CHAR(10),
                   date_of_joining DATE,
                   office CHAR(80)
               )'''
    query3 = '''CREATE TABLE IF NOT EXISTS pay (
                   emp_id CHAR(10),
                   emp_name CHAR(40),
                   month CHAR(10),
                   pay INT,
                   bonus INT,
                   leaves_taken INT,
                   total_pay FLOAT,
                   PRIMARY KEY (emp_id, month)
               )'''
    query4 = '''CREATE TABLE IF NOT EXISTS users (
                   user_id INT AUTO_INCREMENT PRIMARY KEY,
                   username VARCHAR(50) NOT NULL,
                   password VARCHAR(50) NOT NULL,
                   role VARCHAR(20)
               )'''
    cur1.execute(query1)
    cur1.execute(query2)
    cur1.execute(query3)
    cur1.execute(query4)
    con.commit()
    print('\t\t\t**********TABLES CREATED SUCCESSFULLY************')

def display_tables():
    query = 'SHOW TABLES'
    cur1.execute(query)
    k = cur1.fetchall()
    print('\t\t\t**********DISPLAYING ALL TABLES************')
    for i in k:
        print(i[0])
    print('\n')

def main():
    while True:
        menu()
        ch = int(input('\t\t\tEnter your choice: '))
        if ch == 1:
            insert('head_office')
        elif ch == 2:
            update()
        elif ch == 3:
            search()
        elif ch == 4:
            delete()
        elif ch == 5:
            display_all()
        elif ch == 6:
            display_left()
        elif ch == 7:
            display_sorted()
        elif ch == 8:
            avg_salary()
        elif ch == 9:
            create_pay_slip()
        elif ch == 10:
            deleten()
        elif ch == 11:
            create_table()
        elif ch == 12:
            display_tables()
        else:
            print('\t\t\tInvalid choice')
        cont = input('\t\t\tDo you want to continue? (y/n): ')
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
