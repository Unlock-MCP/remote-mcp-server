# Remote MCP Database Server

A production-ready Model Context Protocol (MCP) server that provides AI applications with secure access to a PostgreSQL database over HTTP. This server demonstrates how to build enterprise-grade MCP integrations that can be deployed to the cloud and accessed by multiple clients.

## Features

- **Remote Access**: Uses Streamable HTTP transport for network accessibility
- **Database Integration**: Connects to hosted PostgreSQL databases (Neon, Supabase, etc.)
- **Security**: Environment-based credential management with HTTPS support
- **Production Ready**: Designed for cloud deployment with proper error handling
- **Enterprise Focused**: Scalable architecture suitable for team and organizational use

## Quick Start

### Prerequisites

- Python 3.10+
- A hosted PostgreSQL database (free tier from [Neon](https://neon.tech) or [Supabase](https://supabase.com))
- uv (recommended) or pip

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Unlock-MCP/remote-mcp-server
cd remote-mcp-server
```

2. Set up your environment:
```bash
# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv add "mcp[cli]" fastapi uvicorn psycopg2-binary python-dotenv
```

3. Configure your database:
```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your PostgreSQL connection string
# DATABASE_URL="postgresql://user:password@host:port/dbname"
```

4. Set up your database schema:
```bash
# This script connects to your remote DB and runs the setup SQL
python setup_db.py

5. Run the server:
```bash
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

Your MCP server is now running at `http://localhost:8000/mcp`

## Testing

Test your server with the MCP Inspector:

```bash
npx @modelcontextprotocol/inspector http://localhost:8000/mcp
```

## Deployment

This server is designed for cloud deployment. Popular options include:

- **Render**: Easy Python app deployment with database integration
- **Vercel**: Serverless deployment with environment variable support  
- **Cloudflare Workers**: Global edge deployment
- **AWS/GCP/Azure**: Full-featured cloud platforms

### Environment Variables

Set the following environment variable in your deployment platform:

- `DATABASE_URL`: Your PostgreSQL connection string

## API Reference

### Resources

- **`db://schema`**: Returns the database schema for the products table

### Tools

- **`query_database`**: Executes read-only SQL queries against the products database
  - **Input**: `sql_query` (string) - A SELECT statement
  - **Output**: JSON array of results
  - **Security**: Only SELECT statements are permitted

### Example Usage

```sql
-- Get all electronics products
SELECT * FROM products WHERE category = 'Electronics';

-- Find products under $100
SELECT name, price FROM products WHERE price < 100;

-- Get inventory summary by category  
SELECT category, COUNT(*) as product_count, SUM(stock) as total_stock 
FROM products 
GROUP BY category;
```

### Vercel Deployment

This repository includes a `vercel.json` file for easy deployment to [Vercel](https://vercel.com).

1.  Create a new project on Vercel and link your GitHub repository.
2.  In the Vercel project settings, go to the "Environment Variables" section.
3.  Add a **Secret** named `database_url` and set its value to your PostgreSQL connection string. The `vercel.json` file will automatically use this secret for the `DATABASE_URL` environment variable during deployment.

## Architecture

This server uses:

- **FastMCP**: Simplified MCP server framework for Python
- **FastAPI**: Modern web framework for the HTTP layer
- **PostgreSQL**: Robust relational database
- **Streamable HTTP**: MCP transport for remote access
- **JSON-RPC 2.0**: Underlying protocol for MCP communication

## Security Considerations

- Environment variables for credential management
- HTTPS enforcement in production
- Read-only database access by default
- Input validation and SQL injection prevention
- OAuth 2.1 authentication framework support (extensible)

- **Query Safegaurds**: The server currently allows any `SELECT` query. For high-security production systems, consider implementing a more robust query parser, using an Object-Relational Mapper (ORM) like SQLAlchemy to construct queries programmatically, or exposing only specific, parameterized functions instead of raw SQL execution.

## Related Resources

- **Tutorial**: [How to Build a Remote MCP Server](https://unlockmcp.com/guides/how-to-build-a-remote-mcp-server) - Complete step-by-step guide
- **MCP Documentation**: [Model Context Protocol](https://modelcontextprotocol.io)
- **Local MCP Example**: [MCP Docs Server](https://github.com/Unlock-MCP/mcp-docs-server) - Local filesystem MCP server

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- **Issues**: Report bugs and request features via GitHub Issues
- **Community**: Join the MCP community discussions
- **Documentation**: Visit [UnlockMCP.com](https://unlockmcp.com) for guides and tutorials