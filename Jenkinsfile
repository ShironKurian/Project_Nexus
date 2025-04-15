pipeline {
    agent any

    environment {
        AWS_ACCOUNT_ID = '643716337997'
        AWS_REGION = 'us-east-1'
        ECR_REPO = 'task-master'
        IMAGE_NAME = 'task-master'
        CLUSTER_NAME = 'task-manager-cluster'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/ShironKurian/Project_Nexus.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Login to ECR') {
            steps {
                sh """
                    aws ecr get-login-password --region ${AWS_REGION} | \
                    docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                """
            }
        }

        stage('Push to ECR') {
            steps {
                sh """
                    docker tag ${IMAGE_NAME}:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:latest
                    docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:latest
                """
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh "aws eks update-kubeconfig --region ${AWS_REGION} --name ${CLUSTER_NAME}"
                sh "kubectl apply -f k8s/deployment.yaml"
            }
        }
    }

    post {
        success {
            echo '🎉 Application deployed successfully to EKS!'
        }
        failure {
            echo '❌ Deployment failed. Check logs above.'
        }
    }
}