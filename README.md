# Binance Forced Liquidation Tracker

The Binance Forced Liquidation Tracker is a Python script that utilizes the Binance WebSocket API to monitor and record forced liquidation orders in real-time.

It is designed to track forced liquidation orders that occur on the Binance Futures when a trader's position is automatically closed due to insufficient margin to cover their losses.

This tool allows users to monitor these events and apply custom filters to focus on specific liquidations based on total value and ticker symbols.


## Features

- Real-time monitoring and recording of forced liquidation using the Binance WebSocket API.
- Filter forced liquidation orders based on a minimum total dollar value and specific ticker symbols.
- Store and manipulate tracked data using a pandas DataFrame.
- Run the code as a Python script, Jupyter Notebook, or view live tracking via an HTML file.

## Installation and Usage

1. Download the project code.
```
git clone https://github.com/hgnx/binance-liquidation-tracker.git
```

2. Install the required libraries.
```
pip install -r requirements.txt
```

3. Run the program.

**There are three options to run the program:**

#### * Python Script
```
python main.py
```
#### * Jupyter Notebook
Open `main.ipynb` in a Jupyter Notebook environment and execute the cells.

#### * HTML File
Simply open `live_tracker.html` in your browser to view the live tracking without the need for a Python environment.

Live demo: https://www.hgk.im/liqtracker/

## Disclaimer
This script is for informational purposes only and should not be used as the basis for any financial decisions. I take no responsibility for any personal financial loss. Use this script at your own risk.