from typing import Optional

from fastapi import FastAPI

# Gremlin imports
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import __
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

app = FastAPI()

def invoke_gremlin_connection(self):
    graph = Graph()
    connection = DriverRemoteConnection('ws://localhost:8182/gremlin', 'g')
    # The connection should be closed on shut down to close open connections with connection.close()
    g = graph.traversal().withRemote(connection)
    # Reuse 'g' across the application

@app.get("/")
def read_root():
    self.invoke_gremlin_connection()
    return {"Hello": "World" }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q} 