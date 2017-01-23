def get_tax(euros):
    remainder = euros
    tax = 0

    if  remainder < 20000:
        tax = remainder * 22.0 / 100.0
        remainder = 0
    else:
        tax = 20000 * 22.0 / 100.0
        remainder = remainder - 20000

    if remainder < 10000:
        tax += remainder * 29.0 / 100.0
        remainder = 0
    else:
        tax += 10000 * 29.0 / 100.0
        remainder = remainder - 10000

    if remainder < 10000:
        tax += remainder * 37.0 / 100.0
        remainder = 0
    else:
        tax += 10000 * 37.0 / 100.0
        remainder = remainder - 10000

    if remainder > 0:
        tax += remainder * 45.0 / 100.0
        remainder = 0

    return tax


def get_compasion(euros):
    remainder = euros
    tax = 0

    klimakia = {
        12000: 0.0,
        8000: 2.20,
        10000: 5.0,
        10000: 6.5,
        25000: 7.5,
        155000: 9.0,
        1000000: 10.0,
    }

    for size, rate in klimakia.items():
        if remainder <= size:
            tax += remainder * rate / 100.0
            remainder = 0
        else:
            tax += size * rate / 100.0
            remainder -= size

        if remainder <= 0:
            break

    return tax


def get_safety(euros, asfalistra):
    if euros > 70329:
        euros = 70329

    return euros * asfalistra / 100.0


def get_epitideumatos(euros):
    return 650


def get_year(euros, prokatavoli, asfalistra, last_prokatavoli = 0, last_asfalistra = 0):
    euros -= last_asfalistra
    tax = get_tax(euros)
    paid_prokatavoli = 0
    if prokatavoli:
        paid_prokatavoli = tax
        tax *= 2

    tax -= last_prokatavoli
    compassion = get_compasion(euros)
    pension = get_safety(euros, asfalistra)
    epitideuma = get_epitideumatos(euros)
    return tax, paid_prokatavoli, compassion, pension, epitideuma


def print_range():
    prokatavoli = True
    asfalistra = 26.95
    for thousants in range(1, 100):
        euros = 1000 * thousants
        tax, paid_prokatavoli, compassion, pension, epitideuma = get_year(euros, prokatavoli, asfalistra)
        total = tax + compassion + pension + epitideuma
        profit = euros - total
        profit_percentage = profit / euros * 100.0
        print("For {} tax is {} prokatavoli is {} compassion is {} pension is {} epitideuma is {}. In total: {} profit {} percentage {}"
              .format(euros, tax, paid_prokatavoli, compassion, pension, epitideuma, total, profit, profit_percentage))


def print_years():
    prokatavoli = True
    asfalistra = 26.95
    years = [
        70000,
        62000,
        62000,
        62000,
        62000,
        62000,
        62000,
        62000,
        62000,
    ]

    last_asfalistra = 0.0
    last_prokatavoli = 0.0
    year = 1
    total_profit = 0.0
    total_income = 0.0
    for income in years:
        tax, paid_prokatavoli, compassion, pension, epitideuma = get_year(income, prokatavoli, asfalistra, last_asfalistra=last_asfalistra, last_prokatavoli=last_prokatavoli)
        last_prokatavoli = paid_prokatavoli
        last_asfalistra = pension
        total = tax + compassion + pension + epitideuma
        profit = income - total
        total_income += income
        total_profit += profit
        profit_percentage = profit / income * 100.0
        print("Year {}: Income: {} Tax: {} Compassion: {} Pension: {} Epitideuma: {} Total payment: {} Profit: {} Percentage: {}"
              .format(year, income, tax, compassion, pension, epitideuma, total, profit, profit_percentage))
        year += 1

    avg_profit = total_profit / len(years)
    print("Total profit: {} Average profit: {}".format(total_profit, avg_profit))

if __name__ == "__main__":
    print_years()
