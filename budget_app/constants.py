import re
BUDGET_TYPES = ["save", "invest", "spend"]
KNOWLEDGE_BASE={
    "save":"How much do you want to save this month?",
    "invest":"How much do you want to invest this month",
    "spend":"How much do you want to save this month",
    "accountid" : "^There is your account information above^ \n",
}
DEMO_ACCOUNTS = [{
    "accountid" : 1,
    "name": "dave",
    "account_amount" : 5000,
    "savings" : 4000,
    "checking" : 1000,
    "goals" : ["save", "invest"],
    "spending" : {
        "monthly": [{"sewage_bill": 100}, {"car_loan": 110}], 
        "purchases":[{"item1": 5}, {"item": 20}]
        }
},
{
    "accountid" : 2,
    "name": "todd",
    "account_amount" : 200,
    "savings" : 150,
    "checking" : 50,
    "goals" : ["save", "invest"],
    "spending" : {
        "monthly": [{"sewage_bill": 20}, {"car_loan": 30}], 
        "purchases":[{"item1": 4}, {"item": 2}]
        }
}]

#Neural Network Constants
INPUTS =  [[1.2, 3.1, 1.1],
          [1.6, 5.1, 1.1],
          [3.2, 2.1, 2.1]]
WEIGHTS = [[1.4, -1.3, 1.2],
           [2.1, 1.3, 2.7],
           [1.1,4.3,-1.4]]
BIAS = [2, 3, 4]
