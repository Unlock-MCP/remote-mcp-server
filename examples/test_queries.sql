-- Example SQL queries for testing the MCP server
-- Use these with the MCP Inspector or any MCP client

-- Basic queries
SELECT * FROM products;

-- Filter by category
SELECT * FROM products WHERE category = 'Electronics';

-- Price range queries
SELECT name, price FROM products WHERE price BETWEEN 100 AND 300;

-- Aggregation queries
SELECT 
    category, 
    COUNT(*) as product_count,
    AVG(price) as avg_price,
    SUM(stock) as total_stock
FROM products 
GROUP BY category 
ORDER BY avg_price DESC;

-- Top expensive products
SELECT name, category, price 
FROM products 
ORDER BY price DESC 
LIMIT 5;

-- Low stock alerts
SELECT name, category, stock 
FROM products 
WHERE stock < 50 
ORDER BY stock ASC;

-- Search by name (case insensitive)
SELECT * FROM products 
WHERE LOWER(name) LIKE '%laptop%';

-- Products by category with stock status
SELECT 
    name,
    category,
    price,
    stock,
    CASE 
        WHEN stock > 100 THEN 'High Stock'
        WHEN stock > 50 THEN 'Medium Stock'
        ELSE 'Low Stock'
    END as stock_status
FROM products
ORDER BY category, stock DESC;