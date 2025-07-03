# CHEBI to ModelSEED Compound Mapping Report

## Summary

This report documents the ModelSEED compound IDs found for CHEBI terms referenced in the v4 ontology annotation document. The verification was performed using the `verify_term.py` tool, which searches through loaded ontology files for cross-references.

## Methodology

1. Extracted CHEBI terms from the v4 document
2. Used the `verify_term.py` tool to check each CHEBI ID
3. The tool searches for ModelSEED mappings in the cross-references of CHEBI terms
4. Compiled results showing which CHEBI terms have corresponding ModelSEED compound IDs

## Results

### CHEBI Terms with ModelSEED Mappings

| CHEBI ID | CHEBI Name | ModelSEED ID(s) | Notes |
|----------|------------|------------------|-------|
| CHEBI:16240 | hydrogen peroxide | cpd00025 | Used in oxidative stress examples |
| CHEBI:17814 | salicin | cpd01030 | Used in ANL isolate examples |
| CHEBI:506227 | N-acetyl-D-glucosamine | cpd00122, cpd27608 | Two ModelSEED mappings found |
| CHEBI:28061 | alpha-D-galactose | cpd00724 | Alternative form of D-galactose |
| CHEBI:4139 | D-galactopyranose | cpd00108 | Another form of D-galactose |

### CHEBI Terms WITHOUT ModelSEED Mappings

| CHEBI ID | CHEBI Name | Notes |
|----------|------------|-------|
| CHEBI:17118 | aldehydo-D-galactose | Form of D-galactose, no direct mapping |
| CHEBI:33830 | galacturonic acid | No ModelSEED mapping found |
| CHEBI:50505 | sweetening agent | General category, not a specific compound |
| CHEBI:30849 | L-arabinose | No ModelSEED mapping found |

### Correction Needed

The v4 document incorrectly lists CHEBI:16716 as "L-arabinose" when it actually represents "benzene" (with ModelSEED mapping cpd01007). The correct CHEBI ID for L-arabinose is CHEBI:30849.

## Key Findings

1. **Coverage**: Only 5 out of 9 tested CHEBI terms have ModelSEED mappings (56% coverage)
2. **Multiple Mappings**: Some compounds like N-acetyl-D-glucosamine have multiple ModelSEED IDs
3. **Form Variations**: Different forms of the same compound (e.g., various forms of D-galactose) may have different mappings
4. **Missing Mappings**: Important metabolites like L-arabinose and D-galacturonic acid lack ModelSEED mappings

## Recommendations

1. **Mapping Expansion**: ModelSEED should consider adding mappings for common metabolites like L-arabinose and D-galacturonic acid
2. **Form Standardization**: Clear guidelines needed for which chemical form (e.g., aldehydo vs regular form) should be used for mappings
3. **Documentation**: Cross-reference mappings should be documented in both CHEBI and ModelSEED ontologies
4. **Validation**: Regular validation of cross-references to ensure accuracy and completeness

## Technical Notes

- The verification tool loads ontology files from the local `/ontologies` directory
- ModelSEED cross-references are stored in the CHEBI ontology file
- The tool searches for both "cpd#####" format and "CHEBI:#####" format in cross-references