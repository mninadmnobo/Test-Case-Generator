import os
import re
import json

# 21 Core Requirements extracted from Parabank.md
requirements = [
    {
        "id": "REQ-01",
        "desc": "Login with valid Email/Username and Password authenticates and redirects to Accounts Overview.",
        "keywords": ["login", "valid", "credential", "successful login"]
    },
    {
        "id": "REQ-02",
        "desc": "Login with invalid credentials shows 'Incorrect email or password' and clears password field.",
        "keywords": ["invalid", "incorrect", "unregistered", "fail"]
    },
    {
        "id": "REQ-03",
        "desc": "Valid registration creates account and redirects to Login.",
        "keywords": ["successful registration", "register", "valid"]
    },
    {
        "id": "REQ-04",
        "desc": "Invalid registration fields display specific field-level errors (e.g., mismatch, empty, format).",
        "keywords": ["empty", "blank", "invalid format", "violation", "mismatch", "missing"]
    },
    {
        "id": "REQ-05",
        "desc": "Accounts Overview dashboard displays all accounts with masked account numbers and total balance footer.",
        "keywords": ["accounts overview", "dashboard", "masked", "footer", "total balance"]
    },
    {
        "id": "REQ-06",
        "desc": "Open Checking account validates $25 minimum deposit and sufficient funding balance.",
        "keywords": ["open checking", "checking", "25", "sufficient"]
    },
    {
        "id": "REQ-07",
        "desc": "Open Savings account validates $100 minimum deposit and sufficient funding balance.",
        "keywords": ["open savings", "savings", "100", "sufficient"]
    },
    {
        "id": "REQ-08",
        "desc": "Internal transfer validates amount and sufficient funds.",
        "keywords": ["internal transfer", "transfer funds", "my parabank", "sufficient"]
    },
    {
        "id": "REQ-09",
        "desc": "External transfer validates matching destination account numbers.",
        "keywords": ["external transfer", "match", "account number"]
    },
    {
        "id": "REQ-10",
        "desc": "Bill Pay validates payee info, matching account numbers, sufficient funds, and updates balances.",
        "keywords": ["bill pay", "payee", "payment", "sufficient"]
    },
    {
        "id": "REQ-11",
        "desc": "Request Loan validates amount ranges (Personal, Auto, Home).",
        "keywords": ["request loan", "loan amount", "personal", "auto", "home"]
    },
    {
        "id": "REQ-12",
        "desc": "Request Loan verifies 20% collateral value and minimum 10% down payment.",
        "keywords": ["down payment", "collateral", "loan"]
    },
    {
        "id": "REQ-13",
        "desc": "Update Contact Info validates format/completeness and refreshes data.",
        "keywords": ["update contact", "profile", "contact info"]
    },
    {
        "id": "REQ-14",
        "desc": "Manage Cards (Request) validates complete address and account standing.",
        "keywords": ["request card", "manage cards", "shipping"]
    },
    {
        "id": "REQ-15",
        "desc": "Manage Cards (Controls) validates numeric limits and date ranges.",
        "keywords": ["card controls", "spending limit", "freeze", "active"]
    },
    {
        "id": "REQ-16",
        "desc": "Investments (Trade) validates symbol exists, quantity > 0, and sufficient buying power/shares.",
        "keywords": ["trade", "buy", "sell", "symbol", "investment"]
    },
    {
        "id": "REQ-17",
        "desc": "Investments (Plan) validates future start date, minimum contribution, and adequate funding balance.",
        "keywords": ["recurring", "plan", "investment", "start date"]
    },
    {
        "id": "REQ-18",
        "desc": "Account Statements generates statement based on valid dates/account.",
        "keywords": ["statement", "generate", "period"]
    },
    {
        "id": "REQ-19",
        "desc": "Account Statements (e-Statement) updates paperless preference with valid email.",
        "keywords": ["e-statement", "paperless", "preference"]
    },
    {
        "id": "REQ-20",
        "desc": "Security Settings verifies current password, enforces strong policy, matches new passwords, and updates.",
        "keywords": ["security settings", "change password", "strong", "match"]
    },
    {
        "id": "REQ-21",
        "desc": "Support Center validates Secure Message and Callback Request forms.",
        "keywords": ["support", "message", "callback", "contact"]
    }
]

def score_match(test_title, keywords):
    score = 0
    title_lower = test_title.lower()
    for kw in keywords:
        if kw.lower() in title_lower:
            score += 1
    return score

def map_tests(test_cases_path, output_path, title):
    if not os.path.exists(test_cases_path):
        print(f"File not found: {test_cases_path}")
        return
        
    with open(test_cases_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract all test cases from markdown tables
    # Format: | TC-001 | WF-001 | Sign in with valid credentials | ...
    pattern = re.compile(r'\|\s*(TC-\d+.*?)\s*\|\s*[^|]*\s*\|\s*([^|]+)\s*\|')
    test_cases = []
    for match in pattern.finditer(content):
        tc_id = match.group(1).strip()
        tc_title = match.group(2).strip()
        test_cases.append({"id": tc_id, "title": tc_title})

    print(f"Parsed {len(test_cases)} tests from {test_cases_path}")

    out = []
    out.append(f"# Specification Coverage: Parabank ({title})\n\n")
    out.append("**Objective:** Trace the original functional requirements from the input dataset to the generated test cases.\n\n")
    out.append("## Coverage Matrix\n\n")
    out.append("| Req ID | Functional Description | Mapped Generated Test Case | Status |\n")
    out.append("|--------|------------------------|----------------------------|--------|\n")
    
    covered_count = 0
    
    for req in requirements:
        best_match = None
        best_score = 0
        
        for tc in test_cases:
            score = score_match(tc["title"], req["keywords"])
            if score > best_score:
                best_score = score
                best_match = tc
                
        if best_match and best_score > 0:
            tc_str = f"**{best_match['id']}:** {best_match['title']}"
            out.append(f"| **{req['id']}** | {req['desc']} | {tc_str} | ✅ Covered |\n")
            covered_count += 1
        else:
            out.append(f"| **{req['id']}** | {req['desc']} | *Not explicitly mapped* | ⚠️ Missed |\n")
            
    pct = (covered_count / len(requirements)) * 100
    
    out.append(f"\n## Summary\n")
    out.append(f"The model successfully covered **{covered_count} out of {len(requirements)} ({pct:.0f}%)** of the core functional requirements.\n\n")
    out.append("*(Generated automatically by coverage mapping script. Please manually verify mapped test cases for complete accuracy.)*\n")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(out))
    print(f"Wrote {output_path}")

base_dir = r"d:\Test-Case-Generator\results\Parabank"
out_dir = os.path.join(base_dir, "specification_coverage")

map_tests(os.path.join(base_dir, r"gpt-5-mini\agent\test-cases.md"), 
          os.path.join(out_dir, "sc-parabank-gpt-5-mini-agent.md"), 
          "gpt-5-mini Agentic Pipeline")

map_tests(os.path.join(base_dir, r"gpt-5-mini\few_shot_per_module\test-cases.md"), 
          os.path.join(out_dir, "sc-parabank-gpt-5-mini-few-shot-per-module.md"), 
          "gpt-5-mini Few Shot Per Module")

map_tests(os.path.join(base_dir, r"gpt-5-mini\zero_shot_per_module\test-cases.md"), 
          os.path.join(out_dir, "sc-parabank-gpt-5-mini-zero-shot-per-module.md"), 
          "gpt-5-mini Zero Shot Per Module")
