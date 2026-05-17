# Zero-Touch Deployment Pipeline

This repository contains a foundational DevOps project demonstrating how to containerize a Python **FastAPI** application and automate its deployment to an **AWS EC2** instance using **GitHub Actions**.

## 🚀 Features
- **FastAPI Web Application**: A lightweight, high-performance web API built with Python.
- **Dockerization**: The application is containerized using Docker for consistent environments across development and production.
- **Continuous Integration & Continuous Deployment (CI/CD)**: Automated deployment pipeline built with GitHub Actions.
- **Zero-Touch Deployment**: Code pushed to the `main` branch is automatically built, pushed to Docker Hub, and deployed directly to an AWS EC2 instance without manual intervention.

## 🛠️ Technologies Used
- **Python 3.9+** & **FastAPI**
- **Docker** & **Docker Hub**
- **GitHub Actions**
- **AWS EC2** (Ubuntu Linux)

## 🏗️ Architecture & Workflow

1. **Push**: A developer pushes code changes to the `main` branch.
2. **Build**: GitHub Actions triggers a workflow that builds a new Docker image from the source code.
3. **Push to Registry**: The new Docker image is pushed to Docker Hub.
4. **Deploy**: GitHub Actions SSH's into the AWS EC2 instance, pulls the latest Docker image, stops the old container, and spins up the new one.

---

## 💻 Local Development

### Prerequisites
- Python 3.9+
- Docker (optional, but recommended)

### Running Locally (Without Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/zero-touch-deployment.git
   cd zero-touch-deployment
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
4. Open `http://localhost:8000` in your browser. You can view the API documentation at `http://localhost:8000/docs`.

### Running Locally (With Docker)

1. Build the Docker image:
   ```bash
   docker build -t fastapi-app .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 fastapi-app
   ```

---

## ⚙️ CI/CD Pipeline Configuration

To make the GitHub Actions deployment pipeline work, you must configure the following **Repository Secrets** in your GitHub repository (`Settings > Secrets and variables > Actions`):

| Secret Name | Description |
|---|---|
| `DOCKER_USERNAME` | Your Docker Hub username. |
| `DOCKER_PASSWORD` | Your Docker Hub password or Personal Access Token (PAT). |
| `HOST` | The public IP address or DNS of your AWS EC2 instance. |
| `USERNAME` | The SSH username for your EC2 instance (e.g., `ubuntu` or `ec2-user`). |
| `SSH_PRIVATE_KEY` | The private SSH key (`.pem` file contents) used to connect to your EC2 instance. |

Once these secrets are added, pushing code to the `main` branch will automatically trigger the deployment.
