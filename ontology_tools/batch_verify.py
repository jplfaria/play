#!/usr/bin/env python3
"""
Batch verify all ontology terms in a document.
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
from collections import defaultdict
from verify_term import OntologyVerifier


def extract_terms_from_file(file_path: str) -> Dict[str, List[int]]:
    """Extract all ontology terms from a file with their line numbers"""
    terms = defaultdict(list)
    
    # Pattern to match ontology terms
    # Matches patterns like OMP:0005009, CHEBI:12345, etc.
    pattern = r'\b([A-Z]+:[0-9]+)\b'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            matches = re.findall(pattern, line)
            for match in matches:
                terms[match].append(line_num)
    
    return dict(terms)


def verify_document_terms(file_path: str) -> Tuple[Dict[str, bool], Dict[str, str]]:
    """Verify all terms in a document"""
    print(f"Extracting terms from {file_path}...")
    terms_with_lines = extract_terms_from_file(file_path)
    
    print(f"Found {len(terms_with_lines)} unique terms")
    
    # Load ontologies
    verifier = OntologyVerifier()
    verifier.load_all()
    
    # Verify each term
    verification_results = {}
    term_definitions = {}
    
    for term_id in sorted(terms_with_lines.keys()):
        term = verifier.verify_term(term_id)
        verification_results[term_id] = term is not None
        
        if term:
            term_definitions[term_id] = {
                'name': term.name,
                'definition': term.definition,
                'obsolete': term.is_obsolete
            }
    
    return verification_results, term_definitions, terms_with_lines


def generate_verification_report(
    file_path: str, 
    verification_results: Dict[str, bool], 
    term_definitions: Dict[str, str],
    terms_with_lines: Dict[str, List[int]]
) -> str:
    """Generate a detailed verification report"""
    report = []
    report.append(f"# Ontology Term Verification Report")
    report.append(f"\n**Document**: {file_path}")
    report.append(f"**Date**: 2025-01-03")
    report.append(f"**Total unique terms**: {len(verification_results)}")
    
    # Summary statistics
    verified_count = sum(1 for v in verification_results.values() if v)
    unverified_count = len(verification_results) - verified_count
    
    report.append(f"\n## Summary")
    report.append(f"- ✅ Verified: {verified_count} terms")
    report.append(f"- ❌ Not found: {unverified_count} terms")
    
    # Group by ontology
    by_ontology = defaultdict(list)
    for term_id, verified in verification_results.items():
        prefix = term_id.split(':')[0]
        by_ontology[prefix].append((term_id, verified))
    
    # Detailed results by ontology
    report.append(f"\n## Detailed Results by Ontology")
    
    for ontology in sorted(by_ontology.keys()):
        terms = by_ontology[ontology]
        verified = sum(1 for _, v in terms if v)
        total = len(terms)
        
        report.append(f"\n### {ontology} ({verified}/{total} verified)")
        
        # Show verified terms first
        verified_terms = [(t, v) for t, v in terms if v]
        if verified_terms:
            report.append("\n**Verified Terms:**")
            for term_id, _ in sorted(verified_terms):
                lines = terms_with_lines[term_id]
                line_str = f"lines {', '.join(map(str, lines[:5]))}"
                if len(lines) > 5:
                    line_str += f" and {len(lines)-5} more"
                
                term_info = term_definitions.get(term_id, {})
                name = term_info.get('name', '')
                obsolete = term_info.get('obsolete', False)
                
                status = "✅"
                if obsolete:
                    status = "⚠️ OBSOLETE"
                    
                report.append(f"- {status} `{term_id}`: {name} ({line_str})")
        
        # Show unverified terms
        unverified_terms = [(t, v) for t, v in terms if not v]
        if unverified_terms:
            report.append("\n**NOT FOUND:**")
            for term_id, _ in sorted(unverified_terms):
                lines = terms_with_lines[term_id]
                line_str = f"lines {', '.join(map(str, lines[:5]))}"
                if len(lines) > 5:
                    line_str += f" and {len(lines)-5} more"
                report.append(f"- ❌ `{term_id}` ({line_str})")
    
    # Special section for critical errors
    critical_errors = []
    
    # Check for OMP:0005009 specifically
    if 'OMP:0005009' in verification_results:
        if verification_results['OMP:0005009']:
            term_info = term_definitions.get('OMP:0005009', {})
            if 'acidophile' in term_info.get('name', '').lower():
                critical_errors.append(
                    "- **OMP:0005009** is 'acidophile' (pH phenotype) but document uses it as 'hexose utilization'"
                )
    
    if critical_errors:
        report.append("\n## ⚠️ CRITICAL ERRORS")
        report.extend(critical_errors)
    
    # Recommendations
    report.append("\n## Recommendations")
    
    if unverified_count > 0:
        report.append(f"\n### Terms Requiring Replacement:")
        
        # Group unverified terms by what they might be
        carbon_terms = []
        other_terms = []
        
        for term_id, verified in verification_results.items():
            if not verified:
                if term_id in ['OMP:0005040', 'OMP:0005001', 'OMP:0005135']:
                    if 'utilization' in str(terms_with_lines):
                        carbon_terms.append(term_id)
                    else:
                        other_terms.append(term_id)
        
        if carbon_terms:
            report.append("\n**Carbon utilization phenotypes:** Use post-composition approach")
            report.append("```yaml")
            report.append('id: "[PLACEHOLDER: carbon utilization phenotype]"')
            report.append('extension: "RO:0002503 towards CHEBI:xxxxx"  # specific compound')
            report.append("```")
        
        if other_terms:
            report.append("\n**Other phenotypes:** Search for appropriate terms or request new ones")
    
    return '\n'.join(report)


def main():
    """Main batch verification function"""
    if len(sys.argv) < 2:
        print("Usage: batch_verify.py <document_path>")
        print("Example: batch_verify.py ../ontology_annotation_examples_v4.md")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    # Verify all terms
    verification_results, term_definitions, terms_with_lines = verify_document_terms(file_path)
    
    # Generate report
    report = generate_verification_report(
        file_path, verification_results, term_definitions, terms_with_lines
    )
    
    # Save report
    report_path = Path(file_path).parent / f"{Path(file_path).stem}_verification_report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\nVerification report saved to: {report_path}")
    
    # Print summary
    verified_count = sum(1 for v in verification_results.values() if v)
    print(f"\nSummary: {verified_count}/{len(verification_results)} terms verified")


if __name__ == "__main__":
    main()