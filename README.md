# Deliver Images Function

This repository contains the code and deployment files for the Deliver Images function. The function generates images based on the provided payload and can be deployed as a Docker container, in Kubernetes, or on a serverless platform.

1. Sir, Please Modify the deliver_images.py file to implement the desired image generation logic.

2. I have already built the docker image and added it's tag in the DockerFile only, but if you want to build it again, just do the following
    ```shell
    docker build -t deliver-images-function .

3. Run the Docker container:
    ```shell 
    docker run -d --name deliver-images-container deliver-images-function

### Kubernetes Deployment

1. Apply the deployment configuration:
   ```shell
   kubectl apply -f deployment.yaml

2. Apply the service configuration:
   ```shell
   kubectl apply -f service.yaml

### Serverless Deployment


- To get started, create a new application on the platform on runpod.io

- Choose "Kubernetes Deployment" as the method for deploying your application.

- Upload two files, namely "deployment.yaml" and "service.yaml," to the platform. These files contain important information about your application.

- If there are any additional settings or parameters required by the platform, make sure to configure them accordingly.

- Initiate the deployment process and keep an eye on its progress.

- Once the deployment is finished, you'll receive a URL. This URL allows you to access your application and use it.


I just get to know all this from different places sir, this is how things can be achieved, I don't have your local machine :smile:.
Just let me know, if I can help in some other way

Thank you
