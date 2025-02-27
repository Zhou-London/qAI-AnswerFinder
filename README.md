# AI-Driven Question&Answer Platform

Tianzhe Dong, Zhouzhou Zhang

For now, a platform only for Android. We plan to make it cross-platform in the future.

## Frameworks

Frontend: Flutter
Backend API: FastAPI
Database: Manticore Search
LLM model: chatgpt-4o
Image processing model: YOLO, OCR

## Dependencies

First install the dependencies in **requirements.txt**.

- FastAPI 0.115.8
- Python 3.12.9
- Flutter with Dart
- openai (Python) 1.64.0
- Manticore Search 7.0.0
- YOLO
- PyTorch

## File System

qAI/

├── /src # Source code

│ ├── /config # Congigure File

│ │ └── database.py # DataBase connection

│ ├── /middleware # Middleware

│ │ ├── auth.py # Authentication middleware

│ │ └── logger.py # Logger middleware

│ ├── /models # Structure of model

│ │ └── response.py # Structure of API response

│ ├── /routes # Routes

│ │ ├── index.py # Index router

│ │ └── process.py # Process File router

│ ├── /utils # Utilities

│ │ └── None yet

│ └── main.py # FastAPI Application

├── /static # Frontend

│ ├── /css

│ │ └── style.css

│ ├── /js

│ │ └── app.js

│ └── /images # Image

│ └── logo.png

├── /tests # Testing

│ ├── /unit

│ │ └── test_routes.py

│ └── /integration

│ └── test_api.py

├── .env # Environment file

├── .gitignore # Ignored by Git

├── requirements.txt # Python Dependencies

└── README.md

## Connect to manticore

Use the following command:

    mysql -h0 -P9306

Create Table sample code:

    create table products(title text, price float) morphology='stem_en';

Search data sample code:

    select id, highlight(), price from products where match('remove hair');
