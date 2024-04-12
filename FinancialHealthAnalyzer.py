import unittest
from io import StringIO

#Simon du Plooy - 2304874

#FinancialTransaction class allows for the program to read FinancialTransaction data found in test setUp and main below.
#This class does not need to be edited
class FinancialTransaction:
    def __init__(self, date, type, amount): #Initializing the FinancialTransaction class with its arguments
        self.date = date
        self.type = type
        self.amount = amount #Code to set this instance of FinancialTransanction's variables

    @staticmethod
    def from_line(line): #Defining a method for FinancialTransaction to be able to read from a line
        parts = line.strip().split(',') #Split the different parts of the information with ',' as a delimeter
        date, type, amount = parts[0], parts[1], float(parts[2]) #Set the variables equal to the information read from the parts array made prior
        return FinancialTransaction(date, type, amount) #Return the class

class FinancialHealthAnalyzer:
    def __init__(self, transactions):
        self.transactions = transactions #Code for initializing FinancialHealthAnalyzer instances

    #Adds together all transactions labeled "Income" in dollars
    def total_revenue(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Income") #Checks if a transaction entry is of type Income and then adds the amount

    #Adds together all transactions labeled "Expense" in rands
    def total_expenses(self):
        return sum(transaction.amount for transaction in self.transactions if transaction.type == "Expense") #Checks if a transaction entry is of type Expense and then adds the amount

    def profit(self):
        #Multiplying the revenue by 20 for the exchange rate of $1 = R20 and subtracting it from the rand expenses value
        return self.total_revenue()*20 - self.total_expenses()

    def profit_margin(self):
        #Dividing the rand profit value with the rand total revenue value
        return self.profit()/(self.total_revenue()*20)
    
    def average_transaction_amount(self):
        numerator = self.profit() #Get the profit value
        denominator = 0 #Initialize an amount for num of transactions

        for transaction in self.transactions:
            denominator += 1 #Count how many transactions there are

        return numerator/denominator #Return the calculated average transaction amount

    #Determines financial health and returns the corresponding string
    def financial_health(self):
        profit = self.profit()
        if profit >= 0:
            return "Healthy"
        elif -1000 <= profit < 0:
            return "Warning"
        else:
            return "Critical" #Logic to output the correct message for financial health, checking the values in a range

class TestFinancialHealthAnalyzer(unittest.TestCase):
    #Setup data allows for code to be tested without manually writing test transaction code for every test function. 
    #setUp transaction data and structure may be changed to include more test functions.
    def setUp(self):
        transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 1000),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 1500) #Test cases to check that follow the convention of Dollars for income and rands for expenses
        ]
        self.transactions = transactions_data
        
    #Test for the FinancialTransaction's from_line method
    def test_from_line(self):
        lineTestOne = "2024-01-01,Income,1000" #Strings of the test case information used in the transaction data in setUp
        lineTestTwo = "2024-01-02,Expense,500"
        #inputting a string as the argument for the from_line method to see if it can split it properly
        self.assertEqual(transactions_data[0].from_line(lineTestOne).date, "2024-01-01", "The date of the from_line method is wrong") #Using the unit test assertEqual statement to test the function answer
        self.assertEqual(transactions_data[0].from_line(lineTestOne).type, "Income", "The type of expense of from_line method is wrong")
        self.assertEqual(transactions_data[0].from_line(lineTestOne).amount, 1000, "The amount of the from_line method is wrong")

        self.assertEqual(transactions_data[1].from_line(lineTestTwo).date, "2024-01-02", "The date of the from_line method is wrong")
        self.assertEqual(transactions_data[1].from_line(lineTestTwo).type, "Expense", "The type of expense of from_line method is wrong")
        self.assertEqual(transactions_data[1].from_line(lineTestTwo).amount, 500, "The amount of the from_line method is wrong")

    #Test cases for the FinancialHealthAnalyzer Methods
    def test_total_revenue(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_revenue(), 2500, "The total revenue is wrong") #Using the unit test assertEqual statement to test the function answer

    def test_total_expenses(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.total_expenses(), 800, "The total expenses is wrong")

    def test_profit(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.profit(), 49200, "The profit is wrong")

    def test_profit_margin(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.profit_margin(), 0.984, "The profit margin is wrong")

    def test_average_transaction_amount(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.average_transaction_amount(), 12300, "The average transaction amount is wrong")

    def test_financial_health(self):
        analyzer = FinancialHealthAnalyzer(self.transactions)
        self.assertEqual(analyzer.financial_health(), "Healthy", "The financial health is wrong")

#Main function is where your code starts to run. Methods need to be compiled correctly before they can be called from main    
if __name__ == '__main__':

    #Do not change the transaction data, this data needs to produce the correct output stated in the lab brief
    transactions_data = [
            FinancialTransaction("2024-01-01", "Income", 50),
            FinancialTransaction("2024-01-02", "Expense", 500),
            FinancialTransaction("2024-01-03", "Expense", 300),
            FinancialTransaction("2024-01-04", "Income", 75)
        ] #Creating an array of instances of the FinancialTransaction class to work with
    
    FinancialHealthAnalyzer.transactions = transactions_data
    analyzer = FinancialHealthAnalyzer(FinancialHealthAnalyzer.transactions) #Creating an instance of FinancialHealthAnalyzer called analyzer

    #Outputting the important values in a readable manner
    print("Profit: " + str(analyzer.profit()))
    print("Profit margin: " + str(analyzer.profit_margin()))
    print("Average transaction amount: " + str(analyzer.average_transaction_amount()))
    print("Financial health: " + str(analyzer.financial_health()))
    unittest.main()
    