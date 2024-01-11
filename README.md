# Project Repository

This repository contains the codebase for a system with multiple components. Below is an overview of the project structure:

## Components

### 1. Frontend

The frontend is an Angular application serving as the entry point to the system.

- Directory: `frontend/`

### 2. API Gateway

The API Gateway is built using Flask and forwards traffic to the backend.

- Directory: `apiGateway/`

### 3. Backend

The backend is developed in Django and produces messages to RabbitMQ.

- Directory: `backend/`

### 4. Crawler

The crawler component consumes messages and produces messages to the extractor.

- Directory: `crawler/`

### 5. Extractor

- Directory: `extractor/`


