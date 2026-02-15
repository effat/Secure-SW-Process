# Secure FSMA Traceability Compliance Starter

## Overview

This repository is a starter kit for the Secure Software Processes course project.

Students will:

1. Implement **static taint tracking** for regulatory rules.
2. Handle **regulation updates** with Kubernetes CRDs and Git pre-commit hooks.
3. Perform **threat modeling** (STRIDE) for the compliance pipeline.

---

##  Step 0: Create the Regulatory YAML

- Read FSMA Section 204 [FDA Traceability Rule](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods)
- Extract required Key Data Elements (KDEs)
- Map KDEs into `rules/fsma_traceability.yaml`
- Document the mapping in `docs/regulation-source.md`

---

##  Step 1: Enable Git Hooks

```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit

## Step 2: CI Pipeline

Runs on push to GitHub

Validates schema, regenerates CRD, verifies static taint

# Step 3: Deliverables

Static Taint Tracking: CI + scripts prevent tampering of regulatory rules.

Address Regulation Updates: Pre-commit hooks + K8s CRD propagation enforce rule changes.

Threat Modeling: Document STRIDE analysis with diagram and mitigation plan.

# Step 4: Run / Test
# Validate schema
python scripts/validate_schema.py rules/fsma_traceability.yaml

# Generate CRD
python scripts/generate_crd.py rules/fsma_traceability.yaml

# Verify static taint
python scripts/verify_taint.py
