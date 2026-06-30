# Incident Report — Brute Force & Reconnaissance Activity

*Lab environment — synthetic log data from SOC training platform, not a live production incident.*

Date: June 30, 2026 | Log window: [insert start–end time] | Severity: High | Status: Open — Pending Internal Host Investigation

## Summary
SSH brute force activity detected against [insert target host/IP], with 2,444 of 5,069 failed authentication attempts (48%) traced to internal host 192.168.229.101, out of 7,143 total connection attempts and a 4.2% success rate. Source being internal needs verification — could be a compromised host or an internal scanning tool, not yet confirmed either way. Concurrent web reconnaissance was logged against the application server: automated 404/429 scanning, PHP file probing consistent with WordPress fingerprinting, and a direct request for an exposed database backup file (dump.sql). ModSecurity blocked the dump.sql request and flagged two external IPs for repeated rule violations. No evidence of successful data exfiltration.

## Evidence
SSH log: 7,143 total connections, 301 succeeded, 5,069 failed, remainder undetermined. Top source: 192.168.229.101 (2,444 attempts, internal address).

Access log: 8,059 error lines logged. 135 returned 404, 811 returned 429. 125 requests targeted .php files outside the known application stack, including wp-trackback.php, /z.php, /x.php, /yellow.php. All PHP probe requests returned 301, 404, or 429, no 200 responses recorded.

Error log: ModSecurity blocked a request for /dump.sql. Two external IPs flagged: 42.193.171.36 (4 hits), 91.219.237.39 (2 hits).

## Analysis
The SSH failure volume and rate don't match manual login behavior and fit an automated brute force pattern. The concentration of attempts from a single internal address is the finding that needs follow-up — it could mean an internal host is compromised and being used as a launch point, or it could be a misconfigured internal scanning tool. Can't tell which from this log set alone. "Undetermined" sessions are connections that opened without a clean success/fail outcome, typically a dropped connection or timeout. They don't change the overall picture but should be accounted for.

The web-layer activity reads as reconnaissance, not exploitation. The 429 volume shows the server's rate limiting engaged against an automated client. The PHP probing — non-standard filenames plus a WordPress-specific path on a server that may not run WordPress — looks like a fingerprinting pass to map the stack. None of the probes returned a 200, so nothing was confirmed to exist on the attacker's end.

The dump.sql request is the most serious single line item. It's a known low-effort probe attackers run routinely, checking for backup files left in public web directories. ModSecurity blocked it.

## Impact assessment
No confirmed compromise. Authentication controls, rate limiting, and ModSecurity held across all observed vectors. Open item is the status of 192.168.229.101 — compromised host vs. misconfigured internal tool is unresolved and should be escalated.

## Recommendations
Recommend 192.168.229.101 be isolated and inspected by IR/infra to confirm whether it's compromised or a misconfigured scanner. Recommend confirming dump.sql and other backup files aren't present in the web root on this or other servers. Recommend WAF rule coverage for the observed PHP probe patterns be reviewed, and that 42.193.171.36 and 91.219.237.39 be added to the blocklist. Recommend review of SSH exposure and auth method if internet-facing.
