# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from database import DBMS

# import some db stuff
import json

app = Flask(__name__)


@app.route("/")
def hello(name=None):
    # render static
    # print 'ok'
    return render_template('table.html', name=name)
    return "Hello World!"




@app.route("/articles")
@app.route("/articles/<q>")
def get_articles(range=None):
    # return json response
    #  articles = range(0, 10)
    #  print 'ok'
    q = 'test'
    # print 'ok'
    db = DBMS('stoneDB', 'user', '', 'localhost')
    query = request.args.get('q', 'test')
    rows = db.search_by_title(query)
    result = []
    for row in rows:
        rrow = {'id': row[0],
                'title': row[1],
                'year': row[2],
                'venue_id': row[3]
                }
        result.append(rrow)
    # print 'ok'
    print result
    articles = [
        {'id': 0,
         'name': 'Andrew'}
    ]
    return json.dumps(result)


@app.route("/article")
def get_article():
    return "Article"


if __name__ == "__main__":
    app.run()
