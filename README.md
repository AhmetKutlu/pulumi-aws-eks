# AWS EKS Cluster Setup Using Pulumi Python SDK

This setup creates an AWS EKS Cluster on given AWS account using Pulumi.
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

