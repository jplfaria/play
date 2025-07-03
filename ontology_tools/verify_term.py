#!/usr/bin/env python3
"""
Verify ontology terms and retrieve their definitions.
"""

import sys
from pathlib import Path
from typing import Optional, Dict, List
from ontology_parser import parse_ontology, OntologyTerm, OntologyIndex


class OntologyVerifier:
    """Verify ontology terms against loaded ontologies"""
    
    def __init__(self):
        self.ontologies: Dict[str, OntologyIndex] = {}
        self.ontology_paths = {
            'OMP': Path(__file__).parent.parent / 'ontologies' / 'omp.obo',
            'MCO': Path(__file__).parent.parent / 'ontologies' / 'mco.obo',
            'CHEBI': Path(__file__).parent.parent / 'ontologies' / 'chebi.owl',
            'ECO': Path(__file__).parent.parent / 'ontologies' / 'eco.owl',
            'ENVO': Path(__file__).parent.parent / 'ontologies' / 'envo.owl',
            'GO': Path(__file__).parent.parent / 'ontologies' / 'go.owl',
            'OBI': Path(__file__).parent.parent / 'ontologies' / 'obi-base.owl',
            'PATO': Path(__file__).parent.parent / 'ontologies' / 'pato-base.owl',
            'RO': Path(__file__).parent.parent / 'ontologies' / 'ro-base.owl',
            'UO': Path(__file__).parent.parent / 'ontologies' / 'uo-base.owl',
            'MODELSEED': Path(__file__).parent.parent / 'ontologies' / 'modelseed.owl'
        }
        
    def load_ontology(self, name: str, file_path: Optional[Path] = None):
        """Load an ontology file"""
        if file_path is None:
            file_path = self.ontology_paths.get(name)
            
        if not file_path or not file_path.exists():
            print(f"Warning: Ontology file not found for {name}: {file_path}")
            return
            
        print(f"Loading {name} from {file_path}...")
        terms = parse_ontology(str(file_path))
        
        index = OntologyIndex()
        index.add_terms(terms)
        self.ontologies[name] = index
        
        print(f"Loaded {len(terms)} terms from {name}")
        
    def load_all(self):
        """Load all configured ontologies"""
        for name in self.ontology_paths:
            self.load_ontology(name)
    
    def verify_term(self, term_id: str) -> Optional[OntologyTerm]:
        """Verify if a term exists in any loaded ontology"""
        # Extract ontology prefix
        if ':' in term_id:
            prefix = term_id.split(':')[0]
            
            # Check specific ontology
            if prefix in self.ontologies:
                term = self.ontologies[prefix].get_term(term_id)
                if term:
                    return term
                    
        # Check all ontologies
        for name, index in self.ontologies.items():
            term = index.get_term(term_id)
            if term:
                return term
                
        return None
    
    def get_chebi_modelseed_mapping(self, chebi_id: str) -> List[str]:
        """Get ModelSEED IDs that map to a CHEBI ID"""
        if 'MODELSEED' not in self.ontologies:
            return []
            
        modelseed_ids = []
        modelseed_index = self.ontologies['MODELSEED']
        
        # Search through all ModelSEED terms for CHEBI xrefs
        for term_id, term in modelseed_index.terms.items():
            # Check if this ModelSEED term has the CHEBI ID as xref
            if chebi_id in term.xrefs or f"CHEBI:{chebi_id}" in term.xrefs:
                modelseed_ids.append(term_id)
                
        return modelseed_ids
    
    def format_verification_result(self, term_id: str, term: Optional[OntologyTerm]) -> str:
        """Format verification result for display"""
        if term is None:
            return f"❌ {term_id}: NOT FOUND"
        
        result = f"✅ {term_id}: {term.name}"
        if term.definition:
            result += f"\n   Definition: {term.definition}"
        if term.is_obsolete:
            result += "\n   ⚠️  WARNING: This term is obsolete"
        if term.xrefs:
            result += f"\n   Cross-references: {', '.join(term.xrefs[:5])}"
            if len(term.xrefs) > 5:
                result += f" ... and {len(term.xrefs) - 5} more"
                
        return result


def main():
    """Main verification function"""
    if len(sys.argv) < 2:
        print("Usage: verify_term.py <term_id> [<term_id> ...]")
        print("Example: verify_term.py OMP:0005009 MCO:0000031")
        sys.exit(1)
    
    verifier = OntologyVerifier()
    verifier.load_all()
    
    print("\nVerification Results:")
    print("=" * 60)
    
    for term_id in sys.argv[1:]:
        term = verifier.verify_term(term_id)
        print(verifier.format_verification_result(term_id, term))
        
        # If it's a CHEBI term, also check ModelSEED mappings
        if term_id.startswith('CHEBI:'):
            modelseed_ids = verifier.get_chebi_modelseed_mapping(term_id)
            if modelseed_ids:
                print(f"   ModelSEED mappings: {', '.join(modelseed_ids)}")
        
        print()


if __name__ == "__main__":
    main()