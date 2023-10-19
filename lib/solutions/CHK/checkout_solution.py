"""

Our price table and offers:
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+


Notes:
 - For any illegal input return -1

In order to complete the round you need to implement the following method:
     checkout(String) -> Integer

Where:
 - param[0] = a String containing the SKUs of all the products in the basket
 - @return = an Integer representing the total checkout value of the items
"""
import re
from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    +------+-------+------------------------+
    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    | F    | 10    | 2F get one F free      |
    +------+-------+------------------------+
    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    | F    | 10    | 2F get one F free      |
    | G    | 20    |                        |
    | H    | 10    | 5H for 45, 10H for 80  |
    | I    | 35    |                        |
    | J    | 60    |                        |
    | K    | 80    | 2K for 150             |
    | L    | 90    |                        |
    | M    | 15    |                        |
    | N    | 40    | 3N get one M free      |
    | O    | 10    |                        |
    | P    | 50    | 5P for 200             |
    | Q    | 30    | 3Q for 80              |
    | R    | 50    | 3R get one Q free      |
    | S    | 30    |                        |
    | T    | 20    |                        |
    | U    | 40    | 3U get one U free      |
    | V    | 50    | 2V for 90, 3V for 130  |
    | W    | 20    |                        |
    | X    | 90    |                        |
    | Y    | 10    |                        |
    | Z    | 50    |                        |
    +------+-------+------------------------+

    | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | U    | 40    | 3U get one U free               |
    | V    | 50    | 2V for 90, 3V for 130           |
    | W    | 20    |                                 |
    | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
    +------+-------+---------------------------------+

    """
    if False:
        skus = skus.upper()
        skus = re.sub("[^A-D]", "", skus)
    if True:
        if re.sub("[A-Z]", "", skus).__len__() > 0:
            return -1
    print("\n"+skus)

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 70,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 20,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 17,
        "Y": 20,
        "Z": 21,
    }

    special_offers = {
        "A": ((3, 130), (5,200)),
        "B": ((2, 45), ),
        "H": ((5, 45), (10, 80)),
        "K": ((2, 150), ),
        "P": ((5, 200), ),
        "Q": ((3, 80), ),
        "V": ((2, 90), (3,130)),

    }

    free_item_offers = {
        "E": (2, 1, "B"),
        "F": (2, 1, "F"),
        "N": (3, 1, "M"),
        "R": (3, 1, "Q"),
        "U": (3, 1, "U"),

    }

    group_discount_offers = [
        (("S","T","X","Y","Z"), 3, 45 )
    ]

    item_counts = Counter(skus)
    total_price = 0

    # Group discount offer
    for gdo_rule in group_discount_offers:
        item_counts_gdo_applicable = {k: v for k, v in item_counts.items() if k in gdo_rule[0]}
        num_discountable_items = int(sum(item_counts_gdo_applicable.values())/gdo_rule[1])*gdo_rule[1]
        total_price += int(num_discountable_items/gdo_rule[1]) * gdo_rule[2]

        while num_discountable_items>0:
            most_expensive_item = sorted(list({k: prices[k] for k, v in item_counts.items() if k in gdo_rule[0] and v > 0 }.items()), key=lambda x: -x[1])[0][0]
            item_counts[most_expensive_item] -= 1
            num_discountable_items -=1
        a=0

    for itm_id, offer_rule in free_item_offers.items():
        if itm_id in item_counts.keys():
            if offer_rule[2] in item_counts.keys():

                if itm_id == offer_rule[2]:
                    amount_of_free_items = int(item_counts[itm_id] / (offer_rule[0] + offer_rule[1]))
                    item_counts[offer_rule[2]] = max(0, item_counts[offer_rule[2]] - amount_of_free_items)
                else:
                    amount_of_free_items = int(item_counts[itm_id] / offer_rule[0]) * offer_rule[1]
                    item_counts[offer_rule[2]] = max(0, item_counts[offer_rule[2]] - amount_of_free_items)


    for k, v in item_counts.items():
        if k in special_offers.keys():
            item_count_unprocessed = v
            for price_rule in sorted(special_offers[k], key=lambda x: x[0], reverse=True):
                sets_reduced_price = int(item_count_unprocessed / price_rule[0])
                total_price += sets_reduced_price * price_rule[1]

                item_count_unprocessed -= (sets_reduced_price * price_rule[0])


            total_price += item_count_unprocessed * prices[k]
        else:
            total_price += v * prices[k]
            a = 0
    #print(total_price)

    return total_price


# print(checkout("a-AB"))
# print(checkout(9*"A"))
# print(checkout(2*"E"+4*"B"))
# print(checkout(1*"F"))
# print(checkout(2*"F"))
# print(checkout(3*"F"))
# print(checkout(4*"F"))
# print(checkout(5*"F"))
# print(checkout(6*"F"))
print(checkout("STXYZ"))  # 20 20 17 20 21



