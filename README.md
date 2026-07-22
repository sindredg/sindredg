**About**

The repos below are hands-on labs: real tenants, real enforcement, tested with both positive and negative cases and documented. Design decisions and tradeoffs are written down, not just the happy path.

---

## Projects

| Project | Proof | What it is | Stack |
| --- | --- | --- | --- |
| [**Securing AI with MCP Server and RBAC**](https://github.com/sindredg/claude-azure-mcp-rbac-design) | Screenshots | Gives Claude scoped read-only access to Azure through the Azure MCP Server, with RBAC as the authoritative control, the host and server hardened as defense in depth. | Azure MCP Server · Entra ID · Azure RBAC · Service Principal · Anthropic |
| [**Workforce IAM on Self-Hosted Grafana Web App**](https://github.com/sindredg/IAM-on-self-hosted-webapp) | Screenshots | Runs the full workforce identity lifecycle against self-hosted Grafana: Entra ID as IdP, OIDC SSO with app-role mapping, and SCIM provisioning through a custom bridge. | Entra ID · OIDC · SCIM · Grafana · Bicep · Python · Docker | !
| [**App Registrations and JWT Tokens**](https://github.com/sindredg/app-registrations-and-JWT-tokens) | Screenshots | Builds the full Entra ID authorization chain: a protected API with web and daemon clients, driving access through scopes, app roles, and groups, enforced from token claims in a .NET 8 API. | Entra ID · .NET 8 · OAuth 2.0 · App Roles | 
| [**WinRM Field Guide**](https://github.com/sindredg/WinRM-Field-Guide) | | Field reference for WinRM: connectivity testing, auth settings, and the configs that break Azure Migrate and DMC discovery and data collection. | PowerShell · WinRM · Azure Migrate |
