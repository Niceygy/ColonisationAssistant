print("Loading...")

from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    send_from_directory,
)
from contextlib import contextmanager
# from flask_sqlalchemy import SQLAlchemy

from server.constants import DATABASE_CONNECTION_STRING, INITIAL_STATION_TYPES
from server.database.database import database
from server.database.search import query_star_systems


"""
Flask and database
"""

# database = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_STRING
app.config["SQLALCHEMY_POOL_SIZE"] = 10
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 280
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 20
database.init_app(app)

@contextmanager
def session_scope():
    session = database.session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        print(" * Closing session")
        session.close()

"""
Error Handler
"""


def uhoh(error):
    """
    Returns an error page, when somthing goes REALLY WRONGs
    """
    return render_template(
        "does_not_work.html", ERRORDATA=error, ERRORCODE="IRRECONCILABLE"
    )


"""
Route Handlers
"""


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "GET":
            return render_template(
                "index.html",
                types=INITIAL_STATION_TYPES
            )
        else:
            system_name = request.form.get("system")
            station_type = request.form.get("type")
            return f"{system_name},{station_type}"
    except Exception as e:
        return uhoh(str(e))
    


@app.route("/search_systems", methods=["GET"])
#@cache.cached(timeout=60, query_string=True)
def search_systems():
    query = request.args.get("query")
    results = query_star_systems(query)
    return jsonify(results)


@app.route("/favicon.ico")
#@cache.cached(timeout=60)
def favicon():
    return send_from_directory(app.static_folder, "favicon.ico")


@app.route("/copy_icon.svg")
#@cache.cached(timeout=60)
def copy_icon():
    return send_from_directory(app.static_folder, "copy_solid_icon.svg")


@app.route("/changelog", methods=["GET"])
#@cache.cached(timeout=60)
def changelog():
    return render_template("changelog.html")


@app.route("/robots.txt")
def robots():
    print(request.headers.get("User-Agent"))
    return send_from_directory(app.static_folder, "robots.txt")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)