from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify
import json
import os.path
from werkzeug.utils import secure_filename

def create_app():
    app = Flask(__name__)
    app.secret_key = "HELLO_WORLD"

    @app.route("/")
    def home():
        return render_template("home.html", codes=session.keys())

    @app.route("/your-url", methods=["GET", "POST"])
    def your_url():
        if request.method == "POST":
            urls = {}

            if (os.path.exists("urls.json")):
                with open("urls.json") as url_file:
                    urls = json.load(url_file)

            req_form = request.form
            code = req_form["code"]
            
            if (code in urls.keys()):
                flash("Please select another name. It has already been taken.")
                return redirect(url_for('home'))

            if (len(request.files)):
                temp_file = request.files["file"]
                full_name = code + secure_filename(temp_file.filename)
                temp_file.save(app.root_path + '/static/user_files/' + full_name)
                urls[code] = {"file": full_name}
            else:
                urls[code] = {"url": req_form["url"]}

            with open("urls.json", "w") as url_file:
                json.dump(urls, url_file)
                session[code] = True

            return render_template("your_url.html", code=code)

        return redirect(url_for('home'))

    @app.route('/<string:code>')
    def redirect_to_url(code):
        if os.path.exists('urls.json'):
            with open("urls.json") as urls_file:
                urls = json.load(urls_file)
                if code in urls.keys():
                    if "file" in urls[code]:
                        return redirect(url_for("static", filename="user_files/" + urls[code]["file"]))
                    return redirect(urls[code]["url"])

        return abort(404)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("page_not_found.html"), 404


    @app.route('/api')
    def session_api():
        return jsonify(list(session.keys()))

    return app