# Superstore Sales Data Analysis

## Overview
End-to-end data analysis project on the Superstore Sales dataset (Kaggle), covering data understanding, preprocessing, 
exploratory data analysis, SQL-based analysis, and business insights reporting.

## Project Structure
```
Data-Analysis-SalesReport-Project/
├── notebook/ 
│   ├── DataUnderstanding.ipynb
│   ├── DataPreprocessing.ipynb
│   ├── ExploratoryDataAnalysis.ipynb
│   ├── SqlAnalysis.ipynb
│   ├── BusinessReport.py 
├── data/
│   ├── Raw-Superstore.csv
│   └── Cleaned-Superstore.csv                   
├── reports/
│   └── Business_Insights_Report.pdf
├── screenshots/
│   ├── year+month_full_time_time_superstore.png
│   ├── Top_10products.png
│   ├── Top_Profits_Per_customer.png
│   ├── Top_sales_per_customer.png
│   ├── Sales_By_Region_Bar.png
│   └── Sales_By_Region_Pie.png                 
├── requirements.txt
└── README.md
```

## Setup Instructions
```
git clone <repo-url>
cd Data-Analysis-SalesReport-Project
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Execution Steps
1. Open `notebook/` and run cells in order (Data Understanding → Preprocessing → EDA → SQL Analysis).
2. Generate the Business Insights Report:
   ```bash
   python BusinessReport.py
   ```
3. Output PDF is saved in the project root / `reports/` folder.

## Key Findings
- **Sales Trends:** Consistent year-over-year growth (2014-2017) with a strong seasonal peak every November-December.
- **Customer Behavior:** Profit is concentrated in a small set of high-margin customers (e.g., Tamara Chand, Raymond Buch) rather than spread evenly.
- **Product Performance:** Canon imageCLASS 2200 Advanced Copier is the top profit driver, nearly 3x the next-best product.
- **Regional Performance:** West and East lead in sales; South underperforms by ~46% compared to West.

Full analysis and recommendations available in `reports/Business_Insights_Report.pdf`.

## Screenshots
*[Sales Trend](screenshots/year+month_full_time_time_superstore.png)
*[Top Sales by Customer](screenshots/Top_sales_per_customer.png)
*[Top Customers by Profit](screenshots/Top_Profits_Per_customer.png)
*[Top 10 Products by Profit](screenshots/Top_10products.png)
*[Sales by Region - Bar](screenshots/Sales_By_Region_Bar.png)
*[Sales by Region - Pie](screenshots/Sales_By_Region_Pie.png)

## Tech Stack
- Python (pandas, numpy)
- Matplotlib, Seaborn
- SQL (SQLAlchemy)
- ReportLab (PDF report generation)
- Jupyter Notebook
