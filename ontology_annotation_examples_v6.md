# Microbial Phenotype Ontology Annotations: Comparative Association Model

**Version 6.0**

## Overview

This document demonstrates how to annotate microbial phenotype data using an association-based model, comparing two approaches:
1. **Version A**: Using only currently available ontologies (CHEBI, GO, PATO, ECO, NCBITaxon, RO, UO, OBI)
2. **Version C**: Using OMP (Ontology of Microbial Phenotypes) with standard ontologies (hybrid approach)

**Key Changes in v6:**
- Removed Version B (MCO-based) to reduce complexity
- Corrected ENVO:01001059 (mock community culture) to OBI:0000079 (culture medium)
- Simplified to two-version comparison for better clarity

---

## Dataset 1: RBTnSeq-BW25113 - Transposon Fitness Screening

### Example 1.1: Gene thrB shows severe growth defect on D-galacturonic acid

#### Version A: Without OMP (Current Ontologies Only)

```yaml
association:
  id: rbtn_001a
  type: biolink:GeneToPhenotypicFeatureAssociation
  subject:
    id: EcoGene:EG10999
    label: thrB
    taxon: NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113
  predicate: RO:0002200  # has phenotype
  object:
    entity: GO:0008150  # biological process
    quality: PATO:0000462  # absent
    qualifier: GO:0046396  # D-galacturonic acid metabolic process
  qualifiers:
    chemical_environment:
      compound: CHEBI:33830  # D-galacturonic acid
      role: sole carbon source
      concentration: 0.2% w/v
    physical_environment:
      medium: OBI:0000079  # culture medium
      medium_type: M9 minimal salts  # free text
      temperature:
        value: 37
        unit: UO:0000027  # degree Celsius
    severity: PATO:0000396  # severe intensity
  evidence:
    - type: ECO:0007032  # transposon mutagenesis evidence
      value: {'fitness_score': -4.29, 'statistical_test': 't-test', 'p_value': 0.0008}
      supporting_data: {'barcode_reads': 18234, 'replicates': 2, 'correlation': 0.92}
  provenance:
    source: RBTnSeq-BW25113
    method: Random barcode transposon sequencing
```

#### Version C: With OMP (Hybrid Approach)

```yaml
association:
  id: rbtn_001c
  type: biolink:GeneToPhenotypicFeatureAssociation
  subject:
    id: EcoGene:EG10999
    label: thrB
    taxon: NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113
  predicate: RO:0002200  # has phenotype
  object:
    id: OMP:0006023  # carbon source utilization phenotype
    label: carbon source utilization phenotype
    extension: RO:0002503 towards CHEBI:33830  # towards D-galacturonic acid
  qualifiers:
    phenotype_state: PATO:0000462  # absent
    phenotype_severity: PATO:0000396  # severe intensity
    environmental_context:
      medium: OBI:0000079  # culture medium
      medium_description: M9 minimal salts
      carbon_source: CHEBI:33830  # D-galacturonic acid
      carbon_concentration: 0.2% w/v
      temperature:
        value: 37
        unit: UO:0000027  # degree Celsius
  evidence:
    - type: ECO:0007032  # transposon mutagenesis evidence
      value: {'fitness_score': -4.29, 'statistical_test': 't-test', 'p_value': 0.0008}
      supporting_data: {'barcode_reads': 18234, 'replicates': 2, 'correlation': 0.92}
  provenance:
    source: RBTnSeq-BW25113
    method: Random barcode transposon sequencing
```

### Example 1.2: Gene galK required for galactose utilization

#### Version A: Without OMP (Current Ontologies Only)

```yaml
association:
  id: rbtn_002a
  type: biolink:GeneToPhenotypicFeatureAssociation
  subject:
    id: EcoGene:EG10357
    label: galK
    taxon: NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113
  predicate: RO:0002200  # has phenotype
  object:
    process: GO:0006012  # galactose metabolic process
    quality: PATO:0002303  # decreased rate
    context: growth of unicellular organism
  qualifiers:
    chemical_environment:
      compound: CHEBI:17118  # D-galactose
      role: primary carbon source
      concentration: 0.2% w/v
    physical_environment:
      medium_base: OBI:0000079  # culture medium
      salts: M9 minimal salts
      supplements: none
    phenotype_manifestation: growth defect
  evidence:
    - type: ECO:0007032  # transposon mutagenesis evidence
      value: {'fitness_score': -5.8, 'p_value': 1e-05, 'threshold': 'fitness < -2 indicates growth defect'}
      quality_metrics: {'mad_score': 0.234, 'fdr': 0.001}
  provenance:
    source: RBTnSeq-BW25113
    method: Tn-seq competitive fitness assay
```

#### Version C: With OMP (Hybrid Approach)

```yaml
association:
  id: rbtn_002c
  type: biolink:GeneToPhenotypicFeatureAssociation
  subject:
    id: EcoGene:EG10357
    label: galK
    taxon: NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113
  predicate: RO:0002200  # has phenotype
  object:
    id: OMP:0006023  # carbon source utilization phenotype
    label: carbon source utilization phenotype
    extension: RO:0002503 towards CHEBI:17118  # towards D-galactose
  qualifiers:
    phenotype_state: PATO:0000462  # absent
    growth_conditions:
      medium: OBI:0000079  # culture medium
      medium_type: M9 minimal salts
      carbon_source: CHEBI:17118  # D-galactose
      concentration: 0.2% w/v
  evidence:
    - type: ECO:0007032  # transposon mutagenesis evidence
      value: {'fitness_score': -5.8, 'p_value': 1e-05, 'threshold': 'fitness < -2'}
      quality_metrics: {'mad_score': 0.234, 'fdr': 0.001}
  provenance:
    source: RBTnSeq-BW25113
    method: Tn-seq competitive fitness assay
```

---

## Dataset 2: Nichols et al. Chemical Genomics Screen

### Example 2.1: Gene recA shows increased sensitivity to mecillinam

#### Version A: Without OMP (Current Ontologies Only)

```yaml
association:
  id: nichols_001a
  type: biolink:ChemicalAffectsGeneAssociation
  subject:
    id: CHEBI:50505
    label: mecillinam
    role: antimicrobial agent
  predicate: biolink:affects
  qualified_predicate: biolink:causes
  object:
    id: EcoGene:EG10823
    label: recA
    taxon: NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113
  qualifiers:
    phenotype:
      process: GO:0046677  # response to antibiotic
      quality: PATO:0001549  # increased sensitivity toward
      substance: CHEBI:50505  # mecillinam
    experimental_conditions:
      medium: rich medium  # no specific ontology term for LB
      medium_name: LB broth
      chemical_concentration: 0.06 μg/mL
      temperature:
        value: 30
        unit: UO:0000027  # degree Celsius
      duration: 20 hours
  evidence:
    - type: ECO:0001563  # colony size measurement evidence
      value: {'s_score': -3.8, 'p_value': 0.0003, 'fdr_adjusted': 0.02}
      method_details: {'plate_format': '384-well', 'normalization': 'spatial correction applied', 'replicates': 3}
  provenance:
    source: Nichols et al. 2011
    publication: PMID:21609262
    method: Colony size measurement on agar plates
```

#### Version C: With OMP (Hybrid Approach)

```yaml
association:
  id: nichols_001c
  type: biolink:ChemicalAffectsGeneAssociation
  subject:
    id: CHEBI:50505
    label: mecillinam
    role: beta-lactam antibiotic
  predicate: biolink:affects
  qualified_predicate: biolink:causes
  object:
    id: EcoGene:EG10823
    label: recA
    taxon: NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113
  qualifiers:
    phenotype: OMP:0000336  # beta-lactam resistance phenotype
    phenotype_direction: PATO:0000911  # decreased quality
    experimental_conditions:
      medium_type: LB broth
      compound: CHEBI:50505  # mecillinam
      concentration: 0.06 μg/mL
      temperature:
        value: 30
        unit: UO:0000027  # degree Celsius
      duration: 20 hours
  evidence:
    - type: ECO:0001563  # colony size measurement evidence
      value: {'s_score': -3.8, 'p_value': 0.0003, 'fdr_adjusted': 0.02}
      method_details: {'plate_format': '384-well', 'normalization': 'spatial correction', 'replicates': 3}
  provenance:
    source: Nichols et al. 2011
    publication: PMID:21609262
    method: Colony size measurement
```

### Example 2.2: Gene nuo operon mutants sensitive to oxidative stress

#### Version A: Without OMP (Current Ontologies Only)

```yaml
association:
  id: nichols_002a
  type: biolink:ChemicalAffectsGeneAssociation
  subject:
    id: CHEBI:16240; modelseed.compound:cpd00025  # hydrogen peroxide
    label: hydrogen peroxide
    role: oxidizing agent
  predicate: biolink:affects
  object:
    id: EcoGene:EG10665
    label: nuoA
    pathway: GO:0006979  # response to oxidative stress
  qualifiers:
    phenotype_components:
      biological_process: GO:0006979  # response to oxidative stress
      quality: PATO:0001997  # decreased viability
      stress_type: oxidative stress
    mechanism: damage to iron-sulfur clusters
    conditions:
      medium: nutrient rich medium
      specific_medium: LB
      stressor: CHEBI:16240; modelseed.compound:cpd00025  # hydrogen peroxide
      concentration: 2.5 mM
      temperature: 37°C
  evidence:
    - type: ECO:0001563  # colony size measurement evidence
      value: {'s_score': -4.2, 'p_value': 5e-05, 'phenotype_strength': 'strong'}
      quality_control: {'bias_corrected': True, 'edge_effects_removed': True}
  provenance:
    source: Chemical genomics screen
    method: High-throughput colony pinning
```

#### Version C: With OMP (Hybrid Approach)

```yaml
association:
  id: nichols_002c
  type: biolink:ChemicalAffectsGeneAssociation
  subject:
    id: CHEBI:16240; modelseed.compound:cpd00025  # hydrogen peroxide
    label: hydrogen peroxide
  predicate: biolink:affects
  object:
    id: EcoGene:EG10665
    label: nuoA
    pathway: GO:0006979  # response to oxidative stress
  qualifiers:
    phenotype: OMP:0000173  # oxidative stress sensitivity
    mechanism_note: iron-sulfur cluster damage
    stress_conditions:
      medium: LB
      stressor: CHEBI:16240; modelseed.compound:cpd00025  # hydrogen peroxide
      concentration: 2.5 mM
      temperature: 37°C
  evidence:
    - type: ECO:0001563  # colony size measurement evidence
      value: {'s_score': -4.2, 'p_value': 5e-05, 'category': 'strong'}
      quality_metrics: {'corrections_applied': ['spatial', 'edge']}
  provenance:
    source: Chemical genomics screen
    method: HT colony pinning
```

---

## Dataset 3: ANL Environmental Isolate Metabolic Profiling

### Example 3.1: Isolate 562.61239 cannot utilize D-galacturonic acid

#### Version A: Without OMP (Current Ontologies Only)

```yaml
association:
  id: anl_001a
  type: biolink:OrganismToPhenotypicFeatureAssociation
  subject:
    id: ANL:562.61239
    label: E. coli environmental isolate 61239
    taxon: NCBITaxon:562  # Escherichia coli
  predicate: RO:0002200  # has phenotype
  object:
    biological_process: GO:0046396  # D-galacturonic acid metabolic process
    quality: PATO:0000462  # absent
    context: growth phenotype
  qualifiers:
    assay_conditions:
      base_medium: OBI:0000079  # culture medium
      medium_type: chemically defined minimal medium
      carbon_source: CHEBI:33830  # D-galacturonic acid
      carbon_role: sole carbon source
      temperature: 37°C
      measurement_time: 24 hours
  evidence:
    - type: ECO:0001845  # cell population optical density evidence
      value: {'growth_call': 0, 'od600_reading': 0.102, 'decision_threshold': 'OD600 > 0.2 at 24h = growth'}
      normalization_data: {'substrate_maximum': 0.683, 'substrate_minimum': 0.089, 'method': 'min-max scaling per substrate'}
  provenance:
    source: ANL-SDL-48EcoliPhenos
    method: Growth/no-growth assessment
    data_location: Sheet2, Row 2
```

#### Version C: With OMP (Hybrid Approach)

```yaml
association:
  id: anl_001c
  type: biolink:OrganismToPhenotypicFeatureAssociation
  subject:
    id: ANL:562.61239
    label: E. coli environmental isolate 61239
    taxon: NCBITaxon:562  # Escherichia coli
  predicate: RO:0002200  # has phenotype
  object:
    id: OMP:0006023  # carbon source utilization phenotype
    label: carbon source utilization phenotype
    extension: RO:0002503 towards CHEBI:33830  # towards D-galacturonic acid
  qualifiers:
    phenotype_state: PATO:0000462  # absent
    assay_conditions:
      medium: OBI:0000079  # culture medium
      medium_description: minimal defined medium
      carbon_source: CHEBI:33830  # D-galacturonic acid
      temperature: 37°C
      timepoint: 24 hours
  evidence:
    - type: ECO:0001845  # cell population optical density evidence
      value: {'binary_score': 0, 'od600': 0.102, 'threshold': 'OD600 > 0.2'}
      supporting_data: {'max_for_substrate': 0.683, 'min_for_substrate': 0.089, 'normalization': 'min-max'}
  provenance:
    source: ANL-SDL-48EcoliPhenos
    method: Phenotype array
    location: Sheet2, Row 2
```

### Example 3.2: Isolate 562.61143 can utilize salicin

#### Version A: Without OMP (Current Ontologies Only)

```yaml
association:
  id: anl_002a
  type: biolink:OrganismToPhenotypicFeatureAssociation
  subject:
    id: ANL:562.61143
    label: E. coli environmental isolate 61143
    taxon: NCBITaxon:562  # Escherichia coli
  predicate: RO:0002200  # has phenotype
  object:
    biological_process: GO:0016137  # glycoside metabolic process
    quality: PATO:0000467  # present
    substrate_specification: CHEBI:17814; modelseed.compound:cpd01030  # salicin
  qualifiers:
    growth_conditions:
      medium_base: OBI:0000079  # culture medium
      medium_description: minimal salts medium
      carbon_source: CHEBI:17814; modelseed.compound:cpd01030  # salicin
      source_concentration: standard test concentration
      incubation: 37°C, 24h
  evidence:
    - type: ECO:0001845  # cell population optical density evidence
      value: {'growth_score': 1, 'od600_measured': 0.487, 'above_threshold': True}
      replication: {'technical_replicates': 2, 'biological_replicates': 1}
  provenance:
    source: ANL Environmental Collection
    collector: Aaron's Lab
    assay_type: Binary growth phenotype
```

#### Version C: With OMP (Hybrid Approach)

```yaml
association:
  id: anl_002c
  type: biolink:OrganismToPhenotypicFeatureAssociation
  subject:
    id: ANL:562.61143
    label: E. coli environmental isolate 61143
    taxon: NCBITaxon:562  # Escherichia coli
  predicate: RO:0002200  # has phenotype
  object:
    id: OMP:0006023  # carbon source utilization phenotype
    label: carbon source utilization phenotype
    extension: RO:0002503 towards CHEBI:17814  # towards salicin
  qualifiers:
    phenotype_state: PATO:0000467  # present
    substrate_qualifier: CHEBI:17814; modelseed.compound:cpd01030  # salicin
    growth_medium:
      type: OBI:0000079  # culture medium
      description: minimal salts medium
      carbon_source: CHEBI:17814; modelseed.compound:cpd01030  # salicin
  evidence:
    - type: ECO:0001845  # cell population optical density evidence
      value: {'binary_score': 1, 'od600': 0.487, 'confidence': 'above threshold'}
      quality_metrics: {'technical_replicates': 2}
  provenance:
    source: ANL Collection
    method: Growth assessment
```

---

## Dataset 4: MG1655 Biolog Phenotype MicroArray

### Example 4.1: MG1655 shows low growth on N-acetylglucosamine

#### Version A: Without OMP (Current Ontologies Only)

```yaml
association:
  id: mg1655_001a
  type: biolink:OrganismToPhenotypicFeatureAssociation
  subject:
    id: NCBITaxon:511145
    label: E. coli K-12 MG1655
    strain_type: reference strain
  predicate: RO:0002200  # has phenotype
  object:
    metabolic_process: GO:0006044  # N-acetylglucosamine metabolic process
    quality: PATO:0000911  # decreased quality
    growth_category: partial  # intermediate phenotype
  qualifiers:
    test_conditions:
      plate_system: OBI:0400103  # microplate
      plate_type: Biolog PM1
      well_location: A3
      test_substrate: CHEBI:506227; modelseed.compound:cpd00122; modelseed.compound:cpd27608  # N-acetyl-D-glucosamine
      substrate_role: sole carbon source
      base_medium: Biolog IF-0a  # proprietary medium
    growth_level: Low Growth
  evidence:
    - type: ECO:0001091  # phenotype microarray evidence
      value: {'growth_category': 'Low Growth', 'od_range': 'OD590 0.1-0.3', 'measurement_time': '48 hours'}
      category_definitions: {'no_growth': 'OD590 < 0.1', 'low_growth': 'OD590 0.1-0.3', 'growth': 'OD590 > 0.3'}
  provenance:
    source: Biolog PM analysis
    platform: Phenotype MicroArray
    purpose: wild-type reference
```

#### Version C: With OMP (Hybrid Approach)

```yaml
association:
  id: mg1655_001c
  type: biolink:OrganismToPhenotypicFeatureAssociation
  subject:
    id: NCBITaxon:511145
    label: E. coli K-12 MG1655
    reference_strain: True
  predicate: RO:0002200  # has phenotype
  object:
    id: OMP:0006023  # carbon source utilization phenotype
    label: carbon source utilization phenotype
    extension: RO:0002503 towards CHEBI:506227  # towards N-acetyl-D-glucosamine
  qualifiers:
    phenotype_state: PATO:0000911  # decreased quality
    growth_category: low growth
    biolog_conditions:
      plate_type: PM1
      well: A3
      substrate: CHEBI:506227; modelseed.compound:cpd00122; modelseed.compound:cpd27608  # N-acetyl-D-glucosamine
      medium: Biolog IF-0a
  evidence:
    - type: ECO:0001091  # phenotype microarray evidence
      value: {'category': 'Low Growth', 'od_range': '0.1-0.3', 'timepoint': '48h'}
      thresholds: {'documented_by': 'ECO:0000033  # author statement', 'categories': ['<0.1', '0.1-0.3', '>0.3']}
  provenance:
    source: Biolog PM
    reference_type: WT baseline
```

### Example 4.2: MG1655 cannot grow on L-arabinose (unexpected)

#### Version A: Without OMP (Current Ontologies Only)

```yaml
association:
  id: mg1655_002a
  type: biolink:OrganismToPhenotypicFeatureAssociation
  subject:
    id: NCBITaxon:511145
    label: E. coli K-12 MG1655
  predicate: RO:0002200  # has phenotype
  object:
    process: GO:0019568  # L-arabinose metabolic process
    quality: PATO:0000462  # absent
    note: unexpected - MG1655 typically utilizes arabinose
  qualifiers:
    experimental_setup:
      assay: OBI:0001977  # growth assay
      plate_id: PM1
      well: A2
      carbon_source: CHEBI:30849  # L-arabinose
      medium_base: Biolog IF-0a minimal
      temperature: 37°C
    result_flag: requires_validation
  evidence:
    - type: ECO:0001091  # phenotype microarray evidence
      value: {'growth_result': 'No Growth', 'od590': '< 0.1', 'validated': False}
      concern: Contradicts known MG1655 metabolism
  provenance:
    source: MG1655_Phenotype_Microarray_Table
    method: Biolog PM carbon plate
    quality_note: unexpected result
```

#### Version C: With OMP (Hybrid Approach)

```yaml
association:
  id: mg1655_002c
  type: biolink:OrganismToPhenotypicFeatureAssociation
  subject:
    id: NCBITaxon:511145
    label: E. coli K-12 MG1655
  predicate: RO:0002200  # has phenotype
  object:
    id: OMP:0006023  # carbon source utilization phenotype
    label: carbon source utilization phenotype
    extension: RO:0002503 towards CHEBI:30849  # towards L-arabinose
  qualifiers:
    phenotype_state: PATO:0000462  # absent
    substrate_qualifier: CHEBI:30849  # L-arabinose
    unexpected_result: True
    assay_details:
      plate_system: Biolog PM1
      well: A2
      medium: Biolog IF-0a minimal
      temperature: 37°C
  evidence:
    - type: ECO:0001091  # phenotype microarray evidence
      value: {'result': 'No Growth', 'od590': '< 0.1', 'requires_validation': True}
      note: Unexpected for MG1655
  provenance:
    source: Biolog PM Table
    quality_flag: needs_review
```

---

## Critical Assessment: OMP Adoption and Implementation

### 1. Ontology Maturity and Coverage

**OMP Status:**
- First release: 2014; Latest documented activity: OMPwiki edited March 2024
- Currently adopted by: OMPwiki annotation system, various research publications
- Limited adoption compared to GO (used in >100 biological databases)
- Many specific pre-composed terms do not exist (e.g., individual carbon source utilization phenotypes)
- Requires post-composition approach for many common phenotypes

### 2. The GO/OMP Distinction

**Key Differences:**
- GO describes **gene product functions** (what proteins do)
- OMP describes **observable organism phenotypes** (what happens to the organism)
- Example: GO:0046396 describes the biochemical process of galacturonic acid metabolism, while OMP would describe the phenotype of being unable to grow on galacturonic acid

This distinction aligns with established ontology design principles separating molecular functions from organism-level phenotypes.

### 3. Implementation Comparison

**Version A (Standard Ontologies Only):**
- Requires 3-5 ontology terms to construct each phenotype
- More verbose but uses well-established ontologies
- May lack specificity for microbial phenotypes

**Version C (With OMP):**
- Single phenotype term + state qualifier
- ~40% fewer terms needed
- More concise and specific for microbial phenotypes
- Requires understanding of post-composition patterns

### 4. Recommendations

1. **For New Projects:**
   - Consider Version C (OMP hybrid) for cleaner annotations
   - Establish clear post-composition guidelines
   - Document all term usage patterns

2. **For Existing Projects:**
   - Version A may be more practical if already using standard ontologies
   - Consider gradual migration to incorporate OMP terms

3. **Best Practices:**
   - Always include ECO evidence codes
   - Use ModelSEED identifiers alongside CHEBI when available
   - Document any unexpected or contradictory results
   - Validate ontology terms before use

---

## Summary

### Key Differences Between Approaches:
1. **Version A (Without OMP)**: Requires multiple ontology terms to construct phenotypes; uses only well-established ontologies
2. **Version C (With OMP)**: Single phenotype term + qualifiers; more concise but requires OMP adoption

### Complexity Reduction:
- Version C reduces term count by ~40% while maintaining semantic precision
- Both approaches use the same evidence (ECO) and chemical (CHEBI) ontologies
- Version C provides clearer phenotype representation for microbial data

### Ontology Terms Used:
- **NCBITaxon**: 562 (E. coli), 511145 (BW25113/MG1655)
- **CHEBI**: 33830 (galacturonic acid), 17118 (galactose), 50505 (mecillinam), 16240 (H2O2; modelseed:cpd00025), 17814 (salicin; modelseed:cpd01030), 506227 (GlcNAc; modelseed:cpd00122,cpd27608), 30849 (L-arabinose)
- **GO**: 0046396 (galacturonate metabolism), 0006012 (galactose metabolism), 0046677 (antibiotic response), 0006979 (oxidative stress), 0016137 (glycoside metabolic process), 0006044 (GlcNAc metabolism), 0019568 (arabinose metabolism), 0008150 (biological process)
- **PATO**: 0000462 (absent), 0000467 (present), 0000911 (decreased quality), 0002303 (decreased rate), 0000396 (severe), 0001549 (increased sensitivity toward), 0001997 (decreased viability)
- **ECO**: 0007032 (transposon mutagenesis), 0001563 (colony size), 0001845 (optical density), 0001091 (phenotype microarray), 0000033 (author statement)
- **RO**: 0002200 (has phenotype), 0002503 (towards)
- **UO**: 0000027 (degree Celsius)
- **OBI**: 0000079 (culture medium), 0400103 (microplate), 0001977 (growth assay)
- **OMP**: 0006023 (carbon source utilization phenotype), 0000336 (beta-lactam resistance phenotype), 0000173 (oxidative stress sensitivity)