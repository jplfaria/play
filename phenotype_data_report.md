**Ontology Analysis of Microbial Phenotype Datasets – Mid-Level Report**
=======================================================================

---

**File: RBTnSeq-BW25113_sample.xlsx**
-------------------------------------

### **Data Structure Summary**
- **Sheets:**  
  - *BW25113* – gene × condition fitness matrix.  
  - *exp-meta* – condition identifiers, media, QC metrics.  
  - *Sheet3* – raw barcode counts per locus.  
- **Key columns:** `locusId`, `sysName`, `desc`, followed by 20-plus condition IDs such as `set1IT003 (D-Glucose C)` or `LB`.  
- **Values:** Log₂ fitness scores (negatives = growth defect, ~0 = neutral).  

### **Microbial Data Analysis**
- Detects genes essential for growth on ~15 different carbon sources plus LB.  
- Major phenotype clusters: glycolysis, galacturonate pathway, amino-acid biosynthesis.  
- Single strain (*E. coli* BW25113); high replicate correlation.

### **Current Ontology Assessment**
- **Best fit:** PATO (generic “decreased/abolished growth”) → ~50 % coverage.  
- Must pair with **CHEBI** (substrates), **ENVO** (media), **OBI** (assay), **NCBITaxon**, **RO**.  
- Composite annotations become complex and error-prone.

### **Specialized Ontology Comparison**
- **OMP:** Pre-coordinated “no growth on D-galacturonate”, etc.; covers > 90 %.  
- **MCO:** Ready terms for “M9 + 0.2 % glucose”, “LB broth”; fills medium-level gaps.  
- **Recommendation:** Add both (confidence 10/10 & 9/10).

### **Implementation Highlights**
- Convert numeric fitness < –4 to “abolished growth” OMP term; –4‥–2 to “decreased growth”.  
- Map each exp-meta condition string to an MCO ID or create new one.

---

**File: CarolGross_NIHMS261392_sample.xls**
-------------------------------------------

### **Data Structure Summary**
- 3 975 Keio knockouts × 324 chemical/physical stresses; separate *Condition* sheet (name, supplier, target, concentration).  
- Phenotype cells store colony-size Z-scores; FDR used to flag significance.

### **Microbial Data Analysis**
- Captures antibiotic hypersensitivity (β-lactams, fluoroquinolones), oxidative, osmotic, temperature stress, > 50 auxotrophies.  
- Multi-stress genes (e.g., chaperones, membrane biogenesis) evident via phenotype clustering.

### **Current Ontology Assessment**
- **Best:** PATO (~45 %) for “decreased viability/growth”.  
- Needs CHEBI for ~270 compounds, ENVO/OBI for 30 physical stresses, RO for relations.  
- Manual template assembly is heavy; grouping across screens inconsistent.

### **Specialized Ontology Comparison**
- **OMP:** Terms for antibiotic susceptibility, heat shock sensitivity, amino-acid auxotrophy already exist; minor additions needed.  
- **MCO:** Has/extends terms for “LB + 1.5 M NaCl”, “M9 pH 5 + H₂O₂”.  
- **Recommendation:** Adopt both; unify with ECO evidence codes.

### **Implementation Highlights**
- Auto-generate OMP annotations where Z < –3 (growth defect).  
- Map each *Condition* row to MCO; store compound conc. in annotation extension.

---

**File: ANL-SDL-48EcoliPhenos.xlsx**
------------------------------------

### **Data Structure Summary**
- Sheet2: 48 isolate IDs (e.g., 562.61239) × 29 carbon substrates; binary 1 = growth, 0 = none.  
- Sheets3/4 hold raw OD readings and min/max cut-off values.

### **Microbial Data Analysis**
- Substrates grouped into β-glucosides, raffinose/stachyose family, polyols, uronic acids, organic acids.  
- Broad variation: most isolates grow on glucose; few on pectin or galacturonate.  
- Binary calls simplify borderline growth but enable quick clustering.

### **Current Ontology Assessment**
- **Best:** PATO for presence/absence; CHEBI for substrates.  
- No discrete “raffinose utilization absent” term → 29 custom combos required.

### **Specialized Ontology Comparison**
- **OMP:** Has pattern “unable to utilize [CHEBI] carbon source”; supports hierarchy queries.  
- **MCO:** Standardizes “M9 + salicin” condition across datasets.  
- **Recommendation:** Add both (OMP 10/10, MCO 9/10).

### **Implementation Highlights**
- Record both positive (ability) and negative phenotypes for full isolate fingerprints.  
- Link isolate Genome IDs to NCBITaxon strain instances.

---

**File: MG1655_Phenotype_Microarray_Table.xlsx**
------------------------------------------------

### **Data Structure Summary**
- Sheet2 lists Biolog PM wells: Plate, Well, Compound, “Carbon Source Yes/No”, Growth Status (No, Low, Growth).  
- 336 wells: carbon, nitrogen, phosphorus, sulfur source panels.

### **Microbial Data Analysis**
- Wild-type MG1655: Growth on succinate, citrate; no growth (surprisingly) on L-arabinose; low growth on GlcNAc.  
- Negative controls verify assay quality.

### **Current Ontology Assessment**
- **Best:** PATO (~60 %) captures No/Low/Growth.  
- Needs CHEBI for every compound; ENVO or MCO for well context.

### **Specialized Ontology Comparison**
- **OMP:** Handles “decreased growth on N-acetyl-D-glucosamine”; allows gradation.  
- **MCO:** Clear Biolog PM well condition IDs; reusable across strains.  
- **Recommendation:** Add both; keep Low-growth as “decreased growth” OMP term.

### **Implementation Highlights**
- Store annotations: MG1655 – OMP term – MCO condition – ECO:0001099 (Biolog PM assay).

---

**Cross-Dataset Synthesis**
---------------------------

| Aspect                         | General Ontologies Only | With OMP + MCO |
|--------------------------------|-------------------------|----------------|
| Phenotype classes              | ~30–40 % complete       | > 90 % complete |
| Condition vocabulary           | Free-text / CHEBI only  | Structured, reusable |
| Curation workload              | High, ad-hoc            | Moderate, template-driven |
| Query / integration power      | Fragmented joins        | Unified term look-ups |

### **Unified Annotation Strategy**
1. **OMP** for all phenotype assertions (genes, strains, wild-type).  
2. **MCO** (+ CHEBI/ENVO) for every experimental condition.  
3. Use **NCBITaxon** for organism IDs and **ECO** for evidence links.

### **Cost–Benefit**
- *Cost:* Initial term mapping & curator training.  
- *Benefit:* Interoperable, scalable database; powerful cross-study queries.

### **Final Recommendation**
Adopt **OMP** for microbial phenotypes **and** **MCO** for growth conditions across all four datasets.  
*Confidence: 10/10.*
