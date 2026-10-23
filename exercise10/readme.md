# Exercise 10: Multi-Node Kubernetes Deployment

## Objective
Deploy Product Catalog and Shopping Cart applications on a multi-node Kubernetes cluster using Minikube.

## Technologies
- Python Flask
- Docker
- Kubernetes
- Minikube

## Features
- Product Catalog application with 2 replicas.
- Shopping Cart application with 3 replicas.
- NodePort services for accessing applications.
- Pod anti-affinity to distribute replicas across different nodes.
- Containerized applications deployed on a multi-node cluster.

## Run the Applications

Start the cluster:

```bash
minikube start --nodes 3 -p devops-multinode --driver=docker
```

Build Docker images and load them into Minikube, then deploy the Kubernetes manifests:

```bash
kubectl --context=devops-multinode apply -f product_catalog_deployment.yaml
kubectl --context=devops-multinode apply -f shopping_cart_deployment.yaml
kubectl --context=devops-multinode apply -f product_catalog_service.yaml
kubectl --context=devops-multinode apply -f shopping_cart_service.yaml
```

## Verify Deployment

```bash
kubectl --context=devops-multinode get pods -o wide
kubectl --context=devops-multinode get services
```

## Application Endpoints
- Product Catalog: `/products`
- Shopping Cart: `/cart`

## Expected Outcome
Both applications run successfully in Kubernetes with multiple replicas distributed across the cluster nodes.
