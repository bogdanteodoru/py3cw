API_URL = 'https://api.3commas.io'
API_VERSION = '/public/api/ver1/'

# API methods from
# https://github.com/3commas-io/3commas-official-api-docs
API_METHODS = {
    'accounts': {
        '': ('GET', ''),
        'new': ('POST', 'new'),
        'update': ('POST', 'update'),
        'market_list': ('GET', 'market_list'),
        'market_pairs': ('GET', 'market_pairs'),
        'currency_rates': ('GET', 'currency_rates'),
        'sell_all_to_usd': ('POST', '{id}/sell_all_to_usd'),
        'sell_all_to_btc': ('POST', '{id}/sell_all_to_btc'),
        'rename': ('POST', '{id}/rename'),
        'pie_chart_data': ('POST', '{id}/pie_chart_data'),
        'account_table_data': ('POST', '{id}/account_table_data'),
        'remove': ('POST', '{id}/remove')
    },
    'deals': {
        '': ('GET', ''),
        'update_max_safety_orders': ('POST', '{id}/update_max_safety_orders'),
        'panic_sell': ('POST', '{id}/panic_sell'),
        'cancel': ('POST', '{id}/cancel'),
        'update_deal': ('PATCH', '{id}/update_deal'),
        'update_tp': ('POST', '{id}/update_tp'),
        'show': ('GET', '{id}/show'),
        'cancel_order': ('POST', '{id}/cancel_order'),
        'market_orders': ('GET', '{id}/market_orders'),
        'add_funds': ('POST', '{id}/add_funds'),
        'data_for_adding_funds': ('GET', '{id}/data_for_adding_funds'),
    },
    'bots': {
        '': ('GET', ''),
        'strategy_list': ('GET', 'strategy_list'),
        'pairs_black_list': ('GET', 'pairs_black_list'),
        'update_pairs_black_list': ('POST', 'update_pairs_black_list'),
        'create_bot': ('POST', 'create_bot'),
        'stats': ('GET', 'stats'),
        'update': ('PATCH', '{id}/update'),
        'disable': ('POST', '{id}/disable'),
        'enable': ('POST', '{id}/enable'),
        'start_new_deal': ('POST', '{id}/start_new_deal'),
        'delete': ('POST', '{id}/delete'),
        'panic_sell_all_deals': ('POST', '{id}/panic_sell_all_deals'),
        'cancel_all_deals': ('POST', '{id}/cancel_all_deals'),
        'show': ('GET', '{id}/show')
    },
    'marketplace': {
        'items': ('GET', 'items'),
        'signals': ('GET', '{id}/signals')
    },
    'smart_trades': {
        '': ('GET', ''),
        'create_simple_sell': ('POST', 'create_simple_sell'),
        'create_simple_buy': ('POST', 'create_simple_buy'),
        'create_smart_sell': ('POST', 'create_smart_sell'),
        'create_smart_cover': ('POST', 'create_smart_cover'),
        'create_smart_trade': ('POST', 'create_smart_trade'),
        'cancel_order': ('POST', '{id}/cancel_order'),
        'add_funds': ('POST', '{id}/add_funds'),
        'step_panic_sell': ('POST', '{id}/step_panic_sell'),
        'update': ('PATCH', '{id}/update'),
        'cancel': ('POST', '{id}/cancel'),
        'panic_sell': ('POST', '{id}/panic_sell'),
        'force_process': ('POST', '{id}/force_process'),
    }
}
