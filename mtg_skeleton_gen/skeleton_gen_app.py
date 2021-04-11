from flask import Flask, render_template, request
from sets import sets

from mtg_skeleton_gen.gen_skeleton import generate_skeleton

rarities = ["common", "uncommon", "rare", "mythic"]


def create_app():
    _app = Flask("mtg-skeleton-generator")
    return _app


app = create_app()


@app.route("/")
def index():
    dropdown_sets = sets.keys()
    return render_template(
        "index.html", colors="WUBRG", dropdown_sets=dropdown_sets, rarities=rarities
    )


@app.route("/gen_skeleton")
def gen_skeleton():
    set_choice = request.args.get("set", type=str)
    set_codes = sets[set_choice]
    colors = set(request.values.getlist("colors"))
    print(colors)
    rarity_numbers = {rarity: request.values.get(rarity) for rarity in rarities}
    return generate_skeleton(set_codes, colors, rarity_numbers).replace("\n", "<br/>")


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # noinspection FlaskDebugMode
    app.run(host="127.0.0.1", port=8080, debug=True)
