# Corrections Needed for ontology_annotation_examples_v4.md

## Critical Corrections Required

### 1. OMP Terms
- **OMP:0005009** (line 158): Already fixed - was "hexose utilization", is actually "acidophile"
- **OMP:0005135** (line 335): Label says "oxidative stress sensitivity" but term is "abolished resistance to SDS-EDTA stress"
- **OMP:0005040** (line 575): Label says "N-acetylglucosamine utilization" but term is "response to acid pH stress phenotype"
- **OMP:0005001** (line 649): Label says "pentose utilization" but term is "altered caffeine resistance"

### 2. MCO Terms
- **MCO:0000030** (lines 421, 502, 581, 656): Label says "minimal medium" but term is "LB medium, Lennox"
- **MCO:0000031** (lines 83, 166): Label says "M9 minimal medium" but term is "LB medium, Luria"
- **MCO:0000032** (lines 255, 338): Correct as "LB broth" (it's "LB medium, Miller")

### 3. CHEBI Terms
- **CHEBI:17118** (lines 124, 162, 168): Should note this is "aldehydo-D-galactose"
- Consider using CHEBI:12936 for "D-galactose" instead

### 4. ModelSEED Mappings to Add
- CHEBI:17814 (salicin) → ModelSEED:cpd01030

## Recommended Approach

Since many expected phenotype terms don't exist:

1. **For carbon utilization phenotypes**: Use OMP:0006023 "carbon source utilization phenotype" with post-composition
2. **For stress phenotypes**: Use actual verified terms or placeholders
3. **For media**: Use correct MCO terms or find appropriate minimal medium terms

## Example Corrections

```yaml
# WRONG:
id: "OMP:0005040"  # N-acetylglucosamine utilization

# CORRECT:
id: "OMP:0006023"  # carbon source utilization phenotype
extension: "RO:0002503 towards CHEBI:506227"  # towards N-acetyl-D-glucosamine

# OR:
id: "[PLACEHOLDER: N-acetylglucosamine utilization phenotype]"
```