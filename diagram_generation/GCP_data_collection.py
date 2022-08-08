from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub, Datalab
from diagrams.gcp.iot import IotCore
from diagrams.gcp.storage import GCS
from diagrams.onprem.analytics import Tableau
from diagrams.onprem.analytics import Powerbi


with Diagram("GCP Services Architecture", show=False):
    pubsub = PubSub("pubsub")

    with Cluster("Data Generation"):
        [IotCore("core1"),
         IotCore("core2"),
         IotCore("core3")] >> pubsub

    flow = Dataflow("data flow")

    with Cluster("Data Lake"):
        BQ = BigQuery("bq")
        flow >> [BQ,
                 GCS("storage")]

    with Cluster("Flow into any tool for data visualization"):
        tools = [Datalab("datalab"),
                 Powerbi("PowerBI"),
                 Tableau("Tableau")]

    pubsub >> flow
    BQ >> tools
