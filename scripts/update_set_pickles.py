from context import mtg_skeleton_gen

from mtg_skeleton_gen.mtg_db import db_file, write_set_data
from mtg_skeleton_gen.sets import sets

if __name__ == "__main__":
    set_codes_set = set()

    for set_ in sets.values():
        set_codes_set.update(set_)
    for set_code in set_codes_set:
        print("Updating {}".format(set_code))
        write_set_data(set_code, db_file)
