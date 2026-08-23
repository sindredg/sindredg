**About**

> The projects below are built and tested in real environments and documented with
> implementation workflows, architecture overviews, design decisions, trade-offs,
> validation evidence and troubleshooting records.

---

## Projects

| Project | What it is | Stack |
| --- | --- | --- |
| [**Azure Hub-and-Spoke with Cross-Premises Connectivity**](https://github.com/sindredg/hybrid-network-az) | Hub-and-spoke network in Azure joined to a simulated on-premises datacenter in another region over an encrypted IPsec tunnel, built one mechanism at a time. Gateway transit, subnet NSGs, Bastion access, forced routing through Azure Firewall, Key Vault behind a private endpoint, and two-way DNS across the tunnel. | Terraform · Azure Firewall · VPN Gateway · UDRs · Private DNS · Private Endpoint · GitHub Actions · OIDC · RBAC |
| [**Azure Container Platform**](https://github.com/sindredg/container-app-in-azure) | A public web tier and an internal API on Azure Container Apps, deployed entirely with Terraform. The API has no public address. Passwordless managed-identity image pulls, health probes, revisions, scale-to-zero, remote state with locking, and centralised logging. A database and automated delivery are next. | Terraform · Azure Container Apps · ACR · Managed Identity · CI/CD · Docker · Nginx · Python/FastAPI |
| [**Two Sites, Hybrid Identities, Security Baselines**](https://github.com/sindredg/two-site-hybrid-identity) | Two-site Active Directory forest in Azure, synchronized with Entra ID. Features hybrid-joined endpoints and users, per-machine LAPS credentials, policy-enforced tiered privileged access, and private networks. Built throughout with Terraform and idempotent PowerShell. | Terraform · Azure · Entra ID · Active Directory · Windows Server · Group Policy · Windows LAPS · PowerShell · Entra Connect Sync · GitHub Actions |
| [**Access Control & Identity Governance**](https://github.com/sindredg/Access-Control-and-Identity-Governance) | Governs tenant-wide access and access to in-house applications with Entra ID: Conditional Access, just-in-time administration with PIM, entitlement management and access reviews. | Entra ID · Conditional Access · PIM · FIDO2 · Access Reviews · SSO · SCIM · Microsoft Graph PowerShell |
| [**SSO + SCIM for a Self-Hosted App**](https://github.com/sindredg/entra-app-roles-sso-scim) | Implements the workforce identity lifecycle for self-hosted Grafana: Entra ID as the identity provider, OpenID Connect SSO with app-role mapping, and SCIM provisioning through a custom bridge. | OpenID Connect · SSO · SCIM · Grafana · App Roles · Azure IaaS · Docker |
| [**Securing AI with MCP Server and RBAC**](https://github.com/sindredg/claude-azure-mcp-rbac-design) | Gives Claude scoped, read-only access to Azure through the Azure MCP Server, with Azure RBAC as the authoritative control and host/server hardening as defense in depth. | Azure MCP Server · Azure RBAC · Service Principal · Claude |
| [**Apps, APIs & Access Tokens: OAuth 2.0 in .NET 8**](https://github.com/sindredg/app-registrations-and-JWT-tokens) | Builds an Entra ID authorization chain with a protected API and web and daemon clients. Access is modeled through scopes, app roles and groups, then enforced from token claims in a .NET 8 API. | .NET 8 · OAuth 2.0 · OpenID Connect · App Roles · App Registrations · Application Permissions |
