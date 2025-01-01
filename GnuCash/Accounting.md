# Accounting with GnuCash

## 5 Account Types
* **Assets** - things you own, e.g. cash in bank account
* **Liabilities** - things you owe, e.g. mortgage
* **Equity** - overall net worth
* **Income** - increases the value of your accounts, e.g. paycheck
* **Expenses** - decreases the value of your accounts, e.g. eating out

## Equations
* The static accounting equation
    * `Assets - Liabilities = Equity`
* The dynamic accounting equation
    * `Assets - Liabilities = Equity + (Income - Expenses)`

## Debits and Credits
* Can be confusing since common usage is different from how accountants talk
```
Rearranged accounting equation:

LEFT HAND SIDE        RIGHT HAND SIDE
increased by debit    increased by credit entries
decreased by credit   decreased by debit entries

Assets + Expenses  =  Liabilities + Equity + Income
```

## 3 Levels of Organization
* **Files** - can be XML or SQL
* **Accounts** - track what you own, owe, spend, and receive
    * can contain an arbitrary number of sub-accounts
    * a *placeholder* account groups together sub-accounts, but has no transactions of its own
* **Transactions** - movement of money among accounts
    * *double entry accounting* has a *source* account and *destination* account for each transaction

## Opening Balances
One point of confusion is **how to enter opening balances** when you're just creating your GnuCash
database or starting the beginning of a accounting period. If you just dump that money as a transaction into a bank account,
that will create an imbalance. **Instead,** create the bank account under `Assets` but to enter the
money go to `Equity > Opening Balances` and enter the transaction there. Under `Transfer` select `Assets:Current Assets:My Bank Account`.
Avoid having a black hole (i.e. imbalance) in your accounting software!

## Misc
* Some other YouTube video I watched said that if your online banking lets you download
transaction history in `QFX (Quicken)` format, you can store it in `GnuCash > Data Sources`
and then import it into GnuCash.


## References
* https://www.gnucash.org/docs/v5/C/gnucash-guide/basics-accounting1.html
* https://www.gnucash.org/docs/v5/C/gnucash-guide/basics-entry1.html
* https://www.gnucash.org/docs/v5/C/gnucash-guide/basics-running-gnucash.html
