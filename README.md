# Restaurant Sales Data Pipeline & Interactive Dashboard 

An end-to-end data analytics project featuring an automated Python/SQL ETL pipeline and a dynamic Google Sheets dashboard designed for restaurant menu profitability optimization.

##  Live Project Links
* **Interactive Google Sheets Dashboard:** (https://docs.google.com/spreadsheets/d/1D3VlnRX4qhlMEB_NfvpRv3PLw5WqiOM66tgUrKYDJdk/edit?usp=sharing)
* **Python ETL Script:** [generate_data.py](generate_data.py)
## Technical Stack & Architecture
* **Data Engineering (ETL):** Python (`Pandas`, `SQLAlchemy`), SQLite database.
* **Data Cleaning & Modeling:** Google Sheets (`XLOOKUP`, `ARRAYFORMULA`, `TRIM`, `PROPER`).
* **Business Intelligence:** Dynamic interactive Slicers and executive KPI cards driven by the `SUBTOTAL` function.

## Key Business Insights & Impact
* **Revenue Drivers:** Identified the "Burgers" category as the primary volume driver, generating over $8,700 in sales and serving as the foundational customer acquisition anchor.
* **Hidden Profit Centers:** Uncovered that the "Pizza" category is a major high-margin profit center due to its significantly low cost of goods sold (COGS).
* **Strategic Action Plan:** Recommended introducing targeted "Burger + Side + Drink" combo meals to systematically scale the Average Order Value (AOV) from $12.29 toward a $15.00 target.

## How to Run the ETL Pipeline
1. Clone this repository.
2. Install dependencies: `pip install pandas sqlalchemy`
3. Run `python generate_data.py` to programmatically populate the SQLite database and output clean files.

