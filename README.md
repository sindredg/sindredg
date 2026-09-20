<p align="center">
  <img src="assets/header.svg?v=3" alt="Sindre Grytebust, infrastructure and identity" width="100%">
</p>

<p align="center">
  <a href="https://sindrg.com"><img alt="Live platform" src="https://img.shields.io/badge/Live%20platform-1f3b4d?style=flat-square&logo=google-chrome&logoColor=f2b134"></a>
  <a href="https://github.com/sindredg?tab=repositories"><img alt="Projects" src="https://img.shields.io/badge/Projects-1f3b4d?style=flat-square&logo=github&logoColor=f2b134"></a>
  <a href="mailto:sindre.demetrio@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-1f3b4d?style=flat-square&logo=maildotru&logoColor=f2b134"></a>
</p>

---

### About

I design, build and run cloud infrastructure and identity platforms. My work focuses on the points
where networking, access control, delivery and operations meet.

> Everything below was built and tested in a real environment. The repositories record how each
> system was put together, why it is shaped the way it is, what the trade-offs were, how it was
> validated, and what broke along the way.

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

### Selected work

#### [Kubernetes platform on GKE](https://github.com/sindredg/k8-lab) &nbsp;·&nbsp; [live](https://sindrg.com)

A private GKE platform serving two workloads through one public Gateway with managed TLS. Terraform
builds the network and cluster, and keyless GitHub Actions delivery builds, scans and rolls out each
image. The platform includes Pod Security, default-deny NetworkPolicies, workload and node
autoscaling, observability, failure drills and a threat model with measured findings.

Measured at 125 requests a second with a p95 of 394 ms and no failures after scaling from two to
eight Pods. Connection failures during rollout fell from 72 to zero after the drain path was fixed.

Security Command Center findings currently reach Pub/Sub and a dead-letter path. The triage worker,
verdict notification path and remediation pull requests are the next milestone, not completed work.

`Terraform` `GCP` `GKE` `Kubernetes` `Gateway API` `Cloud Armor` `Workload Identity Federation` `GitHub Actions` `k6`

#### [Cross-cloud workforce identity: Entra ID to AWS](https://github.com/sindredg/cross-cloud-entra-aws)

Microsoft Entra ID is the workforce identity source for AWS IAM Identity Center through SAML and
SCIM. Dynamic role groups, access packages and lifecycle workflows govern joiner, mover, leaver and
time-limited elevated access. Terraform owns the AWS permission sets and the private target running
on ECS Fargate behind Entra Private Access.

The end-to-end lifecycle is measured: baseline access arrived 55 seconds after enablement, role
groups changed 24 seconds after a title update, and SCIM disabled the AWS user 10 minutes after the
Entra account was disabled.

`Terraform` `AWS IAM Identity Center` `Entra ID` `SAML` `SCIM` `Lifecycle Workflows` `ECS Fargate`

#### [Hybrid identity: AD DS synced to Entra ID](https://github.com/sindredg/two-site-hybrid-identity)

A two-site Active Directory forest in Azure, synchronized to Entra ID and reachable only through
Azure Bastion. Terraform builds the private infrastructure and idempotent PowerShell builds the
directory. Hybrid-joined endpoints receive security baselines, per-machine LAPS credentials and
policy-enforced Tier 0, 1 and 2 administration boundaries.

All nine phases are built and verified. The repository includes implementation records, searchable
troubleshooting logs, architecture decisions and an explicit risk register.

`Terraform` `Azure` `Active Directory` `Entra ID` `PowerShell` `Group Policy` `Windows LAPS`

#### [Sky](https://github.com/sindredg/sky) &nbsp;·&nbsp; [live](https://sindrg.com/sky)

A deterministic Python application for sunlight, moon and eclipse data across 37 places, plus a
browser observatory. It uses no external API or database. Solar and lunar calculations have bounded
accuracy checks against published models and NASA JPL Horizons samples, with the limitations stated
alongside the results. Python, frontend, container and deployment contracts run in CI.

`Python` `FastAPI` `JavaScript` `Docker` `pytest` `GitHub Actions`

### More projects

- [Azure hub-and-spoke with cross-premises connectivity](https://github.com/sindredg/hybrid-network-az),
  an IPsec-connected hub, spoke and simulated datacenter with centralized inspection, private DNS
  and no public workload exposure.
- [Azure Container Platform](https://github.com/sindredg/container-app-in-azure), a public web tier
  and internal API on Azure Container Apps with managed identity, remote state, private images and
  automated delivery.
- [Access Control and Identity Governance](https://github.com/sindredg/Access-Control-and-Identity-Governance),
  Conditional Access, PIM, entitlement management and access reviews built and tested on Entra ID P2.
- [SSO and SCIM for self-hosted Grafana](https://github.com/sindredg/entra-app-roles-sso-scim),
  OpenID Connect sign-in, app-role mapping and lifecycle provisioning through a custom SCIM bridge.
- [Least-privilege AI access to Azure](https://github.com/sindredg/claude-azure-mcp-rbac-design),
  read-only Azure MCP access with Azure RBAC as the authoritative boundary.
- [Apps, APIs and access tokens](https://github.com/sindredg/app-registrations-and-JWT-tokens),
  delegated scopes, application roles and token-claim enforcement in a minimal .NET 8 API.

---

<p align="center">
  <img src="assets/footer.svg?v=2" alt="sindrg.com" width="100%">
</p>
