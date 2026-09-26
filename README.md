<p align="center">
  <img src="assets/header.svg?v=3" alt="Sindre Grytebust — cloud infrastructure and identity" width="100%">
</p>

<p align="center">
  I build cloud platforms and the identity systems around them.<br>
  <sub>Real deployments. Measured behaviour. Decisions, trade-offs, and the things that broke.</sub>
</p>

<p align="center">
  <a href="#featured-project">Featured project</a> &nbsp; / &nbsp;
  <a href="#more-projects">More projects</a> &nbsp; / &nbsp;
  <a href="https://github.com/sindredg?tab=repositories">All repositories</a>
</p>

<!--
PROFILE EDITING: Only the two marked sections below contain project content.
Swap the featured block; add, remove, or reorder individual archive rows.
Optional content can be deleted entirely. No empty slots or "coming soon" text needed.
See docs/updating-profile.md for the short editing guide.
-->

## Featured project

<!-- FEATURED:START — Keep everything specific to the main project inside this block. -->
### [Kubernetes platform & AI security triage](https://github.com/sindredg/k8-lab)

A private GKE cluster serving public workloads, with keyless delivery, failure drills, and an AI agent that triages security findings. Built with Terraform and documented from the first network decision to the final shutdown.

**Completed lab** · Ran at sindrg.com from August to 25 September 2026. The infrastructure is shut down; the code, worklogs, and evidence remain.

| Load tested | Delivery measured | Rollouts improved |
| :--- | :--- | :--- |
| **125 requests/s** across 8 Pods, no failures | **70.5 s** median deployment | **72 → 0** connection failures |

[Explore the code](https://github.com/sindredg/k8-lab) · [Architecture decisions](https://github.com/sindredg/k8-lab/blob/main/decisions.md) · [Build & validation log](https://github.com/sindredg/k8-lab/tree/main/worklog)

<details>
<summary>Inside the platform</summary>

<br>

<img src="https://raw.githubusercontent.com/sindredg/k8-lab/main/images/shutdown-final-home.png" alt="The sindrg.com homepage on the final day of the GKE deployment" width="100%">

- **Platform:** private nodes, custom VPC, Cloud NAT, Gateway API, managed TLS, and autoscaling across three zones.
- **Delivery & operations:** keyless federation, immutable images, gated rollouts, default-deny networking, Cloud Armor, and failure drills.
- **[AI triage](https://github.com/sindredg/ai-k8s):** Security Command Center findings flow through Pub/Sub to a worker with four scoped grants. Rules run before Vertex AI; verdicts go to an append-only ledger.

[Final screenshots & shutdown notes](https://github.com/sindredg/k8-lab/blob/main/worklog/shutdown.md)

</details>

<sub>Terraform · GKE · Kubernetes · GitHub Actions · Cloud Armor · Vertex AI · Go</sub>
<!-- FEATURED:END -->

## More projects

<!-- ARCHIVE:START — One project per row. Move a former featured project here; delete rows you no longer want. -->
| Project | What I explored |
| :--- | :--- |
| [AI security triage](https://github.com/sindredg/ai-k8s) | Rules, scoped model access, and an auditable verdict ledger for cloud security findings. |
| [Entra ID → AWS](https://github.com/sindredg/cross-cloud-entra-aws) | Workforce federation, SCIM provisioning, and governed access across clouds. |
| [Hybrid identity](https://github.com/sindredg/two-site-hybrid-identity) | Two-site Active Directory, Entra ID sync, and policy-enforced security baselines. |
| [Identity governance](https://github.com/sindredg/Access-Control-and-Identity-Governance) | Conditional Access, just-in-time administration with PIM, and access reviews. |
| [Grafana SSO & provisioning](https://github.com/sindredg/entra-app-roles-sso-scim) | OIDC sign-in, app-role mapping, and a custom SCIM bridge. |
| [Azure hybrid networking](https://github.com/sindredg/hybrid-network-az) | Hub-and-spoke networking, cross-premises VPN, private endpoints, and two-way DNS. |
| [Azure Container Apps](https://github.com/sindredg/container-app-in-azure) | A public web tier, private API, managed identities, and automated delivery. |
| [Sky](https://github.com/sindredg/sky) | An application deployed on the Kubernetes platform. |
| [OAuth 2.0 in .NET](https://github.com/sindredg/app-registrations-and-JWT-tokens) | API authorization through scopes, app roles, groups, and token claims. |
| [Azure MCP & RBAC](https://github.com/sindredg/claude-azure-mcp-rbac-design) | Scoped, read-only Azure access for Claude, enforced through Azure RBAC. |
<!-- ARCHIVE:END -->

---

<p align="center"><sub>Built, tested, and documented — including the parts that did not go to plan.</sub></p>
