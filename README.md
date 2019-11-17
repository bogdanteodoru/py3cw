# py3cw

Unofficial wrapper for the [3Commas API](https://github.com/3commas-io/3commas-official-api-docs) written in Python.
***

How to install 

```bash
pip install py3cw
```

How to use

```python
from py3cw.request import Py3CW

p3cw = Py3CW(key='', secret='')

# With no action
# Destruct response to error and data
# and check first if we have an error, otherwise check the data
error, data = p3cw.request(
    entity='smart_trades',
    action=''
)

# With payload data
# Destruct response to error and data
# and check first if we have an error, otherwise check the data
error, data  = p3cw.request(
    entity='smart_trades', 
    action='create_smart_trade', 
    payload={
        "account_id": 123456
    }
)

# With action_id replaced in URL
# Destruct response to error and data
# and check first if we have an error, otherwise check the data
error, data = p3cw.request(
    entity='smart_trades', 
    action='pie_chart_data',
    action_id='123456'
)
```

*** 

An `entity` represents main categories. Meaning, you have `accounts`, `bots`, `marketplace`, `deals` or `smart_trades`

An `action` is represented by a ... well, an action of a specific category. There are multiple actions you can use (check 3commas API)

`action_id` is used to replace the necessary account_id or bot_id or deal_id (you get the picture) needed on some actions. For example the `action` `sell_all_to_btc` requires the `account_id` (`POST /ver1/accounts/{account_id}/load_balances`)

`payload` is the data you send.

***

3Commas API helpers.

3Commas Docs: https://github.com/3commas-io/3commas-official-api-docs

Accounts: https://github.com/3commas-io/3commas-official-api-docs/blob/master/accounts_api.md

Bots: https://github.com/3commas-io/3commas-official-api-docs/blob/master/bots_api.md

Deals: https://github.com/3commas-io/3commas-official-api-docs/blob/master/deals_api.md

Marketplace: https://github.com/3commas-io/3commas-official-api-docs/blob/master/marketplace_api.md

Smart Trades: https://github.com/3commas-io/3commas-official-api-docs/blob/master/smart_trades_api.md
