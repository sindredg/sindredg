<img src="assets/header.svg" alt="Sindre Grytebust" width="100%">

<p align="center">
  <a href="#more-projects"><img src="assets/nav-selected.svg" alt="Selected work" height="40"></a>
  &nbsp;
  <a href="https://github.com/sindredg?tab=repositories"><img src="assets/nav-repositories.svg" alt="All repositories" height="40"></a>
</p>

<p align="center"><sub>Cloud platforms and the identity systems around them.<br>Build notes, architecture decisions, testing, and troubleshooting.</sub></p>

<br>

<!-- Editing guide: docs/updating-profile.md. All project content is inside the marked blocks. -->
<a name="more-projects"></a>
<h2><img src="assets/selected.svg" alt="Selected work" width="100%"></h2>

<!-- SELECTED:START. Each td is one card. Keep two cards per tr, or use colspan="2" for one full-width card. -->
<table>
<tr>
<td width="50%" valign="top">
<img src="assets/recovery.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/k8s-dr">Kubernetes disaster recovery</a></h3>
<p>Recovering a stateful service after losing a region. Three drills rebuilt a kubeadm cluster from code in a second region and restored an offsite backup in under 20 minutes.</p>
<sub>Google Cloud, Terraform, Ansible, Flux</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/cluster.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/k8-lab">Kubernetes platform</a></h3>
<p>A private GKE cluster serving public workloads, with keyless delivery, measured rollouts, failure drills, and an AI agent that triages security findings.</p>
<sub>GKE, Terraform, GitHub Actions</sub><br><br>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/identity.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/cross-cloud-entra-aws">Entra ID → AWS</a></h3>
<p>Workforce identity across clouds. Federation, SCIM provisioning, and governed access to AWS.</p>
<sub>Entra ID, AWS, Terraform</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/network.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/hybrid-network-az">Azure hybrid networking</a></h3>
<p>Hub-and-spoke networking with an encrypted cross-premises tunnel, private endpoints, and two-way DNS.</p>
<sub>Azure, VPN, Private Link</sub><br><br>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/hybrid.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/two-site-hybrid-identity">Two-site hybrid identity</a></h3>
<p>A two-site Active Directory forest synced to Entra ID, with hybrid endpoints and policy-enforced security baselines.</p>
<sub>AD DS, Entra ID, PowerShell</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/containers.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/container-app-in-azure">Azure Container Apps</a></h3>
<p>A public web tier and private API, with passwordless image pulls, scale-to-zero, and automated delivery.</p>
<sub>Terraform, containers, CI/CD</sub><br><br>
</td>
</tr>
</table>
<!-- SELECTED:END -->

<!-- ARCHIVE:START. One Markdown bullet per project. Add, remove, or reorder freely. -->
<details>
<summary><strong>Other projects</strong></summary>

- **[AI security triage](https://github.com/sindredg/ai-k8s)**: Rules, scoped model access, and an auditable verdict ledger for cloud security findings.
- **[Identity governance](https://github.com/sindredg/Access-Control-and-Identity-Governance)**: Conditional Access, just-in-time administration with PIM, and access reviews.
- **[Grafana SSO & provisioning](https://github.com/sindredg/entra-app-roles-sso-scim)**: OIDC sign-in, app-role mapping, and a custom SCIM bridge.
- **[Sky](https://github.com/sindredg/sky)**: An application deployed on the Kubernetes platform.
- **[OAuth 2.0 in .NET](https://github.com/sindredg/app-registrations-and-JWT-tokens)**: API authorization through scopes, app roles, groups, and token claims.
- **[Azure MCP & RBAC](https://github.com/sindredg/claude-azure-mcp-rbac-design)**: Scoped, read-only Azure access for Claude, enforced through Azure RBAC.

</details>
<!-- ARCHIVE:END -->

<br>

---

<p align="center"><sub>Notes on building and testing cloud infrastructure.</sub></p>
