#!/bin/bash

# Variables
NAMESPACE="default"
DEPLOYMENT_V1="canary-deployment-v1"
DEPLOYMENT_V2="canary-deployment-v2"
SERVICE="canary-deployment"
INGRESS="canary-deployment"
MAX_WEIGHT=100
STEP=20

# Deploy or upgrade v1 and v2
echo "🔄 Deploying/upgrading v1 and v2..."
kubectl apply -f deployment.yaml -n $NAMESPACE
kubectl apply -f service.yaml -n $NAMESPACE
kubectl apply -f ingress.yaml -n $NAMESPACE

# Check pod status function
check_pod_status() {
  PODS_NOT_RUNNING=$(kubectl get pods -n $NAMESPACE -l app=$SERVICE,version=v2 -o jsonpath='{.items[?(@.status.phase!="Running")].metadata.name}' | wc -l)
  echo "Pods not running: $PODS_NOT_RUNNING"
  return $PODS_NOT_RUNNING
}

# Gradually increase canary traffic
for (( weight=STEP; weight<=MAX_WEIGHT; weight+=STEP )); do
  echo "🔄 Setting canary traffic weight to ${weight}%..."
  kubectl annotate ingress $INGRESS nginx.ingress.kubernetes.io/canary-weight="$weight" --overwrite -n $NAMESPACE
  
  # Wait and validate
  echo "⏳ Waiting for 30 seconds to check pod health..."
  sleep 30
  
  check_pod_status
  if [[ $? -ne 0 ]]; then
    echo "❌ Issue detected! Rolling back canary..."
    kubectl annotate ingress $INGRESS nginx.ingress.kubernetes.io/canary-weight="0" --overwrite -n $NAMESPACE
    exit 1
  fi

  echo "✅ Canary weight increased to ${weight}% successfully!"
done

echo "🎉 Canary release promoted to 100% traffic!"
