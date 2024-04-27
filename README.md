# SalesInsight Analyzer

The SalesInsight Analyzer project is a data analysis tool built using Apache Spark to analyze sales data and provide insights into revenue generated per product category.

## Overview

The project reads sales data from a CSV file containing information about product categories and their corresponding revenue. It then processes this data using Apache Spark to calculate the total revenue for each product category. This allows users to gain insights into which product categories are driving the most revenue.

## Features

- **Data Analysis**: Analyze sales data to calculate total revenue per product category.
- **Scalability**: Utilizes Apache Spark for distributed data processing, enabling scalability for large datasets.
- **Flexibility**: Easily customizable to handle different types of sales data and perform various types of analysis.

## Usage

1. **Setup Apache Spark**: Ensure that Apache Spark is installed on your machine.
2. **Prepare Data**: Create a CSV file containing sales data with columns for `ProductCategory` and `Revenue`.
3. **Run the Script**: Execute the `sales_analysis.py` script using `spark-submit`.
