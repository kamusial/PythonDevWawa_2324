"""Ta funkcja specjalnie jest taka długa.
Jeśli funkcja nie jest udokumentowana i jest długa,
czasem nie warto jej analizować, lepiej ją 'udokumentować' testami jednostkowymi! :)
"""


def process_transactions(transactions):
    """
    Process a list of transactions for a bank account.

    Parameters:
    - transactions (list of dict): List of dictionaries representing transactions.
      Each dictionary should have 'amount' (float) and 'type' (str) keys.

    Returns:
    - float: The final account balance after processing the transactions.
    """
    if not transactions:
        raise ValueError("Transaction list is empty.")

    account_balance = 0.0

    for transaction in transactions:
        if not isinstance(transaction, dict):
            raise ValueError("Each transaction should be a dictionary.")

        if 'amount' not in transaction or 'type' not in transaction:
            raise ValueError("Each transaction dictionary should have 'amount' and 'type' keys.")

        amount = transaction['amount']
        transaction_type = transaction['type']

        if not isinstance(amount, (int, float)) or not isinstance(transaction_type, str):
            raise ValueError("Invalid transaction format. 'amount' should be a number, and 'type' should be a string.")

        if transaction_type not in ['credit', 'debit']:
            raise ValueError("Invalid transaction type. Accepted values are 'credit' or 'debit'.")

        if transaction_type == 'debit' and amount > account_balance:
            raise ValueError("Insufficient funds for debit transaction.")

        if amount < 0:
            raise ValueError("Transaction amount should be positive.")

        if transaction_type == 'credit':
            account_balance += amount
        elif transaction_type == 'debit':
            account_balance -= amount

    return account_balance
