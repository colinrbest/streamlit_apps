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


with Diagram("Splunk_ETL", show=False):
    splunk = Splunk("Splunk")

    with Cluster("Code Management"):
        gitlab = Gitlab("Repository")

    with Cluster("Data Generation"):
        [IotCore("core1"),
         IotCore("core2"),
         IotCore("core3")] >> splunk

    with Cluster("Running in On Prem Linux Server"):
        with Cluster("VM"):
            python = Python(
                "Scheduled Chron\n rolling 1 min window")

        with Cluster("Hadoop"):
            HDFS = Hadoop("HDFS")

        with Cluster("Operational Platform"):
            client = Client("AI Platform")

    splunk >> python >> HDFS >> client
