pipeline {
  agent any

  environment {
    AWS_REGION    = 'us-east-1'
    ECR_REGISTRY  = '643716337997.dkr.ecr.us-east-1.amazonaws.com'
    ECR_REPO      = 'task-master'
    IMAGE_NAME    = "${ECR_REGISTRY}/${ECR_REPO}:latest"
    CLUSTER_NAME  = 'task-manager-cluster'
  }

  stages {
    stage('Checkout Code') {
      steps {
        git credentialsId: 'github-credentials',
            url: 'https://github.com/ShironKurian/Project_Nexus.git',
            branch: 'main'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh "docker build -t ${ECR_REPO} ."
      }
    }

    stage('Run Unit Tests') {
      steps {
        sh '''
          python3 -m ensurepip --upgrade
          python3 -m pip install --user --upgrade pip
          python3 -m pip install --user -r requirements.txt
          python3 -m pip install --user Werkzeug==2.2.3 pytest
          export PATH=$HOME/.local/bin:$PATH
          export PYTHONPATH=.
          echo "✅ PATH: $PATH"
          echo "✅ PYTHONPATH: $PYTHONPATH"
          pytest tests/ --maxfail=1 --disable-warnings -q
        '''
      }
    }

    stage('Login & Push to ECR') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'aws-credentials',
          usernameVariable: 'AWS_ACCESS_KEY_ID',
          passwordVariable: 'AWS_SECRET_ACCESS_KEY'
        )]) {
          sh '''
            aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
            aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
            aws configure set default.region $AWS_REGION

            aws ecr get-login-password --region $AWS_REGION \
              | docker login --username AWS --password-stdin $ECR_REGISTRY

            docker tag ${ECR_REPO}:latest ${IMAGE_NAME}
            docker push ${IMAGE_NAME}
          '''
        }
      }
    }

    stage('Deploy to EKS') {
      steps {
        sh '''
          aws eks update-kubeconfig --region $AWS_REGION --name $CLUSTER_NAME
          kubectl apply -f deployment.yaml
        '''
      }
    }

    stage('Deploy Monitoring') {
      steps {
        sh '''
          # make sure kubectl is pointing at your EKS cluster
          aws eks update-kubeconfig --region $AWS_REGION --name $CLUSTER_NAME

          # add & update the Prometheus Helm chart repo
          helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
          helm repo update

          # create a namespace for monitoring
          kubectl create namespace monitoring --dry-run=client -o yaml \
            | kubectl apply -f -

          # install (or upgrade) the kube-prometheus-stack
          helm upgrade --install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
            --namespace monitoring \
            --set grafana.service.type=LoadBalancer
        '''
      }
    }
  }

  post {
    success {
      echo '✅ Pipeline completed successfully – app, tests, EKS, Prometheus & Grafana are all live!'
    }
    failure {
      echo '❌ Pipeline failed. Inspect the logs to see which stage—and fix as needed.'
    }
  }
}