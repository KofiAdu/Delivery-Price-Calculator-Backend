#  Delivery Fee Calculator API

This project is a Django-based HTTP API for calculating delivery fees based on cart value, delivery distance, number of items, and order time.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

## Features

- Calculate delivery fees based on specified parameters.
- Handles small order surcharge, distance fees, item surcharge, bulk fees, and rush hour multiplier.
- Django admin interface for managing orders.

## Prerequisites

Make sure you have the following installed before proceeding:

- Python 3.x
- Pip (Python package installer)

## Installation

1. Main folder; WOLTBACKENDASSIGNMENT
2. Create a virtual environment (optional but recommended):
   ~~~ 
       python -m venv .venv 
   ~~~
3. Activate the virtual environment:
    i. On Windows: 
    ~~~ 
       .\.venv\Scripts\activate
     ~~~
    
    ii. On macOS/Linux:
     ~~~ 
        source .venv/bin/activate
     ~~~
4. Install dependencies:
    ~~~
       pip install -r requirements.txt
    ~~~
5. Apply database migrations:
    ~~~
       python manage.py migrate
    ~~~
6. Run the development server in the main folder (WOLTBACKENDASSIGNMENT):
    ~~~
       python manage.py runserver
    ~~~

## Usage

Use the API by sending a POST request to the `/api/calculate_delivery_fee/` endpoint
with the required parameters in the request payload. Refer to the API Endpoints section for details.

## API Endpoints

POST `/api/calculate_delivery_fee/`: Calculate delivery fee based on cart value, delivery distance, number of items, and order time.

Example Request:
{
    "cart_value": 790,
    "delivery_distance": 2235, 
    "number_of_items": 4, 
    "time": "2024-01-15T13:00:00Z"
}

Example Response: 
{"delivery_fee": 710}

## Testing
~~~
   python manage.py test
~~~


