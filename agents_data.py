"""
Comprehensive Database of 50 Real-Time Revenue AI Agents for AgentStudio OS.
Includes full schemas, interactive input configurations, output synthesizers, and starter code scaffolds.
"""

def make_scaffold(name, revenue_type, desc):
    return f'''"""
{name} - Production Agent Scaffold
Architecture: FastAPI + LLM Orchestration + Stripe Connect
"""
import os
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import stripe

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_mock_123")
app = FastAPI(title="{name}", description="{desc}")

class ExecutionPayload(BaseModel):
    session_id: str
    target_data: dict

@app.post("/v1/execute")
async def execute_agent(payload: ExecutionPayload):
    """Executes the autonomous agent reasoning loop and captures value."""
    # 1. Context validation & grounding
    session_id = payload.session_id
    
    # 2. Dynamic Tool Calling & LLM reasoning
    result = {{
        "status": "success",
        "agent": "{name}",
        "action_taken": "Automated resolution completed",
        "session_id": session_id
    }}
    
    # 3. Real-Time Stripe Fee Settlement ({revenue_type})
    charge = stripe.Charge.create(
        amount=1500, # In cents ($15.00)
        currency="usd",
        source="tok_visa",
        description=f"{name} autonomous execution fee"
    )
    result["stripe_charge_id"] = charge.id
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
'''

# Helper output generators
def gen_cart_rescue(inputs):
    val = inputs.get("cartValue", 185)
    item = inputs.get("item", "Leather Bomber Jacket")
    loc = inputs.get("city", "Chicago")
    return {
        "action": "Applied Promo Code EXPRESS_COMP",
        "customerMessage": f"Order within 28 minutes and express shipping to {loc} arrives guaranteed Thursday by 4 PM. We've applied complimentary express delivery!",
        "incentiveApplied": "Free Express Delivery ($18.00 Value)",
        "recoveredCartValue": f"${val:.2f}",
        "item": item
    }

def gen_listing_pulse(inputs):
    asin = inputs.get("asin", "B09X8Y7Z12")
    kw = inputs.get("keyword", "Memory Foam Pillow")
    return {
        "status": "ASIN Updated via Amazon SP-API",
        "asin": asin,
        "targetKeyword": kw,
        "optimizedTitle": f"Ultra-Support {kw} - [Guaranteed In-Stock, Same-Day Prime Delivery]",
        "rankDeltaEstimate": "+14 positions within 6 hours",
        "competitorStatus": "Competitor OOS in 4 regional fulfillment centers"
    }

def gen_vendor_nudge(inputs):
    vendor = inputs.get("vendor", "Apex Wholesale Supply")
    raw = inputs.get("material", "Arabica Green Coffee")
    inv = inputs.get("invoiceValue", 4800)
    return {
        "supplierEmailSubject": f"Pricing Index Realignment Request - PO #{inv}",
        "commodityIndexObserved": f"{raw} ICE Futures -11.8% past 60 days",
        "creditMemoRequested": f"${inv * 0.10:.2f} (10% adjustment)",
        "proposedNewUnitPrice": "$4.32 / lb (reduced from $4.80)",
        "vendor": vendor
    }

def gen_return_shield(inputs):
    item = inputs.get("item", "Woven Accent Rug 5x7")
    reason = inputs.get("reason", "Slight fray on lower border")
    return {
        "defectClassification": "Minor Cosmetic Imperfection (96% Confidence)",
        "reverseFreightAvoided": "$19.40 FedEx Ground",
        "customerSettlementOffer": "Instant $25.00 cash refund to card (keep the rug)",
        "customerDecision": "Accepted Instant Partial Refund",
        "netRetailerSavings": "$14.40"
    }

def gen_flash_drop(inputs):
    sku = inputs.get("sku", "SKU-PARKA-04")
    q = inputs.get("question", "What size is the model wearing?")
    return {
        "audioTranscribed": f"Host demoing {sku}",
        "liveCommentProcessed": q,
        "chatResponseSent": "@Sarah The model is 5'7 wearing Size M. Machine wash cold!",
        "overlayCardPinned": f"{sku} (Size M - In Stock - $120.00)",
        "conversionSurge": "28 Units checked out in 120s"
    }

def gen_review_alchemy(inputs):
    star_review = inputs.get("review", "Cleared my acne in 9 days without drying my skin!")
    return {
        "videoHook": "Stop spending $80 on dermatologist cleansers that wreck your skin barrier...",
        "threePartScript": {
            "hook_0_3s": "Look at my skin 9 days ago versus right now.",
            "body_3_20s": f"I used to think acne needed harsh scrubs until I tried this formula. {star_review}",
            "cta_20_30s": "Tap the link below before their batch runs out."
        },
        "voiceModel": "ElevenLabs Rachel (Conversational Natural)",
        "deliverables": "CapCut XML Project, 9:16 Video Storyboard, Audio WAV"
    }

def gen_b2b_quote(inputs):
    qty = inputs.get("quantity", 50000)
    spec = inputs.get("spec", "Cosmetic Embossed Matte Boxes")
    return {
        "quoteId": "Q-2026-9482",
        "totalBindingQuote": "$18,400.00",
        "unitPrice": f"${18400 / qty:.3f}",
        "leadTime": "12 Business Days",
        "guaranteeWindow": "72 Hours Price Lock",
        "specSummary": f"{qty:,} units of {spec} (350 GSM board, hot foil)"
    }

def gen_proposal_sniper(inputs):
    job = inputs.get("jobTitle", "Next.js 14 & Supabase Migration")
    budget = inputs.get("budget", 4000)
    return {
        "proposalStatus": "Submitted First (Rank #1 in Upwork Inbox)",
        "matchScore": "98.4%",
        "targetedPitch": f"Noticed you are migrating to Next.js 14 and Supabase. In my last repo, I migrated 42 route handlers to Server Actions with zero downtime. Here is the exact zero-downtime migration architecture I would use for your ${budget} project...",
        "githubEvidenceLinked": "github.com/freelancer/nextjs-supabase-starter"
    }

def gen_scope_guard(inputs):
    req = inputs.get("clientRequest", "Can we also add multi-currency checkout before Tuesday?")
    rate = inputs.get("hourlyRate", 100)
    return {
        "scopeViolationFlag": "Critical: Multi-Currency not included in signed Statement of Work",
        "changeOrderCalculated": f"14 Engineering Hours (${rate * 14:.2f})",
        "generatedSlackMessage": f"Hi team! We can definitely support multi-currency! Since this is outside the original SOW, I've prepared a quick 1-click Change Order for $1,400 to keep us on track.",
        "stripeApprovalLink": "https://buy.stripe.com/change_order_94820"
    }

def gen_audio_polisher(inputs):
    mins = inputs.get("audioDuration", 45)
    return {
        "audioDurationProcessed": f"{mins} Minutes",
        "fillerWordsRemoved": "42 'ums', 18 'likes', 12 long dead-air pauses",
        "loudnessNormalized": "-16 LUFS (Podcast Standard)",
        "generatedChapters": [
            "00:00 - Introduction & Market Context",
            "12:30 - The Breakdown of Traditional SaaS",
            "28:15 - Autonomous Agent Architecture",
            "41:00 - Final Takeaways & Q&A"
        ],
        "audiogramVideoRendered": "3x Vertical 9:16 Video Reels with Kinetic Captions"
    }

def gen_generic(inputs, agent):
    return {
        "status": "Autonomous Execution Verified",
        "agent": agent["name"],
        "category": agent["category"],
        "telemetry": inputs,
        "verificationToken": f"auth_tok_84920{agent['id']}",
        "deliverable": f"Completed automated output generated adhering to {agent['category']} compliance standards."
    }

# 50 Detailed Agent Definitions
AGENTS_DATABASE = [
    {
        "id": 1,
        "name": "CartRescue Agent",
        "category": "E-Commerce",
        "concept": "Intercepts high-intent cart abandonment sessions via real-time exit triggers, resolving buyer doubts and offering personalized incentives.",
        "targetUsers": "Shopify & WooCommerce DTC Merchants",
        "revenueModel": "8-12% commission on recovered cart value via Stripe webhook.",
        "revenueType": "Commission",
        "difficulty": "Medium",
        "inputFields": [
            {"key": "cartValue", "label": "Cart Total ($)", "type": "number", "defaultValue": 185.00},
            {"key": "item", "label": "Cart Line Item", "type": "text", "defaultValue": "Handcrafted Leather Jacket"},
            {"key": "city", "label": "Destination City", "type": "text", "defaultValue": "Chicago, IL"},
            {"key": "userHesitation", "label": "User Query / Hesitation", "type": "text", "defaultValue": "Will this arrive before Friday?"}
        ],
        "demoSteps": [
            "Session SDK detects 45s idle time and cursor exit vector on shipping step.",
            "Agent evaluates carrier delivery API: FedEx Express delivers Thursday 4 PM.",
            "Agent launches slide-in concierge chat addressing Chicago winter transit times.",
            "Shopper asks: 'Will this arrive before Friday?'",
            "Agent applies promo code EXPRESS_COMP; shopper converts; $18.50 (10%) billed."
        ],
        "generateOutput": gen_cart_rescue,
        "codeScaffold": make_scaffold("CartRescue Agent", "Commission", "E-commerce real-time cart recovery agent")
    },
    {
        "id": 2,
        "name": "ListingPulse",
        "category": "E-Commerce",
        "concept": "Monitors competitor stockouts and keyword ranking volatility to autonomously rewrite product titles and bullet points.",
        "targetUsers": "Amazon FBA & Walmart Marketplace Sellers",
        "revenueModel": "$0.25 per listing rewrite deployed + $1.00 per competitor stockout captured.",
        "revenueType": "Micro-fee",
        "difficulty": "Medium",
        "inputFields": [
            {"key": "asin", "label": "Product ASIN", "type": "text", "defaultValue": "B09X8Y7Z12"},
            {"key": "keyword", "label": "Target Search Keyword", "type": "text", "defaultValue": "Ergonomic Memory Foam Pillow"},
            {"key": "competitorName", "label": "Competitor Brand", "type": "text", "defaultValue": "SleepComfort Pro"}
        ],
        "demoSteps": [
            "Competitor SleepComfort Pro goes out of stock in 4 fulfillment centers.",
            "Keepa & SP-API listener detects stockout in 3 minutes.",
            "Agent analyzes search query velocity and rewrites bullet points to highlight 'Guaranteed In-Stock & 1-Day Prime Delivery'.",
            "Pre-approved autopilot pushes update via Amazon SP-API.",
            "Listing receives 42 surge orders; $1.00 fee charged to seller balance."
        ],
        "generateOutput": gen_listing_pulse,
        "codeScaffold": make_scaffold("ListingPulse", "Micro-fee", "Amazon listing auto-optimizer")
    },
    {
        "id": 3,
        "name": "VendorNudge",
        "category": "E-Commerce",
        "concept": "Ingests supplier invoices, benchmarks raw material price drops against commodities indices, and drafts calibrated renegotiation demands.",
        "targetUsers": "Wholesale Brands & Physical Goods Manufacturers",
        "revenueModel": "15% contingency fee on validated invoice savings upon credit memo approval.",
        "revenueType": "Rev-Share",
        "difficulty": "Medium",
        "inputFields": [
            {"key": "vendor", "label": "Supplier / Vendor Name", "type": "text", "defaultValue": "Highland Green Bean Importers"},
            {"key": "material", "label": "Commodity / Material", "type": "text", "defaultValue": "ICE Arabica Green Coffee"},
            {"key": "invoiceValue", "label": "Invoice Total ($)", "type": "number", "defaultValue": 4800.00}
        ],
        "demoSteps": [
            "Manufacturer uploads $4,800 supplier invoice.",
            "Agent compares invoice unit price against falling ICE Arabica futures (-11.8%).",
            "Agent drafts courteous negotiation citing volume commitment and market index.",
            "Supplier issues $480.00 credit memo for upcoming shipment.",
            "VendorNudge collects $72.00 (15%) fee from client corporate card."
        ],
        "generateOutput": gen_vendor_nudge,
        "codeScaffold": make_scaffold("VendorNudge", "Rev-Share", "Automated supplier renegotiation agent")
    },
    {
        "id": 4,
        "name": "ReturnShield",
        "category": "E-Commerce",
        "concept": "Evaluates return photos and reason codes in real time, offering instant keep-and-partial-refund settlements to eliminate reverse logistics waste.",
        "targetUsers": "Apparel, Furniture & Home Goods Retailers",
        "revenueModel": "$0.50 per automated return triage + $3.00 bonus per avoided return shipment.",
        "revenueType": "Micro-fee",
        "difficulty": "Easy",
        "inputFields": [
            {"key": "item", "label": "Returned Product Name", "type": "text", "defaultValue": "Moroccan Geometric Wool Rug 5x7"},
            {"key": "reason", "label": "Customer Reason Code", "type": "text", "defaultValue": "Minor fringe thread loose on corner"},
            {"key": "cartValue", "label": "Original Item Price ($)", "type": "number", "defaultValue": 65.00}
        ],
        "demoSteps": [
            "Customer initiates return for $65 rug, uploading a smartphone photo.",
            "Vision model classifies defect as cosmetic fringe loose thread.",
            "Agent estimates return freight ($19.40) exceeds restocking value.",
            "Presents instant settlement: 'Keep rug and receive $25 cash refund instantly, or ship back for $65.'",
            "Customer accepts; store saves $19.40; $3.50 fee debited to merchant."
        ],
        "generateOutput": gen_return_shield,
        "codeScaffold": make_scaffold("ReturnShield", "Micro-fee", "Reverse logistics triage agent")
    },
    {
        "id": 5,
        "name": "FlashDrop",
        "category": "E-Commerce",
        "concept": "Listens to live TikTok/Instagram/YouTube shopping streams, answers comments in real time, and pins dynamic checkout links synced with the speaker.",
        "targetUsers": "Live-Stream Creators & Boutique Retailers",
        "revenueModel": "2.5% affiliate commission on stream sales completed via agent-pinned links.",
        "revenueType": "Commission",
        "difficulty": "Hard",
        "inputFields": [
            {"key": "sku", "label": "Featured SKU", "type": "text", "defaultValue": "Waterproof Winter Parka (SKU-PARKA-04)"},
            {"key": "question", "label": "Live Stream Chat Question", "type": "text", "defaultValue": "What size is the model wearing and is it machine washable?"},
            {"key": "cartValue", "label": "Live GMV Generated ($)", "type": "number", "defaultValue": 2400.00}
        ],
        "demoSteps": [
            "Host describes seam-sealed waterproof lining on live stream.",
            "Chat stream fills with sizing and washing questions.",
            "Agent synthesizes real-time audio transcript and product spec sheet.",
            "Posts precise comment: '@Sarah Model is 5 7 wearing Size M. Yes, machine wash cold!'",
            "Pins SKU #04 checkout card; 28 units sold; $60.00 commission captured."
        ],
        "generateOutput": gen_flash_drop,
        "codeScaffold": make_scaffold("FlashDrop", "Commission", "Live social commerce co-host")
    },
    {
        "id": 6,
        "name": "ReviewAlchemy",
        "category": "E-Commerce",
        "concept": "Scrapes verified 5-star customer reviews and autonomously transforms them into TikTok/Reels UGC scripts, storyboards, and audio ad packs.",
        "targetUsers": "DTC Marketers & Performance Ad Agencies",
        "revenueModel": "$4.99 per generated creative ad pack (script + storyboard + voiceover).",
        "revenueType": "Fixed",
        "difficulty": "Easy",
        "inputFields": [
            {"key": "brand", "label": "Brand Name", "type": "text", "defaultValue": "GlowBot Skincare"},
            {"key": "review", "label": "Customer 5-Star Review", "type": "text", "defaultValue": "Cleared my cystic acne in 9 days without drying my skin!"}
        ],
        "demoSteps": [
            "System imports 5-star review from Shopify store inbox.",
            "Agent crafts 3-part UGC script: 3-second hook, agitation, and call-to-action.",
            "Synthesizes natural ElevenLabs voiceover file and CapCut storyboard XML.",
            "Marketer reviews and clicks 'Download Full Production Pack'.",
            "$4.99 charged via Stripe micropayment immediately."
        ],
        "generateOutput": gen_review_alchemy,
        "codeScaffold": make_scaffold("ReviewAlchemy", "Fixed", "Review-to-UGC ad generator")
    },
    {
        "id": 7,
        "name": "B2B QuoteBot",
        "category": "E-Commerce",
        "concept": "Parses custom wholesale RFQ emails and CAD/PDF specs, computes manufacturing margins against live material feeds, and issues binding quotes in 90s.",
        "targetUsers": "Custom Packaging Manufacturers & Machine Shops",
        "revenueModel": "$15 per generated binding quotation + 1% success fee upon customer deposit.",
        "revenueType": "Fixed",
        "inputFields": [
            {"key": "spec", "label": "Custom Specification", "type": "text", "defaultValue": "50,000 Custom Gold-Embossed Cosmetic Boxes (350 GSM)"},
            {"key": "quantity", "label": "Requested Quantity", "type": "number", "defaultValue": 50000},
            {"key": "quoteValue", "label": "Calculated Quote Value ($)", "type": "number", "defaultValue": 18400.00}
        ],
        "demoSteps": [
            "Client sends 14-page packaging spec sheet PDF via email.",
            "QuoteBot extracts board weight, die-cut passes, and foil stamps.",
            "Queries live paper inventory and shop machine hour costs via ERP.",
            "Generates formal branded PDF quote with 72-hour price guarantee.",
            "$15 charged for quote generation; 1% ($184) captured upon deposit."
        ],
        "generateOutput": gen_b2b_quote,
        "codeScaffold": make_scaffold("B2B QuoteBot", "Fixed", "Custom B2B RFQ quoting agent")
    },
    {
        "id": 8,
        "name": "ProposalSniper",
        "category": "Freelance & Agency",
        "concept": "Monitors freelance platforms and RFP feeds, assesses win probability, and drafts bespoke technical proposals within 3 minutes of posting.",
        "targetUsers": "Freelance Developers & Digital Agencies",
        "revenueModel": "$1.50 per sent bid or credit pack ($29 for 25 bids) + 3% won deal fee.",
        "revenueType": "Micro-fee",
        "difficulty": "Easy",
        "inputFields": [
            {"key": "jobTitle", "label": "Upwork / RFP Job Title", "type": "text", "defaultValue": "Next.js 14 & Supabase Auth Migration"},
            {"key": "budget", "label": "Client Budget ($)", "type": "number", "defaultValue": 4000.00},
            {"key": "clientPriority", "label": "Key Client Requirement", "type": "text", "defaultValue": "Zero downtime and test coverage"}
        ],
        "demoSteps": [
            "Job posted on Upwork with $4,000 budget.",
            "Agent cross-references freelancer GitHub portfolio for matching Next.js repos.",
            "Generates 250-word proposal detailing exact zero-downtime database strategy.",
            "Freelancer taps 'Approve & Send' on mobile notification.",
            "Proposal lands first in client inbox; $1.50 deducted from credit pack."
        ],
        "generateOutput": gen_proposal_sniper,
        "codeScaffold": make_scaffold("ProposalSniper", "Micro-fee", "RFP and Upwork automated proposal pitcher")
    },
    {
        "id": 9,
        "name": "ScopeGuard",
        "category": "Freelance & Agency",
        "concept": "Sits in Slack/Teams/email, detects client requests outside the signed Statement of Work, and politely drafts itemized Change Orders.",
        "targetUsers": "Software Agencies & Web Consultants",
        "revenueModel": "5% transaction processing fee on all approved Change Orders paid via payment link.",
        "revenueType": "Commission",
        "difficulty": "Medium",
        "inputFields": [
            {"key": "clientRequest", "label": "Client Slack Message", "type": "text", "defaultValue": "Can we also add multi-currency checkout before next Tuesday's launch?"},
            {"key": "hourlyRate", "label": "Agency Hourly Rate ($)", "type": "number", "defaultValue": 100.00},
            {"key": "cartValue", "label": "Estimated Change Order Value ($)", "type": "number", "defaultValue": 1400.00}
        ],
        "demoSteps": [
            "Client writes in Slack requesting multi-currency support.",
            "ScopeGuard checks indexed project SOW (feature is excluded).",
            "Pings agency owner: 'Out-of-scope detected ($1,400 est). Draft Change Order?'",
            "Owner clicks 'Approve'; ScopeGuard posts polite breakdown with Stripe link.",
            "Client pays $1,400; ScopeGuard deducts $70 (5%) in real time."
        ],
        "generateOutput": gen_scope_guard,
        "codeScaffold": make_scaffold("ScopeGuard", "Commission", "Agency scope creep negotiator")
    },
    {
        "id": 10,
        "name": "AudioPolisher",
        "category": "Freelance & Agency",
        "concept": "Ingests raw audio, removes filler words, and generates show notes, timestamps, audiograms, and sponsor ad markers in real time.",
        "targetUsers": "Podcasters, Voiceover Artists & YouTubers",
        "revenueModel": "Pay-as-you-go $0.15 per audio minute processed charged via Stripe.",
        "revenueType": "Micro-fee",
        "difficulty": "Medium",
        "inputFields": [
            {"key": "episodeTitle", "label": "Episode Title", "type": "text", "defaultValue": "Ep 42: The Future of Autonomous AI Workflows"},
            {"key": "audioDuration", "label": "Recording Duration (Minutes)", "type": "number", "defaultValue": 45}
        ],
        "demoSteps": [
            "Creator uploads 45-minute raw .wav interview.",
            "Agent trims filler words, normalizes audio to -16 LUFS, and generates timestamps.",
            "Extracts 3 high-impact soundbites and renders vertical video audiograms.",
            "Produces SEO show notes and newsletter markdown.",
            "Creator downloads bundle; $6.75 charged to credit card."
        ],
        "generateOutput": gen_audio_polisher,
        "codeScaffold": make_scaffold("AudioPolisher", "Micro-fee", "Podcast post-production agent")
    }
]

# Generate definitions for agents 11 through 50 programmatically with rich schemas
CATEGORIES_MAPPING = [
    (11, "SubDocu", "Freelance & Agency", "Translates subcontractor WhatsApp voice notes into certified daily field logs and reconciles invoices.", "Fixed", 3.00),
    (12, "LocalizationLeap", "Freelance & Agency", "Translates app string files using brand lore and strictly enforces UI button character boundaries.", "Micro-fee", 25.00),
    (13, "GhostThread", "Freelance & Agency", "Converts executive voice notes into high-performing LinkedIn posts and X threads with 1-tap approval.", "Micro-fee", 5.00),
    (14, "DesignBrief AI", "Freelance & Agency", "Conducts interactive intake interviews to extract concrete creative specifications and deliverables.", "Fixed", 10.00),
    (15, "CloudLeak", "Finance & Cost", "Monitors AWS/GCP telemetry, detects idle compute nodes, and submits ready-to-merge Terraform pull requests.", "Rev-Share", 72.00),
    (16, "ChasingDunning", "Finance & Cost", "Monitors overdue invoices in QuickBooks, sending escalating polite reminders with 1-click payment links.", "Commission", 48.00),
    (17, "SaaSSnip", "Finance & Cost", "Detects orphaned SaaS seats (Figma, Slack, Zoom) from departed contractors and automates deprovisioning.", "Rev-Share", 180.00),
    (18, "GrantFinder AI", "Finance & Cost", "Scans non-dilutive grant databases, matches eligibility, and drafts complete federal submission dossiers.", "Fixed", 49.00),
    (19, "TaxReceipt Concierge", "Finance & Cost", "Matches bank transactions to inbox receipts and classifies IRS Section 179 deductions in real time.", "Micro-fee", 0.50),
    (20, "AuditTrail", "Finance & Cost", "Crawls GitHub commits and Jira tickets to compile audit-proof IRS Form 6765 R&D tax credit packages.", "Rev-Share", 2400.00),
    (21, "ColdSignal", "Sales & Leads", "Monitors executive job postings and funding rounds, drafting hyper-personalized outbound emails instantly.", "Lead Bounty", 15.00),
    (22, "WebVisitor Reveal", "Sales & Leads", "Identifies anonymous B2B website visitors via IP reverse-lookup and launches a tailored qualification chat.", "Lead Bounty", 25.00),
    (23, "SpeedToLead", "Sales & Leads", "Dials high-ticket web form leads within 15 seconds, qualifies them, and warm-transfers to available sales reps.", "Lead Bounty", 35.00),
    (24, "PodcastPitcher", "Sales & Leads", "Matches founders and authors with top podcasts, writing pitch angles referencing specific past episodes.", "Lead Bounty", 150.00),
    (25, "ReviewBooster", "Sales & Leads", "Texts homeowners after service completion and directs satisfied customers to 1-click SEO Google review links.", "Micro-fee", 3.00),
    (26, "AffiliateScout", "Sales & Leads", "Crawls publisher articles for dead affiliate links and hot-swaps them in the CMS with higher-paying programs.", "Rev-Share", 1.60),
    (27, "TicketZero", "Customer Support", "Connects to Zendesk/Intercom and autonomously performs deterministic operations without human agents.", "Micro-fee", 0.85),
    (28, "ChurnBuster Live", "Customer Support", "Intercepts users clicking 'Cancel Subscription', negotiating custom pause plans or feature downgrades.", "Commission", 14.85),
    (29, "NightWatch", "Customer Support", "Triages after-hours emergency tenant calls, screening routine issues and dispatching on-call contractors.", "Micro-fee", 12.00),
    (30, "Multilingual Concierge", "Customer Support", "Serves as a 24/7 WhatsApp concierge for boutique hotels, handling door codes and local dining upsells.", "Commission", 8.00),
    (31, "BugTriage AI", "Customer Support", "Ingests Sentry crash reports, reproduces errors in a virtual sandbox, and submits tested GitHub bug fix PRs.", "Micro-fee", 2.00),
    (32, "LeasePencil", "Real Estate", "Ingests 90-page commercial lease PDFs, extracting CAM charges and critical dates into a 5-year cash-flow Excel model.", "Fixed", 39.00),
    (33, "ZoningSherlock", "Real Estate", "Cross-references municipal GIS maps and land development bylaws to evaluate ADU feasibility and setbacks.", "Fixed", 75.00),
    (34, "TenantScreener", "Real Estate", "Verifies rental paystubs via document forensics to detect forged templates and computes income coverage.", "Fixed", 25.00),
    (35, "StagingVision", "Real Estate", "Renders photorealistic 4K virtually staged room photos from empty room images with shoppable decor links.", "Fixed", 12.00),
    (36, "OralExam AI", "Education", "Conducts 15-minute proctored spoken examinations via dynamic voice dialogue, generating CEFR scorecards.", "Fixed", 9.99),
    (37, "CodeVetting AI", "Education", "Proctors live coding interviews in a collaborative browser IDE, evaluating algorithms and anti-cheat telemetry.", "Fixed", 25.00),
    (38, "CourseToAudiobook", "Education", "Converts 150-page textbooks or training syllabi into episodic Socratic podcasts on a private RSS feed.", "Fixed", 19.00),
    (39, "SyllabusCloner", "Education", "Generates accreditation-ready 12-week university course plans, lab rubrics, and Canvas LMS cartridges.", "Fixed", 45.00),
    (40, "RedlineBot", "Legal & Compliance", "Scans incoming vendor contracts, flags non-standard liability clauses, and outputs redlined .docx with Track Changes.", "Fixed", 19.00),
    (41, "PrivacyAudit AI", "Legal & Compliance", "Crawls websites for unconsented tracking pixels, generating compliant privacy policies and cookie banners.", "Fixed", 49.00),
    (42, "TenderShield", "Legal & Compliance", "Audits government tender proposals against Section L & M solicitation requirements to eliminate bid disqualification.", "Fixed", 250.00),
    (43, "MusicClear AI", "Legal & Compliance", "Scans audio tracks for sampled beats, identifies rights holders in ASCAP registries, and drafts sync licenses.", "Fixed", 29.00),
    (44, "PriorAuth Express", "Healthcare", "Cross-checks clinical notes against private insurer criteria, compiling approved prior-authorization request packets.", "Fixed", 15.00),
    (45, "DentistRecall", "Healthcare", "Monitors dental PMS for morning cancellations, texting overdue patients to fill open hygiene chair slots.", "Lead Bounty", 20.00),
    (46, "WellnessIntake", "Healthcare", "Transcribes physical therapy intake voice recordings into EHR SOAP notes and personalized home exercise plans.", "Micro-fee", 4.50),
    (47, "SEC Filings Alerter", "Trading & Arbitrage", "Parses SEC EDGAR 8-K filings within 3 seconds of release, alerting day traders to material non-obvious disclosures.", "Micro-fee", 0.25),
    (48, "CardFlip", "Trading & Arbitrage", "Scrapes newly listed eBay Buy-It-Now sports cards, comparing prices against PSA comps to flag undervalued cards.", "Micro-fee", 2.00),
    (49, "DomainFlippr", "Trading & Arbitrage", "Evaluates expiring domain drop lists, vetting backlink equity and USPTO trademark clearance for site builders.", "Fixed", 5.00),
    (50, "FreightRate Arbitrage", "Trading & Arbitrage", "Monitors freight load boards, matching carrier truck lanes and auto-submitting spot rate counter-bids.", "Lead Bounty", 25.00)
]

for aid, aname, acat, aconcept, arevtype, afee in CATEGORIES_MAPPING:
    AGENTS_DATABASE.append({
        "id": aid,
        "name": aname,
        "category": acat,
        "concept": aconcept,
        "targetUsers": f"Enterprise & SMB {acat} Operators",
        "revenueModel": f"Real-time {arevtype.lower()} fee (${afee:.2f}) upon completed resolution.",
        "revenueType": arevtype,
        "difficulty": "Medium",
        "inputFields": [
            {"key": "targetEntity", "label": "Target Record / Identifier", "type": "text", "defaultValue": f"Record #{aid}-2026-X"},
            {"key": "inputTelemetry", "label": "Input Data / Telemetry", "type": "text", "defaultValue": f"Autonomous trigger parameters for {aname}."},
            {"key": "quoteValue", "label": "Associated Transaction Value ($)", "type": "number", "defaultValue": round(afee * 5, 2)}
        ],
        "demoSteps": [
            f"Ingestion event received for {aname}.",
            "Agent evaluates domain knowledge base and policy guardrails.",
            "Tool execution performed in isolated sandbox environment.",
            "Compliance verification and safety checks satisfied.",
            f"Value verified; ${afee:.2f} fee logged to Stripe Connect ledger."
        ],
        "generateOutput": lambda inputs, a={"name": aname, "category": acat, "id": aid}: gen_generic(inputs, a),
        "codeScaffold": make_scaffold(aname, arevtype, aconcept)
    })
