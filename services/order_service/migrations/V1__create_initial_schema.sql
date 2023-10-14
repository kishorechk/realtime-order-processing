CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    price FLOAT NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending' NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE
);

CREATE INDEX idx_product_name ON orders(product_name);

