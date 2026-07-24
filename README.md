**About**

>The projects below are tested in a real tenant and documented. They include workflows, architecture overviews, design decisions, and tradeoffs are written down, not just the happy path.

---

## Projects

| Project | What it is | Stack |
| --- | --- | --- |
| [**Securing AI with MCP Server and RBAC**](https://github.com/sindredg/claude-azure-mcp-rbac-design) | Gives Claude scoped read-only access to Azure through the Azure MCP Server, with RBAC as the authoritative control, the host and server hardened as defense in depth. | Azure MCP Server · Entra ID · Azure RBAC · Service Principal · Claude |
| [**Workforce Identity Lifecycle (SSO + SCIM) for a Self-Hosted App**](https://github.com/sindredg/IAM-on-self-hosted-webapp) | Runs the full workforce identity lifecycle against self-hosted Grafana: Entra ID as IdP, OIDC SSO with app-role mapping, and SCIM provisioning through a custom bridge. | Entra ID · OIDC · SCIM · Grafana · Bicep · Python · Azure IaaS · Docker |
| [**Apps, APIs & Access Tokens: OAuth 2.0 in .NET 8**](https://github.com/sindredg/app-registrations-and-JWT-tokens) | Builds the full Entra ID authorization chain: a protected API with web and daemon clients, driving access through scopes, app roles, and groups, enforced from token claims in a .NET 8 API. | Entra ID · .NET 8 · OAuth 2.0 · App Roles · App registrations | 
