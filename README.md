# scalable-ecommerce-platform
This project is a scalable e-commerce platform built using Django REST Framework and PostgreSQL, designed to handle complex queries and asynchronous tasks. It will be deployed on AWS Elastic Beanstalk.

## Roadmap

1. **Phase 1: Project Initialization**
   - Set up the repository and environment.
   - Initialize the Django project with basic settings.

2. **Phase 2: User Authentication**
   - Implement user registration, login, and logout functionality using JWT.
   - Test authentication endpoints.

3. **Phase 3: Product Catalog**
   - Build models for products and categories.
   - Develop APIs for CRUD operations.
   - Implement search and filtering features.

4. **Phase 4: Cart and Orders**
   - Create models for cart, cart items, and orders.
   - Build APIs for managing carts and placing orders.

5. **Phase 5: Deployment on AWS**
   - Deploy the application on AWS Elastic Beanstalk.
   - Set up PostgreSQL using AWS RDS.

6. **Phase 6: Additional Features**
   - Integrate Celery for task queues (e.g., email notifications).
   - Use Redis for caching.

7. **Phase 7: Final Showcase**
   - Polish the project with detailed documentation and examples.
   - Add tests and optimize for scalability.

---

## Architecture Diagram

Below is the high-level architecture of the Scalable E-Commerce Platform:

![Architecture Diagram](Public/architecture-diagram.png)


---

## Authentication Features

The application uses JWT for secure authentication. Below are the endpoints:

1. **Register a User:**
   - **Endpoint:** `/api/auth/register/`
   - **Method:** POST
   - **Request Body:**
     ```json
     {
       "username": "testuser",
       "email": "test@example.com",
       "password": "testpassword"
     }
     ```
   - **Response:**
     ```json
     {
       "id": 1,
       "username": "testuser",
       "email": "test@example.com"
     }
     ```

2. **Login:**
   - **Endpoint:** `/api/auth/login/`
   - **Method:** POST
   - **Request Body:**
     ```json
     {
       "username": "testuser",
       "password": "testpassword"
     }
     ```
   - **Response:**
     ```json
     {
       "access": "jwt_access_token",
       "refresh": "jwt_refresh_token"
     }
     ```

3. **Refresh Token:**
   - **Endpoint:** `/api/auth/token/refresh/`
   - **Method:** POST
   - **Request Body:**
     ```json
     {
       "refresh": "jwt_refresh_token"
     }
     ```
   - **Response:**
     ```json
     {
       "access": "new_jwt_access_token"
     }
     ```
