#!/usr/bin/env python3
"""
AgentStudio OS: Real-Time AI Agent Portfolio & Execution Hub Server
Provides unified REST APIs and static UI serving for 50 autonomous AI agent demos.
"""

import sys
import os
import json
import time
import uuid
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# Import or define all 50 Agent Project Specs
from agents_data import AGENTS_DATABASE

PORT = int(os.getenv("PORT", 8050))
METRICS = {
    "totalGmv": 128450.00,
    "totalFeesCaptured": 14920.50,
    "activeDaemons": 18,
    "completedSimulations": 342,
    "transactions": []
}

class AgentStudioHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Serve static directory from project folder
        static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
        super().__init__(*args, directory=static_dir, **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/agents":
            self.send_json_response(200, AGENTS_DATABASE)
            return

        elif path.startswith("/api/agents/"):
            try:
                agent_id = int(path.split("/")[3])
                agent = next((a for a in AGENTS_DATABASE if a["id"] == agent_id), None)
                if agent:
                    self.send_json_response(200, agent)
                else:
                    self.send_json_response(404, {"error": "Agent not found"})
            except (IndexError, ValueError):
                self.send_json_response(400, {"error": "Invalid agent ID format"})
            return

        elif path == "/api/metrics":
            self.send_json_response(200, METRICS)
            return

        elif path.startswith("/api/export/"):
            try:
                agent_id = int(path.split("/")[3])
                agent = next((a for a in AGENTS_DATABASE if a["id"] == agent_id), None)
                if agent:
                    scaffold = agent.get("codeScaffold", "# Default Agent Scaffold\nprint('Running agent...')")
                    self.send_response(200)
                    self.send_header("Content-Type", "text/plain; charset=utf-8")
                    self.send_header("Content-Disposition", f'attachment; filename="agent_{agent_id}_{agent["name"].lower().replace(" ", "_")}.py"')
                    self.end_headers()
                    self.wfile.write(scaffold.encode("utf-8"))
                else:
                    self.send_json_response(404, {"error": "Agent not found"})
            except (IndexError, ValueError):
                self.send_json_response(400, {"error": "Invalid agent ID format"})
            return

        # Fallback to serving static files (index.html, assets)
        super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path.startswith("/api/agents/") and path.endswith("/simulate"):
            try:
                agent_id = int(path.split("/")[3])
                agent = next((a for a in AGENTS_DATABASE if a["id"] == agent_id), None)
                if not agent:
                    self.send_json_response(404, {"error": "Agent not found"})
                    return

                content_len = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_len).decode("utf-8") if content_len > 0 else "{}"
                user_inputs = json.loads(body) if body else {}

                # Execute dynamic simulation
                result = self.simulate_agent_execution(agent, user_inputs)
                self.send_json_response(200, result)
            except Exception as e:
                self.send_json_response(500, {"error": str(e)})
            return

        elif path == "/api/reset":
            METRICS["transactions"] = []
            METRICS["completedSimulations"] = 0
            self.send_json_response(200, {"status": "Reset complete"})
            return

        self.send_json_response(404, {"error": "Endpoint not found"})

    def simulate_agent_execution(self, agent, user_inputs):
        """Simulates end-to-end agent execution with latency timers and real-time fees."""
        # Calculate simulated fee
        base_val = float(user_inputs.get("cartValue") or user_inputs.get("invoiceValue") or user_inputs.get("quoteValue") or 100.0)
        
        fee_amount = 0.0
        fee_label = ""
        if agent["revenueType"] == "Commission":
            pct = 0.10
            fee_amount = round(base_val * pct, 2)
            fee_label = f"10% Recovery Fee ({fee_amount:.2f})"
        elif agent["revenueType"] == "Rev-Share":
            pct = 0.20
            fee_amount = round(base_val * pct, 2)
            fee_label = f"20% Verified Savings ({fee_amount:.2f})"
        elif agent["revenueType"] == "Micro-fee":
            fee_amount = 1.50
            fee_label = f"Micro-Transaction Fee (${fee_amount:.2f})"
        elif agent["revenueType"] == "Lead Bounty":
            fee_amount = 35.00
            fee_label = f"Qualified Lead Bounty (${fee_amount:.2f})"
        else: # Fixed
            fee_amount = 25.00
            fee_label = f"Fixed Dossier Fee (${fee_amount:.2f})"

        # Generate transaction token
        tx_id = f"tx_agt_{uuid.uuid4().hex[:12]}"
        stripe_id = f"ch_3N{uuid.uuid4().hex[:16]}"
        
        timestamp = time.strftime("%H:%M:%S")

        # Dynamic output synthesis
        output_data = agent["generateOutput"](user_inputs)

        # Update server metrics
        METRICS["completedSimulations"] += 1
        METRICS["totalFeesCaptured"] += fee_amount
        METRICS["totalGmv"] += base_val
        
        tx_record = {
            "txId": tx_id,
            "stripeChargeId": stripe_id,
            "agentId": agent["id"],
            "agentName": agent["name"],
            "amount": fee_amount,
            "label": fee_label,
            "timestamp": timestamp,
            "status": "succeeded"
        }
        METRICS["transactions"].insert(0, tx_record)
        if len(METRICS["transactions"]) > 20:
            METRICS["transactions"].pop()

        return {
            "success": True,
            "agentId": agent["id"],
            "agentName": agent["name"],
            "executionTimeMs": 348,
            "transaction": tx_record,
            "stepsExecuted": agent["demoSteps"],
            "output": output_data,
            "stripeWebhookPayload": {
                "id": f"evt_{uuid.uuid4().hex[:14]}",
                "object": "event",
                "type": "charge.captured",
                "data": {
                    "object": {
                        "id": stripe_id,
                        "amount": int(fee_amount * 100),
                        "currency": "usd",
                        "status": "succeeded",
                        "metadata": {
                            "agent_id": agent["id"],
                            "agent_name": agent["name"],
                            "execution_token": tx_id
                        }
                    }
                }
            }
        }

    def send_json_response(self, code, payload):
        body = json.dumps(payload, default=str).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

def run():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, AgentStudioHandler)
    print("\n==================================================================")
    print(f"[AgentStudio OS] Server live at: http://localhost:{PORT}")
    print("[AgentStudio OS] 50 Interactive AI Agent Workspaces Loaded Successfully!")
    print("==================================================================\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server gracefully...")
        httpd.server_close()

if __name__ == "__main__":
    run()
