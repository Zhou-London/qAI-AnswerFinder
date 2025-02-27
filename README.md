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

-   src/
    -   configure/
        -   configuration of external things
    -   middleware/
        -   implementation of middleware
    -   models/
        -   Response models of FastAPI
    -   routes/
        -   implementation of routes
    -   sample/
        -   test data for YOLO
    -   servies/
        -   business logic
    -   main.py
    -   test.py
-   static/
    -   flutter files

env_format.txt

requirements.txt

README.md

## Set up on your device

Create an "**.env**" in the root, following the **env_format.txt**.

    touch .env

Pip install the requirements.txt and brew install manticore search.

    brew install manticoresearch

    brew services start manticoresearch

Get your manticore search host and fill it in your **.env**

    MANTICORE_HOST=...

Next, go to openai platform, get your secret key and fill it into **.env**

    SECRET_KEY=...

Then, since you have all the dependencies of YOLO, train your own YOLO, at configure/yolo_train.py. Run this file from root directory after modifying the output path in the .**env** to be the absolute path of "src/configure/yolo_output"

    YOLO_OUT=...

Finally and ideally, you can set your YOLO_PATH as the following. If this doesn't work, figure it out on your own where your model is.

    YOLO_PATH=src/configure/yolo_output/qAI/weights/best.pt

To check if everything goes well, run the server, go to "/" page and you shall see a doctor.



## Connect to manticore

Use the following command:

    mysql -h0 -P9306

Create Table sample code:

    create table products(title text, price float) morphology='stem_en';

Search data sample code:

    select id, highlight(), price from products where match('remove hair');
