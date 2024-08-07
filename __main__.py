import json
import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx
import pulumi_eks as eks


# VPC Configuration

# Create a VPC for our cluster.
vpc = awsx.ec2.Vpc("VPC-EKS-Cluster")

# IAM Roles
role_args = aws.iam.RoleArgs(
    assume_role_policy=json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "eks.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
    ),
    managed_policy_arns=["arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"],
    name="EKSClusterRole"
)
eks_service_role = aws.iam.Role(
    resource_name="EKSClusterRole",
    args=role_args
)

# Create an EKS cluster inside of the VPC.
cluster = eks.Cluster(
    resource_name="EKS-Cluster",
    authentication_mode=eks.AuthenticationMode.API_AND_CONFIG_MAP,
    vpc_id=vpc.vpc_id,
    service_role=eks_service_role,
    public_subnet_ids=vpc.public_subnet_ids,
    private_subnet_ids=vpc.private_subnet_ids,
    node_associate_public_ip_address=False)


# Export the cluster's kubeconfig.
pulumi.export("kubeconfig", cluster.kubeconfig)
#
