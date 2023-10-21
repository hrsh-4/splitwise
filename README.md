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

The design of the functionalities is as follows : 

 **ExpenseSharingApp Class**:
   - The `Splitwise` class serves as the core of the application.
   - It has the following attributes and methods:
     - `users`: A dictionary that stores user objects with user IDs as keys.
     - `add_user(user_id, name, email, mobile)`: A method for adding a new user to the application.
     - `add_expense(user_paid, participants, amount, expense_type, splits)`: A method for adding a new expense to the application.
     - `show_balances(user_id)`: A method for calculating and retrieving balances for a specific user.
     - The `add_user` and `add_expense` methods ensure that users and expenses are added correctly, and the `show_balances` method calculates balances between users.
   
Overall, this class structure allows you to create and manage users, track expenses, and calculate balances within the expense sharing application. Users, expenses, and their relationships are represented using objects, which provides a convenient way to organize and manipulate the data.

