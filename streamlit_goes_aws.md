
text
# Deploying a Streamlit App to AWS Elastic Beanstalk

To deploy a Streamlit app to AWS Elastic Beanstalk (EB), follow these steps:

## 1. Prepare Your Streamlit App

- Ensure your `app.py` file is in the root directory.
- Create a `requirements.txt` file listing all dependencies, including Streamlit.

## 2. Create a Dockerfile

Create a file named `Dockerfile` in the root directory with the following content:

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 3. Create a Dockerrun.aws.json File
Create a file named Dockerrun.aws.json in the root directory with the following content:
```json
{
  "AWSEBDockerrunVersion": "1",
  "Ports": [
    {
      "ContainerPort": "8501",
      "HostPort": "8501"
    }
  ]
}
```

## 4. Configure EB Environment
Choose Docker as the platform.
Upload your code as a zip file containing app.py, requirements.txt, Dockerfile, and Dockerrun.aws.json.
Under Configure more options, modify:
Instances: Set Root volume type to General Purpose (SSD) and size to at least 8GB.
Capacity: Change Instance type to t3.medium or larger.

## 5. Create and Deploy Your Application
Use the EB CLI or AWS Console to create and deploy your application.
EB will build and deploy your Docker container.

## 6. Configure Load Balancer
In your EB environment, go to Configuration > Load Balancer.
Add a listener for port 8501.
Set up a process for port 8501 forwarding to your instance.

## 7. Enable WebSockets
In the same Load Balancer configuration, enable sticky sessions.
Remember to properly secure your application and consider costs associated with running on AWS. Once deployed, you should be able to access your Streamlit app via the EB URL.
