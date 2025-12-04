import boto3
from pathlib import Path
import re

s3 = boto3.client('s3')

response = s3.list_buckets()

md = "## Resources\n### Buckets\n\n"

for i in response.get('Buckets'):
    try:
        tags = s3.get_bucket_tagging(Bucket = i.get('Name'))
    except:
        tags = {}
    description = [j.get('Value') for j in tags.get('TagSet',[]) if j.get('Key') == 'description']
    print(len(description) > 0)
    md += f'#### {i.get('Name')}\n'
    md += f'##### Created\n * {i.get('CreationDate')}\n'
    if len(description) > 0:
        md += '##### Description\n'
        for j in description:
            md += f'  * {j}\n'

s3_path = Path(f"docs/aws/s3storage/index.md")
content = s3_path.read_text()

pattern = r'## Resources.*?(?=\n##|\n---|\Z)'
if re.search(pattern, content, re.DOTALL):
    # Replace existing section
    content = re.sub(pattern, md.strip(), content, flags=re.DOTALL)

s3_path.write_text(content)
print(f"  ✓ Updated S3 Documentation")