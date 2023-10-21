# splitwise
An expense sharing application is where you can add your expenses and split it among different people. The app keeps balances between people as in who owes how much to whom.

The Schema for the application is as follows : 
1. **User Class**:
   - The User class represents a user in the expense sharing application.
   - It has the following attributes:
     - user_id: A unique identifier for the user.
     - name: The user's name.
     - email: The user's email address.
     - mobile: The user's mobile number.
   - It also has an expenses attribute, which is a list that stores the expenses associated with this user.

2. **Expense Class**:
   - The Expense class represents an expense transaction within the application.
   - It has the following attributes:
     - expense_id: A unique identifier for the expense.
     - user_paid: The user who paid for the expense. This is an instance of the User class.
     - participants: A list of users who participated in the expense. Each participant is an instance of the User class.
     - amount: The total amount of the expense.
     - expense_type: The type of the expense, which can be "EQUAL," "EXACT," or "PERCENT."
     - splits: A dictionary that holds the split details, such as the amount each participant owes. This is used in the case of "EXACT" and "PERCENT" expenses.

