#!/bin/bash


if ! command -v minikube &> /dev/null; then
    echo "Minikube is not installed. "
    exit 1
fi


if ! command -v kubectl &> /dev/null; then
    echo "kubectl is not installed."
    exit 1
fi

minikube start

kubectl cluster-info

if [ $? -ne 0 ]; then
    echo "Unable to connect to the Kubernetes cluster."
    exit 1
fi

kubectl get pods --all-namespaces
