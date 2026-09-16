<p align="center">
  <img src="assets/header.svg" alt="Sindre Grytebust — cloud infrastructure, platforms and identity" width="100%">
</p>

<p align="center">
  <a href="https://sindrg.com"><img alt="Website" src="https://img.shields.io/badge/sindrg.com-1f3b4d?style=flat-square&logo=google-chrome&logoColor=f2b134"></a>
  <a href="https://github.com/sindredg?tab=repositories"><img alt="Projects" src="https://img.shields.io/badge/Projects-1f3b4d?style=flat-square&logo=github&logoColor=f2b134"></a>
  <a href="mailto:sindre.demetrio@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-1f3b4d?style=flat-square&logo=maildotru&logoColor=f2b134"></a>
</p>

---

### About

I design, build and run cloud infrastructure and identity platforms — mostly
around **Entra ID**, **Azure**, **AWS** and **GCP**, with **Terraform** as the
default way to get there.

> Every project below is built and tested in a real environment and documented with
> implementation workflows, architecture overviews, design decisions, trade-offs,
> validation evidence and troubleshooting records.

### Toolbox

<p>
  <img alt="Terraform" src="https://img.shields.io/badge/Terraform-1f3b4d?style=flat-square&logo=terraform&logoColor=f2b134">
  <img alt="Azure" src="https://img.shields.io/badge/Azure-1f3b4d?style=flat-square&logo=microsoftazure&logoColor=f2b134">
  <img alt="AWS" src="https://img.shields.io/badge/AWS-1f3b4d?style=flat-square&logo=amazonwebservices&logoColor=f2b134">
  <img alt="Google Cloud" src="https://img.shields.io/badge/Google%20Cloud-1f3b4d?style=flat-square&logo=googlecloud&logoColor=f2b134">
  <img alt="Kubernetes" src="https://img.shields.io/badge/Kubernetes-1f3b4d?style=flat-square&logo=kubernetes&logoColor=f2b134">
  <img alt="Entra ID" src="https://img.shields.io/badge/Entra%20ID-1f3b4d?style=flat-square&logo=microsoftentraid&logoColor=f2b134">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-1f3b4d?style=flat-square&logo=githubactions&logoColor=f2b134">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-1f3b4d?style=flat-square&logo=docker&logoColor=f2b134">
  <img alt="PowerShell" src="https://img.shields.io/badge/PowerShell-1f3b4d?style=flat-square&logo=powershell&logoColor=f2b134">
  <img alt="Python" src="https://img.shields.io/badge/Python-1f3b4d?style=flat-square&logo=python&logoColor=f2b134">
</p>

---

### Projects
| Project | What it is | Stack |
| --- | --- | --- |
| [**Kubernetes Platform on GKE**](https://github.com/sindredg/k8-lab)<br>**Live at** [sindrg.com](https://sindrg.com) | A secure and reliable Kubernetes platform hosting web applications on a custom domain: private VPC, keyless delivery, Gateway API with managed TLS, Pod Security, NetworkPolicies, HPA, monitoring and failure drills (+ actively building new features). | Terraform · GCP · GKE · Kubernetes · Gateway API · Artifact Registry · Workload Identity Federation · GitHub Actions |
| [**Cross-cloud identity: Entra ID to AWS**](https://github.com/sindredg/cross-cloud-entra-aws) | Entra ID as identity source for AWS. SAML federation and SCIM provisioning to AWS IAM Identity Center, attribute-based security group and JML workflows. Terraform builds an isolated VPC where Grafana runs on ECS, reached over Entra Private Access. | Terraform · AWS IAM Identity Center · Entra ID · Private Access · Lifecycle Workflows · SAML · SCIM · Bicep · MS Graph · Grafana · ECS Fargate |
| [**Azure Hub-and-Spoke with Cross-Premises Connectivity**](https://github.com/sindredg/hybrid-network-az) | Hub-and-spoke network in Azure joined to a simulated on-premises datacenter in another region over an encrypted IPsec tunnel, built one mechanism at a time. Gateway transit, subnet NSGs, Bastion access, forced routing through Azure Firewall, Key Vault behind a private endpoint, and two-way DNS across the tunnel. | Terraform · Azure Networking · VPN Gateway · Hub-and-Spoke · CI/CD · GitHub Actions · OIDC · Azure RBAC |
| [**Azure Container Platform**](https://github.com/sindredg/container-app-in-azure) | A public web tier and an internal API on Azure Container Apps, deployed with Terraform. The API has no public address. Passwordless managed-identity image pulls, health probes, revisions, scale-to-zero, remote state with locking, centralised logging and automated delivery. | Terraform · Azure Container Apps · ACR · Managed Identity · CI/CD · Docker · Nginx · Python/FastAPI |
| [**Hybrid identity: AD DS synced to Entra ID**](https://github.com/sindredg/two-site-hybrid-identity) | Two-site Active Directory forest in Azure, synchronized with Entra ID. Features hybrid-joined endpoints and users, per-machine LAPS credentials, policy-enforced tiered privileged access, and private networks. Built throughout with Terraform and idempotent PowerShell. | Terraform · Azure · Entra ID · Active Directory · Windows Server · Group Policy · Windows LAPS · PowerShell · Entra Connect Sync · GitHub Actions |
| [**Access Control & Identity Governance**](https://github.com/sindredg/Access-Control-and-Identity-Governance) | Governs tenant-wide access and access to in-house applications with Entra ID: Conditional Access, just-in-time administration with PIM, entitlement management and access reviews. | Entra ID · Conditional Access · PIM · FIDO2 · Access Reviews · SSO · SCIM · Microsoft Graph PowerShell |
| [**SSO + SCIM for a Self-Hosted App**](https://github.com/sindredg/entra-app-roles-sso-scim) | Implements the workforce identity lifecycle for self-hosted Grafana: Entra ID as the identity provider, OpenID Connect SSO with app-role mapping, and SCIM provisioning through a custom bridge. | OpenID Connect · SSO · SCIM · Grafana · App Roles · Azure IaaS · Docker |
| [**Securing AI with MCP Server and RBAC**](https://github.com/sindredg/claude-azure-mcp-rbac-design) | Gives Claude scoped, read-only access to Azure through the Azure MCP Server, with Azure RBAC as the authoritative control and host/server hardening as defense in depth. | Azure MCP Server · Azure RBAC · Service Principal · Claude |
| [**Apps, APIs & Access Tokens: OAuth 2.0 in .NET 8**](https://github.com/sindredg/app-registrations-and-JWT-tokens) | Builds an Entra ID authorization chain with a protected API and web and daemon clients. Access is modeled through scopes, app roles and groups, then enforced from token claims in a .NET 8 API. | .NET 8 · OAuth 2.0 · OpenID Connect · App Roles · App Registrations · Application Permissions |

---

<p align="center">
  <img src="assets/footer.svg" alt="sindrg.com" width="100%">
</p>
