<img src="assets/header.svg" alt="Sindre Grytebust" width="100%">

<p align="center">
  <a href="https://github.com/sindredg?tab=repositories"><img src="assets/nav-repositories.svg" alt="All repositories" height="40"></a>
</p>

<!-- Editing guide: docs/updating-profile.md. All project content is inside the marked blocks. -->
<p><img src="assets/selected.svg" alt="Selected work" width="100%"></p>

<!-- SELECTED:START. Each td is one card and each table is one row of two cards. A table with a single td makes a full-width card. -->
<table>
<tr>
<td width="50%" valign="top">
<img src="assets/guard.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/ai-security-platform">AI Security Platform</a></h3>
<p>Self-hosted AI workers that investigate security findings and propose fixes. Isolated platform and target networks, no public addresses, and a single egress point. Actively building.</p>
<sub>Azure, Terraform, K3s, self-hosted LLM</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/recovery.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/k8s-dr">Automated Regional Disaster Recovery</a></h3>
<p>Automated outage detection, infrastructure rebuilds, backup restoration, and DNS cutover for Gitea and PostgreSQL on self-managed Kubernetes. Validated in two consecutive unattended drills: recovery within 36 minutes, with under 11 minutes of data loss.</p>
<sub>Google Cloud, Terraform, Ansible, Flux, GitHub Actions</sub><br><br>
</td>
</tr>
</table>
<table>
<tr>
<td width="50%" valign="top">
<img src="assets/cluster.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/k8-lab">Private GKE Cluster</a></h3>
<p>A private GKE cluster that served public workloads, built with Terraform and deployed from GitHub Actions without a stored key. An AI agent triaged its security findings.</p>
<sub>GKE, Terraform, GitHub Actions</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/identity.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/cross-cloud-entra-aws">Entra ID to AWS</a></h3>
<p>Workforce access to AWS managed from Entra ID: SAML sign-in, SCIM provisioning, access packages with approval and expiry, and joiner, mover, and leaver workflows.</p>
<sub>Entra ID, AWS, Terraform</sub><br><br>
</td>
</tr>
</table>
<table>
<tr>
<td width="50%" valign="top">
<img src="assets/network.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/hybrid-network-az">Azure Hybrid Network</a></h3>
<p>A hub-and-spoke network joined to an external network by an IPsec tunnel, with a hub firewall, private endpoints, and DNS that resolves in both directions.</p>
<sub>Azure, VPN, Private Link</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/governance.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/Access-Control-and-Identity-Governance">Access Governance</a></h3>
<p>Conditional Access and risk-based policies, just-in-time administration with PIM, and recurring access reviews for a self-hosted Grafana.</p>
<sub>Entra ID, Conditional Access, PIM</sub><br><br>
</td>
</tr>
</table>
<!-- SELECTED:END -->

<!-- ARCHIVE:START. One Markdown bullet per project. Add, remove, or reorder freely. -->
<details>
<summary><strong>Other projects</strong></summary>

- **[Azure Container Apps](https://github.com/sindredg/container-app-in-azure)**: A public web tier and an internal API, built with Terraform. Images are pulled with a managed identity, so no registry password exists.
- **[Two-Site Hybrid Identity](https://github.com/sindredg/two-site-hybrid-identity)**: An Active Directory forest across two Azure regions, synced to Entra ID, with hybrid join, Windows LAPS, security baselines, and tiered administration.
- **[Entra ID SSO and SCIM for Grafana](https://github.com/sindredg/entra-app-roles-sso-scim)**: Entra ID as the identity provider for a self-hosted Grafana: OIDC sign-in, groups mapped to Grafana roles through app roles, and SCIM provisioning through a custom bridge.

</details>
<!-- ARCHIVE:END -->

<br>

---

<p align="center"><sub>Notes on building and testing cloud infrastructure.</sub></p>
