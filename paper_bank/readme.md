read in this order:

`` python get_papers.py`` 

will fetch all papers , matching keywords (ai,ml, cv, cogsci etc.). dump a csv


``python convert_json.py``

convert csv to json 


``python create_js.py``

convert json to js object. 

``index.html``

reads the js object, loads the data. 

supports ticking papers, and generating them.

---

todo: 
- [] support huggingface crawl, citation
- [] support arxiv crawl, citation
- [x] basic push
