# variables.tf

# AWS region
variable "aws_region" {
  description = "AWS region to deploy resources"
  default     = "us-east-2"
}

# VPC CIDR block
variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

# Public subnet CIDRs
variable "public_subnets" {
  description = "List of public subnet CIDRs"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

# Private subnet CIDRs
variable "private_subnets" {
  description = "List of private subnet CIDRs"
  type        = list(string)
  default     = ["10.0.3.0/24", "10.0.4.0/24"]
}

# Availability zones
variable "availability_zones" {
  description = "List of AZs to deploy subnets"
  type        = list(string)
  default     = ["us-east-2a", "us-east-2b"]
}
