# Microbial Phenotype Ontology Annotations: Association-Based Model

**Version 2.0** - Using Biolink-inspired association structure for improved clarity and implementation

## Overview

This document provides standardized examples for annotating microbial phenotype data using an association-based model. Each phenotype is represented as a structured association between a biological entity (gene/strain) and a phenotype, with qualifiers providing context and evidence supporting the assertion.

## Core Association Structure

```yaml
association:
  id: <unique_identifier>
  type: <association_type>
  subject: <gene_or_strain>
  predicate: <relationship>
  object: <phenotype>
  qualifiers:
    condition_qualifier: <experimental_condition>
    magnitude_qualifier: <severity_or_degree>
    direction_qualifier: <increased/decreased>
  evidence:
    type: <evidence_code>
    value: <measurement>
    has_confidence_level: <statistical_significance>
  provenance:
    source: <dataset>
    method: <experimental_approach>
```

---

## Dataset 1: RBTnSeq-BW25113 - Transposon Fitness Screening

### Example 1.1: Gene thrB shows severe growth defect on D-galacturonic acid

```yaml
association:
  id: "rbtn_001"
  type: "biolink:GeneToPhenotypicFeatureAssociation"
  subject: 
    id: "EcoGene:EG10999"
    label: "thrB"
    taxon: "NCBITaxon:511145"  # E. coli BW25113
  predicate: "RO:0002200"  # has phenotype
  object:
    id: "OMP:0007622"  # galacturonic acid carbon utilization
    label: "galacturonic acid carbon utilization phenotype"
  qualifiers:
    phenotype_state: "PATO:0000462"  # absent
    condition_qualifier: 
      medium: "MCO:0000031"  # M9 minimal medium
      carbon_source: "CHEBI:33830"  # D-galacturonic acid
      concentration: "0.2% w/v"
      temperature: "37°C"
    magnitude_qualifier: "PATO:0000396"  # severe intensity
  evidence:
    - type: "ECO:0007032"  # transposon mutagenesis evidence
      value: 
        fitness_score: -4.29
        statistical_test: "t-test"
        p_value: 0.0008
        confidence_level: "high"
      supporting_data:
        barcode_reads: 18234
        replicates: 2
        correlation: 0.92
  provenance:
    source: "RBTnSeq-BW25113"
    publication: "PMID:example"
    method: "Random barcode transposon sequencing"
```

### Example 1.2: Gene galK required for galactose utilization

```yaml
association:
  id: "rbtn_002"
  type: "biolink:GeneToPhenotypicFeatureAssociation"
  subject:
    id: "EcoGene:EG10357"
    label: "galK"
    taxon: "NCBITaxon:511145"
  predicate: "RO:0002200"
  object:
    id: "OMP:0005009"  # hexose utilization
    label: "hexose utilization phenotype"
  qualifiers:
    phenotype_state: "PATO:0000462"  # absent
    condition_qualifier:
      medium: "MCO:0000031"  # M9 minimal medium
      carbon_source: "CHEBI:17118"  # D-galactose
      concentration: "0.2% w/v"
    direction_qualifier: "PATO:0002303"  # decreased
  evidence:
    - type: "ECO:0007032"
      value:
        fitness_score: -5.8
        p_value: 0.00001
        threshold: "fitness < -2 indicates growth defect"
      quality_metrics:
        mad_score: 0.234
        fdr: 0.001
  provenance:
    source: "RBTnSeq-BW25113"
    method: "Tn-seq competitive fitness assay"
```

---

## Dataset 2: Nichols et al. Chemical Genomics Screen

### Example 2.1: Gene recA shows increased sensitivity to mecillinam

```yaml
association:
  id: "nichols_001"
  type: "biolink:ChemicalAffectsGeneAssociation"
  subject:
    id: "CHEBI:50505"
    label: "mecillinam"
    role: "antimicrobial agent"
  predicate: "biolink:affects"
  qualified_predicate: "biolink:causes"
  object:
    id: "EcoGene:EG10823"
    label: "recA"
    taxon: "NCBITaxon:511145"
  qualifiers:
    object_aspect: "growth"
    object_direction_qualifier: "decreased"
    anatomical_context: "cell wall"  # mecillinam target
    condition_qualifier:
      medium: "MCO:0000032"  # LB broth
      concentration: "0.06 μg/mL"
      temperature: "30°C"
      duration: "20 hours"
  evidence:
    - type: "ECO:0001563"  # colony size measurement evidence
      value:
        s_score: -3.8  # normalized colony size
        p_value: 0.0003
        fdr_adjusted: 0.02
      method_details:
        plate_format: "384-well"
        normalization: "spatial correction applied"
        replicates: 3
  provenance:
    source: "Nichols et al. 2011"
    publication: "PMID:21609262"
    method: "Colony size measurement on agar plates"
```

### Example 2.2: Gene nuo operon mutants sensitive to oxidative stress

```yaml
association:
  id: "nichols_002"
  type: "biolink:ChemicalAffectsGeneAssociation"
  subject:
    id: "CHEBI:16240"
    label: "hydrogen peroxide"
    role: "oxidizing agent"
  predicate: "biolink:affects"
  object:
    id: "EcoGene:EG10665"  # nuoA as representative
    label: "nuoA"
    pathway: "GO:0006979"  # response to oxidative stress
  qualifiers:
    mechanism_qualifier: "oxidative damage to iron-sulfur clusters"
    phenotype: "OMP:0005135"  # oxidative stress sensitivity
    condition_qualifier:
      medium: "MCO:0000032"  # LB
      concentration: "2.5 mM H2O2"
      temperature: "37°C"
  evidence:
    - type: "ECO:0001563"
      value:
        s_score: -4.2
        p_value: 0.00005
        phenotype_category: "strong"
      quality_control:
        systematic_bias_corrected: true
        edge_effect_corrected: true
  provenance:
    source: "Chemical genomics screen"
    method: "High-throughput colony pinning"
```

---

## Dataset 3: ANL Environmental Isolate Metabolic Profiling

### Example 3.1: Isolate 562.61239 cannot utilize D-galacturonic acid

```yaml
association:
  id: "anl_001"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "ANL:562.61239"  # Internal strain ID
    label: "E. coli environmental isolate 61239"
    taxon: "NCBITaxon:562"
  predicate: "RO:0002200"
  object:
    id: "OMP:0007622"
    label: "galacturonic acid carbon utilization"
  qualifiers:
    phenotype_state: "PATO:0000462"  # absent
    condition_qualifier:
      medium: "minimal medium"  # Could be MCO term
      sole_carbon_source: "CHEBI:33830"
      temperature: "37°C"
      timepoint: "24 hours"
  evidence:
    - type: "ECO:0001845"  # cell population optical density evidence
      value:
        binary_score: 0  # no growth
        od600: 0.102
        threshold: "OD600 > 0.2 at 24h = growth"
      supporting_data:
        max_value_substrate: 0.683
        min_value_substrate: 0.089
        normalization: "min-max per substrate"
  provenance:
    source: "ANL-SDL-48EcoliPhenos"
    method: "Phenotype microarray"
    data_sheet: "Sheet2, Row 2"
```

### Example 3.2: Isolate 562.61143 can utilize salicin

```yaml
association:
  id: "anl_002"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "ANL:562.61143"
    label: "E. coli environmental isolate 61143"
    taxon: "NCBITaxon:562"
  predicate: "RO:0002200"
  object:
    id: "OMP:0019691"  # phenolic glycoside utilization
    label: "phenolic glycoside utilization phenotype"
  qualifiers:
    phenotype_state: "PATO:0000467"  # present
    substrate_qualifier: "CHEBI:17814"  # salicin
    condition_qualifier:
      medium: "minimal medium"
      sole_carbon_source: "CHEBI:17814"
  evidence:
    - type: "ECO:0001845"
      value:
        binary_score: 1  # growth observed
        od600: 0.487
        confidence: "above threshold"
      quality_metrics:
        technical_replicates: 2
        biological_replicates: 1
  provenance:
    source: "ANL Environmental Collection"
    collector: "Aaron's Lab"
    method: "Binary growth assessment"
```

---

## Dataset 4: MG1655 Biolog Phenotype MicroArray

### Example 4.1: MG1655 shows low growth on N-acetylglucosamine

```yaml
association:
  id: "mg1655_001"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "NCBITaxon:511145"  # Could use more specific ID
    label: "E. coli K-12 MG1655"
    reference_strain: true
  predicate: "RO:0002200"
  object:
    id: "OMP:0005040"
    label: "N-acetylglucosamine utilization"
  qualifiers:
    phenotype_state: "PATO:0000911"  # decreased quality
    growth_category: "low growth"
    condition_qualifier:
      plate: "PM1"
      well: "A3"
      substrate: "CHEBI:506227"  # N-acetyl-D-glucosamine
      medium: "MCO:0000030"  # minimal medium (Biolog IF-0a)
  evidence:
    - type: "ECO:0001091"  # phenotype microarray evidence
      value:
        growth_level: "Low Growth"
        categorical_range: "OD590 0.1-0.3"
        timepoint: "48 hours"
      threshold_definitions:
        no_growth: "OD590 < 0.1"
        low_growth: "OD590 0.1-0.3"
        growth: "OD590 > 0.3"
  provenance:
    source: "Biolog PM analysis"
    platform: "Phenotype MicroArray"
    reference_type: "wild-type baseline"
```

### Example 4.2: MG1655 cannot grow on L-arabinose (unexpected result)

```yaml
association:
  id: "mg1655_002"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "NCBITaxon:511145"
    label: "E. coli K-12 MG1655"
  predicate: "RO:0002200"
  object:
    id: "OMP:0005001"  # pentose utilization
    label: "pentose utilization phenotype"
  qualifiers:
    phenotype_state: "PATO:0000462"  # absent
    substrate_qualifier: "CHEBI:16716"  # L-arabinose
    unexpected_result: true  # MG1655 typically can use arabinose
    condition_qualifier:
      plate: "PM1"
      well: "A2"
      substrate_role: "sole carbon source"
  evidence:
    - type: "ECO:0001091"
      value:
        growth_level: "No Growth"
        od590: "< 0.1"
        validated: false  # May need verification
      note: "Unexpected for MG1655 - possible regulatory issue"
  provenance:
    source: "MG1655_Phenotype_Microarray_Table"
    method: "Biolog PM carbon source plate"
    quality_flag: "requires_validation"
```

---

## Implementation Notes

### Using Current Ontologies (Without OMP/MCO)

When OMP and MCO are not available, associations become more complex:

```yaml
# Example without specialized ontologies
association:
  type: "biolink:GeneToPhenotypicFeatureAssociation"
  subject: "EcoGene:EG10999"  # thrB
  predicate: "RO:0002200"
  object:
    process: "GO:0046396"  # galacturonate metabolism
    quality: "PATO:0000462"  # absent
    entity: "growth of organism"
  qualifiers:
    chemical_environment: "CHEBI:33830"  # galacturonic acid
    physical_environment: "ENVO:01001059"  # culture medium
  # Requires multiple ontology terms to express single phenotype
```

### Benefits of Specialized Ontologies

With OMP and MCO, associations are cleaner:
- Single phenotype term (OMP) captures complete biological meaning
- Single condition term (MCO) standardizes experimental context
- Reduces complexity from ~6 ontologies to 3 (OMP + MCO + ECO)
- Enables direct cross-dataset queries

### Evidence Code Selection

- **ECO:0007032**: Transposon mutagenesis (RBTnSeq data)
- **ECO:0001563**: Colony size measurement (Nichols screen)
- **ECO:0001845**: Optical density measurement (ANL isolates, when growth curves measured)
- **ECO:0001091**: Phenotype microarray evidence (Biolog PM data)
- **ECO:0000033**: Author statement (for threshold documentation)

### Database Schema Considerations

This structure maps directly to relational tables:
- `associations` table: core triple + type
- `qualifiers` table: linked to association_id
- `evidence` table: measurements and confidence
- `provenance` table: source tracking

Or to graph database nodes:
- Gene/Strain nodes linked to Phenotype nodes
- Qualifier properties on edges
- Evidence as separate linked nodes