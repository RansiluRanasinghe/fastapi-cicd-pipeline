# FastAPI End-to-End CI/CD Pipeline

> A practical, production-ready Continuous Integration and Continuous Deployment pipeline built over an intensive 2-day learning sprint. The objective of this project is to master automated testing, containerization, and cloud deployment pipelines using entirely **free-tier** industry tools.

![CI/CD Status](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/fastapi-cicd-pipeline/ci-cd.yml?label=CI%2FCD&logo=github-actions&logoColor=white)
![Docker Pulls](https://img.shields.io/docker/pulls/YOUR_DOCKERHUB_USERNAME/fastapi-cicd-pipeline?logo=docker)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Table of Contents

- [System Architecture](#system-architecture)
- [Tech Stack](#tech-stack)
- [Implementation Roadmap](#implementation-roadmap)
  - [Day 1 — Continuous Integration](#day-1--continuous-integration-ci)
  - [Day 2 — Continuous Deployment](#day-2--continuous-deployment-cd)
- [Getting Started](#getting-started)
  - [Step 1: Initialize Your Repository](#step-1-initialize-your-repository)
  - [Step 2: Set Up Your Local Workspace](#step-2-set-up-your-local-workspace)

---

## System Architecture

Every `git push` triggers a fully automated three-stage pipeline:

```
[ Local Code ] ──> git push ──> [ GitHub Repository ]
                                        │
                                        ▼
                            (Triggers GitHub Actions)
                   ┌─────────────────────────────────┐
                   │  🧪  Stage 1: Continuous Testing  │
                   │   - Lint & Format Check           │
                   │   - Run Pytest Suite              │
                   └────────────────┬────────────────┘
                                    │ (If Tests Pass)
                                    ▼
                   ┌─────────────────────────────────┐
                   │  📦  Stage 2: Build & Package    │
                   │   - Build Docker Image           │
                   │   - Push to Docker Hub           │
                   └────────────────┬────────────────┘
                                    │ (Automated Webhook)
                                    ▼
                   ┌─────────────────────────────────┐
                   │  🚀  Stage 3: Live Deployment    │
                   │   - Pull image to Render Web     │
                   │   - Zero-Downtime Rollout        │
                   └─────────────────────────────────┘
```

---

## Tech Stack

| Layer | Tool |
|---|---|
| **Application** | FastAPI (Python 3.11+) |
| **Testing Framework** | Pytest |
| **Containerization** | Docker |
| **CI/CD Engine** | GitHub Actions |
| **Image Registry** | Docker Hub |
| **Cloud Hosting** | Render (Free Tier Web Service) |

---

## Implementation Roadmap

### Day 1 — Continuous Integration (CI)

- [ ] Initialize FastAPI microservice with a `/health` endpoint
- [ ] Implement automated unit testing using `pytest`
- [ ] Configure GitHub Actions workflow (`.github/workflows/ci-cd.yml`)
- [ ] Achieve successful local and remote test execution on code pushes

### Day 2 — Continuous Deployment (CD)

- [ ] Write an optimized multi-stage `Dockerfile` for the application
- [ ] Configure GitHub repository secrets for secure pipeline authentication
- [ ] Expand the workflow to build and push tagged Docker images to Docker Hub
- [ ] Connect the image registry to Render via deployment webhooks for automated live releases
- [ ] Perform an end-to-end drift test: push a code change → verify live in **under 3 minutes**

---

## Getting Started

### Step 1: Initialize Your Repository

1. Go to your GitHub account and click **New Repository**.
2. Name it `fastapi-cicd-pipeline`.
3. Set the visibility to **Public** (required for Render access on the free tier).
4. Leave **Add a README**, **Add .gitignore**, and **Choose a license** **unchecked** — these will be created manually to understand the exact file structures.
5. Click **Create repository**.

### Step 2: Set Up Your Local Workspace

Open your terminal, navigate to your development directory, and run the following commands:

```bash
# Create the project directory and move into it
mkdir fastapi-cicd-pipeline
cd fastapi-cicd-pipeline

# Initialize Git
git init

# Create your README.md
# Copy and paste the markdown contents into this file using VS Code or your preferred editor
```
