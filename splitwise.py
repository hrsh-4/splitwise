class User:
    def __init__(self, userId, name, email, mobile):
        self.userId = userId
        self.name = name
        self.email = email
        self.mobile = mobile
        self.expenses = []

class Expense:
    def __init__(self, paid_by, amount, participants, expense_type):
        self.paid_by = paid_by
        self.amount = amount
        self.participants = participants
        self.expense_type = expense_type

class Splitwise:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.userId] = user

    def add_expense(self, paid_by, amount, participants, expense_type):
        expense = Expense(paid_by, amount, participants, expense_type)
        for participant in participants:
            user = self.users.get(participant)
            if user:
                user.expenses.append(expense)

    def calculate_balances(self):
        balances = {}
        for user_id, user in self.users.items():
            for expense in user.expenses:
                if expense.expense_type == 'EQUAL':
                    share = expense.amount / len(expense.participants)
                elif expense.expense_type == 'EXACT':
                    share = sum(expense.participants.values())
                elif expense.expense_type == 'PERCENT':
                    total_percentage = sum(expense.participants.values())
                    share = (expense.amount * expense.participants[user_id]) / total_percentage

                for participant, percent in expense.participants.items():
                    if participant != user_id:
                        if participant not in balances:
                            balances[participant] = {}
                        if user_id not in balances[participant]:
                            balances[participant][user_id] = 0
                        balances[participant][user_id] += share * percent / 100

        return balances

# Example usage:

# Creating users
user1 = User('u1', 'User1', 'user1@example.com', '1234567890')
user2 = User('u2', 'User2', 'user2@example.com', '1234567891')
user3 = User('u3', 'User3', 'user3@example.com', '1234567892')
user4 = User('u4', 'User4', 'user4@example.com', '1234567893')

# Creating expense manager
splitwise = Splitwise()

# Adding users to the expense manager
splitwise.add_user(user1)
splitwise.add_user(user2)
splitwise.add_user(user3)
splitwise.add_user(user4)


# Adding expenses
splitwise.add_expense('u1', 1000, {'u1': 1, 'u2': 1, 'u3': 1, 'u4': 1}, 'EQUAL')
splitwise.add_expense('u1', 1250, {'u2': 370, 'u3': 880}, 'EXACT')
splitwise.add_expense('u4', 1200, {'u1': 40, 'u2': 20, 'u3': 20, 'u4': 20}, 'PERCENT')

# Calculating balances
balances = splitwise.calculate_balances()

# Printing balances
for debtor, creditors in balances.items():
    for creditor, amount in creditors.items():
        print(f'{debtor} owes {creditor}: Rs {amount:.2f}')

    