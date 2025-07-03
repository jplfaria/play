#!/usr/bin/env python3
"""
Search ontology terms by keyword.
"""

import sys
import argparse
from pathlib import Path
from typing import List
from ontology_parser import parse_ontology, OntologyTerm, OntologyIndex


def search_ontology(ontology_path: str, query: str, search_type: str = 'all') -> List[OntologyTerm]:
    """Search an ontology for terms matching the query"""
    print(f"Loading ontology from {ontology_path}...")
    terms = parse_ontology(ontology_path)
    
    index = OntologyIndex()
    index.add_terms(terms)
    
    print(f"Searching {len(terms)} terms for '{query}'...")
    
    if search_type == 'name':
        results = index.search_by_name(query)
    else:  # 'all' or 'keyword'
        results = index.search_by_keyword(query)
    
    return results


def format_search_results(results: List[OntologyTerm], max_results: int = 20) -> str:
    """Format search results for display"""
    if not results:
        return "No matching terms found."
    
    output = [f"Found {len(results)} matching terms:"]
    
    # Sort by term ID for consistent display
    results.sort(key=lambda t: t.id)
    
    # Display up to max_results
    for i, term in enumerate(results[:max_results]):
        output.append(f"\n{i+1}. {term.id}: {term.name}")
        if term.definition:
            # Truncate long definitions
            def_text = term.definition[:150]
            if len(term.definition) > 150:
                def_text += "..."
            output.append(f"   Definition: {def_text}")
        if term.is_obsolete:
            output.append("   ⚠️  WARNING: This term is obsolete")
    
    if len(results) > max_results:
        output.append(f"\n... and {len(results) - max_results} more results")
    
    return '\n'.join(output)


def main():
    """Main search function"""
    parser = argparse.ArgumentParser(description='Search ontology terms')
    parser.add_argument('--ontology', '-o', required=True, 
                       choices=['OMP', 'MCO', 'MODELSEED'],
                       help='Ontology to search')
    parser.add_argument('--search', '-s', required=True,
                       help='Search query')
    parser.add_argument('--type', '-t', default='all',
                       choices=['name', 'all'],
                       help='Search type: name only or all fields')
    parser.add_argument('--max-results', '-m', type=int, default=20,
                       help='Maximum number of results to display')
    
    args = parser.parse_args()
    
    # Determine ontology path
    ontology_paths = {
        'OMP': Path(__file__).parent.parent / 'ontologies' / 'omp.obo',
        'MCO': Path(__file__).parent.parent / 'ontologies' / 'mco.obo',
        'MODELSEED': Path('/Users/jplfaria/repos/KBaseCDMOntologies_back_up/KBase_CDM_Ontologies/ontology_data_owl/modelseed.owl')
    }
    
    ontology_path = ontology_paths.get(args.ontology)
    if not ontology_path or not ontology_path.exists():
        print(f"Error: Ontology file not found for {args.ontology}")
        sys.exit(1)
    
    # Perform search
    results = search_ontology(str(ontology_path), args.search, args.type)
    
    # Display results
    print("\n" + format_search_results(results, args.max_results))


if __name__ == "__main__":
    main()