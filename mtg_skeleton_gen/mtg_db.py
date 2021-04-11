import os

from contextlib import closing

from mtgtools.MtgDB import MtgDB

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
db_file = os.path.join(project_root, "data", "mtg_db.fs")
sets_dir = os.path.join(project_root, "data", "sets")


def card_manager(filename):
    return closing(MtgDB(filename))


def update_db(filename):
    with card_manager(filename) as mtg_db:
        mtg_db.scryfall_update()
