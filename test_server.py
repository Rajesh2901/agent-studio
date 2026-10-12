import urllib.request
import threading
import time
import json
from server import run

# Run server in daemon thread
t = threading.Thread(target=run, daemon=True)
t.start()
time.sleep(1.2)

# Test GET /api/agents
with urllib.request.urlopen('http://localhost:8050/api/agents') as response:
    agents = json.loads(response.read().decode('utf-8'))
    print(f"VERIFIED: Loaded {len(agents)} agents via API!")

# Test static index.html
with urllib.request.urlopen('http://localhost:8050/') as response:
    content = response.read()
    print(f"VERIFIED: Static UI served (HTTP {response.status}, {len(content)} bytes)!")

# Test POST simulate
post_data = json.dumps({"cartValue": 220.0, "city": "Seattle"}).encode('utf-8')
req = urllib.request.Request(
    'http://localhost:8050/api/agents/1/simulate',
    data=post_data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)
with urllib.request.urlopen(req) as response:
    sim_data = json.loads(response.read().decode('utf-8'))
    print(f"VERIFIED: Simulation successful for {sim_data['agentName']}!")
    print(f"VERIFIED: Stripe Webhook generated: {sim_data['stripeWebhookPayload']['id']}")
    print(f"VERIFIED: Transaction amount: ${sim_data['transaction']['amount']}")
