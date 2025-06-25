-- Database Setup for Remote MCP Server
-- Run this SQL against your PostgreSQL database

-- Create the products table
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price NUMERIC(10, 2),
    stock INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO products (name, category, price, stock) VALUES
  ('Laptop Pro', 'Electronics', 1499.99, 50),
  ('Smart Watch', 'Electronics', 299.50, 120),
  ('Office Chair', 'Furniture', 175.00, 80),
  ('Project Planner', 'Office Supplies', 25.99, 200),
  ('Wireless Headphones', 'Electronics', 249.99, 85),
  ('Standing Desk', 'Furniture', 599.00, 25),
  ('Mechanical Keyboard', 'Electronics', 129.99, 60),
  ('Ergonomic Mouse', 'Electronics', 79.99, 90)
ON CONFLICT DO NOTHING;

-- Create an index for faster category queries
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);

-- Create an index for price range queries
CREATE INDEX IF NOT EXISTS idx_products_price ON products(price);

-- Verify the setup
SELECT 
    'Products table created successfully' as status,
    COUNT(*) as total_products,
    COUNT(DISTINCT category) as unique_categories
FROM products;