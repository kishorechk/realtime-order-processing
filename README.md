# Real-time Order Processing System
Overview:
Imagine an e-commerce platform where users place orders for products. These orders are processed in real-time, and various services are invoked to handle different aspects of the order lifecycle. [Checkout my blog post for more info](https://medium.com/@kishorchukka/introduction-f345491b1eb4)

![order-processing-hld](https://github.com/kishorechk/realtime-order-processing/assets/678734/ba3a423d-7e03-4a42-aaf9-02da184af474)


## Components

* **Order Service**: Accepts orders from users and sends them to a Kafka topic.
* **Inventory Service**: Listens to the Kafka topic for new orders, checks the inventory for product availability, and updates the inventory count.

## Technologies
* **Poetry**: Simplified our project management, ensuring consistent dependencies and a smooth development experience.
* **FastAPI**: Emerged as the hero for crafting efficient and robust web services. Its automatic OpenAPI documentation feature was a boon, providing clarity and interactivity to our API endpoints.
* **SQLAlchemy**: Enabled seamless interactions with our database, allowing us to model, query, and manage our data with ease.
* **Kafka**: Integrated seamlessly into our Python services, ensuring real-time event streaming and facilitating communication between our order and inventory services.
* **Docker**: Ensured consistent development, testing, and deployment, encapsulating our services and their dependencies into isolated containers.
