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
        stage('Check AWS CLI and Docker') {
            steps {
                script {
                    // Check AWS CLI version
                    def awsCheck = bat(script: 'aws --version', returnStatus: true, wait: true)
                    if (awsCheck != 0) {
                        error "AWS CLI is not installed or not in PATH"
                    }

                    // Check Docker version
                    def dockerCheck = bat(script: 'docker --version', returnStatus: true, wait: true)
                    if (dockerCheck != 0) {
                        error "Docker is not installed or not in PATH"
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    // Build the Docker image
                    bat "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('ECR Login') {
            steps {
                script {
                    // Login to AWS ECR
                    def loginStatus = bat(script: """
                        aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                    """, returnStatus: true, wait: true)
                    if (loginStatus != 0) {
                        error "ECR Login failed"
                    }
                    echo "Successfully logged in to ECR"
                }
            }
        }

        stage('Docker Push') {
            steps {
                script {
                    // Tag the image and push to ECR
                    def tagStatus = bat(script: """
                        docker tag ${IMAGE_NAME}:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:latest
                    """, returnStatus: true, wait: true)
                    if (tagStatus != 0) {
                        error "Docker tagging failed"
                    }
                    
                    def pushStatus = bat(script: """
                        docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:latest
                    """, returnStatus: true, wait: true)
                    if (pushStatus != 0) {
                        error "Docker push failed"
                    }
                    echo "Docker image pushed successfully to ECR"
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                script {
                    // Update kubeconfig for kubectl to access the EKS cluster
                    def updateKubeconfigStatus = bat(script: """
                        aws eks update-kubeconfig --name ${EKS_CLUSTER} --region ${AWS_REGION}
                    """, returnStatus: true, wait: true)
                    if (updateKubeconfigStatus != 0) {
                        error "Failed to update kubeconfig for EKS"
                    }

                    // Apply the deployment to EKS
                    def applyStatus = bat(script: 'kubectl apply -f deployment.yaml', returnStatus: true, wait: true)
                    if (applyStatus != 0) {
                        error "Deployment to EKS failed"
                    }
                    echo "Deployment to EKS successful!"
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