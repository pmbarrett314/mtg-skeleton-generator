from flask import Flask

from mtg_skeleton_gen.gen_skeleton import generate_skeleton


def create_app():
    _app = Flask("mtg-skeleton-generator")
    return _app


app = create_app()


@app.route("/")
def main():
    return generate_skeleton(
        "khm", {"R", "G"}, {"common": 2, "uncommon": 1, "rare": 1, "mythic": 1}
    ).replace("\n", "<br/>")


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # noinspection FlaskDebugMode
    app.run(host="127.0.0.1", port=8080, debug=True)
