**About**

> The projects below are built and tested in real environments and documented with
> implementation workflows, architecture overviews, design decisions, trade-offs,
> validation evidence and troubleshooting records.

---

## Projects

| Project | What it is | Stack |
| --- | --- | --- |
| [**Forest to Cloud: Cross-Region Hybrid Identity Infrastructure**](https://github.com/sindredg/two-site-hybrid-identity) |Two-site Active Directory forest in Azure, synchronised to Entra ID. Hybrid-joined endpoints and users, per-machine LAPS credentials, tiered privileged access enforced by policy, and private networks. Terraform and idempotent PowerShell throughout. | Terraform · Azure · Entra ID · Active Directory · Windows Server · Group Policy · Windows LAPS · PowerShell · Entra Connect Sync · Github Actions |
| [**Access Control & Identity Governance**](https://github.com/sindredg/Access-Control-and-Identity-Governance) | Governs tenant-wide access and access to in-house applications with Entra ID: Conditional Access, just-in-time administration with PIM, entitlement management and access reviews. | Entra ID · Conditional Access · PIM · FIDO2 · Access Reviews · SSO · SCIM · Microsoft Graph PowerShell |
| [**Securing AI with MCP Server and RBAC**](https://github.com/sindredg/claude-azure-mcp-rbac-design) | Gives Claude scoped, read-only access to Azure through the Azure MCP Server, with Azure RBAC as the authoritative control and host/server hardening as defense in depth. | Azure MCP Server · Azure RBAC · Service Principal · Claude |
| [**Workforce Identity Lifecycle (SSO + SCIM) for a Self-Hosted App**](https://github.com/sindredg/entra-app-roles-sso-scim) | Implements the workforce identity lifecycle for self-hosted Grafana: Entra ID as the identity provider, OpenID Connect SSO with app-role mapping, and SCIM provisioning through a custom bridge. | OpenID Connect · SSO · SCIM · Grafana · App Roles · Azure IaaS · Docker |
| [**Apps, APIs & Access Tokens: OAuth 2.0 in .NET 8**](https://github.com/sindredg/app-registrations-and-JWT-tokens) | Builds an Entra ID authorization chain with a protected API and web and daemon clients. Access is modeled through scopes, app roles and groups, then enforced from token claims in a .NET 8 API. | .NET 8 · OAuth 2.0 · OpenID Connect · App Roles · App Registrations · Application Permissions |
