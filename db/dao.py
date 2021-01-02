import mysql.connector


def connect():
    cnx = mysql.connector.connect(
        user='root',
        password='wrongpassword',
        host='',
        database='reviewsdb')
    # cursor = cnx.cursor()
    #
    # query = ("SELECT first_name, last_name, hire_date FROM employees "
    #          "WHERE hire_date BETWEEN %s AND %s")
    #
    #
    # cursor.execute(query, (hire_start, hire_end))
    #
    # for (first_name, last_name, hire_date) in cursor:
    #   print("{}, {} was hired on {:%d %b %Y}".format(
    #     last_name, first_name, hire_date))
    #
    # cursor.close()
    cnx.close()
