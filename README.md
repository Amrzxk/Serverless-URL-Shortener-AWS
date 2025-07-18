# Serverless URL Shortener – AWS Free-Tier DevOps Showcase

Fully serverless URL shortener that lives entirely in the AWS always-free tier, complete with CI/CD, monitoring, and budget guard-rails.

## High-Level Architecture
![Architecture](docs/architecture.png)

## Weekly Roadmap
- **Week 1** – design + cost guard-rails (current)
  - Local development environment configured (AWS CLI v2, SAM CLI, Docker Desktop)
  - Initialized Python SAM project scaffold (`src/`, `template.yaml`, Hello World Lambda)
  - Verified build & local invocation with `sam local invoke`
  - Branch protection enabled with passing CI placeholder workflow
- Week 2 – infrastructure code (SAM / CloudFormation)
- Week 3 – CI/CD hardening
- Week 4 – observability & alarms
- Week 5 – UI polish + demo assets # trigger
