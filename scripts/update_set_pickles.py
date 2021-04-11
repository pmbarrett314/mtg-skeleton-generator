from context import mtg_skeleton_gen

from mtg_skeleton_gen.mtg_db import write_set_data, db_file

if __name__ == "__main__":
    for set_code in ["khm", "stx", "sta"]:
        write_set_data(set_code, db_file)
