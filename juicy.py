
'''
'''

import sys


def invest_flash(amount, current_quantity=0):
    # 50 € for 4 months => 68 euros
    return invest(amount, 50, 0.3333333333333333, 1, 68, current_quantity)


def invest_myst(amount, current_quantity=0):
    # 2000 € for 3 years with 4 harvests per year at 300 €
    return invest(amount, 2000, 3, 4, 300, current_quantity)


def invest_kush(amount, current_quantity=0):
    # 2000 € for 4 years with 3 harvests per year at 500 €
    return invest(amount, 2000, 4, 3, 500, current_quantity)


def invest_haze(amount, current_quantity=0):
    # 2000 € for 5 years with 2 harvests per year at 900 €
    return invest(amount, 2000, 5, 2, 900, current_quantity)


def invest(amount, cost_per_lot, duration, harvest_per_year, revenue, current_quantity):
    lots =  min(amount // cost_per_lot, 1000 - current_quantity)
    remains = amount % cost_per_lot
    table = [remains]
    quantity = [lots]
    last = round(12 * duration)
    for idx in range(2, last + 1):
        quantity.append(lots)
        if idx % (12 / harvest_per_year) == 0 or idx == last:
            table.append(lots * revenue)
        else:
            table.append(0)
    quantity[-1] = 0
    return table, lots * cost_per_lot, quantity


def merge_arrays(store, idx, extra):
    for loop in range(len(extra)):
        try:
            store[idx + loop] += extra[loop]
        except IndexError:
            store.append(extra[loop])
    return store


# Limits (from https://www.juicyfields.site/faqs/):
# - 90 plants per order
# - 1000 total per category
def re_invest(duration, book):
    cash = 0
    haze_quantity = []
    quantity = []
    for idx in range(duration * 12 + 1):
        haze_quantity.append(0)
        quantity.append(0)
    for idx in range(duration * 12 + 1):
        cash += book[idx]
        print("                  month %02d: %05d € [%d, %d] plants" %
              (idx + 1, cash, haze_quantity[idx], quantity[idx]),
              file=sys.stderr)
        if cash >= 50:
            boost, invested, plan = invest_flash(cash, quantity[idx])
            cash -= invested
            book[idx] = 0
            merge_arrays(book, idx, boost)
            merge_arrays(quantity, idx, plan)
            print("reinvesting flash month %02d: %05d € %d plants" % (idx + 1, cash, quantity[idx]),
                  file=sys.stderr)
        if cash >= 2000:
            boost, invested, plan = invest_haze(cash, haze_quantity[idx])
            cash -= invested
            book[idx] = 0
            merge_arrays(book, idx, boost)
            merge_arrays(haze_quantity, idx, plan)
            print("reinvesting  haze month %02d: %05d € %d plants" % (idx + 1, cash, haze_quantity[idx]),
                  file=sys.stderr)
    return book

if __name__ == "__main__":
    res = re_invest(int(sys.argv[1]), [int(arg) for arg in sys.argv[2:]])
    print("sum = %d €" % sum(res))
    print(res)

# juicy.py ends here
