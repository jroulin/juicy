
'''
'''

import sys


def invest_flash(amount):
    # 50 € for 4 months => 68 euros
    return invest(amount, 50, 0.3333333333333333, 1, 68)


def invest_myst(amount):
    # 2000 € for 3 years with 4 harvests per year at 300 €
    return invest(amount, 2000, 3, 4, 300)


def invest_kush(amount):
    # 2000 € for 4 years with 3 harvests per year at 500 €
    return invest(amount, 2000, 4, 3, 500)


def invest_haze(amount):
    # 2000 € for 5 years with 2 harvests per year at 900 €
    return invest(amount, 2000, 5, 2, 900)


def invest(amount, cost_per_lot, duration, harvest_per_year, revenue):
    lots = amount // cost_per_lot
    remains = amount % cost_per_lot
    table = [remains]
    last = round(12 * duration)
    for idx in range(2, last + 1):
        if idx % (12 / harvest_per_year) == 0 or idx == last:
            table.append(lots * revenue)
        else:
            table.append(0)
    return table, lots * cost_per_lot


def merge_arrays(store, idx, extra):
    for loop in range(len(extra)):
        try:
            store[idx + loop] += extra[loop]
        except IndexError:
            store.append(extra[loop])
    return store


def re_invest(amount, duration):
    res, remains = invest_haze(amount)
    cash = amount - remains
    current = range(len(res))
    for idx in current:
        cash += res[idx]
        present = res[:idx + 1]
        if cash >= 2000:
            boost = invest_haze(cash)
            print("reinvesting  haze month %02d: %05d €" % (idx + 1, cash), file=sys.stderr)
            cash -= boost[1]
            res[idx] = 0
            merge_arrays(res, idx, boost[0])
        if cash >= 50:
            boost = invest_flash(cash)
            print("reinvesting flash month %02d: %05d €" % (idx + 1, cash), file=sys.stderr)
            cash -= boost[1]
            res[idx] = 0
            merge_arrays(res, idx, boost[0])
    return res

if __name__ == "__main__":
    res = re_invest(int(sys.argv[1]), int(sys.argv[2]))
    print("sum = %d €" % sum(res))
    print(res)

# juicy.py ends here
