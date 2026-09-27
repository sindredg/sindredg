<img src="assets/header.svg" alt="Sindre Grytebust: Infrastructure, Identity, Security" width="100%">

<p align="center">
  <a href="#featured-project">Featured project</a> &nbsp; · &nbsp;
  <a href="#more-projects">Selected work</a> &nbsp; · &nbsp;
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
<sub>Completed lab &nbsp; / &nbsp; Google Cloud + Kubernetes</sub>
<h2>Kubernetes platform &amp; AI security triage</h2>
<p>A private GKE cluster serving public workloads. Keyless delivery, measured rollouts, failure drills, and an AI agent that triages security findings.</p>
<p><a href="https://github.com/sindredg/k8-lab"><strong>Explore the project</strong></a> &nbsp; · &nbsp; <a href="https://github.com/sindredg/k8-lab/blob/main/decisions.md">Decisions</a> &nbsp; · &nbsp; <a href="https://github.com/sindredg/k8-lab/tree/main/worklog">Worklogs</a> &nbsp; · &nbsp; <a href="https://github.com/sindredg/k8-lab/blob/main/worklog/shutdown.md">Shutdown notes</a></p>
<p><sub>Infrastructure retired in September 2026; code, worklogs, and validation notes remain.</sub></p>
</td></tr>
<tr>
<td width="33%" align="center"><h3>125 req/s</h3><sub>8 Pods · no failures</sub><br><br></td>
<td width="33%" align="center"><h3>70.5 s</h3><sub>Median deployment</sub><br><br></td>
<td width="33%" align="center"><h3>72 → 0</h3><sub>Rollout connection failures</sub><br><br></td>
</tr>
</table>

<p><code>Terraform</code> <code>GKE</code> <code>GitHub Actions</code> <code>Cloud Armor</code> <code>Vertex AI</code> <code>Go</code></p>

<details>
<summary><strong>Under the hood:</strong> platform, delivery, and AI triage</summary>

- **Platform:** private nodes, custom VPC, Cloud NAT, Gateway API, managed TLS, and autoscaling across three zones.
- **Delivery & operations:** keyless federation, immutable images, gated rollouts, default-deny networking, Cloud Armor, and failure drills.
- **[AI triage](https://github.com/sindredg/ai-k8s):** Security Command Center findings flow through Pub/Sub to a worker with four scoped grants. Rules run before Vertex AI; verdicts go to an append-only ledger.

</details>
<!-- FEATURED:END -->

<br>

<a name="more-projects"></a>
<h2><img src="assets/selected.svg" alt="Selected work" width="100%"></h2>

<!-- SELECTED:START. Each td is one card. Keep two cards per tr, or use colspan="2" for one full-width card. -->
<table>
<tr>
<td width="50%" valign="top">
<img src="assets/identity.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/cross-cloud-entra-aws">Entra ID → AWS</a></h3>
<p>Workforce identity across clouds. Federation, SCIM provisioning, and governed access to AWS.</p>
<sub>ENTRA ID &nbsp; / &nbsp; AWS &nbsp; / &nbsp; TERRAFORM</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/network.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/hybrid-network-az">Azure hybrid networking</a></h3>
<p>Hub-and-spoke networking with an encrypted cross-premises tunnel, private endpoints, and two-way DNS.</p>
<sub>AZURE &nbsp; / &nbsp; VPN &nbsp; / &nbsp; PRIVATE LINK</sub><br><br>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/hybrid.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/two-site-hybrid-identity">Two-site hybrid identity</a></h3>
<p>A two-site Active Directory forest synced to Entra ID, with hybrid endpoints and policy-enforced security baselines.</p>
<sub>AD DS &nbsp; / &nbsp; ENTRA ID &nbsp; / &nbsp; POWERSHELL</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/containers.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/container-app-in-azure">Azure Container Apps</a></h3>
<p>A public web tier and private API, with passwordless image pulls, scale-to-zero, and automated delivery.</p>
<sub>TERRAFORM &nbsp; / &nbsp; CONTAINERS &nbsp; / &nbsp; CI/CD</sub><br><br>
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
