# 🎯 SubdomainHunter

**Professional subdomain enumeration and categorization tool for security researchers and bug bounty hunters.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Features

- 🔍 **Automated Subdomain Discovery** - Integrates powerful enumeration tools
- 📊 **Intelligent Categorization** - Automatically identifies high-value targets
- 📈 **Professional Reports** - Generates beautiful HTML and JSON reports
- ⚡ **Fast & Efficient** - Optimized for large-scale reconnaissance
- 🎨 **Clean Output** - Color-coded priority levels for quick assessment

## What Makes SubdomainHunter Different?

While many tools just enumerate subdomains, SubdomainHunter provides **actionable intelligence**:

- **Prioritized Targets**: Automatically identifies critical infrastructure (Jenkins, GitLab, Admin panels)
- **Development Environments**: Highlights staging, test, and QA environments often less secured
- **Beautiful Reports**: Professional HTML reports perfect for client delivery or personal tracking
- **Time-Saving**: Focus on what matters - high-value targets identified in seconds

## Installation

### Requirements

- Python 3.8+
- [subfinder](https://github.com/projectdiscovery/subfinder) (included in most pentest distributions)

### Quick Install

```bash
# Clone the repository
git clone https://github.com/yourusername/subdomain-hunter.git
cd subdomain-hunter

# No dependencies required - uses standard library!
python subdomain-hunter.py -d example.com
```

## Usage

### Basic Scan

```bash
python subdomain-hunter.py -d target.com
```

### Custom Output Directory

```bash
python subdomain-hunter.py -d target.com -o my_results
```

### Example Output

```
============================================================
SubdomainHunter - Automated Reconnaissance
Target: example.com
============================================================

[*] Running subfinder on example.com...
[+] Subfinder found 505 subdomains

[*] Categorizing 505 subdomains...
  [JENKINS]: 1 found
  [ADMIN]: 2 found
  [API]: 2 found
  [DEV]: 4 found
  [VPN]: 1 found
  [MAIL]: 4 found
  [OTHER]: 491 found

[*] Generating reports...
[+] Reports generated:
    JSON: results/example.com_20260917_125116.json
    HTML: results/example.com_20260917_125116.html

============================================================
[+] Reconnaissance complete!
[+] Found 505 total subdomains
[+] Identified 14 high-priority targets
============================================================
```

## Target Categories

SubdomainHunter automatically categorizes findings into:

### 🔴 Critical Priority
- **Jenkins** - CI/CD servers (often RCE vulnerable)
- **GitLab** - Source code repositories
- **Admin** - Admin panels and dashboards
- **Jira/Confluence** - Internal tools

### 🟠 High Priority
- **API** - API endpoints and gateways
- **Internal** - Internal corporate systems
- **VPN** - Remote access points

### 🟡 Medium Priority
- **Dev/Staging/QA** - Development environments (often less secured)
- **Test** - Testing environments

### ⚪ Low Priority
- **Mail** - Email infrastructure
- **Other** - Uncategorized subdomains

## Report Formats

### HTML Report
- Beautiful, responsive design
- Color-coded priority levels
- Quick statistics overview
- Perfect for presentations or client delivery

### JSON Report
- Machine-readable format
- Easy integration with other tools
- Complete subdomain listing
- Categorized findings

## Use Cases

- 🎯 **Bug Bounty Hunting** - Quickly identify high-value targets
- 🔒 **Security Assessments** - Professional reconnaissance for pentests
- 📊 **Attack Surface Management** - Track organizational exposure
- 🎓 **Security Research** - Gather intelligence on targets

## Responsible Disclosure

⚠️ **Important**: Only use SubdomainHunter on domains you have permission to test.

- Always follow responsible disclosure practices
- Respect bug bounty program rules
- Never test on unauthorized systems
- Use for defensive security and authorized research only

## Roadmap

- [ ] HTTP probing integration
- [ ] Screenshot capture of live hosts
- [ ] Nuclei template scanning
- [ ] Multi-domain batch processing
- [ ] Export to other formats (PDF, CSV)
- [ ] Integration with other recon tools

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## Support Development

If SubdomainHunter saves you time or helps you find bugs, consider:

- ⭐ Star this repository
- 💰 [Sponsor via GitHub](https://github.com/sponsors/yourusername)
- ☕ [Buy me a coffee](https://buymeacoffee.com/yourusername)
- 🐛 Report bugs and suggest features

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

**ANON Security Research**
- Professional security researcher
- Bug bounty hunter
- Offensive security specialist

## Disclaimer

This tool is provided for educational and defensive security purposes only. Users are responsible for ensuring they have authorization before scanning any systems. The author assumes no liability for misuse or damage caused by this program.

---

**Made with 🔥 by security researchers, for security researchers**
