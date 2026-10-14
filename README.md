# Delivery Delay & Operations Analytics

## Project Overview

This project analyzes supply chain shipping data to understand delivery delays and identify areas where shipping performance can be improved.

The project uses Python for data analysis, visualization, and machine learning. An interactive dashboard built with Streamlit presents the main findings.

## Objectives

- Analyze shipping performance and delivery delays.
- Calculate late-shipping and on-time shipping rates.
- Compare shipping modes, regions, and product categories.
- Identify monthly and weekday shipping patterns.
- Build a decision tree model to estimate late-shipping risk.
- Present the results through an interactive dashboard.

## Dataset

The project uses the DataCo Supply Chain dataset.

- Original dataset size: 180,519 rows and 53 columns.
- Data includes shipping durations, delivery status, shipping mode, product category, market, region, and order dates.
- The original data covers January 2015 to January 2018.

The original dataset is not included in this repository. The repository contains selected summary files used by the dashboard.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Plotly
- Streamlit
- Google Colab
- GitHub

## Project Workflow

1. Load and inspect the dataset.
2. Select relevant shipping and operational columns.
3. Clean the data and prepare date fields.
4. Calculate shipping-duration delays.
5. Analyze shipping modes, regions, categories, weekdays, and months.
6. Build visualizations and a performance dashboard.
7. Train and evaluate a decision tree classifier.
8. Save analysis summaries for the Streamlit application.

## Key Findings

The initial analysis of the dataset identified the following:

- Total order-item rows: 180,519.
- Cancelled rows: 7,754.
- Non-cancelled rows: 172,765.
- Late-shipping rate: approximately 57.29%.
- On-time or early-shipping rate: approximately 42.71%.

These percentages are based on shipping-duration comparisons and exclude cancelled rows. Results may differ from the original delivery-status classifications.

## Interactive Dashboard

The Streamlit dashboard includes:

- Overall shipping performance metrics.
- Late-shipping rates by shipping mode.
- Regional performance comparisons.
- Monthly shipping trends.
- Product category performance.
- Potential operational hotspots.
- Decision tree feature importance.

**Live Dashboard:** Add your Streamlit website URL here.

## Repository Files

- `Delivery_Delay_&_Operations_Analytics.ipynb` — Data analysis notebook.
- `app.py` — Streamlit dashboard application.
- `requirements.txt` — Required Python packages.
- `shipping_mode_summary.csv` — Shipping mode analysis.
- `region_summary.csv` — Regional analysis.
- `category_summary.csv` — Product category analysis.
- `monthly_summary.csv` — Monthly performance analysis.
- `operational_hotspots.csv` — Potential operational hotspots.
- `model_feature_importance.csv` — Decision tree feature importance.

## Limitations

The dataset does not provide separate warehouse identifiers, carrier names, route details, or actual delivery-event timestamps. Therefore, the analysis identifies associations and potential problem areas rather than proving the root cause of each delay.

The decision tree is an exploratory model and requires further validation before operational use.

## Conclusion

This project demonstrates how Python, data visualization, and machine learning can be used to analyze supply chain performance and support data-driven operational decisions.

## Author

Harshit Kardam
