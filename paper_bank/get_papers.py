import pyalex
from pyalex import Works
import pandas as pd
import math

# 1. Configuration
pyalex.config.email = "rajatmodi62@gmail.com" 

def fetch_highly_cited_papers():
    print("Initializing query...")
    
    # OpenAlex IDs for AI, ML, Computer Vision, and Cognitive Science
    concept_ids = "C154945302|C119857082|C153294291|C169900460"

    # 2. Define the Query
    query = Works().filter(
        cited_by_count=">300",
        concepts={"id": concept_ids}
    ).sort(cited_by_count="desc")

    # 3. Get Totals
    try:
        total_works = query.count()
    except Exception as e:
        print(f"Failed to get count: {e}")
        return

    per_page = 200
    total_pages = math.ceil(total_works / per_page)
    
    print(f"Total works found: {total_works}")
    print(f"Total pages to fetch: {total_pages}")
    print("-" * 30)

    all_papers = []
    
    # 4. Use Paging
    pager = query.paginate(per_page=per_page, n_max=None)
    
    try:
        for i, page in enumerate(pager, start=1):
            for work in page:
                # Extract author names from the authorships list
                authorships = work.get("authorships", [])
                author_names = [auth.get("author", {}).get("display_name") for auth in authorships]
                # Filter out None values and join with semicolons
                authors_str = "; ".join(filter(None, author_names))

                all_papers.append({
                    "title": work.get("display_name"),
                    "authors": authors_str,
                    "citations": work.get("cited_by_count"),
                    "year": work.get("publication_year"),
                    "doi": work.get("doi"),
                    "url": work.get("id")
                })
            
            print(f"Progress: {len(all_papers)}/{total_works} papers | Page: {i}/{total_pages}", end="\r")
            
    except Exception as e:
        print(f"\nAn error occurred during fetch: {e}")

    # 5. Save to CSV
    if all_papers:
        df = pd.DataFrame(all_papers)
        # Reorder columns to put authors after title
        df = df[["title", "authors", "citations", "year", "doi", "url"]]
        df.to_csv("high_citation_ai_papers_with_authors.csv", index=False)
        print(f"\n\nSuccess! File saved with {len(df)} entries.")
    else:
        print("\nNo papers found matching criteria.")

if __name__ == "__main__":
    fetch_highly_cited_papers()