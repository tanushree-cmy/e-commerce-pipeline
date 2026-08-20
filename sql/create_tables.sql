-- Table 1: Users
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(100),
    email VARCHAR(150),
    signup_date DATE
);

-- Table 2: Products
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(150),
    category VARCHAR(50),
    unit_price DECIMAL(10, 2)
);

-- Table 3: Orders (Fact Table)
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    total_amount DECIMAL(10, 2),
    order_date DATE
);
