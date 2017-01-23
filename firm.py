from compute import get_safety, get_compasion


def get_epitideuma(euros):
    return 800


def get_tax(euros):
    tax = euros * 29.0 / 100
    return tax


def get_year(euros, prokatavoli, prokatavoli_pososto, asfalistra, last_prokatavoli = 0, last_asfalistra = 0):
    euros -= last_asfalistra
    tax = get_tax(euros)
    paid_prokatavoli = 0
    if prokatavoli:
        paid_prokatavoli = tax * prokatavoli_pososto
        tax += paid_prokatavoli

    tax -= last_prokatavoli
    epitideuma = get_epitideuma(euros)
    compassion = get_compasion(euros - (tax+ epitideuma))
    pension = get_safety(euros, asfalistra)
    return tax, paid_prokatavoli, compassion, pension, epitideuma


def print_range():
    prokatavoli = False
    prokatavoli_pososto = 0.0
    asfalistra = 26.95
    for thousant in range(1,100):
        euros = 1000 * thousant
        tax, paid_prokatavoli, compasion, pension, epitideuma = get_year(euros, prokatavoli, prokatavoli_pososto, asfalistra)
        total = tax + pension + epitideuma + compasion + paid_prokatavoli
        profit = euros - total
        profit_percentage = profit / euros * 100.0
        print("For {} tax is {} pension {} compasion {} epitideuma {} total {} profit {} percentage {}"
              .format(euros, tax, pension, compasion, epitideuma, total, profit, profit_percentage))


def print_years():
    prokatavoli = True
    asfalistra = 26.95
    years = [
        70000,
        62000,
        62000,
        62000,
        62000,
    ]

    prokatavoli_pososto = 1.0
    last_asfalistra = 0.0
    last_prokatavoli = 0.0
    year = 1
    total_profit = 0.0
    total_income = 0.0
    for income in years:
        if year <= 3:
            prokatavoli_pososto = 0.5
        else:
            prokatavoli_pososto = 1.0
        tax, paid_prokatavoli, compassion, pension, epitideuma = get_year(income, prokatavoli, prokatavoli_pososto, asfalistra, last_asfalistra=last_asfalistra, last_prokatavoli=last_prokatavoli)
        last_prokatavoli = paid_prokatavoli
        last_asfalistra = pension
        total = tax + compassion + pension + epitideuma
        profit = income - total
        total_income += income
        total_profit += profit
        profit_percentage = profit / income * 100.0
        print("Year {}: Income: {} Tax: {} Prokatavoli: {} Compassion: {} Pension: {} Epitideuma: {} Total payment: {} Profit: {} Percentage: {}"
              .format(year, income, tax, paid_prokatavoli, compassion, pension, epitideuma, total, profit, profit_percentage))
        year += 1

    avg_profit = total_profit / len(years)
    print("Total profit: {} Average profit: {}".format(total_profit, avg_profit))


if __name__ == "__main__":
    print_years()