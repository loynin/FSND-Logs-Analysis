import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def topThreeArticles():
    sqlstr = ("SELECT l.path, COUNT(l.path), \
    b.title as full_count from log as l \
    JOIN articles as b on substr(l.path,10) = b.slug \
    GROUP BY l.path, b.title ORDER BY COUNT DESC LIMIT 3; \
    ")

    db = connect()
    c = db.cursor()
    c.execute(sqlstr)
    results = c.fetchall()
    print('\n--------------------------------------------------------------\n')
    print ('The most popular three artciles of all time are:\n')
    db.close()
    for row in results:
        if len(row) > 1:
            print('"' + row[2] + '" - ' + str(row[1]) + ' views')
        else:
            print(row[1])
    print('\n--------------------------------------------------------------\n')


def topAuthors():
    sqlstr = ("SELECT A.name, COUNT(b.author) from log as l \
    JOIN articles as b on substr(l.path,10) = b.slug \
    JOIN authors as A on b.author = A.id \
    GROUP BY b.author, A.name \
    ORDER BY COUNT DESC \
    LIMIT 10; \
    ")
    db = connect()
    c = db.cursor()
    c.execute(sqlstr)
    results = c.fetchall()
    print ('The most popular author of all time are:\n')
    db.close()
    for row in results:
        if len(row) > 1:
    	    print('"' + str(row[0]) + '" - ' + str(row[1]) + ' views')
        else:
            print('Error')
    print('\n--------------------------------------------------------------\n')


def checkError():
    sqlstr = "SELECT * FROM \
    (SELECT to_char(log.time,'YYYY/MM/DD') as DATE_VISITED, \
    COUNT(to_char(log.time,'YYYY/MM/DD')) AS TOTAL_COUNT, \
    sum(case when status = '200 OK' then 1 else 0 end) SUCCESS_COUNT, \
    (sum(case when status = '404 NOT FOUND' then 1 else 0 end) * 100.00 / \
    COUNT(to_char(log.time,'YYYY/MM/DD'))) as ERROR_COUNT \
    FROM log GROUP BY DATE_VISITED) x where x.ERROR_COUNT > 1 ;"
    db = connect()
    c = db.cursor()
    c.execute(sqlstr)
    results = c.fetchall()
    print ('The following date has more than 1% of requests lead to errors:\n')
    db.close()
    for row in results:
        if len(row) > 1:
            print(str(row[0]) + ' - ' + "{0:.2f}%".format(row[3]))
        else:
            print(row[1])
    print('\n--------------------------------------------------------------\n')


if __name__ == '__main__':
    topThreeArticles()
    topAuthors()
    checkError()
