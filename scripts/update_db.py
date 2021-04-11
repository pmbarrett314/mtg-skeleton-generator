from context import mtg_skeleton_gen

from mtg_skeleton_gen.mtg_db import db_file, update_db

if __name__ == "__main__":
    update_db(db_file)
