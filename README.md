<img src="assets/header.svg" alt="Sindre Grytebust" width="100%">

<p align="center">
  <a href="#featured-project">Featured project</a> &emsp;&emsp;
  <a href="#more-projects">Selected work</a> &emsp;&emsp;
  <a href="https://github.com/sindredg?tab=repositories">All repositories</a>
</p>

<p align="center">Cloud platforms and the identity systems around them.<br><sub>Build notes, architecture decisions, testing, and troubleshooting.</sub></p>

<br>

<!-- Editing guide: docs/updating-profile.md. All project content is inside the marked blocks. -->
<a name="featured-project"></a>
<h2><img src="assets/featured.svg" alt="Featured project" width="100%"></h2>

<!-- FEATURED:START. Replace this whole block to switch the main project. -->
<table>
<tr><td colspan="3">
<br>
<sub>Completed lab on Google Cloud</sub>
<h2>Kubernetes disaster recovery</h2>
<p>Recovering a stateful service after losing a whole region. Gitea and PostgreSQL run on a kubeadm cluster built on VMs. Three drills stopped the primary region, rebuilt the cluster from code in a second region, restored an offsite backup, and moved the public name to it.</p>
<p><a href="https://github.com/sindredg/k8s-dr"><strong>Explore the project</strong></a> &emsp; <a href="https://github.com/sindredg/k8s-dr#results">Results</a> &emsp; <a href="https://github.com/sindredg/k8s-dr/tree/main/docs/decisions">Decisions</a> &emsp; <a href="https://github.com/sindredg/k8s-dr/tree/main/docs/worklogs">Worklogs</a> &emsp; <a href="https://github.com/sindredg/k8s-dr/blob/main/docs/runbooks/regional-recovery.md">Recovery runbook</a></p>
<p><sub>All eight milestones complete in October 2026. Targets: recovery within 4 hours, at most 2 hours of data lost.</sub></p>
</td></tr>
<tr>
<td width="33%" valign="top"><strong>17 to 19 min</strong> from the first failed probe to a recovered service, in three drills</td>
<td width="33%" valign="top"><strong>10 min</strong> of data lost in the last drill, with backups every 15 minutes</td>
<td width="33%" valign="top"><strong>Under 30 s</strong> to restore a backup set; building the cluster takes the rest</td>
</tr>
</table>

<p><code>Google Cloud</code> <code>Terraform</code> <code>Ansible</code> <code>kubeadm</code> <code>Flux</code> <code>SOPS</code> <code>PostgreSQL</code> <code>Gitea</code></p>

<details>
<summary><strong>Under the hood:</strong> rebuild, backups, and the drill</summary>

- **Rebuild from code:** one Terraform module for both regions, Ansible and kubeadm for the cluster, and Flux with SOPS for everything on it. The recovery region has no VMs until a drill.
- **Backups:** PostgreSQL and the Gitea volume captured at one consistent point, encrypted with age, and stored in another region. The writer cannot delete or overwrite a set, and a restore verifies every digest first.
- **The drill:** an external uptime check starts the clock, a write every five minutes measures data loss, and each stage is timed. A DNS change moves the public name, and the returning primary is fenced from the backups.

</details>
<!-- FEATURED:END -->

<br>

<a name="more-projects"></a>
<h2><img src="assets/selected.svg" alt="Selected work" width="100%"></h2>

<!-- SELECTED:START. Each td is one card. Keep two cards per tr, or use colspan="2" for one full-width card. -->
<table>
<tr>
<td colspan="2" valign="top">
<h3><a href="https://github.com/sindredg/k8-lab">Kubernetes platform &amp; AI security triage</a></h3>
<p>A private GKE cluster serving public workloads. Keyless delivery, measured rollouts, failure drills, and an AI agent that triages security findings. 125 req/s across 8 Pods with no failures; connection failures during rollouts cut from 72 to 0.</p>
<sub>Terraform, GKE, GitHub Actions, Cloud Armor, Vertex AI, Go</sub><br><br>
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
