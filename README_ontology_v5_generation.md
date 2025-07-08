# Generating the Ontology Annotation Examples v5 Document

This README explains the process and tools used to create the `ontology_annotation_examples_v5.md` comparative analysis document.

## Overview

The v5 document demonstrates three approaches for annotating microbial phenotype data:
- **Version A**: Using only standard ontologies (CHEBI, GO, PATO, ECO, NCBITaxon, RO, UO, ENVO, OBI)
- **Version B**: Adding specialized microbial ontologies (OMP and MCO)
- **Version C**: Hybrid approach using OMP but not MCO

## Prerequisites

### Required Ontology Files
The following ontology files must be present in the `ontology_tools/ontologies/` directory:
- `omp.obo` - Ontology of Microbial Phenotypes
- `mco.obo` - Microbial Conditions Ontology
- `chebi.obo` - Chemical Entities of Biological Interest
- `eco.obo` - Evidence and Conclusion Ontology
- `envo.obo` - Environment Ontology
- `go.obo` - Gene Ontology
- `obi.obo` - Ontology for Biomedical Investigations
- `pato.obo` - Phenotype And Trait Ontology
- `ro.obo` - Relations Ontology
- `uo.obo` - Units of Measurement Ontology
- `modelSeed.obo` - ModelSEED compound ontology

### Python Dependencies
```bash
pip install pronto rdflib pyyaml
```

## Generation Process

### Step 1: Analyze Previous Version (v4)
First, run the batch verification tool on the v4 document to identify issues:

```bash
cd ontology_tools
python batch_verify.py ../ontology_annotation_examples_v4.md
```

This generates `ontology_annotation_examples_v4_verification_report.md` which highlights:
- Missing or incorrect ontology terms
- Obsolete terms that need updating
- Terms that need ModelSEED mappings

### Step 2: Search for Appropriate Terms
Use the search tool to find suitable ontology terms for each concept:

```bash
# Search for carbon utilization phenotypes in OMP
python search_ontology.py OMP "carbon utilization"

# Search for specific compounds in CHEBI
python search_ontology.py CHEBI "galacturonic acid"

# Search for minimal medium conditions in MCO
python search_ontology.py MCO "minimal medium"
```

### Step 3: Verify Individual Terms
Verify specific terms and get their definitions:

```bash
# Verify a specific term
python verify_term.py OMP:0006023

# Check CHEBI-ModelSEED mappings
python verify_term.py CHEBI:33830
```

### Step 4: Create the Comparative Document
Based on the verification results and term searches, manually create the v5 document with the following structure:

1. **Header and Overview**
   - Version number and date
   - Description of the three approaches

2. **Dataset Examples**
   For each dataset (RBTnSeq, Nichols, ANL, MG1655):
   - Create parallel examples showing the same phenotype in all three versions
   - Include proper ontology term IDs with labels
   - Add ModelSEED compound IDs alongside CHEBI terms

3. **Critical Assessment Section**
   - Document limitations of OMP and MCO
   - Include adoption statistics and maturity assessments
   - Provide implementation recommendations

### Step 5: Final Verification
Run the batch verification on the completed v5 document:

```bash
python batch_verify.py ../ontology_annotation_examples_v5.md
```

Review the verification report to ensure:
- All ontology terms are valid
- No obsolete terms are used
- ModelSEED mappings are included where appropriate

## Key Formatting Guidelines

### Ontology Term Format
```yaml
# Single term with label
id: "OMP:0006023"  # carbon source utilization phenotype

# Term with extension
extension: "RO:0002503 towards CHEBI:33830"  # towards D-galacturonic acid

# Compound with ModelSEED mapping
compound: "CHEBI:16240; modelseed.compound:cpd00025"  # hydrogen peroxide
```

### Evidence Format
Always include ECO terms for evidence:
```yaml
evidence:
  - type: "ECO:0007032"  # transposon mutagenesis evidence
    value:
      fitness_score: -4.29
      p_value: 0.0008
```

## Maintenance

### Updating Ontologies
Periodically update the ontology files:
```bash
# Download latest versions
wget http://purl.obolibrary.org/obo/omp.obo -O ontologies/omp.obo
wget http://purl.obolibrary.org/obo/mco.obo -O ontologies/mco.obo
# ... etc for other ontologies
```

### Adding New Examples
When adding new phenotype examples:
1. Search for appropriate terms using `search_ontology.py`
2. Verify terms exist using `verify_term.py`
3. Create parallel examples for all three versions
4. Include proper evidence and provenance
5. Run batch verification to ensure correctness

## Troubleshooting

### Common Issues
1. **"Term not found" errors**: Update ontology files or check term ID format
2. **Missing ModelSEED mappings**: Not all CHEBI terms have ModelSEED equivalents
3. **Obsolete terms**: Use the suggested replacements from verification reports

### Getting Help
- OMP documentation: https://github.com/microbialphenotypes/OMP-ontology
- MCO documentation: https://github.com/microbialconditions/MCO-ontology
- OBO Foundry: http://obofoundry.org/

## Authors
This document generation process was developed to create standardized, verifiable ontology annotations for microbial phenotype data across multiple research datasets.