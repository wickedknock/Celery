## Handle heavy AI tasks in the backgorund asynchronously

This project uses the following technologies:
- FastAPI
- Celery
- Redis



## Problem Statement

Our AI microservice is taking to long to handle the tasks , which is bad foruser experience , We want to create a system 
where user can come and give a task and recieve its Id and status , this task will run in the backgroudn and the user can 
check the status in realtime to let them know if thier task is finished instead of waiting.


## Solution

We are going to use celery which can use redis or rabbitmq as a broker and provide asyncrhous task management.
Celery keeps status of our tasks and also changes it after completion , it also have failure retries and its workers can
horizontally scale and provide processing concurrently.We will use Redis as the broker and Flower for realtime task dashboard

## How to use project

# Docker-Compose
- run docker compose up --build


