# Project_Nexus
Project_Nexus
==============

📌 Project Overview: "Task Manager App"
A simple Task Manager that allows users to:
✅ Add tasks
✅ View tasks
✅ Delete tasks
📌 Tech Stack
🔹 Backend: Flask (Python)
🔹 Frontend: HTML, CSS, JavaScript (Flask Templates)
🔹 Database: PostgreSQL (AWS RDS)
🔹 Deployment: AWS Elastic Beanstalk or EC2

# Project DevOps Nexus: Automated CI/CD Pipeline for Kubernetes-based Application Deployment

## 📌 Project Overview

**DevOps Nexus** is a capstone project that demonstrates the end-to-end implementation of DevOps practices using industry-standard tools. The project automates the build, test, and deployment process for a Flask-based Task Manager application and deploys it on a Kubernetes cluster, with observability integrated using Prometheus and Grafana.

---

## ⚙️ Tech Stack

| Area            | Tool/Technology         |
|-----------------|-------------------------|
| Application     | Python Flask, HTML, JS  |
| Version Control | Git + GitHub            |
| Containerization| Docker                  |
| IaC             | Terraform (AWS)         |
| CI/CD           | Jenkins                 |
| Orchestration   | Kubernetes (EKS)        |
| Monitoring      | Prometheus, Grafana     |
| Cloud Provider  | AWS (RDS, EKS, EC2)     |

---

## 📁 Folder Structure

/project-root │ ├── app.py ├── templates/ │ └── index.html ├── Dockerfile ├── Jenkinsfile ├── terraform/ │ ├── main.tf │ ├── variables.tf │ ├── terraform.tfvars │ └── output.tf ├── k8s/ │ └── deployment.yaml └── README.md



---

## 🚀 Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/devops-nexus.git
cd devops-nexus
Step 2: Application Development
Build a basic Flask application with endpoints for creating and viewing tasks.

Use a PostgreSQL database (hosted on AWS RDS).

Create a simple frontend using HTML and JavaScript.

Validate your API using unit tests.

Step 3: Dockerization
Build a Docker image of the Flask app.

Example:

dockerfile

FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
Step 4: Infrastructure with Terraform
Provision AWS resources like VPC, Subnets, RDS, and EKS using Terraform.

Example command:


terraform init
terraform plan
terraform apply
Step 5: CI/CD Pipeline (Jenkins)
Configure Jenkins pipeline with stages for Source, Build, Test, and Deploy.

Use Docker and kubectl within the Jenkins pipeline to deploy to EKS.

Step 6: Kubernetes Deployment
Deploy the app using deployment.yaml.

Expose it via LoadBalancer service.

Use kubectl apply -f deployment.yaml.

Step 7: Monitoring with Prometheus & Grafana
Deploy Prometheus and Grafana via Helm or manifests.

Connect Prometheus as a data source in Grafana.

Create dashboards to monitor app and cluster metrics.

🎯 Learning Objectives
Understand real-world application of CI/CD in Kubernetes environments.

Learn how to use Terraform for Infrastructure as Code on AWS.

Build a fully automated DevOps pipeline integrating Git, Jenkins, Docker, and Kubernetes.

Gain hands-on experience in observability with Prometheus and Grafana.

🧪 Testing
Use unittest or pytest to validate the Flask API.

Run tests as part of your Jenkins pipeline.

📝 Final Notes
This project is built for learning-by-doing. If you're preparing for interviews at companies like EY or RBC, this end-to-end DevOps solution will give you practical talking points and experience with tools companies expect engineers to know.

“Understand the process, don’t just follow instructions.”

👨‍💻 Author
Shiron Kurian
Capstone Project – 2025
LinkedIn: [Your LinkedIn]
GitHub: [Your GitHub Profile]



---

Would you like me to export this as a `.md` file for your GitHub repo or documentation folder?