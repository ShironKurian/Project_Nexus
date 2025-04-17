pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ECR_REGISTRY = '643716337997.dkr.ecr.us-east-1.amazonaws.com'
        ECR_REPO = 'task-master'
        IMAGE_NAME = "${ECR_REGISTRY}/${ECR_REPO}:latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/ShironKurian/Project_Nexus.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${ECR_REPO} ."
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    pip install -r requirements.txt
                    pip install pytest
                    pytest tests/
                '''
            }
        }

        stage('Login to AWS ECR') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'aws-credentials', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh '''
                        aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
                        aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
                        aws configure set default.region $AWS_REGION
                        aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REGISTRY
                    '''
                }
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                    docker tag ${ECR_REPO}:latest ${IMAGE_NAME}
                    docker push ${IMAGE_NAME}
                '''
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh '''
                    aws eks update-kubeconfig --region $AWS_REGION --name task-manager-cluster
                    kubectl apply -f deployment.yaml
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Pipeline failed. Please check logs.'
        }
        success {
            echo '✅ Deployment Successful!'
        }
    }
}