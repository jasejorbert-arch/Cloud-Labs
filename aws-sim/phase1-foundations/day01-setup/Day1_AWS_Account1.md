graph TD
    A[AWS Account / Organization] 

    A --> B[Root User]
    B --> C[Admin IAM User (MFA Enabled)]
    B --> D[Dev Role]
    B --> E[Ops Role]

    A --> F[CloudTrail Logs --> S3 Bucket]
    A --> G[Billing Alerts / CloudWatch]
