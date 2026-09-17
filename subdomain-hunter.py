#!/usr/bin/env python3
"""
SubdomainHunter - Professional Subdomain Enumeration & Analysis Tool
Author: ANON Security Research
License: MIT
Version: 1.0.0

Integrates multiple enumeration tools and provides actionable intelligence
for security researchers and bug bounty hunters.
"""

import subprocess
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set
import concurrent.futures
from collections import defaultdict

class SubdomainHunter:
    def __init__(self, domain: str, output_dir: str = "results"):
        self.domain = domain
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.results = {
            "domain": domain,
            "timestamp": self.timestamp,
            "subdomains": set(),
            "live_hosts": set(),
            "interesting_targets": defaultdict(list)
        }

    def run_subfinder(self) -> Set[str]:
        """Run subfinder for subdomain enumeration"""
        print(f"[*] Running subfinder on {self.domain}...")
        try:
            result = subprocess.run(
                ["E:/pentest-tools/subfinder/subfinder", "-d", self.domain, "-silent"],
                capture_output=True,
                text=True,
                timeout=300
            )
            subdomains = set(result.stdout.strip().split('\n'))
            print(f"[+] Subfinder found {len(subdomains)} subdomains")
            return subdomains
        except Exception as e:
            print(f"[-] Subfinder error: {e}")
            return set()

    def categorize_subdomains(self, subdomains: Set[str]) -> Dict[str, List[str]]:
        """Categorize subdomains by interest level"""
        categories = {
            "jenkins": [],
            "gitlab": [],
            "jira": [],
            "confluence": [],
            "admin": [],
            "api": [],
            "test": [],
            "staging": [],
            "dev": [],
            "qa": [],
            "internal": [],
            "vpn": [],
            "mail": [],
            "other": []
        }

        keywords = {
            "jenkins": ["jenkins"],
            "gitlab": ["gitlab"],
            "jira": ["jira"],
            "confluence": ["confluence", "wiki"],
            "admin": ["admin", "panel", "dashboard", "manage"],
            "api": ["api", "rest", "graphql", "gateway"],
            "test": ["test", "testing", "pentest"],
            "staging": ["stg", "staging", "stage"],
            "dev": ["dev", "development"],
            "qa": ["qa", "quality"],
            "internal": ["internal", "corp", "private"],
            "vpn": ["vpn", "remote", "access"],
            "mail": ["mail", "smtp", "webmail", "exchange"]
        }

        for subdomain in subdomains:
            subdomain_lower = subdomain.lower()
            categorized = False

            for category, terms in keywords.items():
                if any(term in subdomain_lower for term in terms):
                    categories[category].append(subdomain)
                    categorized = True
                    break

            if not categorized:
                categories["other"].append(subdomain)

        return categories

    def generate_report(self):
        """Generate comprehensive HTML and JSON reports"""
        # JSON report
        json_file = self.output_dir / f"{self.domain}_{self.timestamp}.json"

        report_data = {
            "domain": self.domain,
            "scan_time": self.timestamp,
            "total_subdomains": len(self.results["subdomains"]),
            "categories": {k: v for k, v in self.results["interesting_targets"].items() if v},
            "all_subdomains": sorted(list(self.results["subdomains"]))
        }

        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2)

        # HTML report
        html_file = self.output_dir / f"{self.domain}_{self.timestamp}.html"
        html_content = self._generate_html_report(report_data)

        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"\n[+] Reports generated:")
        print(f"    JSON: {json_file}")
        print(f"    HTML: {html_file}")

        return json_file, html_file

    def _generate_html_report(self, data: Dict) -> str:
        """Generate professional HTML report"""
        categories_html = ""
        for category, subdomains in data["categories"].items():
            if subdomains:
                priority = self._get_priority_level(category)
                categories_html += f"""
                <div class="category {priority}">
                    <h3>{category.upper()} ({len(subdomains)})</h3>
                    <ul>
                        {"".join(f'<li>{sub}</li>' for sub in subdomains[:20])}
                        {f'<li><em>...and {len(subdomains) - 20} more</em></li>' if len(subdomains) > 20 else ''}
                    </ul>
                </div>
                """

        html = f"""<!DOCTYPE html>
<html>
<head>
    <title>SubdomainHunter Report - {data['domain']}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .stat-card h3 {{
            margin: 0 0 10px 0;
            color: #667eea;
        }}
        .stat-card .number {{
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }}
        .category {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .category.critical {{
            border-left: 4px solid #e74c3c;
        }}
        .category.high {{
            border-left: 4px solid #f39c12;
        }}
        .category.medium {{
            border-left: 4px solid #3498db;
        }}
        .category.low {{
            border-left: 4px solid #95a5a6;
        }}
        .category h3 {{
            margin-top: 0;
            color: #333;
        }}
        .category ul {{
            list-style: none;
            padding: 0;
        }}
        .category li {{
            padding: 8px;
            border-bottom: 1px solid #eee;
            font-family: monospace;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🎯 SubdomainHunter Report</h1>
        <p>Target: <strong>{data['domain']}</strong></p>
        <p>Scan Time: {data['scan_time']}</p>
    </div>

    <div class="stats">
        <div class="stat-card">
            <h3>Total Subdomains</h3>
            <div class="number">{data['total_subdomains']}</div>
        </div>
        <div class="stat-card">
            <h3>High-Priority Targets</h3>
            <div class="number">{sum(len(v) for k, v in data['categories'].items() if k in ['jenkins', 'gitlab', 'admin', 'api'])}</div>
        </div>
        <div class="stat-card">
            <h3>Development Environments</h3>
            <div class="number">{sum(len(v) for k, v in data['categories'].items() if k in ['dev', 'staging', 'test', 'qa'])}</div>
        </div>
    </div>

    <h2>Categorized Targets</h2>
    {categories_html}

    <div class="footer">
        <p>Generated by <strong>SubdomainHunter v1.0.0</strong></p>
        <p>Professional subdomain enumeration for security researchers</p>
    </div>
</body>
</html>"""
        return html

    def _get_priority_level(self, category: str) -> str:
        """Determine priority level for category"""
        if category in ["jenkins", "gitlab", "admin", "jira", "confluence"]:
            return "critical"
        elif category in ["api", "internal", "vpn"]:
            return "high"
        elif category in ["dev", "staging", "test", "qa"]:
            return "medium"
        else:
            return "low"

    def run(self):
        """Execute full reconnaissance workflow"""
        print(f"\n{'='*60}")
        print(f"SubdomainHunter - Automated Reconnaissance")
        print(f"Target: {self.domain}")
        print(f"{'='*60}\n")

        # Phase 1: Subdomain Enumeration
        subdomains = self.run_subfinder()
        self.results["subdomains"] = subdomains

        if not subdomains:
            print("[-] No subdomains found. Exiting.")
            return

        # Phase 2: Categorization
        print(f"\n[*] Categorizing {len(subdomains)} subdomains...")
        categories = self.categorize_subdomains(subdomains)

        for category, subs in categories.items():
            if subs:
                self.results["interesting_targets"][category] = subs
                print(f"  [{category.upper()}]: {len(subs)} found")

        # Phase 3: Report Generation
        print(f"\n[*] Generating reports...")
        self.generate_report()

        print(f"\n{'='*60}")
        print(f"[+] Reconnaissance complete!")
        print(f"[+] Found {len(subdomains)} total subdomains")
        print(f"[+] Identified {sum(len(v) for v in self.results['interesting_targets'].values())} interesting targets")
        print(f"{'='*60}\n")

def main():
    parser = argparse.ArgumentParser(
        description="SubdomainHunter - Professional subdomain enumeration and analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python subdomain-hunter.py -d example.com
  python subdomain-hunter.py -d target.com -o my_results
        """
    )

    parser.add_argument('-d', '--domain', required=True, help='Target domain')
    parser.add_argument('-o', '--output', default='results', help='Output directory (default: results)')

    args = parser.parse_args()

    hunter = SubdomainHunter(args.domain, args.output)
    hunter.run()

if __name__ == "__main__":
    main()
