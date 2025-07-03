#!/usr/bin/env python3
"""
Ontology parser for OBO and OWL files.
Extracts terms with IDs, labels, definitions, and cross-references.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Set
import xml.etree.ElementTree as ET
from collections import defaultdict


class OntologyTerm:
    """Represents a single ontology term"""
    def __init__(self, term_id: str):
        self.id = term_id
        self.name = ""
        self.definition = ""
        self.synonyms: List[str] = []
        self.xrefs: List[str] = []
        self.is_obsolete = False
        self.namespace = ""
        
    def __repr__(self):
        return f"Term({self.id}: {self.name})"


class OBOParser:
    """Parser for OBO format ontology files"""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.terms: Dict[str, OntologyTerm] = {}
        
    def parse(self) -> Dict[str, OntologyTerm]:
        """Parse OBO file and return dictionary of terms"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            current_term = None
            in_term = False
            
            for line in f:
                line = line.strip()
                
                # Start of new term
                if line == '[Term]':
                    in_term = True
                    current_term = None
                    continue
                
                # End of term section
                if line.startswith('[') and in_term:
                    in_term = False
                    continue
                
                if not in_term:
                    continue
                
                # Parse term fields
                if line.startswith('id:'):
                    term_id = line[3:].strip()
                    current_term = OntologyTerm(term_id)
                    self.terms[term_id] = current_term
                    
                elif current_term and line.startswith('name:'):
                    current_term.name = line[5:].strip()
                    
                elif current_term and line.startswith('def:'):
                    # Definition is quoted, extract it
                    match = re.match(r'def:\s*"([^"]*)"', line)
                    if match:
                        current_term.definition = match.group(1)
                        
                elif current_term and line.startswith('synonym:'):
                    # Synonym is quoted
                    match = re.match(r'synonym:\s*"([^"]*)"', line)
                    if match:
                        current_term.synonyms.append(match.group(1))
                        
                elif current_term and line.startswith('xref:'):
                    xref = line[5:].strip()
                    current_term.xrefs.append(xref)
                    
                elif current_term and line.startswith('is_obsolete:'):
                    current_term.is_obsolete = line[12:].strip().lower() == 'true'
                    
                elif current_term and line.startswith('namespace:'):
                    current_term.namespace = line[10:].strip()
        
        return self.terms


class OWLParser:
    """Parser for OWL format ontology files"""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.terms: Dict[str, OntologyTerm] = {}
        # Define namespaces commonly used in OWL ontologies
        self.namespaces = {
            'owl': 'http://www.w3.org/2002/07/owl#',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
            'obo': 'http://purl.obolibrary.org/obo/',
            'oboInOwl': 'http://www.geneontology.org/formats/oboInOwl#'
        }
        
    def parse(self) -> Dict[str, OntologyTerm]:
        """Parse OWL file and return dictionary of terms"""
        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            
            # Update namespaces from the document
            for prefix, uri in root.attrib.items():
                if prefix.startswith('{'):
                    continue
                self.namespaces[prefix] = uri
            
            # Find all class declarations
            for class_elem in root.findall('.//{http://www.w3.org/2002/07/owl#}Class'):
                about = class_elem.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about')
                if not about:
                    continue
                
                # Extract term ID from IRI
                term_id = self._extract_term_id(about)
                if not term_id:
                    continue
                
                term = OntologyTerm(term_id)
                
                # Get label (name)
                label_elem = class_elem.find('.//{http://www.w3.org/2000/01/rdf-schema#}label')
                if label_elem is not None and label_elem.text:
                    term.name = label_elem.text
                
                # Get definition
                def_elem = class_elem.find('.//{http://purl.obolibrary.org/obo/}IAO_0000115')
                if def_elem is not None and def_elem.text:
                    term.definition = def_elem.text
                
                # Check if obsolete
                deprecated_elem = class_elem.find('.//{http://www.w3.org/2002/07/owl#}deprecated')
                if deprecated_elem is not None and deprecated_elem.text == 'true':
                    term.is_obsolete = True
                
                # Get xrefs
                for xref_elem in class_elem.findall('.//{http://www.geneontology.org/formats/oboInOwl#}hasDbXref'):
                    if xref_elem.text:
                        term.xrefs.append(xref_elem.text)
                
                self.terms[term_id] = term
                
        except ET.ParseError as e:
            print(f"Error parsing OWL file: {e}")
            
        return self.terms
    
    def _extract_term_id(self, iri: str) -> Optional[str]:
        """Extract term ID from IRI"""
        # Handle different IRI formats
        if '#' in iri:
            return iri.split('#')[-1]
        elif '/' in iri:
            term_part = iri.split('/')[-1]
            # Convert underscore to colon for standard format
            if '_' in term_part:
                parts = term_part.split('_', 1)
                if len(parts) == 2:
                    return f"{parts[0]}:{parts[1]}"
            return term_part
        return None


class OntologyIndex:
    """Searchable index of ontology terms"""
    
    def __init__(self):
        self.terms: Dict[str, OntologyTerm] = {}
        self.name_index: Dict[str, Set[str]] = defaultdict(set)
        self.keyword_index: Dict[str, Set[str]] = defaultdict(set)
        
    def add_terms(self, terms: Dict[str, OntologyTerm]):
        """Add terms to the index"""
        self.terms.update(terms)
        
        # Build indices
        for term_id, term in terms.items():
            if term.is_obsolete:
                continue
                
            # Index by name words
            if term.name:
                words = term.name.lower().split()
                for word in words:
                    self.name_index[word].add(term_id)
                    
            # Index by definition words
            if term.definition:
                words = term.definition.lower().split()
                for word in words:
                    # Skip common words
                    if len(word) > 2:
                        self.keyword_index[word].add(term_id)
    
    def get_term(self, term_id: str) -> Optional[OntologyTerm]:
        """Get term by ID"""
        return self.terms.get(term_id)
    
    def search_by_name(self, query: str) -> List[OntologyTerm]:
        """Search terms by name"""
        query_words = query.lower().split()
        matches = None
        
        for word in query_words:
            word_matches = self.name_index.get(word, set())
            if matches is None:
                matches = word_matches.copy()
            else:
                matches &= word_matches
        
        if not matches:
            return []
            
        return [self.terms[term_id] for term_id in matches if term_id in self.terms]
    
    def search_by_keyword(self, query: str) -> List[OntologyTerm]:
        """Search terms by keywords in name or definition"""
        query_words = query.lower().split()
        all_matches = set()
        
        for word in query_words:
            # Search in names
            all_matches.update(self.name_index.get(word, set()))
            # Search in definitions
            all_matches.update(self.keyword_index.get(word, set()))
        
        return [self.terms[term_id] for term_id in all_matches if term_id in self.terms]


def parse_ontology(file_path: str) -> Dict[str, OntologyTerm]:
    """Parse an ontology file (OBO or OWL format)"""
    file_path = Path(file_path)
    
    if file_path.suffix == '.obo':
        parser = OBOParser(file_path)
    elif file_path.suffix == '.owl':
        parser = OWLParser(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")
    
    return parser.parse()


if __name__ == "__main__":
    # Test parsing
    import sys
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        terms = parse_ontology(file_path)
        print(f"Parsed {len(terms)} terms from {file_path}")
        
        # Show first 5 terms
        for i, (term_id, term) in enumerate(terms.items()):
            if i >= 5:
                break
            print(f"\n{term.id}: {term.name}")
            if term.definition:
                print(f"  Definition: {term.definition[:100]}...")