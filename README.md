# holbertonschool-softy-pinko-docker
Softy Pinko Docker Project
This project demonstrates how to containerize and run a full web application using Docker and Docker Compose.
It includes a front-end static website, a Flask back-end API, an Nginx proxy server, and horizontal scaling for the API service.

Project Structure

* task1: Basic back-end API server using Flask.
* task2: Front-end static website served with Nginx.
* task3: Connects the front-end with the back-end API.
* task4: Uses Docker Compose to run the front-end and back-end together.
* task5: Adds an Nginx proxy server to route traffic to the correct service.
* task6: Scales the back-end service horizontally using Docker Compose.

Technologies Used

* Docker
* Docker Compose
* Nginx
* Flask
* Flask-CORS
* HTML, CSS, JavaScript
* jQuery AJAX

How It Works

The application is split into multiple services:

* Front-end: Serves the Softy Pinko static website using Nginx.
* Back-end: Provides a Flask API endpoint at /api/hello.
* Proxy: Uses Nginx to route requests:
    * / routes to the front-end service.
    * /api routes to the back-end service.

In the final task, the back-end service can be scaled to multiple containers using Docker Compose. Nginx automatically load-balances requests between the running back-end containers.

Running the Application

To build the services:

docker-compose build

To start the application:

docker-compose up

Then open the application in the browser:

http://localhost

Scaling the Back-end

To run two back-end API servers:

docker-compose up --scale back-end=2

This allows the proxy server to distribute API requests between multiple back-end containers using round-robin load balancing.

API Endpoint

GET /api/hello

Response:

Hello, World!

Author:
Munirahenad
