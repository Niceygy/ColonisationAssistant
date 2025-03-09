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
    STATION_TYPES,
)
from server.database.database import database
from server.database.search import query_star_systems
from server.find import find_stations
from server.database.share import find, save, load
from server.commodities import get_required_items
from server.inara.inara import get_cmdr_info


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
    return render_template("error.html", ERRORDATA=error, ERRORCODE="IRRECONCILABLE")


"""
Route Handlers
"""


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "GET":
            return render_template("index.html", station_types=STATION_TYPES)
        elif request.method == "POST":
            session["selected_type"] = request.form.get("station_types")
            session["selected_system"] = request.form.get("system")
            return redirect(url_for("results"))
    except Exception as e:
        return uhoh(str(e))


@app.route("/results", methods=["GET"])
def results():
    try:
        selected_station_type = session.get("selected_type", [])
        selected_system = session.get("selected_system", "")
        commodities = get_required_items(selected_station_type)
        stations = find_stations(commodities, selected_system)
        return render_template("results.html", data=stations, system=selected_system, stype=selected_station_type)
    except Exception as e:
        return uhoh(str(e))


@app.route("/import", methods=["GET", "POST"])
def importdata():
    id = None
    if request.method == "GET":
        id = request.args.get("b64")
    else:
        id = request.form.get("b64")
    commodities, system = load(id)
    print(f"commodities {list(commodities)} / system {system}")
    session["selected_commodities"] = commodities
    session["selected_system"] = system
    session["loaded_from_db"] = True
    session["sharecode"] = id
    return redirect(url_for("results"))


@app.route("/sharecode", methods=["GET", "POST"])
def generate_sharecode():
    selected_commodities = session.get("selected_commodities", [])
    selected_system = session.get("selected_system", "")
    sharecode = None
    if session.get("loaded_from_db"):
        sharecode = session.get("sharecode")
    else:
        sharecode = save(selected_commodities, selected_system)
    return sharecode

@app.route("/logon", methods=["GET", "POST"])
def inara():
    if request.method == "GET":
        return render_template("inara.html")
    else:
        sq = request.form.get("sq")
        session["squadron"] = sq
        
        # cmdrname = request.form.get("cmdrname")
        # rawdata = get_cmdr_info(apikey, cmdrname)
        # squadron = rawdata["eventData"]["commanderSquadron"]["SquadronID"]
        #  squadron
        return redirect(url_for("index"))
        

@app.route("/userdata/get", methods=["GET"])
def get_entry():
    name = request.args.get("sq")
    return find(name)
    
@app.route("/userdata/search", methods=["GET", "POST"])
def search_sq_systems():
    if request.method == "GET":
        return render_template("sq_search.html")
    else:
        id = request.form.get("id")
        jsondata, system_name = load(id)
        station_type = jsondata["type"]
                


@app.route("/search_systems", methods=["GET"])
def search_systems():
    query = request.args.get("query")
    results = query_star_systems(query)
    return jsonify(results)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, "favicon.ico")

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
