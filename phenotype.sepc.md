# Minimal Phenotype Object Spec (Spark SQL) & Upload Examples

This document defines a single Spark SQL table that can ingest **individual phenotype calls** from all four Excel datasets.  
All fields are strings unless otherwise noted. `double` = Spark `DOUBLE` type.

| Field name        | Data type | Required | Description                                                                          |
|-------------------|-----------|----------|--------------------------------------------------------------------------------------|
| strain            | string    | **Y**    | Identifier of the bacterial strain / background                                      |
| gene              | string    | N        | Gene symbol or locus tag (NULL for whole-strain calls)                               |
| condition         | string    | **Y**    | Human-readable description of growth / stress condition                              |
| outcome           | string    | **Y**    | Qualitative call: *Growth*, *No growth*, *Reduced growth*, *Sensitive*, etc.         |
| score             | double    | N        | Numeric fitness, Z-score, OD, or other measurement (NULL if none)                    |
| assay_method      | string    | **Y**    | Experimental method (e.g. *TnSeq fitness assay*, *Biolog PM*)                        |
| evidence_code     | string    | **Y**    | Evidence keyword or ECO code (e.g. *IMP*, *EXP*, *ECO:0001099*)                      |
| reference         | string    | **Y**    | Study / dataset citation or internal ID                                              |

> **Notes**  
> • `score` stores raw numbers when available (log₂ fitness, Z-score, OD, etc.).  
> • All optional fields may be left **NULL** in Spark if not present.  
> • Strings can later be mapped to ontology CURIEs without altering schema.

---

## Ready-to-Upload Sample Rows

Below are **illustrative** Spark-ready rows (tab-delimited or CSV) that show how each Excel file maps into the schema.  
They are *not exhaustive*—just two example calls per dataset.

### 1 · RBTnSeq-BW25113 (`RBTnSeq-BW25113_sample.xlsx`)

| strain  | gene | condition                                   | outcome        | score | assay_method          | evidence_code | reference                                      |
|---------|------|---------------------------------------------|----------------|-------|-----------------------|---------------|------------------------------------------------|
| BW25113 | thrA | D-Glucose (M9 minimal, carbon)              | Reduced growth | -3.8  | TnSeq fitness assay   | IMP           | RB-TnSeq BW25113 internal 2025                 |
| BW25113 | uxuB | D-Galacturonic Acid (M9, carbon)            | No growth      | -5.2  | TnSeq fitness assay   | IMP           | RB-TnSeq BW25113 internal 2025                 |

### 2 · Nichols / Carol Gross Screen (`CarolGross_NIHMS261392_sample.xls`)

| strain | gene | condition                         | outcome      | score | assay_method        | evidence_code | reference                 |
|--------|------|-----------------------------------|--------------|-------|---------------------|---------------|---------------------------|
| MG1655 | recA | Hydrogen peroxide 0.5 mM          | Sensitive    | -4.2  | Colony size screen  | IMP           | Nichols et al. 2011       |
| MG1655 | mrdA | Mecillinam 1 µg mL⁻¹              | No growth    | -3.7  | Colony size screen  | IMP           | Nichols et al. 2011       |

### 3 · 48 Environmental Isolates (`ANL-SDL-48EcoliPhenos.xlsx`)

| strain       | gene | condition | outcome   | score | assay_method             | evidence_code | reference                           |
|--------------|------|-----------|-----------|-------|--------------------------|---------------|-------------------------------------|
| 562.61239    | NULL | Salicin   | No growth | NULL  | Biolog GN2 carbon panel  | EXP           | Argonne SDL isolate panel 2024      |
| 562.61140    | NULL | D-Glucose | Growth    | NULL  | Biolog GN2 carbon panel  | EXP           | Argonne SDL isolate panel 2024      |

### 4 · MG1655 Phenotype Microarray (`MG1655_Phenotype_Microarray_Table.xlsx`)

| strain | gene | condition                              | outcome      | score | assay_method        | evidence_code | reference                   |
|--------|------|----------------------------------------|--------------|-------|---------------------|---------------|-----------------------------|
| MG1655 | NULL | L-Arabinose (PM1 A2)                   | No growth    | 0.00  | Biolog PM1          | ECO:0001099   | MG1655 PM run 2025          |
| MG1655 | NULL | N-Acetyl-D-glucosamine (PM1 A3)        | Reduced growth | 0.20 | Biolog PM1          | ECO:0001099   | MG1655 PM run 2025          |

---

### How Each Field Maps → Dataset Columns

| Schema field   | RB-TnSeq sheet                    | Nichols screen            | 48 Isolates sheet            | PM sheet                              |
|----------------|-----------------------------------|---------------------------|------------------------------|---------------------------------------|
| `strain`       | Parent strain *BW25113* (constant)| “strain” = MG1655         | Genome ID column (562.*)     | MG1655 (constant)                     |
| `gene`         | `sysName` / `locusId`             | Keio gene column          | **NULL** (whole-strain)      | **NULL** (whole-strain)               |
| `condition`    | column header text (exp-meta)     | “Condition Name”          | substrate column header      | Plate+Well compound string            |
| `outcome`      | computed sign of fitness score    | binary/ternary phenotype  | binary growth (1/0)          | Growth / Low / No                     |
| `score`        | fitness value (log₂ ratio)        | colony-size Z-score       | **NULL** (binary)            | OD or Biolog intensity (scaled)       |
| `assay_method` | “TnSeq fitness assay”             | “Colony size screen”      | “Biolog GN2 carbon panel”    | “Biolog PM1/PM2/PM3/PM4”              |
| `evidence_code`| IMP                               | IMP                       | EXP                          | ECO:0001099                           |
| `reference`    | internal dataset citation         | Nichols et al. 2011       | Argonne panel ID             | Lab run ID / year                     |

---

### Loading into Spark SQL

1. Save each Excel-derived table as CSV (or Parquet) using the column order above.  
2. In Spark:

```sql
CREATE TABLE microbial_phenotypes (
  strain         STRING,
  gene           STRING,
  condition      STRING,
  outcome        STRING,
  score          DOUBLE,
  assay_method   STRING,
  evidence_code  STRING,
  reference      STRING
)
USING PARQUET;
