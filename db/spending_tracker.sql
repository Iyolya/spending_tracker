CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tags(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    tag_id REFERENCES tags(id),
    merchant_id REFERENCES merchants(id),
    amount INT

);