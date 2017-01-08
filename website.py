#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""website.py:	Diese Datei ist dient des Webinterfaces des Programms maTex"""

__author__ = "Julian Behringer"
__copyright__ = ""
__credits__ = ""

__license__ = ""
__version__ = "0.1"
__email__ = "julian.b@hringer.de"
__status__ = "dev"

import flask
import random
import time

file_used = None
timestr = time.strftime("%Y%m%d-%H%M%S")
app = flask.Flask(__name__)




@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/download")
def files_download():
    global file_used
    response = flask.make_response(file_used)
    response.headers["Content-Disposition"] = "attachment; filename=file.txt"  #   PDF:  file.pdf instead file.txt
    response.mimetype = 'text/plain'                                           #   PDF : application/pdf instead text/plain
    return response


@app.route("/error")
def failed():
    return flask.render_template('error.html')


@app.route("/grade", methods=['POST'])
def echo():
    text = flask.request.form['data']
    if not text:
        return flask.render_template('error.html')
    else:
        global file_used
        file_name = "files/file_" + timestr + ".txt"
        file = open(file_name, "w", encoding="utf-8")
        file.write("=== ANFANG TEXT ===" + "\n" + text + "\n" + "=== ENDE TEXT ===")
        text_grade = random.randint(0, 15)
        evidence = "30%"
        validity = "60%"
        usedtime = time.asctime(time.localtime(time.time()))
        file.write("\n" + "Deine Note: " + str(text_grade))
        file.write("\n" + "Benutzte Methode: " + flask.request.form['Methode'])
        file.write("\n" + "Benutztes Profil: " + flask.request.form['Profil'])
        file.write("\n" + "Evidence: " + evidence)
        file.write("\n" + "Richtigkeit des Profils: " + validity)
        file.write("\n" + "Datum der Korrektur: " + usedtime)
        file.close()
        file = open(file_name, "r", encoding="utf-8")
        file_used = file.read()
        if flask.request.form['Methode'] == "Erste":
            print("Erste Fertig")  # ERSTE METHODE EINFÜGEN
        elif flask.request.form['Methode'] == "Zweite":
            print("Zweite Fertig")  # ZWEITE METHODE EINFÜGEN
        elif flask.request.form['Methode'] == "Dritte":
            print("Dritte Fertig")  # DRITTE METHODE EINFÜGEN
        if flask.request.form['Profil'] == "First":
            print("First Fertig")  # ERSTES PROFIL EINFÜGEN
        elif flask.request.form['Profil'] == "Second":
            print("Second Fertig")  # ZWEITES PROFIL EINFÜGEN
        elif flask.request.form['Profil'] == "Third":
            print("Third Fertig")  # DRITTES PROFIL EINFÜGEN
        return flask.render_template('grade.html', text_grade=text_grade, method=flask.request.form['Methode'], profile=flask.request.form['Profil'], evidence=evidence, validity=validity)


if __name__ == "__main__":
    app.run(host="192.168.1.7", port=5010)
