graph TD
    VPC[VPC: 10.0.0.0/16]

    VPC --> Pub1[Public Subnet 1: 10.0.1.0/24]
    VPC --> Pub2[Public Subnet 2: 10.0.2.0/24]
    VPC --> Priv1[Private Subnet 1: 10.0.3.0/24]
    VPC --> Priv2[Private Subnet 2: 10.0.4.0/24]

    Pub1 --> IGW[Internet Gateway]
    Pub2 --> IGW

    Priv1 --> NAT1[NAT Gateway in Public Subnet 1]
    Priv2 --> NAT2[NAT Gateway in Public Subnet 2]

    Pub1 --> RT_Pub[Route Table: Public]
    Pub2 --> RT_Pub
    Priv1 --> RT_Priv[Route Table: Private]
    Priv2 --> RT_Priv

    RT_Pub --> IGW
    RT_Priv --> NAT1
    RT_Priv --> NAT2

    Priv1 --> SG1[Security Group]
    Priv2 --> SG2[Security Group]
    Pub1 --> SG3[Security Group]
    Pub2 --> SG4[Security Group]
