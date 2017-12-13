#!/usr/bin/env python

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def get_query_results(query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def topThreeArticles():
    sqlstr = ("""
            SELECT l.path, COUNT(l.path),
            b.title as full_count from log as l
            JOIN articles as b on substr(l.path,10) = b.slug
            GROUP BY l.path, b.title ORDER BY COUNT DESC LIMIT 3;
            """)
    results = get_query_results(sqlstr)
    print('\n--------------------------------------------------------------\n')
    print ('The most popular three artciles of all time are:\n')
    for row in results:
        if len(row) > 1:
            print('"' + row[2] + '" - ' + str(row[1]) + ' views')
        else:
            print(row[1])
    print('\n--------------------------------------------------------------\n')


def topAuthors():
    sqlstr = ("""
            SELECT A.name, COUNT(b.author) from log as l
            JOIN articles as b on substr(l.path,10) = b.slug
            JOIN authors as A on b.author = A.id
            GROUP BY b.author, A.name
            ORDER BY COUNT DESC;
            """)
    results = get_query_results(sqlstr)
    print ('The most popular author of all time are:\n')
    for row in results:
        print('"' + str(row[0]) + '" - ' + str(row[1]) + ' views')
    print('\n--------------------------------------------------------------\n')


def checkError():
    sqlstr = ("""
            SELECT to_char(date_visited, 'YYYY/MM/DD'),
            error_count FROM
            (SELECT date(log.time) as DATE_VISITED,
            (sum(case when status = '404 NOT FOUND' then 1 else 0 end) * 100.00
            / COUNT(*)) AS ERROR_COUNT
            FROM log
            GROUP BY DATE_VISITED) x
            WHERE x.ERROR_COUNT > 1;
            """)
    results = get_query_results(sqlstr)
    print ('The following date has more than 1% of requests lead to errors:\n')
    for row in results:
        print(str(row[0]) + ' - ' + "{0:.2f}%".format(row[1]))
    print('\n--------------------------------------------------------------\n')


if __name__ == '__main__':
    topThreeArticles()
    topAuthors()
    checkError()
