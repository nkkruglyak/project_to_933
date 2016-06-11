# coding: utf-8
from flask import Flask, render_template

from utils import prepare_list_of_genres_for_template, download_and_put_in_base

app = Flask(__name__)


@app.route('/')
def checkboxes():
    data = prepare_list_of_genres_for_template()
    return render_template('checkboxes.html', posts=data)


if __name__ == '__main__':
    download_and_put_in_base()
    app.run()