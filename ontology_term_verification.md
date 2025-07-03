# Ontology Term Verification Report

**Date**: 2025-01-03
**Document**: ontology_annotation_examples_v4.md

## Verification Status Summary

### Critical Issues Found
- **OMP:0005009**: INCORRECTLY labeled as "hexose utilization" - Actually means "acidophile" (pH-related phenotype)

## Detailed Term Verification

### OMP (Ontology of Microbial Phenotypes) Terms

| Term ID | Our Usage | Official Definition | Status | Source |
|---------|-----------|-------------------|---------|---------|
| OMP:0005009 | hexose utilization | acidophile - A population growth phenotype for microorganisms with optimal growth at pH 0-5.5 | ❌ INCORRECT | User provided |
| OMP:0000336 | beta-lactam resistance phenotype | beta-lactam resistance phenotype - Used when the chemical described in the extension is a beta-lactam (e.g., penicillin, ampicillin, methicillin) | ✅ CORRECT | PMC6631659 |
| OMP:0005135 | oxidative stress sensitivity | Likely correct based on OMP structure, but exact definition not found | ⚠️ UNVERIFIED | |
| OMP:0005040 | N-acetylglucosamine utilization | Likely refers to GlcNAc utilization phenotype, but exact term not found | ⚠️ UNVERIFIED | |
| OMP:0005001 | pentose utilization | Likely refers to pentose sugar utilization (arabinose/xylose), but exact term not found | ⚠️ UNVERIFIED | |

### MCO (Microbial Conditions Ontology) Terms

| Term ID | Our Usage | Official Definition | Status | Source |
|---------|-----------|-------------------|---------|---------|
| MCO:0000030 | minimal medium | Likely correct - MCO includes minimal media classifications | ⚠️ UNVERIFIED BUT PLAUSIBLE | PMC7963087 mentions minimal media in MCO |
| MCO:0000031 | M9 minimal medium | Likely correct - MCO specifically includes M9 as a defined medium | ⚠️ UNVERIFIED BUT PLAUSIBLE | PMC7963087 mentions M9 in MCO |
| MCO:0000032 | LB broth | Likely correct - MCO specifically includes LB as a defined medium | ⚠️ UNVERIFIED BUT PLAUSIBLE | PMC7963087 mentions LB in MCO |

### CHEBI (Chemical Entities of Biological Interest) Terms

| Term ID | Our Usage | Official Definition | Status | Source |
|---------|-----------|-------------------|---------|---------|
| CHEBI:16240 | hydrogen peroxide | [TO BE VERIFIED] | ⏳ | |
| CHEBI:16716 | L-arabinose | [TO BE VERIFIED] | ⏳ | |
| CHEBI:17118 | D-galactose | [TO BE VERIFIED] | ⏳ | |
| CHEBI:17814 | salicin | [TO BE VERIFIED] | ⏳ | |
| CHEBI:33830 | D-galacturonic acid | [TO BE VERIFIED] | ⏳ | |
| CHEBI:50505 | mecillinam | [TO BE VERIFIED] | ⏳ | |
| CHEBI:506227 | N-acetyl-D-glucosamine | [TO BE VERIFIED] | ⏳ | |

### GO (Gene Ontology) Terms

| Term ID | Our Usage | Official Definition | Status | Source |
|---------|-----------|-------------------|---------|---------|
| GO:0006012 | galactose metabolic process | [TO BE VERIFIED] | ⏳ | |
| GO:0006044 | N-acetylglucosamine metabolic process | [TO BE VERIFIED] | ⏳ | |
| GO:0006979 | response to oxidative stress | [TO BE VERIFIED] | ⏳ | |
| GO:0008150 | biological process | [TO BE VERIFIED] | ⏳ | |
| GO:0016137 | glycoside metabolic process | [TO BE VERIFIED] | ⏳ | |
| GO:0019568 | L-arabinose metabolic process | [TO BE VERIFIED] | ⏳ | |
| GO:0046396 | D-galacturonic acid metabolic process | [TO BE VERIFIED] | ⏳ | |
| GO:0046677 | response to antibiotic | [TO BE VERIFIED] | ⏳ | |

### PATO (Phenotypic Quality Ontology) Terms

| Term ID | Our Usage | Official Definition | Status | Source |
|---------|-----------|-------------------|---------|---------|
| PATO:0000396 | severe intensity | [TO BE VERIFIED] | ⏳ | |
| PATO:0000462 | absent | [TO BE VERIFIED] | ⏳ | |
| PATO:0000467 | present | [TO BE VERIFIED] | ⏳ | |
| PATO:0000911 | decreased quality | [TO BE VERIFIED] | ⏳ | |
| PATO:0001549 | increased sensitivity toward | [TO BE VERIFIED] | ⏳ | |
| PATO:0001997 | decreased viability | [TO BE VERIFIED] | ⏳ | |
| PATO:0002303 | decreased rate | [TO BE VERIFIED] | ⏳ | |

### ECO (Evidence and Conclusion Ontology) Terms

| Term ID | Our Usage | Official Definition | Status | Source |
|---------|-----------|-------------------|---------|---------|
| ECO:0000033 | author statement | [TO BE VERIFIED] | ⏳ | |
| ECO:0001091 | phenotype microarray evidence | [TO BE VERIFIED] | ⏳ | |
| ECO:0001563 | colony size measurement evidence | [TO BE VERIFIED] | ⏳ | |
| ECO:0001845 | cell population optical density evidence | [TO BE VERIFIED] | ⏳ | |
| ECO:0007032 | transposon mutagenesis evidence | [TO BE VERIFIED] | ⏳ | |

### Other Ontology Terms

| Term ID | Ontology | Our Usage | Official Definition | Status | Source |
|---------|----------|-----------|-------------------|---------|---------|
| NCBITaxon:511145 | NCBITaxon | E. coli str. K-12 substr. BW25113/MG1655 | [TO BE VERIFIED] | ⏳ | |
| NCBITaxon:562 | NCBITaxon | Escherichia coli | [TO BE VERIFIED] | ⏳ | |
| RO:0002200 | RO | has phenotype | [TO BE VERIFIED] | ⏳ | |
| RO:0002503 | RO | towards | [TO BE VERIFIED] | ⏳ | |
| UO:0000027 | UO | degree Celsius | [TO BE VERIFIED] | ⏳ | |
| ENVO:01001059 | ENVO | microbial culture medium | [TO BE VERIFIED] | ⏳ | |
| OBI:0001977 | OBI | growth assay | [TO BE VERIFIED] | ⏳ | |
| OBI:0400103 | OBI | microplate | [TO BE VERIFIED] | ⏳ | |

## Legend
- ✅ Verified correct
- ❌ INCORRECT - needs fixing
- ⏳ Pending verification
- ⚠️ Term not found - needs placeholder
- 📝 Requires post-composition

## Verification Summary

### Critical Findings:
1. **OMP:0005009 is INCORRECT** - This is "acidophile" NOT "hexose utilization"
2. **Multiple OMP terms could not be verified** - Terms for specific carbon utilization phenotypes may not exist as pre-composed terms
3. **MCO terms appear plausible** but could not be verified with exact definitions
4. **Most CHEBI, GO, PATO, ECO terms are standard and widely used**

### Recommendations for v4 Corrections:

1. **For OMP:0005009 (currently mislabeled as "hexose utilization")**:
   ```yaml
   # REPLACE WITH:
   id: "[PLACEHOLDER: hexose utilization phenotype]"
   label: "carbon source utilization phenotype"
   extension: "RO:0002503 towards CHEBI:17118"  # towards D-galactose
   ```

2. **For unverified OMP terms**, add warning comments:
   ```yaml
   id: "OMP:0005040"  # [UNVERIFIED: N-acetylglucosamine utilization - term may not exist]
   ```

3. **For MCO terms**, add notes about plausibility:
   ```yaml
   id: "MCO:0000031"  # M9 minimal medium [UNVERIFIED but mentioned in MCO publications]
   ```

## Next Steps
1. Fix the critical OMP:0005009 error in v4
2. Add verification warnings to all unverified terms
3. Update critical assessment to reflect limited pre-composed term availability
4. Add verification statement to document header