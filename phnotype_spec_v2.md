# Unified Phenotype Object Spec (Spark SQL) + Upload Examples

*Covers all four Excel datasets, with structured condition details*

---

## 1. Full Table Schema

All required fields are **bold**. Optional fields may be `NULL`.  
`double` = Spark `DOUBLE`.

| Field name | Data type | Required | Description |
|------------|-----------|----------|-------------|
| **strain** | `string` | **Y** | Bacterial strain / background identifier |
| gene | `string` | N | Gene symbol or locus tag (`NULL` for whole-strain calls) |
| **base_medium** | `string` | N | Core medium or plate matrix (e.g. `M9`, `LB`, `Biolog IF-0`) |
| **compound** | `string` | N | Primary test compound or stressor (e.g. `D-Glucose`, `H2O2`) |
| compound_role | `string` | N | Functional role of compound — `carbon_source`, `nitrogen_source`, `stress_agent`, `antibiotic`, `control` |
| concentration | `double` | N | Numeric concentration value |
| conc_unit | `string` | N | Unit for concentration (`mM`, `µg/mL`, `% w/v`, etc.) |
| temperature_C | `double` | N | Incubation temperature (°C) |
| pH | `double` | N | Medium pH |
| other_params | `string` | N | Rare/complex extras (`1.5 M NaCl`, `anaerobic`, ...) |
| plate_well | `string` | N | Platform-specific locator (`set1IT003`, `PM1_A02`) |
| **outcome** | `string` | **Y** | Qualitative call — `Growth`, `No growth`, `Reduced growth`, `Sensitive`, etc. |
| score | `double` | N | Numeric fitness / OD / Z-score (`NULL` if absent) |
| **assay_method** | `string` | **Y** | Experimental method (`TnSeq fitness assay`, `Biolog PM`, ...) |
| **evidence_code** | `string` | **Y** | Evidence keyword / ECO code (`IMP`, `EXP`, `ECO:0001099`, ...) |
| **reference** | `string` | **Y** | Study or dataset citation / internal ID |

> **Why split the old `condition` field?**  
> *Searchability* (e.g. "all carbon_source tests in LB"), *future ontology links* (map `compound` to CHEBI, `compound_role` to MCO), and *null-friendly* storage.

---

## 2. Spark DDL

```sql
CREATE TABLE microbial_phenotypes (
  strain          STRING,
  gene            STRING,
  base_medium     STRING,
  compound        STRING,
  compound_role   STRING,
  concentration   DOUBLE,
  conc_unit       STRING,
  temperature_C   DOUBLE,
  pH              DOUBLE,
  other_params    STRING,
  plate_well      STRING,
  outcome         STRING,
  score           DOUBLE,
  assay_method    STRING,
  evidence_code   STRING,
  reference       STRING
)
USING PARQUET;
```

---

## 3. Illustrative Upload Rows (one per dataset)

| strain | gene | base_medium | compound | compound_role | concentration | conc_unit | temperature_C | pH | other_params | plate_well | outcome | score | assay_method | evidence_code | reference |
|--------|------|-------------|----------|---------------|---------------|-----------|---------------|----|--------------|-----------|---------|----|--------------|---------------|-----------|
| BW25113 | thrA | M9 | D-Galacturonic acid | carbon_source | NULL | NULL | 37 | NULL | NULL | set1IT018 | Reduced growth | -5.2 | TnSeq fitness assay | IMP | RB-TnSeq BW25113 2025 |
| MG1655 | recA | LB | Hydrogen peroxide | stress_agent | 0.5 | mM | 37 | NULL | NULL | Exp_H2O2 | Sensitive | -4.2 | Colony size screen | IMP | Nichols et al. 2011 |
| 562.61239 | NULL | GN2 minimal | Salicin | carbon_source | NULL | NULL | 37 | NULL | NULL | GN2_Salicin | No growth | NULL | Biolog GN2 panel | EXP | Argonne SDL 2024 |
| MG1655 | NULL | IF-0 | L-Arabinose | carbon_source | NULL | NULL | 37 | NULL | NULL | PM1_A02 | No growth | 0.00 | Biolog PM1 | ECO:0001099 | MG1655 PM 2025 |

---

## 4. Dataset-to-Field Mapping Quick Reference

| Dataset | base_medium source | compound (+role) source | conc / unit columns | plate_well mapping | Other notes |
|---------|-------------------|------------------------|---------------------|-------------------|-------------|
| **RBTnSeq BW25113** | Constant `"M9"` | Column header "X (C)" → `compound`; role = `carbon_source`; time-zero → `control` | n/a | `set1ITnnn` | May flag Time0 samples in `other_params` |
| **Nichols / Carol Gross Screen** | Condition sheet (LB / M9) | Condition sheet lists compound & category → role = `antibiotic` / `stress_agent` | yes | experiment ID or row key | Variable temps (e.g. 42°C) → `temperature_C` |
| **48 Isolates Carbon Panel** | `"GN2 minimal"` | Substrate column header; role = `carbon_source` | n/a | Substrate name | Binary growth; leave `score` NULL |
| **MG1655 PM Plates** | `"IF-0"` base medium | Biolog lookup table; roles: carbon / nitrogen / P/S source | n/a | `PM1_A02`, etc. | OD in `score`; Growth class → `outcome` |
