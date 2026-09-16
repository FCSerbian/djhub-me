import csv
import os
from jinja2 import Template

# Get the exact folder where this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define absolute paths
CSV_PATH = os.path.join(BASE_DIR, "data", "master_gear.csv")
TEMPLATE_PATH = os.path.join(BASE_DIR, "templates", "page_template.md")
OUTPUT_DIR = os.path.join(BASE_DIR, "content", "posts")

def get_jog_analysis(brand, model_name, size_mm):
    """Generates dynamic SEO copy based on jog wheel size."""
    if size_mm >= 200:
        return f"Featuring full club-sized {size_mm}mm jog wheels, the **{brand} {model_name}** mimics the exact platter feel of professional CDJ-3000 setups, making it ideal for tight beatmatching and tech house transitions."
    elif size_mm >= 140:
        return f"Equipped with mid-sized {size_mm}mm jog wheels, the **{brand} {model_name}** offers a balanced middle ground between tactile control and gig portability."
    else:
        return f"With compact {size_mm}mm jog wheels, the **{brand} {model_name}** prioritizes ultimate portability over full-scale platter feel."

def main():
    # Force creation of content/posts directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Read the Jinja2 Markdown template
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = Template(f.read())

    # Parse CSV and generate pages
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        count = 0
        
        for row in reader:
            processed_data = {
                k: (v.upper() == 'TRUE' if v.upper() in ['TRUE', 'FALSE'] else v)
                for k, v in row.items()
            }
            
            size = int(processed_data['jog_wheel_size_mm'])
            processed_data['jog_analysis'] = get_jog_analysis(
                processed_data['brand'], 
                processed_data['model_name'], 
                size
            )

            rendered_md = template.render(processed_data)
            
            output_filename = os.path.join(OUTPUT_DIR, f"{processed_data['hardware_id']}.md")
            with open(output_filename, "w", encoding="utf-8") as out_file:
                out_file.write(rendered_md)
                
            count += 1

    print(f"SUCCESS: Generated {count} markdown files inside: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()