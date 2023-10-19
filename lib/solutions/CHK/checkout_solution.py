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

    """
    if False:
        skus = skus.upper()
        skus = re.sub("[^A-D]", "", skus)
    if True:
        if re.sub("[A-D]", "", skus).__len__() > 0:
            return -1

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
    }

    special_offers = {
        "A": ((3, 130), (5,200)),
        "B": ((2, 45)),
    }

    free_items = {
        "E": (2, 1, "B")
    }

    item_counts = Counter(skus)
    total_price = 0
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
    print(total_price)

    return total_price


print(checkout("a-AB"))
print(checkout(9*"A"))
