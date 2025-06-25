# server.py
import os
import json
import psycopg2
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from decimal import Decimal
from fastapi import FastAPI

# Load environment variables from the .env file
load_dotenv()

# Initialize a stateless HTTP server. 'stateless_http=True' is crucial
# as it tells FastMCP not to manage sessions, leaving it to our web framework.
mcp = FastMCP(
    name="CompanyDB_Postgres_Server",
    description="Provides access to the company product database.",
    stateless_http=True
)

DATABASE_URL = os.getenv("DATABASE_URL")

# Helper function to handle Decimal serialization in JSON
def json_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

# Define a RESOURCE to expose the database schema
@mcp.resource("db://schema", title="Database Schema")
def get_schema() -> str:
    """Provides the database schema for the 'products' table as a string."""
    # For a real application, you would query the information_schema.
    # For this guide, we'll return a static DDL string for simplicity.
    return """
    CREATE TABLE products (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT,
        price NUMERIC(10, 2),
        stock INTEGER
    );
    """

# Define a TOOL for running read-only queries
@mcp.tool(title="Query Products DB")
def query_database(sql_query: str) -> str:
    """
    Executes a read-only SQL query against the products database.
    Only SELECT statements are permitted for security.
    """
    if not sql_query.strip().upper().startswith("SELECT"):
        return json.dumps({"error": "Security violation: Only SELECT queries are allowed."})

    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute(sql_query)

        column_names = [desc[0] for desc in cur.description]
        results = [dict(zip(column_names, row)) for row in cur.fetchall()]

        cur.close()
        # Format as a JSON string for clear, structured output
        return json.dumps(results, indent=2, default=json_default)
    except (Exception, psycopg2.DatabaseError) as error:
        return json.dumps({"error": str(error)})
    finally:
        if conn is not None:
            conn.close()

# Create a FastAPI application instance
app = FastAPI(
    title="UnlockMCP Remote Database Server",
    description="An MCP server providing access to a company database, exposed via HTTP."
)

# Mount the MCP server's HTTP application to a path.
# All MCP communication will happen through this endpoint (e.g., /mcp).
app.mount("/mcp", mcp.streamable_http_app())

# Add a root endpoint for health checks or basic info
@app.get("/")
def read_root():
    return {"message": "MCP Database Server is running. Access MCP at /mcp"}

# Health check endpoint for deployment platforms
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "remote-mcp-server"}