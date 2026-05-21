# Project Summary

## Overview

This project demonstrates a hybrid cloud migration workflow using Microsoft Azure services. The objective was to simulate how a medium-sized manufacturing company could migrate selected workloads from an on-premise environment to Azure cloud infrastructure.

The project focused on cloud deployment, database migration, monitoring, backup, security configuration, and CI/CD automation.

---

## Project Objectives

- Reduce reliance on physical infrastructure
- Improve scalability and flexibility
- Demonstrate cloud-based application deployment
- Configure secure database connectivity
- Implement monitoring and backup strategies
- Explore Azure hybrid cloud architecture concepts

---

## Solution Architecture

The solution was designed using a hybrid cloud approach, combining local development and cloud-hosted services.

### Main Azure Services Used

- Azure App Service
- Azure Database for MySQL
- Azure Virtual Machine
- Azure Blob Storage
- Azure Backup
- Azure Monitor
- Azure Advisor
- Microsoft Defender for Cloud
- Network Security Group (NSG)

---

## Implementation Highlights

### Web Application Deployment

A Python Flask web application was developed locally and deployed to Azure App Service using GitHub Actions CI/CD workflows.

### Database Migration

A MySQL database was migrated to Azure Database for MySQL using secure SSH tunnelling and MySQL Workbench.

### Monitoring and Performance

Azure Monitor dashboards were used to track CPU, disk, network, and memory utilisation metrics.

### Backup and Recovery

Azure Backup and restore points were configured to support basic recovery capability.

### Security Configuration

Basic security measures were implemented using Network Security Groups (NSG), Azure Advisor recommendations, and Microsoft Defender for Cloud.

---

## Key Outcomes

- Successfully deployed a Flask web application to Azure
- Configured automated CI/CD deployment workflow
- Migrated and connected Azure MySQL database
- Demonstrated Azure monitoring and backup functionality
- Implemented hybrid cloud architecture concepts
- Performed Azure TCO cost analysis

---

## Cost Analysis

Azure Total Cost of Ownership (TCO) analysis estimated potential long-term infrastructure savings compared with traditional on-premises deployment models.

Estimated potential savings over 3 years:

### NZ$139,283

---

## Screenshots

### Hybrid Cloud Architecture

![Architecture Diagram](architecture-diagram.png)

### GitHub Actions Deployment

![GitHub Actions Deployment](github-actions-deployment.png)

### Monitoring Dashboard

![Azure Monitoring](azure-monitoring.png)

### Cost Analysis

![Cost Analysis](cost-analysis.png)

---

## Repository

Main repository:

https://github.com/RubyKuang/Azure-HybridCloudMigration
