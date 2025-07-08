#!/usr/bin/env python3
"""
Generate ontology_annotation_examples_v6.md

This script generates the complete v6 ontology annotation examples document
with Version A (without OMP) and Version C (with OMP) comparisons.

Usage: python generate_ontology_v6.py
"""

import textwrap
from typing import Dict, List, Any, Optional
from datetime import datetime


class OntologyV6Generator:
    """Generator for ontology annotation examples v6 document."""
    
    def __init__(self):
        """Initialize the generator with all example data."""
        self.datasets = self._load_datasets()
        self.chebi_modelseed_mappings = self._load_mappings()
    
    def _load_mappings(self) -> Dict[str, str]:
        """Load CHEBI to ModelSEED mappings."""
        return {
            "CHEBI:16240": "modelseed.compound:cpd00025",  # hydrogen peroxide
            "CHEBI:17814": "modelseed.compound:cpd01030",  # salicin
            "CHEBI:506227": "modelseed.compound:cpd00122; modelseed.compound:cpd27608",  # N-acetyl-D-glucosamine
        }
    
    def _load_datasets(self) -> List[Dict[str, Any]]:
        """Load all dataset examples."""
        return [
            {
                "name": "Dataset 1: RBTnSeq-BW25113 - Transposon Fitness Screening",
                "examples": [
                    {
                        "title": "Example 1.1: Gene thrB shows severe growth defect on D-galacturonic acid",
                        "data": {
                            "gene_id": "EcoGene:EG10999",
                            "gene_name": "thrB",
                            "compound_id": "CHEBI:33830",
                            "compound_name": "D-galacturonic acid",
                            "phenotype": "growth_defect",
                            "severity": "severe",
                            "fitness_score": -4.29,
                            "p_value": 0.0008,
                            "medium": "M9 minimal salts",
                            "temperature": 37,
                            "concentration": "0.2% w/v"
                        }
                    },
                    {
                        "title": "Example 1.2: Gene galK required for galactose utilization",
                        "data": {
                            "gene_id": "EcoGene:EG10357",
                            "gene_name": "galK",
                            "compound_id": "CHEBI:17118",
                            "compound_name": "D-galactose",
                            "phenotype": "growth_defect",
                            "fitness_score": -5.8,
                            "p_value": 0.00001,
                            "medium": "M9 minimal salts",
                            "temperature": 37,
                            "concentration": "0.2% w/v"
                        }
                    }
                ]
            },
            {
                "name": "Dataset 2: Nichols et al. Chemical Genomics Screen",
                "examples": [
                    {
                        "title": "Example 2.1: Gene recA shows increased sensitivity to mecillinam",
                        "data": {
                            "gene_id": "EcoGene:EG10823",
                            "gene_name": "recA",
                            "compound_id": "CHEBI:50505",
                            "compound_name": "mecillinam",
                            "phenotype": "antibiotic_sensitivity",
                            "s_score": -3.8,
                            "p_value": 0.0003,
                            "medium": "LB broth",
                            "temperature": 30,
                            "concentration": "0.06 μg/mL",
                            "duration": "20 hours"
                        }
                    },
                    {
                        "title": "Example 2.2: Gene nuo operon mutants sensitive to oxidative stress",
                        "data": {
                            "gene_id": "EcoGene:EG10665",
                            "gene_name": "nuoA",
                            "compound_id": "CHEBI:16240",
                            "compound_name": "hydrogen peroxide",
                            "phenotype": "oxidative_stress_sensitivity",
                            "s_score": -4.2,
                            "p_value": 0.00005,
                            "medium": "LB",
                            "temperature": 37,
                            "concentration": "2.5 mM"
                        }
                    }
                ]
            },
            {
                "name": "Dataset 3: ANL Environmental Isolate Metabolic Profiling",
                "examples": [
                    {
                        "title": "Example 3.1: Isolate 562.61239 cannot utilize D-galacturonic acid",
                        "data": {
                            "strain_id": "ANL:562.61239",
                            "strain_name": "E. coli environmental isolate 61239",
                            "compound_id": "CHEBI:33830",
                            "compound_name": "D-galacturonic acid",
                            "phenotype": "no_growth",
                            "od600": 0.102,
                            "growth_score": 0,
                            "medium": "minimal defined medium",
                            "temperature": 37,
                            "timepoint": "24 hours"
                        }
                    },
                    {
                        "title": "Example 3.2: Isolate 562.61143 can utilize salicin",
                        "data": {
                            "strain_id": "ANL:562.61143",
                            "strain_name": "E. coli environmental isolate 61143",
                            "compound_id": "CHEBI:17814",
                            "compound_name": "salicin",
                            "phenotype": "growth",
                            "od600": 0.487,
                            "growth_score": 1,
                            "medium": "minimal salts medium",
                            "temperature": 37,
                            "timepoint": "24 hours"
                        }
                    }
                ]
            },
            {
                "name": "Dataset 4: MG1655 Biolog Phenotype MicroArray",
                "examples": [
                    {
                        "title": "Example 4.1: MG1655 shows low growth on N-acetylglucosamine",
                        "data": {
                            "strain_id": "NCBITaxon:511145",
                            "strain_name": "E. coli K-12 MG1655",
                            "compound_id": "CHEBI:506227",
                            "compound_name": "N-acetyl-D-glucosamine",
                            "phenotype": "low_growth",
                            "plate": "PM1",
                            "well": "A3",
                            "od_range": "0.1-0.3",
                            "medium": "Biolog IF-0a",
                            "timepoint": "48 hours"
                        }
                    },
                    {
                        "title": "Example 4.2: MG1655 cannot grow on L-arabinose (unexpected)",
                        "data": {
                            "strain_id": "NCBITaxon:511145",
                            "strain_name": "E. coli K-12 MG1655",
                            "compound_id": "CHEBI:30849",
                            "compound_name": "L-arabinose",
                            "phenotype": "no_growth",
                            "plate": "PM1",
                            "well": "A2",
                            "od590": "< 0.1",
                            "medium": "Biolog IF-0a minimal",
                            "unexpected": True
                        }
                    }
                ]
            }
        ]
    
    def _format_yaml_value(self, value: Any, indent: int = 0) -> str:
        """Format a single YAML value."""
        indent_str = "  " * indent
        
        if isinstance(value, dict):
            lines = []
            for k, v in value.items():
                if isinstance(v, dict) or isinstance(v, list):
                    lines.append(f"{indent_str}{k}:")
                    lines.append(self._format_yaml_value(v, indent + 1))
                else:
                    lines.append(f"{indent_str}{k}: {v}")
            return "\n".join(lines)
        elif isinstance(value, list):
            lines = []
            for item in value:
                lines.append(f"{indent_str}- {item}")
            return "\n".join(lines)
        else:
            return f"{indent_str}{value}"
    
    def _format_yaml(self, data: Dict[str, Any], indent: int = 0) -> str:
        """Format dictionary as YAML with proper indentation."""
        lines = []
        indent_str = "  " * indent
        
        for key, value in data.items():
            if value is None:
                continue
                
            if key.startswith("#"):
                # This is a comment line
                lines.append(f"{indent_str}{key}")
                continue
                
            if isinstance(value, dict):
                lines.append(f"{indent_str}{key}:")
                lines.append(self._format_yaml(value, indent + 1))
            elif isinstance(value, list):
                lines.append(f"{indent_str}{key}:")
                for item in value:
                    if isinstance(item, dict):
                        # Special handling for lists of dicts
                        first_key = list(item.keys())[0]
                        if len(item) == 1:
                            # Single key-value in dict
                            lines.append(f"{indent_str}  - {first_key}: {item[first_key]}")
                        else:
                            # Multiple keys in dict
                            lines.append(f"{indent_str}  - {first_key}: {item[first_key]}")
                            for k, v in list(item.items())[1:]:
                                if isinstance(v, dict):
                                    lines.append(f"{indent_str}    {k}:")
                                    for sub_k, sub_v in v.items():
                                        lines.append(f"{indent_str}      {sub_k}: {sub_v}")
                                else:
                                    lines.append(f"{indent_str}    {k}: {v}")
                    else:
                        lines.append(f"{indent_str}  - {item}")
            elif isinstance(value, str) and ("  #" in value):
                # Don't quote strings with inline comments
                lines.append(f"{indent_str}{key}: {value}")
            elif isinstance(value, str) and (": " in value):
                # Quote strings that contain colons
                lines.append(f'{indent_str}{key}: "{value}"')
            else:
                lines.append(f"{indent_str}{key}: {value}")
        
        return "\n".join(lines)
    
    def _get_modelseed_id(self, chebi_id: str) -> Optional[str]:
        """Get ModelSEED ID for a CHEBI ID if available."""
        return self.chebi_modelseed_mappings.get(chebi_id)
    
    def _generate_version_a_rbtseq(self, example_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Version A (without OMP) for RBTnSeq examples."""
        data = example_data["data"]
        
        if data["gene_name"] == "thrB":
            return {
                "association": {
                    "id": "rbtn_001a",
                    "type": "biolink:GeneToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["gene_id"],
                        "label": data["gene_name"],
                        "taxon": "NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113"
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "# Must construct phenotype from multiple components": None,
                        "entity": "GO:0008150  # biological process",
                        "quality": "PATO:0000462  # absent",
                        "qualifier": "GO:0046396  # D-galacturonic acid metabolic process"
                    },
                    "qualifiers": {
                        "chemical_environment": {
                            "compound": f"{data['compound_id']}  # {data['compound_name']}",
                            "role": "sole carbon source",
                            "concentration": data["concentration"]
                        },
                        "physical_environment": {
                            "medium": "OBI:0000079  # culture medium",
                            "medium_type": "M9 minimal salts  # free text",
                            "temperature": {
                                "value": data["temperature"],
                                "unit": "UO:0000027  # degree Celsius"
                            }
                        },
                        "severity": "PATO:0000396  # severe intensity"
                    },
                    "evidence": [{
                        "type": "ECO:0007032  # transposon mutagenesis evidence",
                        "value": {
                            "fitness_score": data["fitness_score"],
                            "statistical_test": "t-test",
                            "p_value": data["p_value"]
                        },
                        "supporting_data": {
                            "barcode_reads": 18234,
                            "replicates": 2,
                            "correlation": 0.92
                        }
                    }],
                    "provenance": {
                        "source": "RBTnSeq-BW25113",
                        "method": "Random barcode transposon sequencing"
                    }
                }
            }
        else:  # galK
            return {
                "association": {
                    "id": "rbtn_002a",
                    "type": "biolink:GeneToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["gene_id"],
                        "label": data["gene_name"],
                        "taxon": "NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113"
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "# Complex multi-part phenotype": None,
                        "process": "GO:0006012  # galactose metabolic process",
                        "quality": "PATO:0002303  # decreased rate",
                        "context": "growth of unicellular organism"
                    },
                    "qualifiers": {
                        "chemical_environment": {
                            "compound": f"{data['compound_id']}  # {data['compound_name']}",
                            "role": "primary carbon source",
                            "concentration": data["concentration"]
                        },
                        "physical_environment": {
                            "medium_base": "OBI:0000079  # culture medium",
                            "salts": "M9 minimal salts",
                            "supplements": "none"
                        },
                        "phenotype_manifestation": "growth defect"
                    },
                    "evidence": [{
                        "type": "ECO:0007032  # transposon mutagenesis evidence",
                        "value": {
                            "fitness_score": data["fitness_score"],
                            "p_value": data["p_value"],
                            "threshold": "fitness < -2 indicates growth defect"
                        },
                        "quality_metrics": {
                            "mad_score": 0.234,
                            "fdr": 0.001
                        }
                    }],
                    "provenance": {
                        "source": "RBTnSeq-BW25113",
                        "method": "Tn-seq competitive fitness assay"
                    }
                }
            }
    
    def _generate_version_c_rbtseq(self, example_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Version C (with OMP) for RBTnSeq examples."""
        data = example_data["data"]
        
        if data["gene_name"] == "thrB":
            return {
                "association": {
                    "id": "rbtn_001c",
                    "type": "biolink:GeneToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["gene_id"],
                        "label": data["gene_name"],
                        "taxon": "NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113"
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "id": "OMP:0006023  # carbon source utilization phenotype",
                        "label": "carbon source utilization phenotype",
                        "extension": f"RO:0002503 towards {data['compound_id']}  # towards {data['compound_name']}"
                    },
                    "qualifiers": {
                        "phenotype_state": "PATO:0000462  # absent",
                        "phenotype_severity": "PATO:0000396  # severe intensity",
                        "environmental_context": {
                            "medium": "OBI:0000079  # culture medium",
                            "medium_description": "M9 minimal salts",
                            "carbon_source": f"{data['compound_id']}  # {data['compound_name']}",
                            "carbon_concentration": data["concentration"],
                            "temperature": {
                                "value": data["temperature"],
                                "unit": "UO:0000027  # degree Celsius"
                            }
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0007032  # transposon mutagenesis evidence",
                        "value": {
                            "fitness_score": data["fitness_score"],
                            "statistical_test": "t-test",
                            "p_value": data["p_value"]
                        },
                        "supporting_data": {
                            "barcode_reads": 18234,
                            "replicates": 2,
                            "correlation": 0.92
                        }
                    }],
                    "provenance": {
                        "source": "RBTnSeq-BW25113",
                        "method": "Random barcode transposon sequencing"
                    }
                }
            }
        else:  # galK
            return {
                "association": {
                    "id": "rbtn_002c",
                    "type": "biolink:GeneToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["gene_id"],
                        "label": data["gene_name"],
                        "taxon": "NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113"
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "id": "OMP:0006023  # carbon source utilization phenotype",
                        "label": "carbon source utilization phenotype",
                        "extension": f"RO:0002503 towards {data['compound_id']}  # towards {data['compound_name']}"
                    },
                    "qualifiers": {
                        "phenotype_state": "PATO:0000462  # absent",
                        "growth_conditions": {
                            "medium": "OBI:0000079  # culture medium",
                            "medium_type": "M9 minimal salts",
                            "carbon_source": f"{data['compound_id']}  # {data['compound_name']}",
                            "concentration": data["concentration"]
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0007032  # transposon mutagenesis evidence",
                        "value": {
                            "fitness_score": data["fitness_score"],
                            "p_value": data["p_value"],
                            "threshold": "fitness < -2"
                        },
                        "quality_metrics": {
                            "mad_score": 0.234,
                            "fdr": 0.001
                        }
                    }],
                    "provenance": {
                        "source": "RBTnSeq-BW25113",
                        "method": "Tn-seq competitive fitness assay"
                    }
                }
            }
    
    def _generate_version_a_nichols(self, example_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Version A for Nichols examples."""
        data = example_data["data"]
        
        if data["gene_name"] == "recA":
            return {
                "association": {
                    "id": "nichols_001a",
                    "type": "biolink:ChemicalAffectsGeneAssociation",
                    "subject": {
                        "id": data["compound_id"],
                        "label": data["compound_name"],
                        "role": "antimicrobial agent"
                    },
                    "predicate": "biolink:affects",
                    "qualified_predicate": "biolink:causes",
                    "object": {
                        "id": data["gene_id"],
                        "label": data["gene_name"],
                        "taxon": "NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113"
                    },
                    "qualifiers": {
                        "phenotype": {
                            "process": "GO:0046677  # response to antibiotic",
                            "quality": "PATO:0001549  # increased sensitivity toward",
                            "substance": f"{data['compound_id']}  # {data['compound_name']}"
                        },
                        "experimental_conditions": {
                            "medium": "rich medium  # no specific ontology term for LB",
                            "medium_name": data["medium"],
                            "chemical_concentration": data["concentration"],
                            "temperature": {
                                "value": data["temperature"],
                                "unit": "UO:0000027  # degree Celsius"
                            },
                            "duration": data["duration"]
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0001563  # colony size measurement evidence",
                        "value": {
                            "s_score": data["s_score"],
                            "p_value": data["p_value"],
                            "fdr_adjusted": 0.02
                        },
                        "method_details": {
                            "plate_format": "384-well",
                            "normalization": "spatial correction applied",
                            "replicates": 3
                        }
                    }],
                    "provenance": {
                        "source": "Nichols et al. 2011",
                        "publication": "PMID:21609262",
                        "method": "Colony size measurement on agar plates"
                    }
                }
            }
        else:  # nuoA
            compound_with_ms = f"{data['compound_id']}; {self._get_modelseed_id(data['compound_id'])}"
            return {
                "association": {
                    "id": "nichols_002a",
                    "type": "biolink:ChemicalAffectsGeneAssociation",
                    "subject": {
                        "id": f"{compound_with_ms}  # {data['compound_name']}",
                        "label": data["compound_name"],
                        "role": "oxidizing agent"
                    },
                    "predicate": "biolink:affects",
                    "object": {
                        "id": data["gene_id"],
                        "label": data["gene_name"],
                        "pathway": "GO:0006979  # response to oxidative stress"
                    },
                    "qualifiers": {
                        "phenotype_components": {
                            "biological_process": "GO:0006979  # response to oxidative stress",
                            "quality": "PATO:0001997  # decreased viability",
                            "stress_type": "oxidative stress"
                        },
                        "mechanism": "damage to iron-sulfur clusters",
                        "conditions": {
                            "medium": "nutrient rich medium",
                            "specific_medium": data["medium"],
                            "stressor": f"{compound_with_ms}  # {data['compound_name']}",
                            "concentration": data["concentration"],
                            "temperature": "37°C"
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0001563  # colony size measurement evidence",
                        "value": {
                            "s_score": data["s_score"],
                            "p_value": data["p_value"],
                            "phenotype_strength": "strong"
                        },
                        "quality_control": {
                            "bias_corrected": True,
                            "edge_effects_removed": True
                        }
                    }],
                    "provenance": {
                        "source": "Chemical genomics screen",
                        "method": "High-throughput colony pinning"
                    }
                }
            }
    
    def _generate_version_c_nichols(self, example_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Version C for Nichols examples."""
        data = example_data["data"]
        
        if data["gene_name"] == "recA":
            return {
                "association": {
                    "id": "nichols_001c",
                    "type": "biolink:ChemicalAffectsGeneAssociation",
                    "subject": {
                        "id": data["compound_id"],
                        "label": data["compound_name"],
                        "role": "beta-lactam antibiotic"
                    },
                    "predicate": "biolink:affects",
                    "qualified_predicate": "biolink:causes",
                    "object": {
                        "id": data["gene_id"],
                        "label": data["gene_name"],
                        "taxon": "NCBITaxon:511145  # Escherichia coli str. K-12 substr. BW25113"
                    },
                    "qualifiers": {
                        "phenotype": "OMP:0000336  # beta-lactam resistance phenotype",
                        "phenotype_direction": "PATO:0000911  # decreased quality",
                        "experimental_conditions": {
                            "medium_type": data["medium"],
                            "compound": f"{data['compound_id']}  # {data['compound_name']}",
                            "concentration": data["concentration"],
                            "temperature": {
                                "value": data["temperature"],
                                "unit": "UO:0000027  # degree Celsius"
                            },
                            "duration": data["duration"]
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0001563  # colony size measurement evidence",
                        "value": {
                            "s_score": data["s_score"],
                            "p_value": data["p_value"],
                            "fdr_adjusted": 0.02
                        },
                        "method_details": {
                            "plate_format": "384-well",
                            "normalization": "spatial correction",
                            "replicates": 3
                        }
                    }],
                    "provenance": {
                        "source": "Nichols et al. 2011",
                        "publication": "PMID:21609262",
                        "method": "Colony size measurement"
                    }
                }
            }
        else:  # nuoA
            compound_with_ms = f"{data['compound_id']}; {self._get_modelseed_id(data['compound_id'])}"
            return {
                "association": {
                    "id": "nichols_002c",
                    "type": "biolink:ChemicalAffectsGeneAssociation",
                    "subject": {
                        "id": f"{compound_with_ms}  # {data['compound_name']}",
                        "label": data["compound_name"]
                    },
                    "predicate": "biolink:affects",
                    "object": {
                        "id": data["gene_id"],
                        "label": data["gene_name"],
                        "pathway": "GO:0006979  # response to oxidative stress"
                    },
                    "qualifiers": {
                        "phenotype": "OMP:0000173  # oxidative stress sensitivity",
                        "mechanism_note": "iron-sulfur cluster damage",
                        "stress_conditions": {
                            "medium": data["medium"],
                            "stressor": f"{compound_with_ms}  # {data['compound_name']}",
                            "concentration": data["concentration"],
                            "temperature": "37°C"
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0001563  # colony size measurement evidence",
                        "value": {
                            "s_score": data["s_score"],
                            "p_value": data["p_value"],
                            "category": "strong"
                        },
                        "quality_metrics": {
                            "corrections_applied": ["spatial", "edge"]
                        }
                    }],
                    "provenance": {
                        "source": "Chemical genomics screen",
                        "method": "HT colony pinning"
                    }
                }
            }
    
    def _generate_version_a_anl(self, example_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Version A for ANL examples."""
        data = example_data["data"]
        
        if data["strain_id"] == "ANL:562.61239":
            return {
                "association": {
                    "id": "anl_001a",
                    "type": "biolink:OrganismToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["strain_id"],
                        "label": data["strain_name"],
                        "taxon": "NCBITaxon:562  # Escherichia coli"
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "# Construct from multiple terms": None,
                        "biological_process": "GO:0046396  # D-galacturonic acid metabolic process",
                        "quality": "PATO:0000462  # absent",
                        "context": "growth phenotype"
                    },
                    "qualifiers": {
                        "assay_conditions": {
                            "base_medium": "OBI:0000079  # culture medium",
                            "medium_type": "chemically defined minimal medium",
                            "carbon_source": f"{data['compound_id']}  # {data['compound_name']}",
                            "carbon_role": "sole carbon source",
                            "temperature": "37°C",
                            "measurement_time": data["timepoint"]
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0001845  # cell population optical density evidence",
                        "value": {
                            "growth_call": data["growth_score"],
                            "od600_reading": data["od600"],
                            "decision_threshold": "OD600 > 0.2 at 24h = growth"
                        },
                        "normalization_data": {
                            "substrate_maximum": 0.683,
                            "substrate_minimum": 0.089,
                            "method": "min-max scaling per substrate"
                        }
                    }],
                    "provenance": {
                        "source": "ANL-SDL-48EcoliPhenos",
                        "method": "Growth/no-growth assessment",
                        "data_location": "Sheet2, Row 2"
                    }
                }
            }
        else:  # 562.61143
            compound_with_ms = f"{data['compound_id']}; {self._get_modelseed_id(data['compound_id'])}"
            return {
                "association": {
                    "id": "anl_002a",
                    "type": "biolink:OrganismToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["strain_id"],
                        "label": data["strain_name"],
                        "taxon": "NCBITaxon:562  # Escherichia coli"
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "# No GO term for salicin metabolism, use parent process": None,
                        "biological_process": "GO:0016137  # glycoside metabolic process",
                        "quality": "PATO:0000467  # present",
                        "substrate_specification": f"{compound_with_ms}  # {data['compound_name']}"
                    },
                    "qualifiers": {
                        "growth_conditions": {
                            "medium_base": "OBI:0000079  # culture medium",
                            "medium_description": data["medium"],
                            "carbon_source": f"{compound_with_ms}  # {data['compound_name']}",
                            "source_concentration": "standard test concentration",
                            "incubation": "37°C, 24h"
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0001845  # cell population optical density evidence",
                        "value": {
                            "growth_score": data["growth_score"],
                            "od600_measured": data["od600"],
                            "above_threshold": True
                        },
                        "replication": {
                            "technical_replicates": 2,
                            "biological_replicates": 1
                        }
                    }],
                    "provenance": {
                        "source": "ANL Environmental Collection",
                        "collector": "Aaron's Lab",
                        "assay_type": "Binary growth phenotype"
                    }
                }
            }
    
    def _generate_version_c_anl(self, example_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Version C for ANL examples."""
        data = example_data["data"]
        
        if data["strain_id"] == "ANL:562.61239":
            return {
                "association": {
                    "id": "anl_001c",
                    "type": "biolink:OrganismToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["strain_id"],
                        "label": data["strain_name"],
                        "taxon": "NCBITaxon:562  # Escherichia coli"
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "id": "OMP:0006023  # carbon source utilization phenotype",
                        "label": "carbon source utilization phenotype",
                        "extension": f"RO:0002503 towards {data['compound_id']}  # towards {data['compound_name']}"
                    },
                    "qualifiers": {
                        "phenotype_state": "PATO:0000462  # absent",
                        "assay_conditions": {
                            "medium": "OBI:0000079  # culture medium",
                            "medium_description": data["medium"],
                            "carbon_source": f"{data['compound_id']}  # {data['compound_name']}",
                            "temperature": "37°C",
                            "timepoint": data["timepoint"]
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0001845  # cell population optical density evidence",
                        "value": {
                            "binary_score": data["growth_score"],
                            "od600": data["od600"],
                            "threshold": "OD600 > 0.2"
                        },
                        "supporting_data": {
                            "max_for_substrate": 0.683,
                            "min_for_substrate": 0.089,
                            "normalization": "min-max"
                        }
                    }],
                    "provenance": {
                        "source": "ANL-SDL-48EcoliPhenos",
                        "method": "Phenotype array",
                        "location": "Sheet2, Row 2"
                    }
                }
            }
        else:  # 562.61143
            compound_with_ms = f"{data['compound_id']}; {self._get_modelseed_id(data['compound_id'])}"
            return {
                "association": {
                    "id": "anl_002c",
                    "type": "biolink:OrganismToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["strain_id"],
                        "label": data["strain_name"],
                        "taxon": "NCBITaxon:562  # Escherichia coli"
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "id": "OMP:0006023  # carbon source utilization phenotype",
                        "label": "carbon source utilization phenotype",
                        "extension": f"RO:0002503 towards {data['compound_id']}  # towards {data['compound_name']}"
                    },
                    "qualifiers": {
                        "phenotype_state": "PATO:0000467  # present",
                        "substrate_qualifier": f"{compound_with_ms}  # {data['compound_name']}",
                        "growth_medium": {
                            "type": "OBI:0000079  # culture medium",
                            "description": data["medium"],
                            "carbon_source": f"{compound_with_ms}  # {data['compound_name']}"
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0001845  # cell population optical density evidence",
                        "value": {
                            "binary_score": data["growth_score"],
                            "od600": data["od600"],
                            "confidence": "above threshold"
                        },
                        "quality_metrics": {
                            "technical_replicates": 2
                        }
                    }],
                    "provenance": {
                        "source": "ANL Collection",
                        "method": "Growth assessment"
                    }
                }
            }
    
    def _generate_version_a_biolog(self, example_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Version A for Biolog examples."""
        data = example_data["data"]
        
        if data["compound_name"] == "N-acetyl-D-glucosamine":
            compound_with_ms = f"{data['compound_id']}; {self._get_modelseed_id(data['compound_id'])}"
            return {
                "association": {
                    "id": "mg1655_001a",
                    "type": "biolink:OrganismToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["strain_id"],
                        "label": data["strain_name"],
                        "strain_type": "reference strain"
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "metabolic_process": "GO:0006044  # N-acetylglucosamine metabolic process",
                        "quality": "PATO:0000911  # decreased quality",
                        "growth_category": "partial  # intermediate phenotype"
                    },
                    "qualifiers": {
                        "test_conditions": {
                            "plate_system": "OBI:0400103  # microplate",
                            "plate_type": f"Biolog {data['plate']}",
                            "well_location": data["well"],
                            "test_substrate": f"{compound_with_ms}  # {data['compound_name']}",
                            "substrate_role": "sole carbon source",
                            "base_medium": "Biolog IF-0a  # proprietary medium"
                        },
                        "growth_level": "Low Growth"
                    },
                    "evidence": [{
                        "type": "ECO:0001091  # phenotype microarray evidence",
                        "value": {
                            "growth_category": "Low Growth",
                            "od_range": f"OD590 {data['od_range']}",
                            "measurement_time": data["timepoint"]
                        },
                        "category_definitions": {
                            "no_growth": "OD590 < 0.1",
                            "low_growth": "OD590 0.1-0.3",
                            "growth": "OD590 > 0.3"
                        }
                    }],
                    "provenance": {
                        "source": "Biolog PM analysis",
                        "platform": "Phenotype MicroArray",
                        "purpose": "wild-type reference"
                    }
                }
            }
        else:  # L-arabinose
            return {
                "association": {
                    "id": "mg1655_002a",
                    "type": "biolink:OrganismToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["strain_id"],
                        "label": data["strain_name"]
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "process": "GO:0019568  # L-arabinose metabolic process",
                        "quality": "PATO:0000462  # absent",
                        "note": "unexpected - MG1655 typically utilizes arabinose"
                    },
                    "qualifiers": {
                        "experimental_setup": {
                            "assay": "OBI:0001977  # growth assay",
                            "plate_id": data["plate"],
                            "well": data["well"],
                            "carbon_source": f"{data['compound_id']}  # {data['compound_name']}",
                            "medium_base": data["medium"],
                            "temperature": "37°C"
                        },
                        "result_flag": "requires_validation"
                    },
                    "evidence": [{
                        "type": "ECO:0001091  # phenotype microarray evidence",
                        "value": {
                            "growth_result": "No Growth",
                            "od590": data["od590"],
                            "validated": False
                        },
                        "concern": "Contradicts known MG1655 metabolism"
                    }],
                    "provenance": {
                        "source": "MG1655_Phenotype_Microarray_Table",
                        "method": "Biolog PM carbon plate",
                        "quality_note": "unexpected result"
                    }
                }
            }
    
    def _generate_version_c_biolog(self, example_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Version C for Biolog examples."""
        data = example_data["data"]
        
        if data["compound_name"] == "N-acetyl-D-glucosamine":
            compound_with_ms = f"{data['compound_id']}; {self._get_modelseed_id(data['compound_id'])}"
            return {
                "association": {
                    "id": "mg1655_001c",
                    "type": "biolink:OrganismToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["strain_id"],
                        "label": data["strain_name"],
                        "reference_strain": True
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "id": "OMP:0006023  # carbon source utilization phenotype",
                        "label": "carbon source utilization phenotype",
                        "extension": f"RO:0002503 towards {data['compound_id']}  # towards {data['compound_name']}"
                    },
                    "qualifiers": {
                        "phenotype_state": "PATO:0000911  # decreased quality",
                        "growth_category": "low growth",
                        "biolog_conditions": {
                            "plate_type": data["plate"],
                            "well": data["well"],
                            "substrate": f"{compound_with_ms}  # {data['compound_name']}",
                            "medium": "Biolog IF-0a"
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0001091  # phenotype microarray evidence",
                        "value": {
                            "category": "Low Growth",
                            "od_range": data["od_range"],
                            "timepoint": "48h"
                        },
                        "thresholds": {
                            "documented_by": "ECO:0000033  # author statement",
                            "categories": ["<0.1", "0.1-0.3", ">0.3"]
                        }
                    }],
                    "provenance": {
                        "source": "Biolog PM",
                        "reference_type": "WT baseline"
                    }
                }
            }
        else:  # L-arabinose
            return {
                "association": {
                    "id": "mg1655_002c",
                    "type": "biolink:OrganismToPhenotypicFeatureAssociation",
                    "subject": {
                        "id": data["strain_id"],
                        "label": data["strain_name"]
                    },
                    "predicate": "RO:0002200  # has phenotype",
                    "object": {
                        "id": "OMP:0006023  # carbon source utilization phenotype",
                        "label": "carbon source utilization phenotype",
                        "extension": f"RO:0002503 towards {data['compound_id']}  # towards {data['compound_name']}"
                    },
                    "qualifiers": {
                        "phenotype_state": "PATO:0000462  # absent",
                        "substrate_qualifier": f"{data['compound_id']}  # {data['compound_name']}",
                        "unexpected_result": True,
                        "assay_details": {
                            "plate_system": f"Biolog {data['plate']}",
                            "well": data["well"],
                            "medium": data["medium"],
                            "temperature": "37°C"
                        }
                    },
                    "evidence": [{
                        "type": "ECO:0001091  # phenotype microarray evidence",
                        "value": {
                            "result": "No Growth",
                            "od590": data["od590"],
                            "requires_validation": True
                        },
                        "note": "Unexpected for MG1655"
                    }],
                    "provenance": {
                        "source": "Biolog PM Table",
                        "quality_flag": "needs_review"
                    }
                }
            }
    
    def _generate_example(self, example: Dict[str, Any], dataset_name: str) -> str:
        """Generate both versions for a single example."""
        # Select appropriate generator based on dataset
        if "RBTnSeq" in dataset_name:
            version_a = self._generate_version_a_rbtseq(example)
            version_c = self._generate_version_c_rbtseq(example)
        elif "Nichols" in dataset_name:
            version_a = self._generate_version_a_nichols(example)
            version_c = self._generate_version_c_nichols(example)
        elif "ANL" in dataset_name:
            version_a = self._generate_version_a_anl(example)
            version_c = self._generate_version_c_anl(example)
        else:  # Biolog
            version_a = self._generate_version_a_biolog(example)
            version_c = self._generate_version_c_biolog(example)
        
        # Format as markdown
        output = f"### {example['title']}\n\n"
        output += "#### Version A: Without OMP (Current Ontologies Only)\n\n"
        output += "```yaml\n"
        output += self._format_yaml(version_a)
        output += "\n```\n\n"
        output += "#### Version C: With OMP (Hybrid Approach)\n\n"
        output += "```yaml\n"
        output += self._format_yaml(version_c)
        output += "\n```\n"
        
        return output
    
    def generate_document(self) -> str:
        """Generate the complete v6 document."""
        doc = []
        
        # Header
        doc.append("# Microbial Phenotype Ontology Annotations: Comparative Association Model\n")
        doc.append("**Version 6.0**\n")
        doc.append("## Overview\n")
        doc.append("This document demonstrates how to annotate microbial phenotype data using an association-based model, comparing two approaches:")
        doc.append("1. **Version A**: Using only currently available ontologies (CHEBI, GO, PATO, ECO, NCBITaxon, RO, UO, OBI)")
        doc.append("2. **Version C**: Using OMP (Ontology of Microbial Phenotypes) with standard ontologies (hybrid approach)\n")
        doc.append("**Key Changes in v6:**")
        doc.append("- Removed Version B (MCO-based) to reduce complexity")
        doc.append("- Corrected ENVO:01001059 (mock community culture) to OBI:0000079 (culture medium)")
        doc.append("- Simplified to two-version comparison for better clarity\n")
        doc.append("---\n")
        
        # Generate examples for each dataset
        for dataset in self.datasets:
            doc.append(f"## {dataset['name']}\n")
            for example in dataset["examples"]:
                doc.append(self._generate_example(example, dataset["name"]))
            doc.append("---\n")
        
        # Critical Assessment
        doc.append("## Critical Assessment: OMP Adoption and Implementation\n")
        doc.append("### 1. Ontology Maturity and Coverage\n")
        doc.append("**OMP Status:**")
        doc.append("- First release: 2014; Latest documented activity: OMPwiki edited March 2024")
        doc.append("- Currently adopted by: OMPwiki annotation system, various research publications")
        doc.append("- Limited adoption compared to GO (used in >100 biological databases)")
        doc.append("- Many specific pre-composed terms do not exist (e.g., individual carbon source utilization phenotypes)")
        doc.append("- Requires post-composition approach for many common phenotypes\n")
        
        doc.append("### 2. The GO/OMP Distinction\n")
        doc.append("**Key Differences:**")
        doc.append("- GO describes **gene product functions** (what proteins do)")
        doc.append("- OMP describes **observable organism phenotypes** (what happens to the organism)")
        doc.append("- Example: GO:0046396 describes the biochemical process of galacturonic acid metabolism, while OMP would describe the phenotype of being unable to grow on galacturonic acid\n")
        doc.append("This distinction aligns with established ontology design principles separating molecular functions from organism-level phenotypes.\n")
        
        doc.append("### 3. Implementation Comparison\n")
        doc.append("**Version A (Standard Ontologies Only):**")
        doc.append("- Requires 3-5 ontology terms to construct each phenotype")
        doc.append("- More verbose but uses well-established ontologies")
        doc.append("- May lack specificity for microbial phenotypes\n")
        doc.append("**Version C (With OMP):**")
        doc.append("- Single phenotype term + state qualifier")
        doc.append("- ~40% fewer terms needed")
        doc.append("- More concise and specific for microbial phenotypes")
        doc.append("- Requires understanding of post-composition patterns\n")
        
        doc.append("### 4. Recommendations\n")
        doc.append("1. **For New Projects:**")
        doc.append("   - Consider Version C (OMP hybrid) for cleaner annotations")
        doc.append("   - Establish clear post-composition guidelines")
        doc.append("   - Document all term usage patterns\n")
        doc.append("2. **For Existing Projects:**")
        doc.append("   - Version A may be more practical if already using standard ontologies")
        doc.append("   - Consider gradual migration to incorporate OMP terms\n")
        doc.append("3. **Best Practices:**")
        doc.append("   - Always include ECO evidence codes")
        doc.append("   - Use ModelSEED identifiers alongside CHEBI when available")
        doc.append("   - Document any unexpected or contradictory results")
        doc.append("   - Validate ontology terms before use\n")
        doc.append("---\n")
        
        # Summary
        doc.append("## Summary\n")
        doc.append("### Key Differences Between Approaches:")
        doc.append("1. **Version A (Without OMP)**: Requires multiple ontology terms to construct phenotypes; uses only well-established ontologies")
        doc.append("2. **Version C (With OMP)**: Single phenotype term + qualifiers; more concise but requires OMP adoption\n")
        doc.append("### Complexity Reduction:")
        doc.append("- Version C reduces term count by ~40% while maintaining semantic precision")
        doc.append("- Both approaches use the same evidence (ECO) and chemical (CHEBI) ontologies")
        doc.append("- Version C provides clearer phenotype representation for microbial data\n")
        doc.append("### Ontology Terms Used:")
        doc.append("- **NCBITaxon**: 562 (E. coli), 511145 (BW25113/MG1655)")
        doc.append("- **CHEBI**: 33830 (galacturonic acid), 17118 (galactose), 50505 (mecillinam), 16240 (H2O2; modelseed:cpd00025), 17814 (salicin; modelseed:cpd01030), 506227 (GlcNAc; modelseed:cpd00122,cpd27608), 30849 (L-arabinose)")
        doc.append("- **GO**: 0046396 (galacturonate metabolism), 0006012 (galactose metabolism), 0046677 (antibiotic response), 0006979 (oxidative stress), 0016137 (glycoside metabolic process), 0006044 (GlcNAc metabolism), 0019568 (arabinose metabolism), 0008150 (biological process)")
        doc.append("- **PATO**: 0000462 (absent), 0000467 (present), 0000911 (decreased quality), 0002303 (decreased rate), 0000396 (severe), 0001549 (increased sensitivity toward), 0001997 (decreased viability)")
        doc.append("- **ECO**: 0007032 (transposon mutagenesis), 0001563 (colony size), 0001845 (optical density), 0001091 (phenotype microarray), 0000033 (author statement)")
        doc.append("- **RO**: 0002200 (has phenotype), 0002503 (towards)")
        doc.append("- **UO**: 0000027 (degree Celsius)")
        doc.append("- **OBI**: 0000079 (culture medium), 0400103 (microplate), 0001977 (growth assay)")
        doc.append("- **OMP**: 0006023 (carbon source utilization phenotype), 0000336 (beta-lactam resistance phenotype), 0000173 (oxidative stress sensitivity)")
        
        return "\n".join(doc)


def main():
    """Main function to generate the document."""
    generator = OntologyV6Generator()
    document = generator.generate_document()
    
    # Write to file
    output_file = "ontology_annotation_examples_v6.md"
    with open(output_file, "w") as f:
        f.write(document)
    
    print(f"Successfully generated {output_file}")
    print(f"Document size: {len(document)} characters")


if __name__ == "__main__":
    main()