pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ECR_REPO = '643716337997.dkr.ecr.us-east-1.amazonaws.com/task-master'
        IMAGE_TAG = 'latest'
    }

        stage('Docker Build') {
            steps {
                sh 'docker build -t task-master:latest .'
            }
        }

        stage('ECR Login') {
            steps {
                withAWS(credentials: 'aws-jenkins-creds', region: "${AWS_REGION}") {
                    sh 'aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REPO'
                }
            }
        }

        stage('Docker Push') {
            steps {
                sh '''
                docker tag task-master:latest $ECR_REPO:$IMAGE_TAG
                docker push $ECR_REPO:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh 'kubectl apply -f eks-cluster/manifests/deployment.yaml'
                sh 'kubectl apply -f eks-cluster/manifests/service.yaml'
            }
        }
    }
}