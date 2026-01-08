# Automated Data Collection & Analysis Pipeline

This repository contains an **end-to-end automated data collection and preprocessing pipeline** built to transform raw, messy operational data into **clean, validated, Tableau-ready datasets**.

The primary goal of this system is to **eliminate manual data preparation**, enforce consistent data quality checks, and reliably support downstream analytics, dashboards, and reporting workflows.

---

## Problem

In real-world analytics workflows, raw data is often:
- inconsistent across sources
- manually cleaned each week
- prone to formatting and validation errors
- not directly usable for dashboards or reporting

At The Marcus Harris Foundation and similar analytics projects, this resulted in:
- 10+ hours/week spent cleaning and reformatting data
- inconsistent metrics across reports
- difficulty maintaining reliable Tableau dashboards for stakeholders

---

## Solution Overview

I built a **Python-based automated data collection and analysis pipeline** that:

- Ingests raw data from files or operational sources
- Applies deterministic data quality checks (schema, nulls, ranges)
- Standardizes formats and field definitions
- Produces **analytics- and Tableau-ready outputs**
- Enables fast, repeatable dashboard refreshes

This pipeline directly powers Tableau dashboards used by **100+ stakeholders**.

---

## Pipeline Architecture

Raw Data
   ↓
Ingestion
   ↓
Validation (Quality Checks)
   ↓
Transformation (Standardization / Metrics)
   ↓
Clean Outputs (CSV / Excel)
   ↓
Tableau Dashboards


---

## Key Design Decisions

### Deterministic Data Validation
- Enforced Snowflake-style data quality checks using SQL and Python
- Early failure on missing values, invalid formats, or inconsistent fields
- Prevents bad data from silently reaching dashboards

### Modular, dbt-Style Transformations
- Transform logic separated into reusable, modular scripts
- Raw data is never overwritten (immutable inputs)
- Clean outputs follow consistent schemas for Tableau ingestion

### Tableau-First Output Design
- Output tables are explicitly shaped for Tableau:
  - consistent column names
  - standardized date formats
  - precomputed metrics
- Eliminates last-minute dashboard fixes

---

## Impact & Results

- ⏱️ **Reduced weekly data preparation time from 10+ hours to under 2 hours**
- 📊 Enabled reliable Tableau dashboards for **100+ stakeholders**
- ✅ Improved reporting accuracy and clarity by ~25% through standardized KPIs
- 🔁 Enabled repeatable, low-risk dashboard refreshes
- 📄 Improved cross-project consistency through documented datasets and definitions

---

## Real-World Usage

This pipeline supported:
- Tableau dashboards tracking donations, attendance, and engagement
- Excel-based validated reports for leadership review
- Automated metric summaries used in stakeholder presentations

The same architecture can be reused for:
- business intelligence dashboards
- ML-ready datasets
- reporting automation

---

## Reliability & Data Quality Approach

- Raw data preserved for traceability
- Validation enforced before transformation
- Standardized schemas across outputs
- Clear data definitions documented for stakeholders
- Fail-fast behavior for data quality issues

---

## Tech Stack

Python, SQL, Excel, Tableau, Data Validation, Modular ETL Scripts

---

## What I’d Improve Next

- Add orchestration (Airflow / Dagster)
- Introduce automated testing for validation rules
- Support incremental and scheduled loads
- Add monitoring and data freshness alerts

---

## How This Fits My Experience

This pipeline directly reflects my work as a **Data Entry & Analysis Intern at The Marcus Harris Foundation**, where I:
- cleaned and validated 1,500+ records
- built and maintained Tableau dashboards
- developed lightweight ETL workflows
- reduced manual reporting time by ~25%
- supported data-driven decision making for 100+ stakeholders
