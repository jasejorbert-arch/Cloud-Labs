# Day 02 — AWS VPC Architecture (LocalStack)

## Objective
Design and deploy a basic AWS VPC with subnets and routing using Terraform.

## Architecture

- VPC: 10.0.0.0/16
- Public Subnet: 10.0.1.0/24
- Private Subnet: 10.0.2.0/24
- Internet Gateway
- Route Tables

## Tools
- Terraform
- LocalStack
- AWS CLI

## Steps Performed

1. Created Terraform project:
2. Created main.tf with:
- aws_vpc
- aws_subnet
- aws_internet_gateway
- aws_route_table

3. Ran:

## Validation

- VPC created successfully
- Subnets assigned correct CIDR
- IGW attached
- Routes propagated

## Issues & Fixes

| Issue | Fix |
|-------|------|
| Terraform error | Updated provider config |
| IGW missing | Added route association |

## Outcome

Successfully deployed simulated AWS VPC architecture using Infrastructure as Code.
