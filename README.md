# Project Repository

This repository contains the codebase for a system with multiple components. Below is an overview of the project structure:

## Components

### 1. Frontend

The frontend is an Angular application serving as the entry point to the system.

- Directory: `frontend/`

### 2. API Gateway

The API Gateway is built using Flask and forwards traffic to the backend.

- Directory: `apiGateway/`

### 3. Site service

The Site Service is developed in Django and produces messages to RabbitMQ.

- Directory: `SiteService/`

### 4. Article service

The Site Service is developed in Django and produces messages to RabbitMQ.

- Directory: `ArticleService/`

### 5. Crawler

The crawler component consumes messages and produces messages to the extractor.

- Directory: `crawler/`

### 6. Extractor

- Directory: `extractor/`


