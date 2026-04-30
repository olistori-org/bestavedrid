# 🚀 Bestavedrid – Full DevOps Platform Demo

This project demonstrates a **production-style DevOps platform** built from scratch using modern tooling and best practices.

It showcases infrastructure provisioning, configuration management, CI/CD, containerization, Kubernetes orchestration, GitOps deployment, and ingress routing — all working together end-to-end.

---

## 🧱 Architecture Overview

Internet → Nginx (VPS) → Kubernetes Ingress → Services → Pods

CI/CD Flow:

Git Push → GitHub Actions → Docker Build → GHCR → Argo CD → Kubernetes

---

## ⚙️ Tech Stack

Infrastructure:
- Terraform (Hetzner VPS)
- Ansible (Configuration)

CI/CD:
- GitHub Actions
- GHCR (private registry)

Runtime:
- Docker
- Kubernetes (Minikube)

GitOps:
- Argo CD

Networking:
- Nginx (edge proxy)
- Kubernetes Ingress

Application:
- FastAPI

---

## 📁 Project Structure

app/ – FastAPI app  
k8s/ – Kubernetes manifests  
argocd/ – Argo CD configs  
terraform/ – Infrastructure  
ansible/ – Configuration  
.github/workflows/ – CI  

---

## 🌐 Access

Application:
http://hello.local/hello

Argo CD:
http://argocd.local

Hosts file:
94.130.107.84 hello.local  
94.130.107.84 argocd.local  

---

## 🚀 Workflow

1. Terraform provisions VPS  
2. Ansible configures system  
3. GitHub Actions builds & pushes image  
4. Argo CD deploys to Kubernetes  
5. Ingress + Nginx expose services  

---

## 🧠 Key Learnings

- CI/CD pipelines  
- GitOps with Argo CD  
- Kubernetes networking  
- Private registry auth  
- Infrastructure as Code  
- Debugging real-world issues  

---

## 🔥 Future Improvements

- PostgreSQL integration  
- TLS (HTTPS)  
- Monitoring  
- Multi-env setup  
- Secret management  

---

## 👨‍💻 Author
