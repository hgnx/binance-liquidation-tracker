import websocket
import json
import pandas as pd
import pytz

socket                          = 'wss://fstream.binance.com/ws/!forceOrder@arr'

'''
No filters:
minimum_total_dollars           = 0
set_ticker                      = None

For "minimum_total_dollars", it must be set to an integer value. Prints only values that are liquidated above that value.
For "set_ticker", it must be set as a list. Prints only the liquidation value of the ticker.

Example:
minimum_total_dollars           = 100
set_ticker                      = ['BTCUSDT, 'ETHUSDT', 'XRPUSDT', 'ADAUSDT', 'DOGEUSDT']
'''

minimum_total_dollars           = 0
set_ticker                      = None

df                              = pd.DataFrame(columns=['Symbol', 'Side', 'Price',
                                                        'Quantity', 'Total($)', 'Trade Time'])
def on_message(ws, message):
    data                        = json.loads(message)
    order_data                  = data['o']

    trade_time                  = pd.to_datetime(order_data['T'], unit='ms', utc=True)
    tz                          = pytz.timezone('Asia/Seoul')
    trade_time                  = trade_time.tz_convert(tz)

    new_row                     = {
        'Symbol'                : order_data['s'],
        'Side'                  : order_data['S'],
        'Price'                 : float(order_data['p']),
        'Quantity'              : float(order_data['q']),
        'Total($)'              : round(float(order_data['p']) * float(order_data['q']), 2),
        'Trade Time'            : trade_time.strftime('%Y-%m-%d %H:%M:%S')
    }

    global df
    if (set_ticker is None or new_row['Symbol'] in set_ticker) and \
    (minimum_total_dollars is None or new_row['Total($)'] >= minimum_total_dollars):
        df                      = pd.concat([pd.DataFrame(new_row, index=[0]), df]).reset_index(drop=True)
        print(df)
        print("")
    else:
        print("Error: Please check the filter.")

def on_error(ws, error):
    print('Error:', error)


def on_close(ws):
    print('Connection closed')


def on_open(ws):
    print('Connection opened')


ws                              = websocket.WebSocketApp(socket,
                                                        on_message=on_message,
                                                        on_error=on_error,
                                                        on_close=on_close)
ws.on_open                      = on_open
ws.run_forever()