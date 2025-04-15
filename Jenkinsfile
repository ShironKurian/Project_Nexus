pipeline {
    agent any

    environment {
        AWS_ACCOUNT_ID = '643716337997'
        AWS_REGION = 'us-east-1'
        ECR_REPO = 'task-master'
        EKS_CLUSTER = 'task-manager-cluster'
        IMAGE_NAME = 'task-master'
    }

    stages {
        stage('Docker Build') {
            steps {
                script {
                    bat 'docker build -t %IMAGE_NAME% .'
                }
            }
        }

        stage('ECR Login') {
            steps {
                script {
                    bat """
                        aws ecr get-login-password --region %AWS_REGION% | docker login --username AWS --password-stdin %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com
                    """
                }
            }
        }

        stage('Docker Push') {
            steps {
                script {
                    bat """
                        docker tag %IMAGE_NAME%:latest %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com/%ECR_REPO%:latest
                        docker push %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com/%ECR_REPO%:latest
                    """
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                script {
                    bat 'kubectl apply -f deployment.yaml'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment to EKS was successful!'
        }
        failure {
            echo 'There was a failure during the deployment process.'
        }
    }
}