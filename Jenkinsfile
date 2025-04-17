pipeline {
  agent any

  environment {
    // AWS credentials stored in Jenkins (add under Manage Jenkins → Credentials)
    AWS_ACCESS_KEY_ID     = credentials('aws-access-key-id')
    AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    AWS_DEFAULT_REGION    = 'us-east-1'

    // Your ECR image URI (including tag)
    ECR_URI      = '643716337997.dkr.ecr.us-east-1.amazonaws.com/task-master:latest'
    // Your EKS cluster name
    CLUSTER_NAME = 'task-manager-cluster'
    // Your GitHub repository
    GIT_REPO     = 'https://github.com/ShironKurian/Project_Nexus.git'
  }

  stages {
    stage('Checkout') {
      steps {
        // Clone the main branch
        git branch: 'main', url: "${GIT_REPO}"
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t task-master .'
      }
    }

    stage('Run Tests') {
      steps {
        // Install dependencies and run pytest
        sh '''
          pip install --upgrade pip
          pip install -r requirements.txt
          pytest --maxfail=1 --disable-warnings -q
        '''
      }
    }

    stage('Login to ECR') {
      steps {
        sh """
          aws ecr get-login-password \
            --region ${AWS_DEFAULT_REGION} \
          | docker login --username AWS --password-stdin 643716337997.dkr.ecr.us-east-1.amazonaws.com
        """
      }
    }

    stage('Push to ECR') {
      steps {
        sh """
          docker tag task-master:latest ${ECR_URI}
          docker push ${ECR_URI}
        """
      }
    }

    stage('Configure kubectl') {
      steps {
        // Fetch and merge kubeconfig for your EKS cluster
        sh """
          aws eks update-kubeconfig \
            --region ${AWS_DEFAULT_REGION} \
            --name ${CLUSTER_NAME}
        """
      }
    }

    stage('Deploy to EKS') {
      steps {
        // Apply your Kubernetes manifests
        sh 'kubectl apply -f deployment.yaml'
        sh 'kubectl apply -f service.yaml'
      }
    }
  }

  post {
    success {
      echo '✅ Pipeline completed successfully!'
    }
    failure {
      echo '❌ Pipeline failed. Check the console output for errors.'
    }
  }
}