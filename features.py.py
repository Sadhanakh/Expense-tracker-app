#Linear search for transction by date
def search_by_date(transactions):
  date=input("enter date: ")
  for transaction in transactions:
    if transaction['date']==date:
      return transaction
  return "Transaction Not Found"

#Sorting transction based on amount with bubble sort
def sort_amount(transactions):
  n=len(transactions)
  for i in range(n):
    for j in range(n-1):
      if transactions[j]["amount"]>transactions[j+1]["amount"]:
        transactions[j],transactions[j+1]=transactions[j+1],transactions[j]
  return transactions

#Fetchinh input from the user
def add_data(transactions):
  dic={"date": input("enter date: "),
       "amount": int(input("enter amount: ")),
       "desc":input("enter desc: ")}
  transactions.append(dic)
  return transactions

#Delete data from list
def dele_dic(transactions):
  date=input("enter date: ")
  for transaction in transactions:
    if date in transaction["date"]:
      transactions.remove(transaction)
  return transactions

#Enter the amount
def sum_amount(transctions):
  year=input("enter year: ")
  sum=0
  for transction in transctions:
    if transction["date"][0:4]==year:
        sum+=transction["amount"]
  return sum
