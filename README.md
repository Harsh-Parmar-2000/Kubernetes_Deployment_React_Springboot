# Deploying Spring Boot and React Applications with Docker and Kubernetes

This repository contains the code and instructions to deploy a Spring Boot backend application and a React frontend application using Docker containers and orchestrate them in Kubernetes with the help of Nginx. This project serves as a practical guide to gain hands-on experience with Kubernetes and Nginx.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed and configured on your system:

- **Docker**: Install [Docker](https://docs.docker.com/get-docker/) to containerize your applications.
- **Kubernetes**: Set up a Kubernetes cluster, you can use [Minikube](https://minikube.sigs.k8s.io/docs/start/) for a local development environment or a cloud provider like [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine) for a production-like setup.
- **kubectl**: Install [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) to interact with your Kubernetes cluster.
- **Nginx**: Ensure you have a basic understanding of Nginx for reverse proxy configuration.

## Project Structure

The project is organized into two main directories:

- **backend**: Contains the Spring Boot backend application.
- **frontend**: Contains the React frontend application.

## Building and Dockerizing the Applications

1. **Backend**:
   - Navigate to the `backend` directory.
   - Build the Spring Boot application using your preferred build tool (e.g., Maven or Gradle).
   - Create a Docker image for the Spring Boot application using a `Dockerfile` provided in the `backend` directory.

2. **Frontend**:
   - Navigate to the `frontend` directory.
   - Build the React application using `npm` or `yarn`.
   - Create a Docker image for the React application using a `Dockerfile` provided in the `frontend` directory.

## Deploying to Kubernetes without Helm

1. **Kubernetes Deployment**:
   - Create Kubernetes deployment configurations (e.g., YAML files) for both the Spring Boot backend and React frontend applications. Example deployment files are located in the `kubernetes` directory.

2. **Service Configuration**:
   - Define Kubernetes Services to expose your applications within the cluster. Ensure that services are correctly configured to allow communication between frontend and backend.

3. **Nginx Configuration**:
   - Configure Nginx as a reverse proxy to route requests to the appropriate services.
   - Create a Kubernetes ConfigMap for Nginx configuration and mount it to your Nginx pods.

## Accessing the Applications

Once deployed, you can access the applications as follows:

- Spring Boot Backend: Access the backend API at `http://backend-service-host:backend-service-port`.

- React Frontend: Access the frontend application at `http://frontend-service-host:frontend-service-port`.

## Contributing

If you'd like to contribute to this project or make improvements, please fork the repository, make your changes, and submit a pull request.

## Acknowledgments

- Thank you to the Spring Boot and React communities for their excellent documentation and support.
- Special thanks to the Kubernetes and Nginx teams for their powerful tools and resources.
- Contributors and open-source maintainers who make projects like this possible.

Happy coding and Kubernetes orchestration!
