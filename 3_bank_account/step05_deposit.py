def deposit(account, amount):
    account["balance"] = account["balance"] + amount

if __name__ == "__main__":
    import checks
    checks.run(5)
