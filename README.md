**About**

>The projects below are tested in a real environment and documented.
>They include workflows, architecture overviews, design decisions, tradeoffs, troubleshooting steps
>and more.
---

## Projects

| Project | What it is | Stack |
| --- | --- | --- |
| [**Forest to Cloud: Cross-Region Hybrid Identity Infrastructure**](https://github.com/sindredg/two-site-hybrid-identity) | On-prem style Active Directory forest hosted in Azure spanning two regions. Azure infrastructure declared in Terraform. Client endpoints hybrid-joined to Active Directory and Entra ID. Group Policy linked against the OU structure and verified. Security baselines and Windows LAPS coming up next. Built from scratch. | Terraform · Azure · Active Directory · Windows Server · Group Policy · PowerShell · Entra ID · Entra Connect |
| [**Access Control & Identity Governance**](https://github.com/sindredg/Access-Control-and-Identity-Governance) | Governs access tenant wide and to in-house apps with Entra ID: tenant-wide Conditional Access, just-in-time admin access with PIM, and identity governance through entitlement management and access reviews. | Entra ID · Conditional Access · PIM · FIDO2 · Access Reviews · SSO · SCIM · Microsoft Graph PowerShell |
| [**Securing AI with MCP Server and RBAC**](https://github.com/sindredg/claude-azure-mcp-rbac-design) | Gives Claude scoped read-only access to Azure through the Azure MCP Server, with RBAC as the authoritative control, the host and server hardened as defense in depth. | Azure MCP Server · Entra ID · Azure RBAC · Service Principal · Claude |
| [**Workforce Identity Lifecycle (SSO + SCIM) for a Self-Hosted App**](https://github.com/sindredg/entra-app-roles-sso-scim) | Runs the full workforce identity lifecycle against self-hosted Grafana: Entra ID as IdP, OIDC SSO with app-role mapping, and SCIM provisioning through a custom bridge. Built from scratch. | Entra ID · OIDC · SCIM · Grafana · App Roles · Azure IaaS · Docker |
| [**Apps, APIs & Access Tokens: OAuth 2.0 in .NET 8**](https://github.com/sindredg/app-registrations-and-JWT-tokens) | Builds the full Entra ID authorization chain: a protected API with web and daemon clients, driving access through scopes, app roles, and groups, enforced from token claims in a .NET 8 API. | Entra ID · .NET 8 · OAuth 2.0 · App Roles · App registrations |
