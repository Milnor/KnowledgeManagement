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
* **Transactions** - movement of money among accounts
    * *double entry accounting* has a *source* account and *destination* account for each transaction

## Misc
* Some YouTube video I watched said that if your online banking lets you download
transaction history in `QFX (Quicken)` format, you can store it in `GnuCash > Data Sources`
and be imported into GnuCash.


## References
* https://www.gnucash.org/docs/v5/C/gnucash-guide/basics-accounting1.html
* https://www.gnucash.org/docs/v5/C/gnucash-guide/basics-entry1.html
