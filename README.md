# Price-Search
Price Search is a market research bot that crawls pricing data to determine the frequency and extent of arbitage trading opportunities in Australian Crypto markets.
An arbitage trade is a discrepancy in pricing where an asset can be sold on one exchange for more than it can be purchased on another. This bot aims to find and catalouge
these discrepancies as they occur with the eventual goal of collecting a dataset large enough to assess the size, frequency and market conditions in which these trades can be
found. 

## Features
### Latest Release: v2.0.0-alpha
- Utilises SQL Database to provide detailed and accessible results
- Multi-Threaded searching allows for fast and consistent recording of discrepancies
- Actively searches three markets Coinspot, Coinjar and Swiftx
- Supports 5 assests: Bitcoin, Ripple, Litecoin, Stellar and Cardano*
- Exit with CTRL + C to view key infomation and stop search

**Cardano is not sold on Coinjar, comparisons will be made between Swiftx and CoinSpot*

## Using Price-Search
- Start search by running run.py from there searching will run automatically 
- Results will be stored in .DB file labled discrepancy_data
- A program supporting .DB format will be required to access results

### Viewing Results
If you don't have an easy method of viewing results, I recommend DB Browser for SQLite. It's open source and user friendly, can be accessed at https://sqlitebrowser.org/ 

## In Progress
- [ ] A robust and detailed system for tracking and recording discrepancies
- [ ] Comparisons between more assets and more markets
- [ ] Statistics Database to be built from collected data showcasing key infomation

## Long Term Goals
- [ ] User Friendly GUI
- [ ] More expansive collection of data to assess where discrepcancies are found including: swapping of assets, market conditions: volume, volatility
- [ ] Pre-courser to trading bot built on collected data 
