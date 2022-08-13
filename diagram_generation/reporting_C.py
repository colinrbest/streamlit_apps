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
from diagrams.onprem.vcs import Gitlab
from diagrams.onprem.analytics import Hadoop
from diagrams.onprem.client import Client
from diagrams.onprem.database import Oracle
from diagrams.onprem.database import Postgresql


with Diagram("Reporting", show=False):

    oracle = Oracle("Database")
    powerbi = Powerbi()

    with Cluster("Code Management"):
        gitlab = Gitlab("Repository")

    with Cluster("Running in On Prem Linux Server"):
        with Cluster("VM"):
            python = Python(
                "Scheduled chron\n daily report")
        with Cluster("PostGresql DB"):
            postg = Postgresql()

    oracle >> python >> postg >> powerbi
