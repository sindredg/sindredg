<p align="center">
  <img src="assets/header.svg?v=3" alt="Sindre Grytebust, infrastructure and identity" width="100%">
</p>

<p align="center">
  <a href="https://github.com/sindredg/k8-lab"><img alt="Latest project" src="https://img.shields.io/badge/LATEST-k8--lab-f2b134?style=for-the-badge&labelColor=1f3b4d"></a>
  <a href="https://github.com/sindredg?tab=repositories"><img alt="Projects" src="https://img.shields.io/badge/EXPLORE-projects-f2b134?style=for-the-badge&logo=github&logoColor=f2b134&labelColor=1f3b4d"></a>
</p>

<p align="center">
  <strong>Cloud infrastructure and identity.</strong><br>
  <sub>Architecture decisions, measured behaviour, failure drills, trade-offs and the things that broke.</sub>
</p>

<p align="center">
  <img alt="Terraform" src="https://img.shields.io/badge/Terraform-1f3b4d?style=flat-square&logo=terraform&logoColor=f2b134">
  <img alt="Kubernetes" src="https://img.shields.io/badge/Kubernetes-1f3b4d?style=flat-square&logo=kubernetes&logoColor=f2b134">
  <img alt="Google Cloud" src="https://img.shields.io/badge/Google%20Cloud-1f3b4d?style=flat-square&logo=googlecloud&logoColor=f2b134">
  <img alt="Azure" src="https://img.shields.io/badge/Azure-1f3b4d?style=flat-square&logo=microsoftazure&logoColor=f2b134">
  <img alt="AWS" src="https://img.shields.io/badge/AWS-1f3b4d?style=flat-square&logo=amazonwebservices&logoColor=f2b134">
  <img alt="Entra ID" src="https://img.shields.io/badge/Entra%20ID-1f3b4d?style=flat-square&logo=microsoftentraid&logoColor=f2b134">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-1f3b4d?style=flat-square&logo=githubactions&logoColor=f2b134">
</p>

---

## Latest project

<h3 align="center">Kubernetes platform: Built, tested, secured and validated</h3>

<p align="center">
  <a href="https://github.com/sindredg/k8-lab"><img alt="Open repository" src="https://img.shields.io/badge/source-k8--lab-24292f?style=flat-square&logo=github&logoColor=white"></a>
  <a href="https://github.com/sindredg/k8-lab/blob/main/decisions.md"><img alt="Architecture decisions" src="https://img.shields.io/badge/read-decisions-4f6f82?style=flat-square"></a>
  <a href="https://github.com/sindredg/k8-lab/tree/main/worklog"><img alt="Implementation worklogs" src="https://img.shields.io/badge/inspect-worklogs-4f6f82?style=flat-square"></a>
</p>

A private GKE cluster hosting public workloads, and an AI agent that triages security findings. It ran at sindrg.com from late August until 25 September 2026, when I shut it down. The repo still has the Terraform, the decisions, a worklog for every phase and the [final screenshots](https://github.com/sindredg/k8-lab/blob/main/worklog/shutdown.md).

<p align="center">
  <img src="https://raw.githubusercontent.com/sindredg/k8-lab/main/images/shutdown-final-home.png" alt="sindrg.com on its last day" width="85%">
</p>

<table>
  <tr>
    <td align="center"><strong>125 rps</strong><br><sub>8 Pods, no failures</sub></td>
    <td align="center"><strong>394 ms</strong><br><sub>p95 under load</sub></td>
    <td align="center"><strong>70.5 s</strong><br><sub>median deploy</sub></td>
    <td align="center"><strong>0</strong><br><sub>rollout connection failures, from 72</sub></td>
  </tr>
  <tr>
    <td align="center"><strong>7 of 7</strong><br><sub>holdout findings right every run, rules alone 5</sub></td>
    <td align="center"><strong>0</strong><br><sub>false contradictions in 125 runs, from 15</sub></td>
    <td align="center"><strong>~2 s</strong><br><sub>p95 per model call</sub></td>
    <td align="center"><strong>0</strong><br><sub>critical or high in the frontend image, from 17</sub></td>
  </tr>
</table>

<details>
<summary><strong>What was inside</strong></summary>
<br>

<table>
  <tr>
    <td width="33%"><strong>Platform</strong><br><sub>Private nodes, custom VPC, Cloud NAT, Gateway API, managed TLS and autoscaling across three zones.</sub></td>
    <td width="33%"><strong>Delivery</strong><br><sub>Keyless federation, immutable images, required checks, gated rollouts and automated upstream pin updates.</sub></td>
    <td width="33%"><strong>Security and operations</strong><br><sub>Pod Security, default-deny networking, Cloud Armor, observability, failure drills and a measured threat model.</sub></td>
  </tr>
  <tr>
    <td colspan="3"><strong>AI triage</strong> in <a href="https://github.com/sindredg/ai-k8s">ai-k8s</a><br><sub>Security Command Center findings over Pub/Sub to a worker with four scoped grants. The model can never accept a finding, a contradiction must land on a control that applies, every verdict is written to an append-only ledger before anyone is told, and every failure path was drilled.</sub></td>
  </tr>
</table>

```mermaid
flowchart LR
    User((User)) --> Edge[Global Gateway<br/>TLS + Cloud Armor]
    Edge --> Nginx[nginx]
    Edge --> Sky[sky]
    Actions[GitHub Actions<br/>keyless delivery] --> Registry[Artifact Registry]
    Registry --> GKE[Private GKE nodes]
    GKE --> Nginx
    GKE --> Sky
    GKE -. logs and metrics .-> Monitor[Cloud Monitoring]
    SCC[Security Command Center] --> PubSub[Pub/Sub]
    PubSub --> Agent[Triage agent<br/>rules, then Vertex AI]
    Agent --> Ledger[Verdict ledger]
    Agent -. verdict .-> Monitor
```

</details>

<p align="center">
  <code>Terraform</code>&nbsp; <code>GKE</code>&nbsp; <code>Kubernetes</code>&nbsp;
  <code>Gateway API</code>&nbsp; <code>Cloud Armor</code>&nbsp;
  <code>Workload Identity Federation</code>&nbsp; <code>GitHub Actions</code>&nbsp; <code>k6</code>&nbsp;
  <code>Security Command Center</code>&nbsp; <code>Vertex AI</code>&nbsp; <code>Go</code>
</p>

---

## Project map

The rest of the work is grouped by the problem it explores. The larger labs include build notes,
architecture decisions, validation evidence and troubleshooting records.

| Area | Projects |
| --- | --- |
| **Identity across clouds** | [Entra ID to AWS IAM Identity Center](https://github.com/sindredg/cross-cloud-entra-aws) · [Two-site AD DS synced to Entra ID](https://github.com/sindredg/two-site-hybrid-identity) |
| **Identity governance** | [Conditional Access, PIM and access reviews](https://github.com/sindredg/Access-Control-and-Identity-Governance) · [OIDC SSO and SCIM for Grafana](https://github.com/sindredg/entra-app-roles-sso-scim) |
| **Azure platforms** | [Hub-and-spoke with cross-premises connectivity](https://github.com/sindredg/hybrid-network-az) · [Azure Container Apps platform](https://github.com/sindredg/container-app-in-azure) |
| **Applications and access** | [Sky](https://github.com/sindredg/sky) · [OAuth 2.0 and token claims in .NET 8](https://github.com/sindredg/app-registrations-and-JWT-tokens) · [Least-privilege Azure MCP access](https://github.com/sindredg/claude-azure-mcp-rbac-design) |

---

<p align="center">
  <img src="assets/footer.svg?v=3" alt="github.com/sindredg" width="100%">
</p>
