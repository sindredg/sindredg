<img src="assets/header.svg" alt="Sindre Grytebust — Infrastructure. Identity. Security. Built in the cloud. Tested in practice." width="100%">

<p align="center">
  <a href="#featured-project">In focus</a> &nbsp; · &nbsp;
  <a href="#more-projects">Selected work</a> &nbsp; · &nbsp;
  <a href="https://github.com/sindredg?tab=repositories">All repositories ↗</a>
</p>

<p align="center">Cloud platforms and the identity systems around them.<br><sub>Real deployments, architecture decisions, failure drills, and the things that broke.</sub></p>

<br>

<!-- Editing guide: docs/updating-profile.md. All project content is inside the marked blocks. -->
<a name="featured-project"></a>
<h2><img src="assets/featured.svg" alt="In focus" width="100%"></h2>

<!-- FEATURED:START — Replace this whole block to switch the main project. -->
<table>
<tr><td>
<br>
<sub>COMPLETED LAB &nbsp; / &nbsp; GOOGLE CLOUD + KUBERNETES</sub>
<h2>Kubernetes platform &amp; AI security triage</h2>
<p>A private GKE cluster serving public workloads. Keyless delivery, measured rollouts, failure drills, and an AI agent that triages security findings.</p>
<p><a href="https://github.com/sindredg/k8-lab"><strong>Explore the project ↗</strong></a> &nbsp; · &nbsp; <a href="https://github.com/sindredg/k8-lab/blob/main/decisions.md">Decisions</a> &nbsp; · &nbsp; <a href="https://github.com/sindredg/k8-lab/tree/main/worklog">Worklogs</a></p>
<a href="https://github.com/sindredg/k8-lab/blob/main/worklog/shutdown.md"><img src="https://raw.githubusercontent.com/sindredg/k8-lab/main/images/shutdown-final-home.png" alt="The sindrg.com homepage on the final day of the GKE deployment" width="100%"></a>
<p><sub>Ran at sindrg.com from August to 25 September 2026. Infrastructure shut down; code, worklogs, and evidence preserved.</sub></p>
</td></tr>
</table>

<table>
<tr>
<td width="33%" align="center"><h2>125 req/s</h2><sub>8 PODS · NO FAILURES</sub><br><br></td>
<td width="33%" align="center"><h2>70.5 s</h2><sub>MEDIAN DEPLOYMENT</sub><br><br></td>
<td width="33%" align="center"><h2>72 → 0</h2><sub>ROLLOUT CONNECTION FAILURES</sub><br><br></td>
</tr>
</table>

<p><code>Terraform</code> <code>GKE</code> <code>GitHub Actions</code> <code>Cloud Armor</code> <code>Vertex AI</code> <code>Go</code></p>

<details>
<summary><strong>Under the hood</strong> — platform, delivery, and AI triage</summary>

- **Platform:** private nodes, custom VPC, Cloud NAT, Gateway API, managed TLS, and autoscaling across three zones.
- **Delivery & operations:** keyless federation, immutable images, gated rollouts, default-deny networking, Cloud Armor, and failure drills.
- **[AI triage](https://github.com/sindredg/ai-k8s):** Security Command Center findings flow through Pub/Sub to a worker with four scoped grants. Rules run before Vertex AI; verdicts go to an append-only ledger.

</details>
<!-- FEATURED:END -->

<br>

<a name="more-projects"></a>
<h2><img src="assets/selected.svg" alt="Selected work" width="100%"></h2>

<!-- SELECTED:START — Each td is one card. Keep two cards per tr, or use colspan="2" for one full-width card. -->
<table>
<tr>
<td width="50%" valign="top">
<img src="assets/identity.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/cross-cloud-entra-aws">Entra ID → AWS ↗</a></h3>
<p>Workforce identity across clouds. Federation, SCIM provisioning, and governed access to AWS.</p>
<sub>ENTRA ID &nbsp; / &nbsp; AWS &nbsp; / &nbsp; TERRAFORM</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/network.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/hybrid-network-az">Azure hybrid networking ↗</a></h3>
<p>Hub-and-spoke networking with an encrypted cross-premises tunnel, private endpoints, and two-way DNS.</p>
<sub>AZURE &nbsp; / &nbsp; VPN &nbsp; / &nbsp; PRIVATE LINK</sub><br><br>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<img src="assets/hybrid.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/two-site-hybrid-identity">Two sites. One identity. ↗</a></h3>
<p>A two-site Active Directory forest synced to Entra ID, with hybrid endpoints and policy-enforced security baselines.</p>
<sub>AD DS &nbsp; / &nbsp; ENTRA ID &nbsp; / &nbsp; POWERSHELL</sub><br><br>
</td>
<td width="50%" valign="top">
<img src="assets/containers.svg" alt="" width="100%">
<h3><a href="https://github.com/sindredg/container-app-in-azure">Azure Container Apps ↗</a></h3>
<p>A public web tier and private API, with passwordless image pulls, scale-to-zero, and automated delivery.</p>
<sub>TERRAFORM &nbsp; / &nbsp; CONTAINERS &nbsp; / &nbsp; CI/CD</sub><br><br>
</td>
</tr>
</table>
<!-- SELECTED:END -->

<!-- ARCHIVE:START — One Markdown bullet per project. Add, remove, or reorder freely. -->
<details>
<summary><strong>More from the workbench ↗</strong></summary>

- **[AI security triage](https://github.com/sindredg/ai-k8s)** — Rules, scoped model access, and an auditable verdict ledger for cloud security findings.
- **[Identity governance](https://github.com/sindredg/Access-Control-and-Identity-Governance)** — Conditional Access, just-in-time administration with PIM, and access reviews.
- **[Grafana SSO & provisioning](https://github.com/sindredg/entra-app-roles-sso-scim)** — OIDC sign-in, app-role mapping, and a custom SCIM bridge.
- **[Sky](https://github.com/sindredg/sky)** — An application deployed on the Kubernetes platform.
- **[OAuth 2.0 in .NET](https://github.com/sindredg/app-registrations-and-JWT-tokens)** — API authorization through scopes, app roles, groups, and token claims.
- **[Azure MCP & RBAC](https://github.com/sindredg/claude-azure-mcp-rbac-design)** — Scoped, read-only Azure access for Claude, enforced through Azure RBAC.

</details>
<!-- ARCHIVE:END -->

<br>

---

<p align="center"><sub>BUILD IT. &nbsp; TEST IT. &nbsp; WRITE IT DOWN.</sub></p>
