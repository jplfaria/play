#!/usr/bin/env python3
"""Verify all ontology terms from v5 report against source ontology files."""

import re
import os
from collections import defaultdict

# All unique ontology terms from the v5 report
terms = {
    'CHEBI': ['16240', '17118', '17814', '30849', '33830', '50505', '506227'],
    'ECO': ['0000033', '0001091', '0001563', '0001845', '0007032'],
    'ENVO': ['01001059'],  # This is the suspicious one
    'GO': ['0006012', '0006044', '0006979', '0008150', '0016137', '0019568', '0046396', '0046677'],
    'MCO': ['0000032', '0000881'],
    'NCBITaxon': ['511145', '562'],
    'OBI': ['0001977', '0400103'],
    'OMP': ['0000173', '0000336', '0006023'],
    'PATO': ['0000396', '0000462', '0000467', '0000911', '0001549', '0001997', '0002303'],
    'RO': ['0002200', '0002503'],
    'UO': ['0000027']
}

# Mapping of ontology prefixes to file names
ontology_files = {
    'CHEBI': 'chebi.owl',
    'ECO': 'eco.owl',
    'ENVO': 'envo.owl',
    'GO': 'go.owl',
    'MCO': ['mco.obo', 'mco.owl'],  # Check both formats
    'OBI': 'obi-base.owl',
    'OMP': ['omp.obo', 'omp.owl'],  # Check both formats
    'PATO': 'pato-base.owl',
    'RO': 'ro-base.owl',
    'UO': 'uo-base.owl'
}

base_path = '/Users/jplfaria/repos/play/ontologies'
results = defaultdict(lambda: {'found': [], 'not_found': []})

def check_term_in_file(filepath, prefix, term_id):
    """Check if a term exists in an ontology file."""
    full_term = f"{prefix}:{term_id}"
    # Also check underscore format for OBO files
    alt_term = f"{prefix}_{term_id}"
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            if full_term in content or alt_term in content:
                return True
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return False

def verify_terms():
    """Verify all terms against their ontology files."""
    
    # Skip NCBITaxon as we don't have that file
    for prefix, term_list in terms.items():
        if prefix == 'NCBITaxon':
            print(f"\nSkipping {prefix} - no local ontology file")
            continue
            
        print(f"\nChecking {prefix} terms...")
        
        if prefix not in ontology_files:
            print(f"  WARNING: No ontology file mapping for {prefix}")
            continue
            
        files = ontology_files[prefix]
        if not isinstance(files, list):
            files = [files]
            
        for term_id in term_list:
            found = False
            for filename in files:
                filepath = os.path.join(base_path, filename)
                if os.path.exists(filepath):
                    if check_term_in_file(filepath, prefix, term_id):
                        results[prefix]['found'].append(term_id)
                        found = True
                        break
            
            if not found:
                results[prefix]['not_found'].append(term_id)
                print(f"  ❌ {prefix}:{term_id} - NOT FOUND")

def print_summary():
    """Print summary of verification results."""
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60)
    
    total_found = 0
    total_not_found = 0
    
    for prefix in sorted(results.keys()):
        found = results[prefix]['found']
        not_found = results[prefix]['not_found']
        
        total_found += len(found)
        total_not_found += len(not_found)
        
        print(f"\n{prefix}:")
        print(f"  ✓ Found: {len(found)} terms")
        if found:
            print(f"    {', '.join([f'{prefix}:{t}' for t in found[:5]])}", end='')
            if len(found) > 5:
                print(f" ... and {len(found)-5} more")
            else:
                print()
        
        if not_found:
            print(f"  ✗ Not found: {len(not_found)} terms")
            for t in not_found:
                print(f"    - {prefix}:{t}")
    
    print(f"\n{'='*60}")
    print(f"TOTAL: {total_found} found, {total_not_found} not found")
    print(f"{'='*60}")
    
    # Special analysis for ENVO:01001059
    print("\nSPECIAL ANALYSIS: ENVO:01001059")
    print("-" * 40)
    print("This term uses a different ID format than typical ENVO terms.")
    print("Standard ENVO IDs use 8 digits (e.g., ENVO:00000001)")
    print("ENVO:01001059 appears to be malformed or from a different namespace.")
    
    # Search for correct culture medium terms
    print("\nSearching for correct 'culture medium' terms in ENVO...")
    envo_file = os.path.join(base_path, 'envo.owl')
    if os.path.exists(envo_file):
        with open(envo_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Look for culture medium related terms
            culture_terms = re.findall(r'(ENVO:\d{8})[^>]*>[^<]*culture[^<]*medium', content, re.IGNORECASE)
            if culture_terms:
                print("Found culture medium related terms:")
                for term in set(culture_terms[:5]):  # Show first 5 unique terms
                    print(f"  - {term}")

if __name__ == "__main__":
    verify_terms()
    print_summary()