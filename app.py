print("Loading...")

# External Imports
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
from dotenv import load_dotenv
import os

# Local Files
from server.constants import STATION_TYPES, COMMDOTIES
from server.database.database import database
from server.database.search import query_star_systems
from server.find import find_stations
from server.database.share import save, load, update
from server.commodities import get_required_items
from server.auth.fdev import configure_oauth


"""
Flask and database
"""

load_dotenv()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_CONNECTION_STRING")
app.config["SQLALCHEMY_POOL_SIZE"] = 10
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 280
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 20
app.config["SECRET_KEY"] = os.getenv("SESSION_KEY")
database.init_app(app)
configure_oauth(app)


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
    return render_template("error.html", ERRORDATA=error, ERRORCODE="IRRECONCILABLE")


"""
Route Handlers
"""


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "GET":
            return render_template("index.html", station_types=STATION_TYPES, items=COMMDOTIES)
        elif request.method == "POST":
            session["selected_type"] = request.form.get("station_types")
            session["selected_system"] = request.form.get("system")
            session["redirect"] = False
            return redirect(url_for("results"))
    except Exception as e:
        return uhoh(str(e))

@app.route("/selected", methods=["GET", "POST"])
def results_seleced():
    try:
        items = request.form.getlist("commodities")
        commodities = []
        for item in items:
            commodities.append([item, 0])
        system = request.form.get("system")
        stations = find_stations(commodities, system)
        return render_template("results.html", data=stations, values=[], system=system, stype="Manual Mode: Unknown")
    except Exception as e:
        return uhoh(e)

@app.route("/results", methods=["GET"])
def results():
    try:
        if session.get("redirect", False):
            # This is a redirect from /userdata/get
            selected_station_type = session.get("selected_type", [])
            selected_system = session.get("selected_system", "")
            commodities = session.get("selected_commodities", None)
            id = session.get("id")
            # Just In Case!
            if commodities == None:
                commodities = get_required_items(selected_station_type)
            stations = find_stations(commodities, selected_system)
            values = session.get("user_progress")
            # Also include the ID, to avoid creating new entries when not needed
            return render_template(
                "results.html",
                data=stations,
                system=selected_system,
                stype=selected_station_type,
                values=values,
                id=id,
            )
        else:
            # From main page, id of -1 means it doesn't exist
            selected_station_type = session.get("selected_type", [])
            selected_system = session.get("selected_system", "")
            commodities = get_required_items(selected_station_type)
            stations = find_stations(commodities, selected_system)

            return render_template(
                "results.html",
                data=stations,
                system=selected_system,
                stype=selected_station_type,
                values=[],
                id="-1",
            )
    except Exception as e:
        return uhoh(str(e))


@app.route("/sharecode", methods=["POST"])
def generate_sharecode():
    try:
        selected_commodities = request.json.get("values")
        selected_system = session.get("selected_system", "")
        selected_type = session.get("selected_type", "")
        squadron = session.get("squadron", "Nightspeed LLC")
        id = request.json.get("id")
        if id != "-1":
            # Entry! Update old one
            update(id, selected_commodities)
            window = request.json.get("window")
            return f"{window}/userdata/get?id={id}"
        else:
            # No entry! Make a new one
            sharecode = save(
                selected_commodities, selected_system, selected_type, squadron
            )
            window = request.json.get("window")
            return f"{window}/userdata/get?id={sharecode}"
    except Exception as e:
        # Oopsie
        return uhoh(e)


@app.route("/userdata/get", methods=["GET"])
def get_entry():
    try:
        id = request.args.get("id")
        user_progress, system_name, station_type = load(id)
        session["selected_type"] = station_type
        session["selected_system"] = system_name
        session["selected_commodities"] = get_required_items(station_type)
        session["user_progress"] = user_progress
        session["redirect"] = True
        session["id"] = id
        return redirect(url_for("results"))
    except Exception as e:
        return uhoh(e)


@app.route("/search_systems", methods=["GET"])
def search_systems():
    query = request.args.get("query")
    results = query_star_systems(query)
    return jsonify(results)


"""
Static files
"""


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, "icons/favicon.ico")


@app.route("/js/util.js")
def js_util():
    return send_from_directory(app.static_folder, "js/util.js")


@app.route("/changelog", methods=["GET"])
def changelog():
    return render_template("changelog.html")


@app.route("/robots.txt")
def robots():
    print(request.headers.get("User-Agent"))
    return send_from_directory(app.static_folder, "robots.txt")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
