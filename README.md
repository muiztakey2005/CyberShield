:::writing{variant="document" id="63821"}
# CyberShield – Cybersecurity Incident & Threat Intelligence Analytics Platform

## Project Overview

CyberShield is a Data Analytics project that analyzes cybersecurity incident records and known exploited vulnerabilities to identify patterns, understand threats, and explore vulnerability trends.

The project uses Python, SQL, MySQL, and Power BI to clean, process, analyze, and visualize cybersecurity data through an interactive dashboard.

It focuses on two separate datasets:
- **VERIS Community Database (VCDB):** Used to analyze reported cybersecurity incidents, attack patterns, attacker types, industries, regions, and yearly trends.
- **CISA Known Exploited Vulnerabilities (KEV):** Used to analyze known exploited vulnerabilities, affected vendors and products, ransomware campaign usage, and remediation deadlines.

## Project Objectives

- Analyze reported cybersecurity incident records.
- Identify frequently observed attack patterns and attacker types.
- Explore incident trends across years and regions.
- Analyze vulnerabilities listed in the CISA KEV catalog.
- Identify vendors and products with the highest number of catalog entries.
- Examine known ransomware campaign usage.
- Analyze listed remediation deadlines.
- Build an interactive Power BI dashboard to communicate findings.

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data cleaning and analysis |
| Pandas & NumPy | Data manipulation |
| Matplotlib, Seaborn & Plotly | Exploratory data analysis and visualization |
| Google Colab | Python development |
| MySQL | Data storage and SQL analysis |
| SQL | Data querying and analysis |
| Power BI | Interactive dashboard development |

## Datasets Used

### 1. VERIS Community Database (VCDB)

The VERIS dataset contains reported cybersecurity incident records.

**Analysis includes:**
- Incident records and unique incident IDs
- Attack pattern distribution
- Attacker type distribution
- Victim industry and region analysis
- Yearly incident trends
- Attack pattern comparisons

Dataset source: [VERIS Community Database](https://github.com/vz-risk/VCDB)

### 2. CISA Known Exploited Vulnerabilities (KEV)

The CISA KEV catalog contains vulnerabilities that have been identified as exploited in the wild.

**Analysis includes:**
- Total vulnerability entries
- Vendor and product analysis
- Yearly vulnerability additions
- Ransomware campaign usage
- Remediation deadline status
- Vulnerability details and required actions

Dataset source: [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)

## Project Workflow

1. **Data Collection:** Obtained cybersecurity incident and vulnerability datasets.
2. **Data Cleaning:** Used Python and Pandas to handle missing values, remove exact duplicate records, select relevant columns, and prepare clean datasets.
3. **Exploratory Data Analysis:** Analyzed attack patterns, attacker types, vendors, products, ransomware usage, and trends.
4. **Database Management:** Stored the cleaned datasets in MySQL.
5. **SQL Analysis:** Used filtering, aggregation, joins where appropriate, CTEs, subqueries, and window functions for analytical queries.
6. **Dashboard Development:** Built interactive Power BI dashboards to present the analytical results.

## Power BI Dashboard

The project contains two dashboard pages:

### Page 1 – Cybersecurity Incident Overview

Focuses on reported incident records from the VERIS dataset.

Includes:
- Incident record KPIs
- Attack pattern distribution
- Yearly incident trends
- Attacker type distribution
- Industry and region analysis
- Incident-related visualizations

### Page 2 – Vulnerability Intelligence

Focuses on vulnerabilities from the CISA KEV catalog.

Includes:
- KEV vulnerability KPIs
- Top vulnerable vendors
- Top vulnerable products
- Yearly vulnerability additions
- Ransomware campaign usage
- Remediation deadline status
- Vulnerability details table

## Key Analytical Areas

- Cybersecurity incident pattern analysis
- Attacker behavior analysis
- Industry and regional distribution
- Vulnerability vendor and product analysis
- Ransomware-related vulnerability analysis
- Remediation deadline analysis
- Time-based trend analysis

## Important Data Limitations

- VERIS and CISA KEV are separate datasets and are not directly joined in this project.
- VERIS records represent incidents available in the dataset, not all cybersecurity incidents worldwide.
- Attack pattern categories may overlap, so their counts should not be added to calculate total incidents.
- CISA KEV entries do not confirm whether a particular organization is exposed or has patched a vulnerability.
- A passed remediation deadline does not prove that a vulnerability remains unpatched.
- The KEV catalog is updated over time, so analytical results may change as new entries are added.

## Project Structure

```text
CyberShield/
│
├── Dataset/
│   ├── veris_incidents_clean.csv
│   └── cisa_kev_clean.csv
│
├── Python/
│   └── CyberShield_Analysis.ipynb
│
├── SQL/
│   └── CyberShield_Analysis.sql
│
├── PowerBI/
│   └── CyberShield_Dashboard.pbix
│
└── README.md
```

## Skills Demonstrated

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Python for Data Analytics
- SQL Querying and Data Analysis
- MySQL Database Management
- Data Visualization
- Power BI Dashboard Development
- Analytical Thinking and Data Interpretation

## Conclusion

CyberShield demonstrates an end-to-end data analytics workflow using cybersecurity datasets. It combines Python-based data preparation, SQL analysis, MySQL database management, and Power BI visualization to explore reported incidents and known exploited vulnerabilities.

The project provides an analytical view of cybersecurity data and demonstrates practical skills relevant to Data Analyst and Data Science roles.
:::