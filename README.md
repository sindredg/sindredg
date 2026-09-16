<p align="center">
  <img src="assets/header.svg" alt="Sindre Grytebust, cloud infrastructure and identity" width="100%">
</p>

<p align="center">
  <a href="https://sindrg.com"><img alt="Website" src="https://img.shields.io/badge/sindrg.com-1f3b4d?style=flat-square&logo=google-chrome&logoColor=f2b134"></a>
  <a href="https://github.com/sindredg?tab=repositories"><img alt="Projects" src="https://img.shields.io/badge/Projects-1f3b4d?style=flat-square&logo=github&logoColor=f2b134"></a>
  <a href="mailto:sindre.demetrio@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-1f3b4d?style=flat-square&logo=maildotru&logoColor=f2b134"></a>
</p>

---

### About

I design, build and run cloud infrastructure and identity platforms.

> Everything below is built and tested in a real environment, and written up as I go:
> how it was put together, why it is shaped the way it is, what the trade-offs were,
> and what broke along the way.

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

<sub>Click a project to open it.</sub>

<details>
<summary><b>Kubernetes Platform on GKE</b> &nbsp;·&nbsp; Kubernetes on GKE, running on my own domain &nbsp;<sub>live</sub></summary>

<br>

A secure and reliable Kubernetes platform hosting web applications on a custom domain: private VPC,
keyless delivery, Gateway API with managed TLS, Pod Security, NetworkPolicies, HPA, monitoring and
failure drills. Still adding to it.

<sub>Terraform · GCP · GKE · Kubernetes · Gateway API · Artifact Registry · Workload Identity Federation · GitHub Actions</sub>

[Repository](https://github.com/sindredg/k8-lab) &nbsp;·&nbsp; [Live at sindrg.com](https://sindrg.com)

</details>

<details>
<summary><b>Cross-cloud identity: Entra ID to AWS</b> &nbsp;·&nbsp; Entra ID as the identity source for AWS</summary>

<br>

Entra ID as identity source for AWS. SAML federation and SCIM provisioning to AWS IAM Identity Center,
attribute-based security group and JML workflows. Terraform builds an isolated VPC where Grafana runs
on ECS, reached over Entra Private Access.

<sub>Terraform · AWS IAM Identity Center · Entra ID · Private Access · Lifecycle Workflows · SAML · SCIM · Bicep · MS Graph · Grafana · ECS Fargate</sub>

[Repository](https://github.com/sindredg/cross-cloud-entra-aws)

</details>

<details>
<summary><b>Azure Hub-and-Spoke with Cross-Premises Connectivity</b> &nbsp;·&nbsp; Azure joined to an on-prem datacenter over IPsec</summary>

<br>

Hub-and-spoke network in Azure joined to a simulated on-premises datacenter in another region over an
encrypted IPsec tunnel, built one mechanism at a time. Gateway transit, subnet NSGs, Bastion access,
forced routing through Azure Firewall, Key Vault behind a private endpoint, and two-way DNS across the
tunnel.

<sub>Terraform · Azure Networking · VPN Gateway · Hub-and-Spoke · CI/CD · GitHub Actions · OIDC · Azure RBAC</sub>

[Repository](https://github.com/sindredg/hybrid-network-az)

</details>

<details>
<summary><b>Azure Container Platform</b> &nbsp;·&nbsp; a public web tier and an API with no public address</summary>

<br>

A public web tier and an internal API on Azure Container Apps, deployed with Terraform. The API has no
public address. Passwordless managed-identity image pulls, health probes, revisions, scale-to-zero,
remote state with locking, centralised logging and automated delivery.

<sub>Terraform · Azure Container Apps · ACR · Managed Identity · CI/CD · Docker · Nginx · Python/FastAPI</sub>

[Repository](https://github.com/sindredg/container-app-in-azure)

</details>

<details>
<summary><b>Hybrid identity: AD DS synced to Entra ID</b> &nbsp;·&nbsp; a two-site AD forest synced to Entra ID</summary>

<br>

Two-site Active Directory forest in Azure, synchronized with Entra ID. Features hybrid-joined endpoints
and users, per-machine LAPS credentials, policy-enforced tiered privileged access, and private networks.
Built throughout with Terraform and idempotent PowerShell.

<sub>Terraform · Azure · Entra ID · Active Directory · Windows Server · Group Policy · Windows LAPS · PowerShell · Entra Connect Sync · GitHub Actions</sub>

[Repository](https://github.com/sindredg/two-site-hybrid-identity)

</details>

<details>
<summary><b>Access Control &amp; Identity Governance</b> &nbsp;·&nbsp; Conditional Access, PIM and access reviews</summary>

<br>

Governs tenant-wide access and access to in-house applications with Entra ID: Conditional Access,
just-in-time administration with PIM, entitlement management and access reviews.

<sub>Entra ID · Conditional Access · PIM · FIDO2 · Access Reviews · SSO · SCIM · Microsoft Graph PowerShell</sub>

[Repository](https://github.com/sindredg/Access-Control-and-Identity-Governance)

</details>

<details>
<summary><b>SSO + SCIM for a Self-Hosted App</b> &nbsp;·&nbsp; OIDC sign-in and SCIM provisioning for Grafana</summary>

<br>

Implements the workforce identity lifecycle for self-hosted Grafana: Entra ID as the identity provider,
OpenID Connect SSO with app-role mapping, and SCIM provisioning through a custom bridge.

<sub>OpenID Connect · SSO · SCIM · Grafana · App Roles · Azure IaaS · Docker</sub>

[Repository](https://github.com/sindredg/entra-app-roles-sso-scim)

</details>

<details>
<summary><b>Securing AI with MCP Server and RBAC</b> &nbsp;·&nbsp; read-only Azure access for Claude, scoped with RBAC</summary>

<br>

Gives Claude scoped, read-only access to Azure through the Azure MCP Server, with Azure RBAC as the
authoritative control and host/server hardening as defense in depth.

<sub>Azure MCP Server · Azure RBAC · Service Principal · Claude</sub>

[Repository](https://github.com/sindredg/claude-azure-mcp-rbac-design)

</details>

<details>
<summary><b>Apps, APIs &amp; Access Tokens: OAuth 2.0 in .NET 8</b> &nbsp;·&nbsp; scopes, app roles and token claims in .NET 8</summary>

<br>

Builds an Entra ID authorization chain with a protected API and web and daemon clients. Access is
modeled through scopes, app roles and groups, then enforced from token claims in a .NET 8 API.

<sub>.NET 8 · OAuth 2.0 · OpenID Connect · App Roles · App Registrations · Application Permissions</sub>

[Repository](https://github.com/sindredg/app-registrations-and-JWT-tokens)

</details>

---

<p align="center">
  <img src="assets/footer.svg" alt="sindrg.com" width="100%">
</p>
