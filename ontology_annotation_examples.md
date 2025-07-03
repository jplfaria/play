# Detailed Annotation Examples: Current vs Specialized Ontologies

## File 1: RBTnSeq-BW25113_sample.xlsx

### Example: Gene b0002 (thrB) shows fitness = -4.29 on D-Galacturonic Acid

#### Using Current Ontologies + ECO Only

```yaml
# Complex multi-part annotation required
Entity:
  Organism: NCBITaxon:511145 (Escherichia coli str. K-12 substr. BW25113)
  Gene: EcoGene:EG10999 (thrB)
  Gene_product: UniProt:P00547 (aspartokinase/homoserine dehydrogenase)
  
Phenotype_components:
  Process: GO:0006106 (fumarate metabolic process) # closest GO term
  Quality: PATO:0001997 (decreased rate)
  Severity: PATO:0000396 (severe intensity)
  
Environmental_context:
  Base_medium: ENVO:01000003 (culture medium) # generic term
  Carbon_source: CHEBI:16537 (D-galacturonic acid)
  Carbon_concentration: 0.2% w/v
  Temperature: 37°C (UO:0000027)
  Other_nutrients: "M9 salts minus carbon source" # free text
  
Experimental_condition:
  Assay: OBI:0002048 (genetic perturbation assay)
  Perturbation_type: "transposon insertion" # no specific term
  Selection_time: 6 generations
  
Evidence:
  Primary_evidence: ECO:0007032 (transposon mutagenesis phenotypic evidence)
  Measurement_type: ECO:0000362 (computational evidence from multiple sources)
  
Quantitative_data:
  Fitness_score: -4.29
  Statistical_test: ECO:0000033 (author statement based on evidence)
  P_value: < 0.001
  Barcode_reads: 18,234
  Replicates: 2
  Correlation: 0.92 (from exp-meta)
  
Relations_to_link_components:
  - has_participant: gene thrB
  - has_quality: decreased rate
  - occurs_in: culture medium with galacturonic acid
  - has_evidence: transposon mutagenesis
  
Database_statement: "thrB mutant has severely decreased growth rate in M9 + galacturonic acid"
# Note: Requires 6+ ontologies and custom assembly
```

#### Using Current + OMP + MCO + ECO

```yaml
# Single integrated annotation
Organism: NCBITaxon:511145 (Escherichia coli str. K-12 substr. BW25113)
Gene: EcoGene:EG10999 (thrB)

Phenotype: OMP:0007518 (inability to utilize D-galacturonic acid as sole carbon source)
Condition: MCO:0000256 (M9 minimal medium with D-galacturonic acid)

Evidence: 
  Type: ECO:0007032 (transposon mutagenesis phenotypic evidence)
  Details:
    fitness_score: -4.29
    p_value: < 0.001  
    threshold: "fitness < -2 indicates growth defect" (ECO:0000033)
    barcode_reads: 18,234
    replicates: 2
    quality_metrics:
      correlation: 0.92
      MAD_score: 0.645

# Complete annotation in 3 primary terms + structured evidence
```

---

## File 2: CarolGross_NIHMS261392_sample.xls (Nichols et al.)

### Example: Gene recA shows S-score = -3.8 with Mecillinam 0.06 μg/mL

#### Using Current Ontologies + ECO Only

```yaml
# Highly complex annotation
Entity:
  Organism: NCBITaxon:83333 (Escherichia coli K-12)
  Strain: "Keio collection derivative" # free text
  Gene: EcoGene:EG10823 (recA)
  Gene_function: GO:0006281 (DNA repair)
  
Phenotype_assembly:
  Biological_process: GO:0046677 (response to antibiotic)
  Quality: PATO:0000911 (increased sensitivity to chemicals)
  Chemical: CHEBI:50505 (mecillinam)
  Concentration: 0.06 μg/mL (UO:0000274)
  
  # No single term for "antibiotic sensitivity phenotype"
  Additional_qualities:
    - PATO:0001997 (decreased rate) # of growth
    - PATO:0001624 (decreased viability)
    
Environmental_setup:
  Medium: "LB broth" # no ontology term
  Temperature: 30°C (UO:0000027) # suboptimal temp
  Growth_phase: "exponential" # free text
  Incubation: 20 hours
  
Assay_details:
  Method: OBI:0000070 (assay)
  Specific_type: "colony size measurement" # no term
  Plate_format: "384-well plates"
  
Evidence:
  Primary: ECO:0001563 (colony size measurement evidence)
  Secondary: ECO:0007634 (chemical genetic interaction evidence)
  Analysis: ECO:0000053 (computational combinatorial evidence)
  
Measurements:
  S_score: -3.8 (normalized colony size)
  P_value: 0.0003
  FDR: 0.02
  Plate_normalization: "spatial correction applied"
  Biological_replicates: 3
  
Complex_relations:
  - has_phenotype: [process + quality + chemical]
  - measured_by: colony size assay
  - under_condition: LB + mecillinam
  - statistical_support: p < 0.001
  
# Requires complex OWL expression or 8+ statements
```

#### Using Current + OMP + MCO + ECO

```yaml
# Streamlined annotation
Strain: NCBITaxon:83333 (Escherichia coli K-12) 
Gene: EcoGene:EG10823 (recA)

Phenotype: OMP:0000289 (increased mecillinam sensitivity)
  # or more general: OMP:0006098 (increased beta-lactam antibiotic sensitivity)
  
Condition: MCO:0000512 (LB broth with mecillinam 0.06 μg/mL at 30°C)
  # MCO incorporates medium, drug, concentration, temperature

Evidence:
  Type: ECO:0001563 (colony size measurement evidence)
  Quantification:
    s_score: -3.8
    p_value: 0.0003
    fdr_adjusted: 0.02
  Methods:
    normalization: ECO:0000033 "spatial correction for plate effects"
    replicates: 3
    incubation: 20h
    
Cross_reference: ECO:0007634 (chemical genetic interaction)

# Clean 3-term annotation with full evidence trail
```

---

## File 3: ANL-SDL-48EcoliPhenos.xlsx

### Example: Isolate 562.61239 cannot grow on D-Galacturonic Acid (0) but can grow on Salicin (1)

#### Using Current Ontologies + ECO Only

```yaml
# Multiple separate annotations needed
Organism: NCBITaxon:562 (Escherichia coli)
Strain_ID: "562.61239" # internal identifier
Source: "Aaron's Lab environmental collection"

# Phenotype 1 - Galacturonic acid
Phenotype_1_components:
  Entity: "growth on galacturonic acid" # constructed concept
  Process: GO:0042840 (D-glucuronate catabolic process) # closest match
  Quality: PATO:0000462 (absent)
  Substrate: CHEBI:33830 (D-galacturonic acid)
  
Condition_1:
  Medium_type: "minimal medium" # free text
  Sole_carbon_source: CHEBI:33830
  Role: CHEBI:78616 (sole carbon source) # if exists
  
Evidence_1:
  Method: ECO:0005007 (reporter gene assay evidence) # if colorimetric
  # or ECO:0001091 (phenotype microarray evidence) if Biolog
  
  Binary_threshold: ECO:0000033 (author statement)
    Details: "Growth called if OD600 > 0.2 at 24h"
  Raw_data_location: "Sheet3, column D, row 2"
  Max_value_for_substrate: 0.683
  Min_value_for_substrate: 0.089
  This_isolate_value: 0.102
  
# Phenotype 2 - Salicin  
Phenotype_2_components:
  Entity: "growth on salicin"
  Process: GO:0046218 (salicin catabolic process) # if exists
  Quality: PATO:0000467 (present)
  Substrate: CHEBI:17814 (salicin)
  
Condition_2:
  Medium_type: "minimal medium"
  Sole_carbon_source: CHEBI:17814
  
Evidence_2:
  Method: ECO:0001091 (phenotype microarray evidence)
  Binary_threshold: ECO:0000033
    Details: "Same threshold as above"
  This_isolate_value: 0.487
  
# No integrated way to express carbon utilization profile
```

#### Using Current + OMP + MCO + ECO

```yaml
# Integrated strain profile
Organism: NCBITaxon:562 (Escherichia coli)
Strain: "562.61239" (BioSample pending)

Phenotypes:
  - OMP:0007519 (inability to utilize D-galacturonic acid as carbon source)
  - OMP:0005126 (ability to utilize salicin as carbon source)
  
Conditions:
  - MCO:0000331 (minimal medium with D-galacturonic acid as sole carbon source)
  - MCO:0000332 (minimal medium with salicin as sole carbon source)

Evidence:
  Type: ECO:0001091 (phenotype microarray evidence)
  Threshold_method: ECO:0000033 (author statement)
    Criteria: "OD600 > 0.2 at 24h = growth"
  Quality_control:
    Normalization: "max/min per substrate"
    Galacturonate_result: 0.102 (below 0.2)
    Salicin_result: 0.487 (above 0.2)
  Data_sheets: "Raw values in Sheet3-4"

# Complete metabolic profile in structured format
```

---

## File 4: MG1655_Phenotype_Microarray_Table.xlsx

### Example: MG1655 shows "Low Growth" on N-Acetyl-D-Glucosamine (PM1 Well A3)

#### Using Current Ontologies + ECO Only

```yaml
# Complex three-tier annotation
Organism: NCBITaxon:511145 (Escherichia coli str. K-12 substr. MG1655)
Reference_strain: true

Phenotype_components:
  Process: GO:0006044 (N-acetylglucosamine metabolic process)
  Quality: PATO:0002302 (decreased process quality)
  # No term for "low growth" specifically
  Qualifier: "intermediate between normal and absent"
  
Test_compound: CHEBI:506227 (N-acetyl-D-glucosamine)
Role: "sole carbon source in minimal medium"

Assay_context:
  Platform: "Biolog Phenotype MicroArray"
  Plate: "PM1"
  Well: "A3"
  Base_medium: "IF-0a" # Biolog proprietary, no ontology
  
Evidence:
  Primary: ECO:0001091 (phenotype microarray evidence)
  Specific: ECO:0005024 (growth inhibition assay evidence)
  
  Categorization: ECO:0000033 (author statement)
    No_growth: "OD590 < 0.1"
    Low_growth: "OD590 0.1-0.3"  # This result
    Growth: "OD590 > 0.3"
    
  Controls:
    Negative: "A1 well, no carbon"
    Positive: "glucose wells"
    
Measurements:
  Time_point: 48 hours
  Reading: "OD590 ~0.18" # estimated from category
  Replicate_info: "standard PM protocol"
  
# Difficult to express 3-tier growth levels
```

#### Using Current + OMP + MCO + ECO

```yaml
# Clear graduated phenotype
Organism: NCBITaxon:511145 (Escherichia coli str. K-12 substr. MG1655)
Type: "wild-type reference"

Phenotype: OMP:0005088 (decreased growth rate on N-acetylglucosamine)
  # OMP supports gradations beyond binary

Condition: MCO:0000623 (Biolog PM1-A3 condition)
  # or expanded: MCO:0000624 (IF-0a minimal medium with N-acetylglucosamine)
  
Evidence:
  Type: ECO:0001091 (phenotype microarray evidence)
  
  Category_definitions: ECO:0000033
    No_growth: "OD590 < 0.1 at 48h"
    Low_growth: "OD590 0.1-0.3 at 48h" 
    Growth: "OD590 > 0.3 at 48h"
    
  This_result:
    Category: "Low Growth"
    Inferred_range: "OD590 between 0.1-0.3"
    
  Quality_markers:
    Negative_control: "PM1-A1 confirmed no growth"
    Positive_controls: "standard sugars showed growth"
    
Biological_note: "Unexpected given functional nag operon"

# Graduated phenotypes cleanly captured
```

---

## Cross-Dataset Integration Example

### Query: "Find all sources showing galacturonate utilization defects"

#### Using Current Ontologies Only
```sql
-- Pseudo-query showing complexity
SELECT DISTINCT source, gene_or_strain FROM annotations WHERE
  (substrate = 'CHEBI:33830' OR text_match('galacturonic acid')) AND
  (quality IN ('PATO:0000462', 'PATO:0001997') OR 
   process_match('GO:0042840 decreased')) AND
  (evidence_type LIKE 'ECO:00%') AND
  (manually_curated_phenotype_class = 'no growth' OR 
   fitness_score < -2 OR
   binary_growth = 0 OR
   growth_category IN ('No Growth', 'Low Growth'))
   
-- Returns scattered results needing manual integration
```

#### Using OMP + MCO + ECO
```sparql
# Clean SPARQL query
SELECT ?source ?gene_or_strain ?evidence_type ?confidence WHERE {
  ?annotation omp:has_phenotype omp:0007519 . # galacturonate utilization defect
  ?annotation mco:has_condition ?condition .
  ?condition mco:involves_compound CHEBI:33830 .
  ?annotation eco:has_evidence ?evidence .
  ?evidence rdf:type ?evidence_type .
  ?evidence eco:confidence_score ?confidence .
}

# Returns:
# - RBTnSeq: thrB (ECO:0007032, fitness -4.29)
# - Isolates: 562.61239, 562.61143, 562.55535 (ECO:0001091, binary)
# - MG1655: Not found (can utilize galacturonate)
```

The specialized ontologies enable:
1. **Consistent phenotype representation** across different experimental types
2. **Unified queries** without complex joins
3. **Evidence tracking** for quality filtering
4. **Automatic grouping** of related phenotypes
