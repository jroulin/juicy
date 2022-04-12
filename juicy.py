
'''
'''


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


def invest(amount, cost, duration, harvest_per_year, revenue):
    lots = amount // cost
    remains = amount % cost
    table = []
    max = round(12 * duration)
    for idx in range(1, max+1):
        if idx == 1:
            table.append(remains)
        elif idx != 0 and (idx % (12 / harvest_per_year) == 0 or idx == max):
            table.append(lots * revenue)
        else:
            table.append(0)
    return table

# juicy.py ends here
