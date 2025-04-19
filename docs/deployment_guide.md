# Deployment Guide

## Prerequisites
- AWS CLI configured
- kubectl installed
- Helm installed
- Docker installed

## Infrastructure Setup
### EKS Cluster
```bash
eksctl create cluster \
  --name task-manager \
  --region us-east-1 \
  --nodegroup-name standard-workers \
  --node-type t3.medium \
  --nodes 3
```

### Database
- RDS PostgreSQL instance
- Proper security groups
- Backup configuration

## Application Deployment
### Build and Push
```bash
docker build -t task-manager .
docker tag task-manager:latest $ECR_REPO/task-manager:latest
docker push $ECR_REPO/task-manager:latest
```

### Deploy to Kubernetes
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

## Post-Deployment
### Verification
- Check pod status
- Verify endpoints
- Monitor logs
- Check metrics

### Rollback Plan
1. Identify issues
2. Revert deployment
3. Verify rollback
4. Document incident 