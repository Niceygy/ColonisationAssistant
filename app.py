print("Loading...")

from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
    session,
)
from contextlib import contextmanager

from server.constants import (
    DATABASE_CONNECTION_STRING,
    INITIAL_STATION_TYPES,
    MATERIAL_LISTS,
)
from server.database.database import database
from server.database.search import query_star_systems
from server.find import find_stations
from server.share import encode_to_share

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
app.secret_key = "supersecretkey"
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
            return render_template("index.html", commodities=MATERIAL_LISTS)
        elif request.method == "POST":
            session["selected_commodities"] = request.form.getlist("commodities")
            session["selected_system"] = request.form.get("system")
            return redirect(url_for("results"))
    except Exception as e:
        return uhoh(str(e))


@app.route("/results", methods=["GET"])
def results():
    try:
        selected_commodities = session.get("selected_commodities", [])
        selected_system = session.get("selected_system", "")
        stations = find_stations(selected_commodities, selected_system)
        result = {}
        i = 0
        for item in selected_commodities:
            result[item] = stations[i]
            i += 1
        sharecode = encode_to_share(f"{result}@{selected_system}")
        return render_template("general.html", data=result, system=selected_system, sharecode=sharecode)
    except Exception as e:
        return uhoh(str(e))


@app.route("/search_systems", methods=["GET"])
def search_systems():
    query = request.args.get("query")
    results = query_star_systems(query)
    return jsonify(results)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, "favicon.ico")


@app.route("/copy_icon.svg")
def copy_icon():
    return send_from_directory(app.static_folder, "copy_solid_icon.svg")


@app.route("/changelog", methods=["GET"])
def changelog():
    return render_template("changelog.html")


@app.route("/robots.txt")
def robots():
    print(request.headers.get("User-Agent"))
    return send_from_directory(app.static_folder, "robots.txt")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
