import psycopg2

def send_ex(command):
    mydb = psycopg2.connect(user="postgres",
                            password="lopsed2211tyg",
                            host="127.0.0.1",
                            port="5432",
                            database="piramid")
    mycursor = mydb.cursor()

    mycursor.execute(command)
    res = mycursor.fetchall()
    mydb.commit()
    mycursor.close()
    mydb.close()
    return res