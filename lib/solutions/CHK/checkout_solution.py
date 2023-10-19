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

    """
    if False:
        skus = skus.upper()
        skus = re.sub("[^A-D]", "", skus)
    if True:
        if re.sub("[A-F]", "", skus).__len__() > 0:
            return -1
    print("\n"+skus)

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
    }

    special_offers = {
        "A": ((3, 130), (5,200)),
        "B": ((2, 45), ),
    }

    free_item_offers = {
        "E": (2, 1, "B"),
        "F": (2, 1, "F"),
    }

    item_counts = Counter(skus)
    total_price = 0

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
print(checkout(1*"F"))
print(checkout(2*"F"))
print(checkout(3*"F"))
print(checkout(4*"F"))
print(checkout(5*"F"))
print(checkout(6*"F"))
