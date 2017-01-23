from compute import get_year as get_year_atom
from firm import get_year as get_year_firm

def print_years(year_income, years):
    prokatavoli = True
    asfalistra = 26.95

    firm_prokatavoli_pososto = 1.0
    firm_last_asfalistra = 0.0
    firm_last_prokatavoli = 0.0
    firm_total_profit = 0.0
    firm_total_income = 0.0

    atom_last_asfalistra = 0.0
    atom_last_prokatavoli = 0.0
    atom_total_profit = 0.0
    atom_total_income = 0.0

    for year in range(1, years):
        income = year_income
        if year <= 3:
            firm_prokatavoli_pososto = 0.5
        else:
            firm_prokatavoli_pososto = 1.0
        firm_tax, firm_paid_prokatavoli, firm_compassion, firm_pension, firm_epitideuma = get_year_firm(income, prokatavoli, firm_prokatavoli_pososto, asfalistra, last_asfalistra=firm_last_asfalistra, last_prokatavoli=firm_last_prokatavoli)
        firm_last_prokatavoli = firm_paid_prokatavoli
        firm_last_asfalistra = firm_pension
        firm_total = firm_tax + firm_compassion + firm_pension + firm_epitideuma
        firm_profit = income - firm_total
        firm_total_income += income
        firm_total_profit += firm_profit

        atom_tax, atom_paid_prokatavoli, atom_compassion, atom_pension, atom_epitideuma = get_year_atom(income, prokatavoli, asfalistra, last_asfalistra=atom_last_asfalistra, last_prokatavoli=atom_last_prokatavoli)
        atom_last_prokatavoli = atom_paid_prokatavoli
        atom_last_asfalistra = atom_pension
        atom_total = atom_tax + atom_compassion + atom_pension + atom_epitideuma
        atom_profit = income - atom_total
        atom_total_income += income
        atom_total_profit += atom_profit

    avg_atom_profit = atom_total_profit / years
    avg_firm_profit = firm_total_profit / years
    return avg_atom_profit, avg_firm_profit


if __name__ == "__main__":
    years = 20
    for euro in range(1000, 100000, 1000):
        atom, firm = print_years(euro, years)
        print("For {} personal {} firm {} diff {}".format(euro, atom, firm, atom-firm))