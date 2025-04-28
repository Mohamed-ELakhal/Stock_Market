Stock Market Data Pipeline
Overview
This project is an end-to-end data pipeline that extracts stock market prices from the Yahoo Finance API, processes the data using Apache Spark, stores it on MinIO, and loads it into a PostgreSQL data warehouse.
The workflow is orchestrated with Apache Airflow and monitored through Slack notifications, with data visualization handled by Metabase.

Architecture

Yahoo Finance API: Provides real-time stock prices.

Apache Airflow: Manages and schedules the workflow (ETL process).

MinIO: Used as an object storage service (similar to AWS S3) to store raw and processed data.

Apache Spark: Cleans and formats stock price data.

PostgreSQL: Serves as the data warehouse for structured storage.

Slack: Notifies users about pipeline execution results.

Metabase: Visualizes data from PostgreSQL for analysis.

Pipeline Steps
Check API Availability

Task: is_api_available

Verifies that the Yahoo Finance API is reachable.

Fetch Stock Prices

Task: fetch_stock_prices

Pulls stock price data from the API.

Store Prices

Task: store_prices

Saves the raw stock data into MinIO.

Format Prices

Task: format_prices

Processes and cleans data using Apache Spark.

Get Formatted CSV

Task: get_formatted_csv

Outputs cleaned data back into MinIO in CSV format.

Load to Data Warehouse

Task: load_to_dw

Loads the cleaned stock prices into PostgreSQL.

Notify via Slack

Task: notifies

Sends a notification to a Slack channel with the pipeline status.

Visualization

Metabase connects to PostgreSQL to provide dashboards and reports.

Tech Stack

Technology	Purpose
Apache Airflow	Workflow orchestration
Yahoo Finance API	Data source for stock prices
MinIO	Object storage for raw and processed data
Apache Spark	Data processing and transformation
PostgreSQL	Data warehousing
Slack	Alerts and notifications
Metabase	Data visualization and reporting
Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Mohamed-ELakhal/Stock_Market.git
cd Stock_Market
Configure environment variables (API keys, MinIO, PostgreSQL credentials).

Start Airflow services:

bash
Copy
Edit
docker-compose up airflow-init
docker-compose up
Trigger the DAG manually or schedule it.

Future Improvements
Add retries and error handling for API failures.

Implement unit tests for each task.

Add monitoring with Airflow metrics to Prometheus/Grafana.

Secure credentials using Airflow Connections and Vault integration.

Author
Mohamed ELakhal
GitHub Profile
