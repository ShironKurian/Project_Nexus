# 🚀 Task Manager Web Application | Capstone Project

This project is a fully containerized and Kubernetes-deployed **Task Manager Web Application** built with Flask, integrated with PostgreSQL, and monitored using Prometheus and Grafana. The entire workflow is automated through a CI/CD pipeline implemented in **Jenkins**, making the deployment process seamless and production-ready.

---

## 🧠 Project Overview

This web application allows users to manage tasks with functionalities such as:
- Creating a task
- Viewing tasks
- Updating task status
- Deleting tasks

The application is designed with **microservices principles**, and it's deployed to an AWS EKS cluster with monitoring and alerting set up.

---

## 🛠️ Tech Stack

| Layer               | Tools Used                                           |
|--------------------|------------------------------------------------------|
| Application Layer   | Python, Flask                                        |
| Database            | PostgreSQL (hosted on RDS/local)                    |
| Containerization    | Docker                                               |
| CI/CD Pipeline      | Jenkins, GitHub, AWS ECR, AWS EKS                   |
| Orchestration       | Kubernetes (EKS)                                     |
| Monitoring          | Prometheus, Grafana                                  |
| Infrastructure as Code | Terraform (optional module)                      |

---

## ⚙️ Project Architecture

[ GitHub ] │ ▼ [ Jenkins (CI/CD) ] ├── Checkout code ├── Run Unit Tests (pytest) ├── Docker Build & Push to ECR └── Deploy to EKS │ ▼ [ AWS EKS Cluster ] │ └── Flask App (Pods + Service) │ ▼ [ LoadBalancer + External URL ] │ ▼ [ Prometheus & Grafana Monitoring ]



---

## 🔁 CI/CD Pipeline (Jenkins)

The Jenkins pipeline consists of the following stages:

1. **Checkout Code** – Pulls source code from GitHub repo.
2. **Build Docker Image** – Builds the Flask app Docker image.
3. **Run Unit Tests** – Executes tests using `pytest`.
4. **Login to ECR** – Authenticates with AWS Elastic Container Registry.
5. **Push to ECR** – Pushes the built image.
6. **Deploy to EKS** – Applies the Kubernetes deployment using `kubectl`.

> ✅ Jenkins triggers the entire pipeline on every code push to `main`.

---

## 🐳 Docker

Build your image locally (optional):

```bash
docker build -t task-master .
Push to ECR manually (if needed):


docker tag task-master:latest <your-ECR-URI>
docker push <your-ECR-URI>
☸️ Kubernetes (EKS)
Deploy your application:


aws eks update-kubeconfig --region us-east-1 --name task-manager-cluster
kubectl apply -f deployment.yaml
Check the status:


kubectl get pods
kubectl get svc
📊 Monitoring with Prometheus and Grafana
Installed via Helm:


helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
Access Grafana UI:


kubectl get svc -n monitoring
Copy the EXTERNAL-IP for Grafana and open it in the browser.

Default Credentials:

Username: admin

Password: prom-operator

📂 Directory Structure

Capestone_2025/
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── deployment.yaml
├── templates/
├── static/
├── tests/
│   └── test_app.py
└── terraform/ (optional)

✅ Achievements
✔️ CI/CD pipeline fully automated with Jenkins

✔️ Dockerized Flask application

✔️ Deployed to EKS with zero downtime

✔️ Real-time metrics using Prometheus and Grafana

✔️ Scalable and production-ready architecture

🌱 Future Enhancements

Add user authentication and role-based access

Integrate with RDS and S3 for production database and file storage

Setup alerting in Grafana

🙋‍♂️ Author
Shiron Kurian
GitHub: https://github.com/ShironKurian/Project_Nexus.git  | Email : shironkurian@gmail.com| [Location: Kitchener, ON, Canada]