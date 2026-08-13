**About**

> The projects below are built and tested in real environments and documented with
> implementation workflows, architecture overviews, design decisions, trade-offs,
> validation evidence and troubleshooting records.

---

## Projects

| Project | What it is | Stack |
| --- | --- | --- |
| [**Azure Container App with Terraform**](https://github.com/sindredg/container-app-in-azure) | **In-progress** | Terraform ·Docker · Nginx · Azure Container Apps · Managed Identity · Log Analytics |
| [**Two Sites, Hybrid Identities, Security Baselines**](https://github.com/sindredg/two-site-hybrid-identity) | Two-site Active Directory forest in Azure, synchronized with Entra ID. Features hybrid-joined endpoints and users, per-machine LAPS credentials, policy-enforced tiered privileged access, and private networks. Built throughout with Terraform and idempotent PowerShell. | Terraform · Azure · Entra ID · Active Directory · Windows Server · Group Policy · Windows LAPS · PowerShell · Entra Connect Sync · GitHub Actions |
| [**Access Control & Identity Governance**](https://github.com/sindredg/Access-Control-and-Identity-Governance) | Governs tenant-wide access and access to in-house applications with Entra ID: Conditional Access, just-in-time administration with PIM, entitlement management and access reviews. | Entra ID · Conditional Access · PIM · FIDO2 · Access Reviews · SSO · SCIM · Microsoft Graph PowerShell |
| [**Workforce Identity Lifecycle (SSO + SCIM) for a Self-Hosted App**](https://github.com/sindredg/entra-app-roles-sso-scim) | Implements the workforce identity lifecycle for self-hosted Grafana: Entra ID as the identity provider, OpenID Connect SSO with app-role mapping, and SCIM provisioning through a custom bridge. | OpenID Connect · SSO · SCIM · Grafana · App Roles · Azure IaaS · Docker |
| [**Apps, APIs & Access Tokens: OAuth 2.0 in .NET 8**](https://github.com/sindredg/app-registrations-and-JWT-tokens) | Builds an Entra ID authorization chain with a protected API and web and daemon clients. Access is modeled through scopes, app roles and groups, then enforced from token claims in a .NET 8 API. | .NET 8 · OAuth 2.0 · OpenID Connect · App Roles · App Registrations · Application Permissions |
