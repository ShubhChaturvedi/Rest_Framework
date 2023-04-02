# Django REST Framework Learning Project

This project was created to learn and explore the following concepts in Django:

- Django Rest Framework
- Generic Views
- JWT Tokens
- Token Authentication
- API Views
- Dockerizing a Django application via Dockerfile

## Requirements

- Python 3.x
- Django 3.x
- Django Rest Framework 3.x
- Docker

## Getting Started

To get started with this project, you should first clone the repository to your local machine:

git clone https://github.com/your-username/django-rest-framework-learning.git


### Setting up the Virtual Environment

It is recommended that you create a virtual environment to work on this project. To do so, navigate to the project directory and run the following commands:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


### Running the Server

Once you have installed the project dependencies, you can start the Django development server by running the following command:

python manage.py runserver



You should now be able to access the server at http://localhost:8000.

### API Endpoints

The following API endpoints are available:

- `/api/token/` - Obtain JWT token
- `/api/token/refresh/` - Refresh JWT token
- `/api/hello/` - Hello world view with token authentication
- `/api/snippets/` - List and create snippets (requires token authentication)
- `/api/snippets/<pk>/` - Retrieve, update, or delete a snippet (requires token authentication)

## Dockerizing the Application

To Dockerize this application, we have created a Dockerfile that specifies how the application should be built and run. To build the Docker image, navigate to the project directory and run the following command:

docker build -t django-rest-learning .


Once the image has been built, you can run a container using the following command:

docker run -p 8000:8000 django-rest-learning


You should now be able to access the server at http://localhost:8000.

## Conclusion

This project has provided an introduction to Django Rest Framework, JWT tokens, and Token Authentication. We have also learned how to use Docker to containerize our application. With this knowledge, you can now create your own RESTful APIs with Django and containerize them for easy deployment.
