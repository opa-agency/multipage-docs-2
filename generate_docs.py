import os
import json
import re
from pathlib import Path

# Map folder names to their display titles and slugs
pages = {
    'installation': 'Installation',
    'understanding-caching': 'Understanding caching',
    'basics-of-time-travel': 'Basics of time-travel',
    'predicting-user-behavior': 'Predicting user behavior',
    'introduction-to-string-theory': 'Introduction to string theory',
    'the-butterfly-effect': 'The butterfly effect',
    'writing-plugins': 'Writing plugins',
    'neuralink-integration': 'Neuralink integration',
    'temporal-paradoxes': 'Temporal paradoxes',
    'testing': 'Testing',
    'compile-time-caching': 'Compile-time caching',
    'predictive-data-generation': 'Predictive data generation',
    'cacheadvance-predict': 'CacheAdvance.predict()',
    'cacheadvance-flush': 'CacheAdvance.flush()',
    'cacheadvance-revert': 'CacheAdvance.revert()',
    'cacheadvance-regret': 'CacheAdvance.regret()',
    'how-to-contribute': 'How to contribute',
    'architecture-guide': 'Architecture guide',
    'design-principles': 'Design principles',
}

docs_dir = Path('example/src/app/docs')
output = {}

for slug, title in pages.items():
    page_file = docs_dir / slug / 'page.md'
    if page_file.exists():
        with open(page_file, 'r') as f:
            content = f.read()
        
        # Extract frontmatter
        match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
        if match:
            frontmatter = match.group(1)
            body = match.group(2).strip()
            
            # Extract title from frontmatter
            title_match = re.search(r"title:\s*(.+)", frontmatter)
            extracted_title = title_match.group(1).strip() if title_match else title
            
            output[slug] = {
                'title': extracted_title,
                'slug': slug,
                'content': body,
                'sections': []
            }

# Write to file
with open('src/data/docs.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"Generated docs.json with {len(output)} pages")
