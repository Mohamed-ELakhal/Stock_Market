# Stock Market Data Pipeline

<p align="center">
  <img src="diagram.jpg" alt="Pipeline Diagram" width="700"/>
</p>

## Overview

This project is an **end-to-end data pipeline** that extracts stock market prices from the **Yahoo Finance API**, processes the data using **Apache Spark**, stores it on **MinIO**, and loads it into a **PostgreSQL** data warehouse.  
The workflow is orchestrated with **Apache Airflow** and monitored through **Slack** notifications, with data visualization handled by **Metabase**.

---

## Architecture

- **Yahoo Finance API**: Provides real-time stock prices.
- **Apache Airflow**: Manages and schedules the workflow (ETL process).
- **MinIO**: Object storage service (similar to AWS S3) to store raw and processed data.
- **Apache Spark**: Cleans and formats stock price data.
- **PostgreSQL**: Serves as the data warehouse for structured storage.
- **Slack**: Notifies users about pipeline execution results.
- **Metabase**: Visualizes data from PostgreSQL for analysis.

---

## Pipeline Steps

1. **Check API Availability**
   - Task: `is_api_available`
   - Verifies that the Yahoo Finance API is reachable.

2. **Fetch Stock Prices**
   - Task: `fetch_stock_prices`
   - Pulls stock price data from the API.

3. **Store Prices**
   - Task: `store_prices`
   - Saves the raw stock data into **MinIO**.

4. **Format Prices**
   - Task: `format_prices`
   - Processes and cleans data using **Apache Spark**.

5. **Get Formatted CSV**
   - Task: `get_formatted_csv`
   - Outputs cleaned data back into **MinIO** in CSV format.

6. **Load to Data Warehouse**
   - Task: `load_to_dw`
   - Loads the cleaned stock prices into **PostgreSQL**.

7. **Notify via Slack**
   - Task: `notifies`
   - Sends a notification to a Slack channel with the pipeline status.

8. **Visualization**
   - **Metabase** connects to PostgreSQL to provide dashboards and reports.

---

## Tech Stack

| Technology     | Purpose                                  |
|----------------|------------------------------------------|
| Apache Airflow | Workflow orchestration                  |
| Yahoo Finance API | Data source for stock prices         |
| MinIO          | Object storage for raw and processed data |
| Apache Spark   | Data processing and transformation      |
| PostgreSQL     | Data warehousing                        |
| Slack          | Alerts and notifications                |
| Metabase       | Data visualization and reporting        |

---

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mohamed-ELakhal/Stock_Market.git
   cd Stock_Market
   ```

2. **Configure environment variables** (API keys, MinIO, PostgreSQL credentials).

3. **Start Airflow services**:
   ```bash
   docker-compose up airflow-init
   docker-compose up
   ```

4. **Trigger the DAG** manually or set it on a schedule.

---

## Future Improvements

- Add retries and error handling for API failures.
- Implement unit tests for each task.
- Add monitoring with Airflow metrics to Prometheus/Grafana.
- Secure credentials using Airflow Connections and Vault integration.

---

## Author

**Mohamed ELakhal**  
[GitHub Profile](https://github.com/Mohamed-ELakhal)

---
