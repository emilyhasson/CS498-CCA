import boto3
import json
from collections import deque
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mp3')

def bfs(graph, start):
    visited = {vertex: None for vertex in graph}
    distance = {vertex: float('infinity') for vertex in graph}
    queue = deque([start])
    distance[start] = 0
    
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if distance[neighbor] == float('infinity'):
                distance[neighbor] = distance[vertex] + 1
                visited[neighbor] = vertex
                queue.append(neighbor)
    return distance

def lambda_handler(event, context):
    logger.info('Received event: ' + json.dumps(event))
    # Directly use the event to get the graph data
    graph_input = event.get('graph')
    if not graph_input:
        logger.error("Graph data is missing in the event")
        return {'statusCode': 400, 'body': json.dumps("Bad Request: Missing 'graph' data")}

    # Log the received input
    logger.info(f"Received graph input: {graph_input}")

    # Parse the graph from the event
    edges = [edge.split('->') for edge in graph_input.split(',')]

    # Construct the graph and ensure all vertices are accounted for
    graph = {}
    vertices = set()  # Track all unique vertices
    for source, destination in edges:
        vertices.add(source)
        vertices.add(destination)
        if source not in graph:
            graph[source] = []
        graph[source].append(destination)

    # Add missing vertices to the graph with no outgoing edges
    for vertex in vertices:
        if vertex not in graph:
            graph[vertex] = []

    # Compute shortest paths using BFS for all vertices
    for start in vertices:  # Iterate over all vertices
        distances = bfs(graph, start)
        for destination, distance in distances.items():
            if distance != float('infinity'):
                # Delete operation removed for clarity and because it's not specified as needed every time
                table.put_item(Item={'source': start, 'destination': destination, 'distance': distance})

    return {'statusCode': 200, 'body': json.dumps('Graph processed successfully')}
