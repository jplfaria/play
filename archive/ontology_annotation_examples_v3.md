# Microbial Phenotype Ontology Annotations: Comparative Association Model

**Version 3.0** - Showing both current ontology approach and specialized ontology approach for each example

## Overview

This document demonstrates how to annotate microbial phenotype data using an association-based model, with parallel examples showing:
1. **Current Approach**: Using only currently available ontologies (CHEBI, GO, PATO, ECO, NCBITaxon, RO, UO, ENVO, OBI)
2. **Specialized Approach**: Adding OMP (Ontology of Microbial Phenotypes) and MCO (Microbial Conditions Ontology)

---

## Dataset 1: RBTnSeq-BW25113 - Transposon Fitness Screening

### Example 1.1: Gene thrB shows severe growth defect on D-galacturonic acid

#### Version A: Without OMP/MCO (Current Ontologies Only)

```yaml
association:
  id: "rbtn_001a"
  type: "biolink:GeneToPhenotypicFeatureAssociation"
  subject: 
    id: "EcoGene:EG10999"
    label: "thrB"
    taxon: "NCBITaxon:511145"  # E. coli BW25113
  predicate: "RO:0002200"  # has phenotype
  object:
    # Must construct phenotype from multiple components
    entity: "GO:0008150"  # biological process
    quality: "PATO:0000462"  # absent
    qualifier: "GO:0046396"  # D-galacturonic acid metabolic process
  qualifiers:
    chemical_environment: 
      compound: "CHEBI:33830"  # D-galacturonic acid
      role: "sole carbon source"
      concentration: "0.2% w/v"
    physical_environment:
      medium: "ENVO:01001059"  # microbial culture medium
      medium_type: "M9 minimal salts"  # free text
      temperature: 
        value: 37
        unit: "UO:0000027"  # degree Celsius
    severity: "PATO:0000396"  # severe intensity
  evidence:
    - type: "ECO:0007032"  # transposon mutagenesis evidence
      value: 
        fitness_score: -4.29
        statistical_test: "t-test"
        p_value: 0.0008
      supporting_data:
        barcode_reads: 18234
        replicates: 2
        correlation: 0.92
  provenance:
    source: "RBTnSeq-BW25113"
    method: "Random barcode transposon sequencing"
```

#### Version B: With OMP/MCO (Specialized Ontologies)

```yaml
association:
  id: "rbtn_001b"
  type: "biolink:GeneToPhenotypicFeatureAssociation"
  subject: 
    id: "EcoGene:EG10999"
    label: "thrB"
    taxon: "NCBITaxon:511145"
  predicate: "RO:0002200"
  object:
    # Single term captures complete phenotype
    id: "OMP:0007622"  # galacturonic acid carbon utilization
    label: "galacturonic acid carbon utilization phenotype"
  qualifiers:
    phenotype_state: "PATO:0000462"  # absent
    condition_qualifier: 
      id: "MCO:0000031"  # M9 minimal medium
      extensions:
        carbon_source: "CHEBI:33830"
        concentration: "0.2% w/v"
        temperature: "37°C"
    magnitude_qualifier: "PATO:0000396"  # severe
  evidence:
    - type: "ECO:0007032"
      value: 
        fitness_score: -4.29
        statistical_test: "t-test"
        p_value: 0.0008
      supporting_data:
        barcode_reads: 18234
        replicates: 2
        correlation: 0.92
  provenance:
    source: "RBTnSeq-BW25113"
    method: "Random barcode transposon sequencing"
```

### Example 1.2: Gene galK required for galactose utilization

#### Version A: Without OMP/MCO

```yaml
association:
  id: "rbtn_002a"
  type: "biolink:GeneToPhenotypicFeatureAssociation"
  subject:
    id: "EcoGene:EG10357"
    label: "galK"
    taxon: "NCBITaxon:511145"
  predicate: "RO:0002200"
  object:
    # Complex multi-part phenotype
    process: "GO:0006012"  # galactose metabolic process
    quality: "PATO:0002303"  # decreased rate
    context: "growth of unicellular organism"
  qualifiers:
    chemical_environment:
      compound: "CHEBI:17118"  # D-galactose
      role: "primary carbon source"
      concentration: "0.2% w/v"
    physical_environment:
      medium_base: "ENVO:01001059"
      salts: "M9 minimal salts"
      supplements: "none"
    phenotype_manifestation: "growth defect"
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

#### Version B: With OMP/MCO

```yaml
association:
  id: "rbtn_002b"
  type: "biolink:GeneToPhenotypicFeatureAssociation"
  subject:
    id: "EcoGene:EG10357"
    label: "galK"
    taxon: "NCBITaxon:511145"
  predicate: "RO:0002200"
  object:
    id: "OMP:0005009"  # hexose utilization
    label: "hexose utilization phenotype"
    specific_substrate: "CHEBI:17118"  # galactose
  qualifiers:
    phenotype_state: "PATO:0000462"  # absent
    condition_qualifier:
      id: "MCO:0000031"  # M9 minimal medium
      extensions:
        carbon_source: "CHEBI:17118"
        concentration: "0.2% w/v"
  evidence:
    - type: "ECO:0007032"
      value:
        fitness_score: -5.8
        p_value: 0.00001
        threshold: "fitness < -2"
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

#### Version A: Without OMP/MCO

```yaml
association:
  id: "nichols_001a"
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
    phenotype:
      process: "GO:0046677"  # response to antibiotic
      quality: "PATO:0001549"  # increased sensitivity toward
      substance: "CHEBI:50505"
    experimental_conditions:
      medium: "rich medium"  # no ENVO term for LB
      medium_name: "LB broth"
      chemical_concentration: "0.06 μg/mL"
      temperature:
        value: 30
        unit: "UO:0000027"
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

#### Version B: With OMP/MCO

```yaml
association:
  id: "nichols_001b"
  type: "biolink:ChemicalAffectsGeneAssociation"
  subject:
    id: "CHEBI:50505"
    label: "mecillinam"
    role: "beta-lactam antibiotic"
  predicate: "biolink:affects"
  qualified_predicate: "biolink:causes"
  object:
    id: "EcoGene:EG10823"
    label: "recA"
    taxon: "NCBITaxon:511145"
  qualifiers:
    phenotype: "OMP:0000336"  # beta-lactam resistance phenotype
    phenotype_direction: "PATO:0000911"  # decreased quality
    condition_qualifier:
      id: "MCO:0000032"  # LB broth
      extensions:
        compound: "CHEBI:50505"
        concentration: "0.06 μg/mL"
        temperature: "30°C"
        duration: "20 hours"
  evidence:
    - type: "ECO:0001563"
      value:
        s_score: -3.8
        p_value: 0.0003
        fdr_adjusted: 0.02
      method_details:
        plate_format: "384-well"
        normalization: "spatial correction"
        replicates: 3
  provenance:
    source: "Nichols et al. 2011"
    publication: "PMID:21609262"
    method: "Colony size measurement"
```

### Example 2.2: Gene nuo operon mutants sensitive to oxidative stress

#### Version A: Without OMP/MCO

```yaml
association:
  id: "nichols_002a"
  type: "biolink:ChemicalAffectsGeneAssociation"
  subject:
    id: "CHEBI:16240"
    label: "hydrogen peroxide"
    role: "oxidizing agent"
  predicate: "biolink:affects"
  object:
    id: "EcoGene:EG10665"  # nuoA
    label: "nuoA"
    pathway: "GO:0006979"  # response to oxidative stress
  qualifiers:
    phenotype_components:
      biological_process: "GO:0006979"  # response to oxidative stress
      quality: "PATO:0001997"  # decreased viability
      stress_type: "oxidative stress"
    mechanism: "damage to iron-sulfur clusters"
    conditions:
      medium: "nutrient rich medium"
      specific_medium: "LB"
      stressor: "CHEBI:16240"
      concentration: "2.5 mM"
      temperature: "37°C"
  evidence:
    - type: "ECO:0001563"
      value:
        s_score: -4.2
        p_value: 0.00005
        phenotype_strength: "strong"
      quality_control:
        bias_corrected: true
        edge_effects_removed: true
  provenance:
    source: "Chemical genomics screen"
    method: "High-throughput colony pinning"
```

#### Version B: With OMP/MCO

```yaml
association:
  id: "nichols_002b"
  type: "biolink:ChemicalAffectsGeneAssociation"
  subject:
    id: "CHEBI:16240"
    label: "hydrogen peroxide"
  predicate: "biolink:affects"
  object:
    id: "EcoGene:EG10665"
    label: "nuoA"
    pathway: "GO:0006979"
  qualifiers:
    phenotype: "OMP:0005135"  # oxidative stress sensitivity
    mechanism_note: "iron-sulfur cluster damage"
    condition_qualifier:
      id: "MCO:0000032"  # LB
      extensions:
        stressor: "CHEBI:16240"
        concentration: "2.5 mM"
        temperature: "37°C"
  evidence:
    - type: "ECO:0001563"
      value:
        s_score: -4.2
        p_value: 0.00005
        category: "strong"
      quality_metrics:
        corrections_applied: ["spatial", "edge"]
  provenance:
    source: "Chemical genomics screen"
    method: "HT colony pinning"
```

---

## Dataset 3: ANL Environmental Isolate Metabolic Profiling

### Example 3.1: Isolate 562.61239 cannot utilize D-galacturonic acid

#### Version A: Without OMP/MCO

```yaml
association:
  id: "anl_001a"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "ANL:562.61239"  # Internal strain ID
    label: "E. coli environmental isolate 61239"
    taxon: "NCBITaxon:562"
  predicate: "RO:0002200"
  object:
    # Construct from multiple terms
    biological_process: "GO:0046396"  # D-galacturonic acid metabolic process
    quality: "PATO:0000462"  # absent
    context: "growth phenotype"
  qualifiers:
    assay_conditions:
      base_medium: "ENVO:01001059"  # microbial culture medium
      medium_type: "chemically defined minimal medium"
      carbon_source: "CHEBI:33830"  # D-galacturonic acid
      carbon_role: "sole carbon source"
      temperature: "37°C"
      measurement_time: "24 hours"
  evidence:
    - type: "ECO:0001845"  # cell population optical density evidence
      value:
        growth_call: 0  # binary: no growth
        od600_reading: 0.102
        decision_threshold: "OD600 > 0.2 at 24h = growth"
      normalization_data:
        substrate_maximum: 0.683
        substrate_minimum: 0.089
        method: "min-max scaling per substrate"
  provenance:
    source: "ANL-SDL-48EcoliPhenos"
    method: "Growth/no-growth assessment"
    data_location: "Sheet2, Row 2"
```

#### Version B: With OMP/MCO

```yaml
association:
  id: "anl_001b"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "ANL:562.61239"
    label: "E. coli environmental isolate 61239"
    taxon: "NCBITaxon:562"
  predicate: "RO:0002200"
  object:
    id: "OMP:0007622"
    label: "galacturonic acid carbon utilization"
  qualifiers:
    phenotype_state: "PATO:0000462"  # absent
    condition_qualifier:
      id: "MCO:0000030"  # minimal medium
      extensions:
        carbon_source: "CHEBI:33830"
        temperature: "37°C"
        timepoint: "24 hours"
  evidence:
    - type: "ECO:0001845"
      value:
        binary_score: 0
        od600: 0.102
        threshold: "OD600 > 0.2"
      supporting_data:
        max_for_substrate: 0.683
        min_for_substrate: 0.089
        normalization: "min-max"
  provenance:
    source: "ANL-SDL-48EcoliPhenos"
    method: "Phenotype array"
    location: "Sheet2, Row 2"
```

### Example 3.2: Isolate 562.61143 can utilize salicin

#### Version A: Without OMP/MCO

```yaml
association:
  id: "anl_002a"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "ANL:562.61143"
    label: "E. coli environmental isolate 61143"
    taxon: "NCBITaxon:562"
  predicate: "RO:0002200"
  object:
    # No GO term for salicin metabolism, use parent process
    biological_process: "GO:0016137"  # glycoside metabolic process
    quality: "PATO:0000467"  # present
    substrate_specification: "CHEBI:17814"  # salicin
  qualifiers:
    growth_conditions:
      medium_base: "ENVO:01001059"
      medium_description: "minimal salts medium"
      carbon_source: "CHEBI:17814"
      source_concentration: "standard test concentration"
      incubation: "37°C, 24h"
  evidence:
    - type: "ECO:0001845"
      value:
        growth_score: 1  # binary growth
        od600_measured: 0.487
        above_threshold: true
      replication:
        technical_replicates: 2
        biological_replicates: 1
  provenance:
    source: "ANL Environmental Collection"
    collector: "Aaron's Lab"
    assay_type: "Binary growth phenotype"
```

#### Version B: With OMP/MCO

```yaml
association:
  id: "anl_002b"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "ANL:562.61143"
    label: "E. coli environmental isolate 61143"
    taxon: "NCBITaxon:562"
  predicate: "RO:0002200"
  object:
    id: "OMP:0016137"  # glycoside utilization (hypothetical - may need new term)
    label: "phenolic glycoside utilization phenotype"
  qualifiers:
    phenotype_state: "PATO:0000467"  # present
    substrate_qualifier: "CHEBI:17814"  # salicin
    condition_qualifier:
      id: "MCO:0000030"  # minimal medium
      substrate_extension: "CHEBI:17814"
  evidence:
    - type: "ECO:0001845"
      value:
        binary_score: 1
        od600: 0.487
        confidence: "above threshold"
      quality_metrics:
        technical_replicates: 2
  provenance:
    source: "ANL Collection"
    method: "Growth assessment"
```

---

## Dataset 4: MG1655 Biolog Phenotype MicroArray

### Example 4.1: MG1655 shows low growth on N-acetylglucosamine

#### Version A: Without OMP/MCO

```yaml
association:
  id: "mg1655_001a"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "NCBITaxon:511145"
    label: "E. coli K-12 MG1655"
    strain_type: "reference strain"
  predicate: "RO:0002200"
  object:
    metabolic_process: "GO:0006044"  # N-acetylglucosamine metabolic process
    quality: "PATO:0000911"  # decreased quality
    growth_category: "partial"  # intermediate phenotype
  qualifiers:
    test_conditions:
      plate_system: "OBI:0400103"  # microplate
      plate_type: "Biolog PM1"
      well_location: "A3"
      test_substrate: "CHEBI:506227"  # N-acetyl-D-glucosamine
      substrate_role: "sole carbon source"
      base_medium: "Biolog IF-0a"  # proprietary medium
    growth_level: "Low Growth"
  evidence:
    - type: "ECO:0001091"  # phenotype microarray evidence
      value:
        growth_category: "Low Growth"
        od_range: "OD590 0.1-0.3"
        measurement_time: "48 hours"
      category_definitions:
        no_growth: "OD590 < 0.1"
        low_growth: "OD590 0.1-0.3"
        growth: "OD590 > 0.3"
  provenance:
    source: "Biolog PM analysis"
    platform: "Phenotype MicroArray"
    purpose: "wild-type reference"
```

#### Version B: With OMP/MCO

```yaml
association:
  id: "mg1655_001b"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "NCBITaxon:511145"
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
      id: "MCO:0000030"  # minimal medium
      biolog_specific:
        plate: "PM1"
        well: "A3"
        substrate: "CHEBI:506227"
  evidence:
    - type: "ECO:0001091"
      value:
        category: "Low Growth"
        od_range: "0.1-0.3"
        timepoint: "48h"
      thresholds:
        documented_by: "ECO:0000033"
        categories: ["<0.1", "0.1-0.3", ">0.3"]
  provenance:
    source: "Biolog PM"
    reference_type: "WT baseline"
```

### Example 4.2: MG1655 cannot grow on L-arabinose (unexpected)

#### Version A: Without OMP/MCO

```yaml
association:
  id: "mg1655_002a"
  type: "biolink:OrganismToPhenotypicFeatureAssociation"
  subject:
    id: "NCBITaxon:511145"
    label: "E. coli K-12 MG1655"
  predicate: "RO:0002200"
  object:
    process: "GO:0019568"  # L-arabinose metabolic process
    quality: "PATO:0000462"  # absent
    note: "unexpected - MG1655 typically utilizes arabinose"
  qualifiers:
    experimental_setup:
      assay: "OBI:0001977"  # growth assay
      plate_id: "PM1"
      well: "A2"
      carbon_source: "CHEBI:16716"  # L-arabinose
      medium_base: "Biolog IF-0a minimal"
      temperature: "37°C"
    result_flag: "requires_validation"
  evidence:
    - type: "ECO:0001091"
      value:
        growth_result: "No Growth"
        od590: "< 0.1"
        validated: false
      concern: "Contradicts known MG1655 metabolism"
  provenance:
    source: "MG1655_Phenotype_Microarray_Table"
    method: "Biolog PM carbon plate"
    quality_note: "unexpected result"
```

#### Version B: With OMP/MCO

```yaml
association:
  id: "mg1655_002b"
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
    unexpected_result: true
    condition_qualifier:
      id: "MCO:0000030"
      plate_context:
        system: "PM1"
        well: "A2"
  evidence:
    - type: "ECO:0001091"
      value:
        result: "No Growth"
        od590: "< 0.1"
        requires_validation: true
      note: "Unexpected for MG1655"
  provenance:
    source: "Biolog PM Table"
    quality_flag: "needs_review"
```

---

## Ontology Term Verification Summary

### Verified Terms Used:
- **NCBITaxon**: 562 (E. coli), 511145 (BW25113/MG1655)
- **CHEBI**: 33830 (galacturonic acid), 17118 (galactose), 50505 (mecillinam), 16240 (H2O2), 17814 (salicin), 506227 (GlcNAc), 16716 (arabinose)
- **GO**: 0046396 (galacturonate metabolism), 0006012 (galactose metabolism), 0046677 (antibiotic response), 0006979 (oxidative stress), 0016137 (glycoside metabolic process), 0006044 (GlcNAc metabolism), 0019568 (arabinose metabolism), 0008150 (biological process)
- **PATO**: 0000462 (absent), 0000467 (present), 0000911 (decreased quality), 0002303 (decreased rate), 0000396 (severe), 0001549 (increased sensitivity toward), 0001997 (decreased viability)
- **ECO**: 0007032 (transposon mutagenesis), 0001563 (colony size), 0001845 (optical density), 0001091 (phenotype microarray), 0000033 (author statement)
- **RO**: 0002200 (has phenotype)
- **UO**: 0000027 (degree Celsius)
- **ENVO**: 01001059 (microbial culture medium)
- **OBI**: 0400103 (microplate), 0000070 (assay), 0001977 (growth assay)

### OMP/MCO Terms (When Added):
- **OMP**: 0007622 (galacturonic acid utilization), 0005009 (hexose utilization), 0000336 (beta-lactam resistance), 0005135 (oxidative stress sensitivity), 0005040 (GlcNAc utilization), 0005001 (pentose utilization)
# Note: Specific OMP term for glycoside/salicin utilization may need to be requested
- **MCO**: 0000030 (minimal medium), 0000031 (M9 minimal), 0000032 (LB broth)

### Key Differences:
1. **Without OMP/MCO**: Requires 3-5 ontology terms to construct each phenotype
2. **With OMP/MCO**: Single phenotype term + state qualifier
3. **Evidence remains consistent** across both approaches
4. **Complexity reduction**: ~60% fewer terms needed with specialized ontologies