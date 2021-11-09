from typing import Dict, Set

from mtg_skeleton_gen.mtg_db import read_set_data


def is_land_touching_colors(card, colors):
    return "Land" in card.type_line and (len(set(card.color_identity) & colors) > 0)


def generate_skeleton(
    set_codes: Set[str],
    colors: Set[str],
    rarity_numbers: Dict[str, int],
):
    def is_valid_card(card):
        if (
            (not card.booster)
            or ("Basic" in card.type_line)
            or (rarity_numbers[card.rarity] == "0")
        ):
            return False
        if (
            card.colors is None
            and card.card_faces is not None
            and len(card.card_faces) > 0
        ):
            card.colors = {c for f in card.card_faces for c in f["colors"]}
        return is_land_touching_colors(card, colors) or set(card.colors) <= colors

    def make_card_line(card):
        rarity_count = rarity_numbers[card.rarity]
        return "{} {}".format(rarity_count, card.name)

    card_list = []
    for set_code in set_codes:
        card_list = card_list + read_set_data(set_code)

    return "\n".join(map(make_card_line, filter(is_valid_card, card_list)))
