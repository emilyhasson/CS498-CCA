import boto3
import json
from collections import deque

import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # You can adjust this to DEBUG or ERROR as needed


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
    # Assuming 'event' contains the POST request data
    body = event.get('body')
    
    # Log the received input
    logger.info(f"Received input: {body}")
    
    # Delete all items in the DynamoDB table
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(Key={'source': each['source'], 'destination': each['destination']})
    
    # Parse the graph from the event body
    body = json.loads(event['body'])
    graph_input = body['graph']
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
                table.put_item(Item={'source': start, 'destination': destination, 'distance': distance})
    
    return {'statusCode': 200, 'body': json.dumps('Graph processed successfully')}
