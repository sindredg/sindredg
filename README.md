**About**

> Infrastructure and identity work, built in real environments and documented
> with the decisions and trade-offs behind them. Each repository carries its
> architecture notes, rejected alternatives and validation evidence.

---

## Platform & delivery

### [Golden Hour](https://github.com/sindredg/aca-prod) — [live ↗](https://ca-aca-prod-production.yellowglacier-15588c53.norwayeast.azurecontainerapps.io)

A sunlight planner running in production, and the delivery pipeline that puts
it there. Three Terraform states split by who may apply them: the pipeline
holds Contributor and cannot create role assignments, so it cannot widen its
own permissions. Four workload identities, each trusted on exactly one OIDC
subject; images deploy by digest, never by tag, behind an approval gate.

`Terraform` `Container Apps` `OIDC` `GitHub Actions` `FastAPI` `Docker`

### [Azure Container Platform](https://github.com/sindredg/container-app-in-azure)

The learning lab behind Golden Hour, optimised for showing the reasoning rather
than for reuse. A public web tier and an internal API with no public address,
passwordless managed-identity image pulls, revisions and scale-to-zero. The
infrastructure has been torn down; the repository is the artefact.

`Terraform` `Container Apps` `ACR` `Managed Identity` `Nginx` `FastAPI`

---

## Identity & access

### [Two Sites, Hybrid Identities, Security Baselines](https://github.com/sindredg/two-site-hybrid-identity)

A two-site Active Directory forest in Azure, synchronised with Entra ID, with
hybrid-joined endpoints and per-machine LAPS credentials. Privileged access is
tiered and policy-enforced, built throughout with Terraform and idempotent
PowerShell.

`Terraform` `Entra ID` `Active Directory` `Group Policy` `Windows LAPS` `PowerShell`

### [Access Control & Identity Governance](https://github.com/sindredg/Access-Control-and-Identity-Governance)

Tenant-wide and per-application access governed through Entra ID: Conditional
Access, just-in-time administration with PIM, entitlement management and access
reviews.

`Entra ID` `Conditional Access` `PIM` `FIDO2` `Access Reviews` `Graph PowerShell`

### [SSO + SCIM for a Self-Hosted App](https://github.com/sindredg/entra-app-roles-sso-scim)

The workforce identity lifecycle for self-hosted Grafana, with Entra ID as the
identity provider. OpenID Connect SSO with app-role mapping, and SCIM
provisioning through a custom bridge.

`OpenID Connect` `SCIM` `App Roles` `Grafana` `Azure IaaS` `Docker`

### [Apps, APIs & Access Tokens: OAuth 2.0 in .NET 8](https://github.com/sindredg/app-registrations-and-JWT-tokens)

An Entra ID authorization chain with a protected API and both web and daemon
clients. Access is modelled through scopes, app roles and groups, then enforced
from token claims in the API itself.

`.NET 8` `OAuth 2.0` `OpenID Connect` `App Roles` `App Registrations`

---

## Networking & security

### [Azure Hub-and-Spoke with Cross-Premises Connectivity](https://github.com/sindredg/hybrid-network-az)

A hub-and-spoke network joined to a simulated on-premises datacenter in another
region over an encrypted IPsec tunnel, built one mechanism at a time. Forced
routing through Azure Firewall, Key Vault behind a private endpoint, and
two-way DNS resolution across the tunnel.

`Terraform` `Azure Firewall` `VPN Gateway` `UDRs` `Private DNS` `Private Endpoint`

### [Securing AI with MCP Server and RBAC](https://github.com/sindredg/claude-azure-mcp-rbac-design)

Scoped, read-only Azure access for Claude through the Azure MCP Server, with
Azure RBAC as the authoritative control rather than a convention. Host and
server hardening as defence in depth.

`Azure MCP Server` `Azure RBAC` `Service Principal` `Claude`
