<img src="assets/header.svg" alt="Sindre Grytebust" width="100%">

<p align="center">
  <a href="#more-projects"><img src="assets/nav-selected.svg" alt="Selected work" height="40"></a>
  &nbsp;
  <a href="https://github.com/sindredg?tab=repositories"><img src="assets/nav-repositories.svg" alt="All repositories" height="40"></a>
</p>

<br>

<!-- Editing guide: docs/updating-profile.md. All project content is inside the marked blocks. -->
<a name="more-projects"></a>
<h2><img src="assets/selected.svg" alt="Selected work" width="100%"></h2>

<!-- SELECTED:START. Each td is one card. Keep two cards per tr, or use colspan="2" for one full-width card. -->
<table>
<tr>
<td width="50%" valign="top">
<img src="assets/guard.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/ai-security-platform">AI security operations platform</a></h3>
<p>Self-hosted AI workers that investigate security findings and propose fixes. Isolated platform and target networks, no public addresses, and a single egress point. In progress.</p>
<sub>Azure, Terraform, K3s, self-hosted LLM</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/recovery.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/k8s-dr">Kubernetes disaster recovery</a></h3>
<p>Recovering a stateful service after losing a region. Three drills rebuilt a kubeadm cluster from code in a second region and restored an offsite backup in under 20 minutes.</p>
<sub>Google Cloud, Terraform, Ansible, Flux</sub><br><br>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/cluster.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/k8-lab">Private GKE platform</a></h3>
<p>A private GKE cluster that served public workloads, built with Terraform and deployed from GitHub Actions without a stored key. An AI agent triaged its security findings.</p>
<sub>GKE, Terraform, GitHub Actions</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/identity.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/cross-cloud-entra-aws">Entra ID federation to AWS</a></h3>
<p>Workforce access to AWS managed from Entra ID: SAML sign-in, SCIM provisioning, access packages with approval and expiry, and joiner, mover, and leaver workflows.</p>
<sub>Entra ID, AWS, Terraform</sub><br><br>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/network.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/hybrid-network-az">Azure hybrid networking</a></h3>
<p>A hub-and-spoke network joined to an external network by an IPsec tunnel, with a hub firewall, private endpoints, and DNS that resolves in both directions.</p>
<sub>Azure, VPN, Private Link</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/governance.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/Access-Control-and-Identity-Governance">Entra ID access governance</a></h3>
<p>Conditional Access and risk-based policies, just-in-time administration with PIM, and recurring access reviews for a self-hosted Grafana.</p>
<sub>Entra ID, Conditional Access, PIM</sub><br><br>
</td>
</tr>
</table>
<!-- SELECTED:END -->

<!-- ARCHIVE:START. One Markdown bullet per project. Add, remove, or reorder freely. -->
<details>
<summary><strong>Other projects</strong></summary>

- **[Web app on Azure Container Apps](https://github.com/sindredg/container-app-in-azure)**: A public web tier and an internal API, built with Terraform. Images are pulled with a managed identity, so no registry password exists.
- **[AI security triage](https://github.com/sindredg/ai-k8s)**: The triage agent for the private GKE platform: rules first, then a model with scoped access, and an auditable ledger of verdicts.
- **[Two-site hybrid identity](https://github.com/sindredg/two-site-hybrid-identity)**: An Active Directory forest in Azure synced to Entra ID, serving a branch office in a second region, with hybrid-joined clients hardened through Group Policy and Windows LAPS.
- **[Grafana SSO & provisioning](https://github.com/sindredg/entra-app-roles-sso-scim)**: OIDC sign-in to a self-hosted Grafana, with Entra groups mapped to Grafana roles and accounts created and disabled through a custom SCIM bridge.
- **[OAuth 2.0 in .NET](https://github.com/sindredg/app-registrations-and-JWT-tokens)**: A protected API, a web client, and a daemon registered in Entra ID, with the API enforcing scopes and app roles from token claims.
- **[Read-only Azure access for Claude](https://github.com/sindredg/claude-azure-mcp-rbac-design)**: A dedicated service principal with Reader on one resource group, used through the Azure MCP Server.

</details>
<!-- ARCHIVE:END -->

<br>

---

<p align="center"><sub>Notes on building and testing cloud infrastructure.</sub></p>
