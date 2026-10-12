# AgentStudio OS: 50 Real-Time Revenue AI Agent Projects & Live Demos

> **Autonomous Real-Time Revenue Agent Orchestration Hub**  
> 50 Production-Ready AI Agent Project Workspaces with Live Execution Playgrounds & Stripe Settlement.

[![Live Demo](https://img.shields.io/badge/Live_Demo-GitHub_Pages-6366f1?style=for-the-badge&logo=github)](https://rajesh2901.github.io/agent-studio/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-emerald?style=for-the-badge&logo=python)](https://python.org)

🌐 **Live Hosted Web UI**: [https://rajesh2901.github.io/agent-studio/](https://rajesh2901.github.io/agent-studio/)

---

## ⚡ Quick Start

### 1. Launch via PowerShell or Batch
Run the provided one-click launcher:
```powershell
.\run.ps1
```
Or with Windows Command Prompt:
```cmd
run.bat
```

### 2. Manual Launch
```bash
python server.py
```
Open **[http://localhost:8050](http://localhost:8050)** in your browser.

---

## 🧭 Project Layout

```
agent-studio/
├── server.py              # Zero-dependency Python HTTP & REST API server
├── agents_data.py         # Complete database of 50 agent project schemas, steps & generators
├── GEMINI.md              # Project rules & execution permissions
├── run.ps1                # PowerShell one-click runner with auto-browser opening
├── run.bat                # Windows Batch one-click runner
├── README.md              # Documentation
└── static/
    └── index.html         # Rich 3-column obsidian dark-mode web application (Tailwind CSS)
```

---

## 🎯 Features per Agent Project

For every single one of the 50 ideas across 10 categories:
1. **Interactive Demo Playground:**
   - Tailored form inputs for custom parameters (cart value, line items, cloud burn rate, voice transcript, lease spec, etc.).
   - Visual execution DAG timeline (Steps 1–5).
   - Live streaming reasoning terminal with simulated sub-millisecond execution logs.
   - Synthesized output deliverable viewer with 1-click clipboard copy.
2. **Real-Time Monetization HUD:**
   - Dynamic real-time fee calculation (Commissions, Micro-transactions, Rev-share, Lead bounties).
   - Idempotency transaction tokens and unique Stripe charge IDs.
   - Live Stripe Webhook payload inspector (`charge.captured` event JSON).
   - Real-time session ledger showing all recent billing actions.
3. **Starter Code Scaffolder:**
   - Production-ready FastAPI + LLM orchestration + Stripe Connect starter code for every agent.
   - 1-click download button (`.py` export) for each project.
4. **Architecture & Tech Specs:**
   - Detailed target customer profile, monetization mechanics, and recommended technology stack.
