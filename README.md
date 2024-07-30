# Flask Application with PostgreSQL in Kubernetes

This project is a Flask web application with a PostgreSQL database, deployed using Kubernetes. The application allows users to add and view meals.

## Table of Contents

- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Testing the Aplication](#testing-the-application)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.6+
- Docker
- Kubernetes (Minikube or a Kubernetes cluster)
- kubectl
- pip

## Project Structure

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── templates
│ ├── add_meal_form.html
│ └── meals.html
├── deploy.yaml
├── tests
│ └── test_app.py
├── init-db-config.yaml
├── pytest.ini
└── .gitignore

```

## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add the following:

    ```plaintext
    DATABASE_URL=postgresql://flaskuser:flaskpass@postgres:5432/flaskdb
    ```

## Running the Application

1. **Initialize the database:**

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

2. **Run the Flask application:**

    ```bash
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Testing the Application

1. **Set up environment variables for testing:**

    Create a `pytest.ini` file in the root directory of the project and add the following:

    ```ini
    [pytest]
    env =
        DATABASE_URL=postgresql://testuser:testpass@localhost:5432/testdb
    ```

2. **Run tests locally:**

    Ensure you have a PostgreSQL server running locally (or use Docker to start one), then run:

    ```bash
    pytest
    ```

3. **Run tests in GitHub Actions:**

    Tests are configured to run automatically in GitHub Actions with a PostgreSQL server

## Kubernetes Deployment

1. **Start Minikube (if using Minikube):**

    ```bash
    minikube start
    ```

2. **Apply Kubernetes configurations:**

    ```bash
    kubectl apply -f init-db-config.yaml
    kubectl apply -f deploy.yaml
    ```

3. **Check the status of the deployment:**

    ```bash
    kubectl rollout status deployment flask-app
    ```

4. **Access the Flask application:**

    For Minikube, you can access the application using the service's NodePort. Get the URL with:

    ```bash
    minikube service flask-app --url
    ```

## Environment Variables

- `DATABASE_URL`: The connection URL for the PostgreSQL database.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
