# CI/CD Pipeline for Cars_for_sale Flask Application
### Overview:
This project aims to create a continuous integration and continuous deployment (CI/CD) pipeline for a Python application built using Flask, named Cars_for_sale. The application stores all its data in a JSON file.

#### Key Features and Functionalities

- Jenkins-based CI/CD pipeline

- Containerization using Docker

- Jenkins client installed in local Docker container

- Docker-in-Docker container for running Docker commands from Jenkins pipeline

- Jenkins pipeline runs tests for Flask application

- Image building using Dockerfile

- Deployment to Dockerhub after build stage

- Jenkins auto-build using webhook smee

#### Target Audience
Developers seeking to automate build, test, and deployment processes for their Flask applications.

Technologies and Tools Used:

- Python
- Flask
- Docker
- DockerHub
- Jenkins
- Git
- Webhook smee

#### Cars_for_sale Application
The "Cars_for_sale" application is a Python RESTful API built using Flask that allows you to perform CRUD (Create, Read, Update, Delete) operations on a list of cars.

Endpoints:

- GET /cars: Retrieves the entire list of cars.
- GET /cars/:car_id: Retrieves a specific car by ID.
- POST /cars: Adds a new car to the list.
- DELETE /cars/:car_id: Deletes a specific car by ID.

#### Jenkins and Docker in Docker Setup
This setup allows you to run Jenkins, a popular CI/CD tool, within a Docker container, along with a Docker-in-Docker container that acts as a Docker daemon. This enables a self-contained CI/CD environment that can be easily deployed and managed.

Components

- Docker: The containerization platform used to run the Jenkins and Docker-in-Docker containers.
- Jenkins: The CI/CD tool that will be running within a Docker container.
- Docker-in-Docker: A Docker container that runs a Docker daemon, allowing Jenkins to run - - - Docker agents and pipelines.

Setup Steps

1. Create a Docker network for Jenkins and the Docker-in-Docker container.
2. Run a Docker-in-Docker container with the docker:dind image, which will act as a Docker daemon.
3. Test the Docker-in-Docker container by running a Python container within it.
4. Create a new Jenkins image that includes the Docker CLI tool.
5. Run a Jenkins controller container that uses the Docker-in-Docker container as an agent.
6. Test the Jenkins container by running various Docker commands and connecting to the Jenkins GUI.

Benefits

- Self-contained CI/CD environment that can be easily deployed and managed.
- Jenkins can run Docker agents and pipelines within a Docker container.
- Easy to scale and manage resources.

#### Docker Image: cars_image
- Based on Python 3.12 Alpine
- Includes files for a cars database application
- Installs required packages using pip
- Sets default command to run main application file

This image provides a basic setup for a cars database application, with the necessary files and dependencies installed.

#### Jenkins Pipeline
- Pre-Build: Stops and removes running containers (if any)
- Test: Builds image, runs container, executes tests, stops and removes container
- Build: Builds new image
- Deploy: Pushes new image to registry

In summary, this pipeline automates the process of building, testing, and deploying a Docker image, ensuring that changes made to the codebase are properly tested and deployed to production.

#### Webhook in Jenkins

- Go to the "Configure" page for your project.
- Select "Webhook" in the "Build Triggers" section.
- Enter the URL of your Git repository's webhook endpoint.
- Enter a secret token for authentication.

This will enable Jenkins to automatically build your project when changes are pushed to your Git repository.
