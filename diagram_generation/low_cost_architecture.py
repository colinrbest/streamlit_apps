from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub, Datalab
from diagrams.gcp.iot import IotCore
from diagrams.gcp.storage import GCS
from diagrams.onprem.analytics import Tableau
from diagrams.onprem.analytics import Powerbi
from diagrams.onprem.monitoring import Splunk
from diagrams.onprem.queue import Kafka
from diagrams.gcp.compute import ComputeEngine
from diagrams.programming.language import Python
from diagrams.onprem.workflow import Airflow


with Diagram("orchestrator_driven_ETL", show=False):
    splunk = Splunk("Splunk")

    with Cluster("Data Generation"):
        [IotCore("core1"),
         IotCore("core2"),
         IotCore("core3")] >> splunk

    with Cluster("Running on GCP"):
        with Cluster("VM"):
            airflow = Airflow("Airflow Orchestrator")
            python = Python()

        with Cluster("BigQuery"):
            BQ = BigQuery("BQ")

    splunk >> airflow >> python >> BQ
