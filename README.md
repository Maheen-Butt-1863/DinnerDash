# DinnerDash

## Overview
This project is a Resturant App, a pure Django-based web application where users can place their ordes,view their order details and view past orders.Admin can add,remove categories and items and view orders and edit them.

## Features

### Authentication
- **Sign Up and Login:**
  - Users can sign up and log in to the application.
  - Users can log out of the application.
  - 
- **User Profile:**
  - Users must provide a name,email, username during sign-up.

### Home Page
- **Home view:**
  - Users can view all items on home and various other option as cart and orders.

- **Search Functionality:**
  - Users can search food items on base of category.

### Cart page
- **Cart Creation:**
  - Users can add multiple items to their cart.
- **Cart Editing:**
  - Users can view their cart
  - Users can edit their cart by adding or removing items from the cart
    
### Order Page
- **Order View:**
  - Users can view his/her past orders and thier details.
  - Users can view item details from their order detail.
  - Admin can view all the order placed.
  - Admin can change the status of the orders.
    
### Item Page
  - Admin can add and Item
  - Admin can edit and exsisting Item.
  

## Technical Considerations

- **Django Application:**
  - This is a pure Django-based application.

- **Dockerization:**
  - Docker containers are used for the deployment of the application.

- **Database:**
  - PostgreSQL is used as the primary database system.

- **Image Storage:**
  - Images are stored on [Cloudinary](https://cloudinary.com/).

## Getting Started

### Prerequisites
- Make sure you have Docker installed on your machine. If not, you can download it [here](https://www.docker.com/get-started).
- Ensure you have Python installed. You can download it [here](https://www.python.org/downloads/).

### Setup

#### Dockerized Environment
1. Clone the repository:
    ```bash
    git clone https://github.com/Maheen-Butt-1863/DinnerDash
    cd DinnerDash
    ```

2. Build the Docker image:
    ```bash
    docker build -t resturant .
    ```

3. Run the Docker container:
    ```bash
    docker run -p 8000:8000 resturant
    ```

4. The Django application should now be accessible at `http://localhost:8000`.

#### Non-Dockerized Environment
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-quora-clone.git
    cd your-quora-clone
    ```

2. Create and activate a virtual environment:
    ```bash
    pipenv shell
    ```

3. Install dependencies:
    ```bash
    pipenv install
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

6. The Django application should now be accessible at `http://localhost:8000`.

### Running Tests (not implemented yet)
To run tests, use the following command:
```bash
python manage.py test
```
