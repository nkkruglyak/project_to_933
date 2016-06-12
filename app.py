# coding: utf-8
from flask import Flask, render_template
from flask import request

from utils import prepare_list_of_genres_for_template, download_and_put_in_base, mark_genres_as_chosen_by_id

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def checkboxes():
    if request.method == "POST":
        if request.form['submit'] == 'submit':
            keys = request.form.keys()
            list_id_of_checked = [int(i) for i in keys if not i.isalpha()]
            mark_genres_as_chosen_by_id(list_id_of_checked)
    data = prepare_list_of_genres_for_template()

    return render_template('checkboxes.html', posts=data)


if __name__ == '__main__':
    download_and_put_in_base()
    app.run()
