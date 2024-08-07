# AWS EKS Cluster Setup Using Pulumi Python SDK

This setup creates an AWS EKS Cluster within a private VPC on given AWS account using Pulumi.
To work collaboratively on infrastructure code, Pulumi Cloud is used as backend state.
- Install pulumi and aws-iam-authenticator binaries according to your operating system.
- Create an account on Pulumi Cloud.
- Create a token on Pulumi Cloud.
- Go to project directory on CMD.
- Execute "pulumi login" providing the token you got from Pulumi Cloud.
- Set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN, AWS_REGION as environment variables.
- Execute "pulumi up" and wait for setup to complete.
- Execute "pulumi stack output kubeconfig > kubeconfig.yml" to get cluster's config file.
- Set it as an environment variable named as KUBECONFIG.
- Access to cluster with kubectl command.
- To destroy the stack, execute "pulumi destroy".

### Issues about AWS EKS Cluster with private endpoint only

In order to access EKS cluster using secure and authenticated channels, cluster should be
created private endpoint only.

However, because of a bug in pulumi-eks Python module, cluster creation fails with private endpoint only.
You can find the open issue on https://github.com/pulumi/pulumi-eks/issues/1191.

In order to overcome this bug, I created the cluster with public and private access first, 
after the setup completes, I changed the cluster configuration by adding endpoint_private_access=True,
endpoint_public_access=False parameters to constructor.

