# CLi Growth


**CLi Growth** is a lightweight command-line tool that calculates the compound growth of a stock over a specified time horizon using historical market data.

The program includes:
- Simple terminal interface/interactions
- Historical market data(via yfinance)
- Compound growth computation engine

# What is compound growth?
Compound growth is the process of an investment increasing in value over time that gains value from both the original investment and the value that has been added over time.

For example, if you put **$1,000** into a stock that returned an average of 10% per year, that does not mean that you will earn **$100** per year. Rather, the growth of each year is based on the last year's balance, so that your returns can compound.

This compounding effect is one of the main factors that can cause long-term investments to grow significantly.


# How it works
**CLi Growth** is split into 3 separate files each responsible for a specific task.

1. **main.py** collects the user's inputs.

2. The inputs are then passed into **computation.py**, which downloads the historical data using **yfinance**. Then uses that data to calculate the stock's estimated return over time and computes the investment's compounding growth.

3. The calculation results are then sent back to **main.py**

4. Finally, **display.py** formats and displays the results.

# Installation
### Using the installer (Recommended):

1. Navigate to the GitHub Releases page.

2. Download the latest [.exe](https://github.com/MxpleSticks/CLi-Growth/releases) file.

3. Run the .exe file to launch the application.

### Building from source:
Python 3.13.13 is recommended (for packages) --> [Here](https://www.python.org/downloads/windows/) <--

1. Clone or download the GitHub repo.

2. Install the required dependencies: `pip install -r requirements.txt`

3. Run the program: py main.py or python main.py

# Support

| Platform | Minimum Version | Download Link / Instructions |
| :--- | :--- | :--- |
| **Windows** | Windows 10/11 | Download the [.exe](https://github.com/MxpleSticks/CLi-Growth/releases) installer |
| **macOS** | 12.0+ (Monterey) | Not currently supported natively |
| **Linux** | Ubuntu 22.04+ | Not currently supported natively |

**The only way to run this program on macOS or Linux is to build via source.**

# Usage
**When the program is launched, you will be asked to enter the following details:**

1. Initial Investment Amount | How much money you already have in your brokerage
2. Stock Symbol | The stock ticker (e.g. AAPL, TSLA)
2.5 Stock Percentage | amount of your portfolio that you want to allocate to the previous symbol
3. Monthly Contribution Amount | How much money will you contribute monthly (can be 0)
4. Compound Frequency | The frequency used to calculate compound growth (monthly, quarterly, or annually).
5. Time Horizon | The number of years to calculate the growth over

After all of this your results will be displayed in the cli.