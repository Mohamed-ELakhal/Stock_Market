from airflow.decorators import task, dag
from datetime import datetime
import random

# Define DAG arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 3, 23)
}

# Define DAG
@dag(
    dag_id="taskflow_dag",
    default_args=default_args,
    schedule="@daily",  # FIX: Changed from "daily" to "@daily"
    catchup=False,
    tags=["taskflow"]
)
def taskflow():
    @task
    def generate_random_number():
        number = random.randint(1, 100)
        print(f"Generated random number: {number}")
        return number

    @task
    def check_even_odd(number):
        result = "even" if number % 2 == 0 else "odd"
        print(f"The number {number} is {result}.")
    
    # Define task dependencies
    random_number = generate_random_number()
    check_even_odd(random_number)

# Instantiate the DAG
taskflow()
