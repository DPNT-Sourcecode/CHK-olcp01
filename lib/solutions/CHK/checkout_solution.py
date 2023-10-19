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
    skus = skus.upper()
    skus = re.sub("^[A-D]", "", skus)

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
    }

    special_offers = {
        "A": (3, 130),
        "B": (2, 45),
    }
    item_counts = Counter(skus)
    total_price = 0
    for k, v in item_counts.items():
        if k in special_offers.keys():
            sets_reduced_price = int(v / special_offers[k][0])
            items_regular_price = v % special_offers[k][0]
            total_price += sets_reduced_price * special_offers[k][1]
            total_price += items_regular_price * prices[k]
        else:
            total_price += v * prices[k]
            a = 0
    print(total_price)

    return total_price


checkout("a")
