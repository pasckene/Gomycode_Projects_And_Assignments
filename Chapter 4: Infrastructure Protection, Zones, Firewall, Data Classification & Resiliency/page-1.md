
# Infrastructure Protection, Zones, Firewall, Data Classification & Resiliency

## Question:

You are a Security Administrator. How would you protect:

* Your server (e.g., web server)?
* Your hosts/endpoints (e.g., employee machines)?
* Your network?

## Answer:

### Protecting a Server

I would protect a server by:

* Applying regular patches and updates
* Using firewalls
* Enabling HTTPS/TLS
* Disabling unnecessary services
* Implementing strong authentication and MFA
* Monitoring logs
* Using antivirus/EDR tools
* Backing up data regularly

---

### Protecting Hosts/Endpoints

I would protect endpoints by:

* Installing antivirus/EDR solutions
* Enforcing strong passwords
* Using disk encryption
* Applying OS updates
* Restricting user privileges
* Enabling MFA
* Providing security awareness training

---

### Protecting the Network

I would secure the network by:

* Using firewalls
* Implementing IDS/IPS
* Segmenting the network with VLANs
* Using VPNs
* Monitoring network traffic
* Securing Wi-Fi
* Applying access control lists (ACLs)

---

# 2. Cloud Service Models – IaaS, PaaS, SaaS

## Question:

What are the three main types of cloud service models?

## Answer:

| Model | Meaning                     |
| ----- | --------------------------- |
| IaaS  | Infrastructure as a Service |
| PaaS  | Platform as a Service       |
| SaaS  | Software as a Service       |

---

## Follow-up Question:

Returning to your XAMPP web application, which cloud service model would be most suitable if you wanted to migrate it to the cloud, and why?

## Answer:

The best cloud service model for a XAMPP web application would be **IaaS** because it provides:

* Full server control
* OS-level access
* Custom software installation
* Flexibility for Apache, PHP, and MySQL configuration

Example:
Deploying the application on Amazon Web Services EC2.

---

# 3. Server Placement – Network Architecture Planning

## Question:

There’s a specific zone in a network where public-facing servers (like your XAMPP web server) are usually placed for security and access control.

What is this type of zone called?

## Answer:

The zone is called a **DMZ (Demilitarized Zone)**.

A DMZ is used to isolate public-facing servers from the internal network for better security.

---

## Question:

Draw a simple network diagram showing:

* Internet
* Firewall(s)
* Web server
* Internal network
* Security layers

## Answer:

```text id="x5p73r"
                INTERNET
                    |
           [External Firewall]
                    |
                  DMZ
                    |
              [Web Server]
                    |
           [Internal Firewall]
                    |
            INTERNAL NETWORK
         ---------------------
         |         |         |
      Users     Database   Admin
```

---

# 4. Firewall vs IDS vs IPS – Key Differences

## Question:

What are the main differences between the following security technologies?

* Firewall
* IDS
* IPS

## Answer:

| Technology | Function                    | Action                    |
| ---------- | --------------------------- | ------------------------- |
| Firewall   | Filters network traffic     | Allows or blocks traffic  |
| IDS        | Detects suspicious activity | Sends alerts only         |
| IPS        | Detects and blocks attacks  | Alerts and blocks traffic |

---

### Firewall

A firewall controls incoming and outgoing network traffic based on security rules.

---

### IDS (Intrusion Detection System)

An IDS monitors network traffic and alerts administrators about suspicious activity.

Example:
Snort

---

### IPS (Intrusion Prevention System)

An IPS detects and automatically blocks malicious activity in real time.

---

# 5. Practical Task – Using iptables on Kali Linux

## Question:

Check if iptables is installed.

## Answer:

```bash id="b1a9cs"
sudo iptables -L
```

This command displays current firewall rules.

---

## Question:

Test basic connectivity from Windows to Kali.

## Answer:

```bash id="m11w9k"
ping <Kali_IP>
```

If connectivity works, replies will be received.

---

## Question:

Block ICMP traffic (ping) from Windows.

## Answer:

```bash id="p3k7rt"
sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
```

### Observation:

Ping requests from Windows will timeout because ICMP packets are blocked.

---

## Question:

Remove the ICMP block rule.

## Answer:

```bash id="s9q2lv"
sudo iptables -D INPUT -p icmp --icmp-type echo-request -j DROP
```

Ping should work again.

---

## Question:

Block the entire Windows host IP.

## Answer:

```bash id="w8f4na"
sudo iptables -A INPUT -s <Windows_IP> -j DROP
```

### Observation:

All traffic from the Windows machine will be blocked.

---

## Question:

Remove the IP block.

## Answer:

```bash id="g7t5ux"
sudo iptables -D INPUT -s <Windows_IP> -j DROP
```

Connectivity is restored.

---

# 6. Data Classification Types + Scenario

## Question:

What are the common types of data classification used in cybersecurity?

## Answer:

| Classification | Description                         |
| -------------- | ----------------------------------- |
| Public         | Information safe for public access  |
| Internal       | Information for internal use only   |
| Confidential   | Sensitive organizational data       |
| Restricted     | Highly sensitive and regulated data |

---

## Scenario Question:

Imagine your organization stores employee health records and customer banking data. How would you classify that data, and what protections would you apply?

## Answer:

Employee health records and banking data should be classified as:

# Restricted / Highly Confidential

Because they contain:

* Personally Identifiable Information (PII)
* Financial data
* Medical records

### Protections:

* Encryption
* MFA
* Access control
* Data Loss Prevention (DLP)
* Logging and monitoring
* Secure backups
* Compliance with regulations such as:

  * Health Insurance Portability and Accountability Act
  * Payment Card Industry Security Standards Council

---

# 7. Backup vs Resiliency – What’s the Difference?

## Question:

What’s the difference between Backup and Resiliency?

## Answer:

| Backup                 | Resiliency                            |
| ---------------------- | ------------------------------------- |
| Creates copies of data | Keeps systems running during failures |
| Used for recovery      | Used for uptime and continuity        |
| Reactive measure       | Proactive measure                     |

---

## Follow-up Question:

Can you name a tool or technique used for:

* Regular backups
* Ensuring system uptime/resilience?

## Answer:

### Backup Tools/Techniques

* Veeam Backup & Replication
* Cloud backups
* External storage
* rsync

---

### Resiliency Tools/Techniques

* RAID
* Clustering
* Load balancing
* UPS systems
* Offsite replication
