import os
import pickle

from contextlib import closing

from mtgtools.MtgDB import MtgDB

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
db_file = os.path.join(project_root, "data", "mtg_db.fs")
sets_dir = os.path.join(project_root, "data", "sets")


def card_manager(filename):
    return closing(MtgDB(filename))


def update_db(filename=None):
    if filename is None:
        filename = db_file

    with card_manager(filename) as mtg_db:
        mtg_db.scryfall_update()


def write_set_data(set_code, input_filename=None, output_filename=None):
    if input_filename is None:
        input_filename = db_file
    if output_filename is None:
        output_file = os.path.join(sets_dir, "{}.pickle".format(set_code))

    with card_manager(input_filename) as mtg_db:
        scryfall_cards = mtg_db.root.scryfall_cards
        set_cards = list(scryfall_cards.where_exactly(set=set_code))
        with open(output_file, "wb") as f:
            pickle.dump(list(set_cards), f)


def read_set_data(set_code, set_filename=None):
    if set_filename is None:
        set_filename = os.path.join(sets_dir, "{}.pickle".format(set_code))
    with open(set_filename, "rb") as f:
        return pickle.load(f)
