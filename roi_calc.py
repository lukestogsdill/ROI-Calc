class Calcuator():
    def __init__(self):
        self.income = {'Rental': 0, 'Laundry': 0, 'Storage': 0, 'Misc': 0}
        self.expense = {'Tax': 0, 'Insurance': 0, 'Utilities': 0, 'HOA': 0, 'Vacancy': 0, 'Repairs': 0, 'CapEX': 0, 'Property Management': 0, 'Mortgage': 0}
        self.investment = {'Down Payment': 0, 'Closing Costs': 0, 'Rehab Budget': 0}

    def display_dict(self, a_dict, name):
        print(f'\n\n---------{name.upper()}----------')
        print(f'Common kinds of {name.title()}s ')
        for k,v in a_dict.items():
            print(f'{k}: ${v}')
        print(f'\nTotal: ${sum(a_dict.values())}')
    
    def cash_flow(self):
        return sum(self.income.values()) - sum(self.expense.values())

    def calc_roi(self):
        return float((self.cash_flow() * 12 / sum(self.investment.values()))*100)

    def get_inputs(self, a_dict, name):
        try:
            key = str(input(f'\t\nEnter kind of {name} to add :')).title()
            value = int(input('\t\nEnter value :'))
            a_dict[key] = value
            return a_dict
        except ValueError:
            print('Error! Please enter a valid number.')

    def edit_inputs(self, a_dict, name):
        try:
            self.display_dict(a_dict, name)
            option = int(input(f'| 1: Add / Edit | 2: Remove | 3: Back | :'))
            if option == 1:
                self.get_inputs(a_dict, name)
            elif option == 2:
                key = str(input(f'\t\nEnter kind of {name} to remove :')).title()
                del a_dict[key]
            elif option == 3:
                self.runner()
            self.edit_inputs(a_dict, name)
        except ValueError:
            print('Error! Please enter a valid number.')

    def runner(self):
        while True:
            print('\n\n\n--------------------------------------Main Menu-----------------------------------')
            print(f'\n\tCurrent monthly cash flow ${self.cash_flow()}')
            print(f'\tIncome Total ${sum(self.income.values())}')
            print(f'\tExpense Total ${sum(self.expense.values())}')
            print(f'\tInvestment Total ${sum(self.investment.values())}')
            try:
                option = int(input('\t\n\n| 1: Edit Income | 2: Edit Expenses | 3: Edit Investment | 4: Calculate ROI | 5: Exit :'))
                if option == 1:
                    name = 'Income'
                    self.edit_inputs(self.income, name)
                elif option == 2:
                    name = 'Expense'
                    self.edit_inputs(self.expense, name)
                elif option == 3:
                    name = 'Investment'
                    self.edit_inputs(self.investment, name)
                elif option == 4:
                    try:
                        print(f'\n\n\t-------------Cash on Cash ROI: {self.calc_roi()}%--------------------')
                    except:
                        print('\n\tError! All fields must have values')
                elif option == 5:
                    exit()
            except ValueError:
                print('Error! Please enter a valid number.')

luke = Calcuator()
luke.runner()