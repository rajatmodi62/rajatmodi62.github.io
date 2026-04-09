---
layout: page
title: CV
permalink: /cv/
includelink: true
---


---

### **Summary**
A fifth year PhD candidate working on Efficient AI. In free time, I write [tech blogs](https://rajatmodi62.github.io/), give [talks](https://rajatmodi62.github.io/talks/), teach [cool stuff](https://www.youtube.com/@rajatmodi1573/playlists), and build scrapers to collect dataset-collection, [auto-summarize](https://github.com/rajatmodi62/ai-conf-abstract-generator/tree/main) abstracts of all conferences in one place. 

---

### **Education**

**University of Central Florida** | Orlando, United States  
*PhD in Computer Science, CRCV* | Aug 2021 -- June 2027  
Advisor: [Dr. Yogesh Singh Rawat](https://www.crcv.ucf.edu/person/rawat/), Lab Director: [Dr. Mubarak Shah](https://www.crcv.ucf.edu/person/mubarak-shah/)  


**University of Central Florida** | Orlando, United States  
*Masters in Computer Science (On the way)* | Aug 2021 -- Dec 2024  
On the way


**Netaji Subhas Institute Of Technology** | New Delhi, India  
*B.tech In Electronics And Communication Engineering* | Aug 2013 -- Aug 2017  
Advisor: [Dr. K.R. Parthasarathy](https://en.wikipedia.org/wiki/K._R._Parthasarathy_(probabilist)), [Dr. Harish Parthasarathy](https://www.quora.com/Why-is-someone-as-brilliant-as-Dr-Harish-Parthasarathy-still-teaching-in-NSIT)

---

### **A Few Interesting Directions (After PhD)**
How to build efficient AI architectures (LLMs/Transformers) that are:

  - **Faster to train**
  - **Run on edge devices in less than 1GB memory**
  - **Can learn even during “testing” (TTT) on one sample**
  - **Consume lower energy than a light bulb.**
  - **Work on-device in regions with limited internet**
  - **Don’t require storing hidden neural activities/gradient signals.**
  - **Can transfer knowledge between different architectures *faster than* knowledge distillation.**
  - **Capable of meta-learning their own hyperparameters and discovering network structure on the fly.**
  - **Use new kinds of local biologically plausible learning algorithms.**
  - **Explore beyond the Mcullough Pitts (MCP) neuron, (for eg, recent Artificial Kuramoto Oscillatory model inspired from the principles of synchronization in brain).**


---

### **Research Experience**

> * **Asynchronous Perception Machine** [[Paper]](https://arxiv.org/abs/2410.20535) [[Project]](https://rajatmodi62.github.io/apm_project_page/) [[Code]](https://github.com/) [[Patent]](https://drive.google.com/file/d/1lz2fZO29fTUk_fqDD2qVSIlQrzSsYQlp/view?usp=drive_link): In 2021, Geoffrey Hinton published [GLOM](https://arxiv.org/abs/2102.12627): whose abstract described it as ‘not a working system’, remained [unimplemented](https://www.technologyreview.com/2021/04/16/1021871/geoffrey-hinton-glom-godfather-ai-neural-networks/) for over three years. Key question was how to encode part-whole parse-tree like structures in a given input image (similar to unsyntactic constituency-parsing in NLP). Our key contribution was to provide the $1^{st}$ implementation of GLOM. Notably, we showed that a MLP can *also do* ImageNet-classification, and *generate* novel-images, a task previously attributed to CNNs/transformers. Achieved 10x inference speedup over ViT-B/16 and +2% accuracy over a VLM (OpenCLIP ViT-H) on ImageNet val set **(NeurIPS 2024 & US Patent-filed)**.

> * **Sky2Ground** [[Paper]](https://arxiv.org/abs/2410.20535): Developed first cross-view dataset (satellite, aerial, ground imagery) for 3-D reconstruction in outdoor scenes. Key observation was that models like [VGGT](https://arxiv.org/abs/2503.11651) etc, worsen in performance when fine-tuned jointly. Key contributions include 1) SkyNet: a model with a two-stream architecture explicitly processing different views, 2) a restricted-attention mechanism preventing aerial/ground from interacting with satellite, and maintain coherent feature-maps. 3) progressively- training by gradually sampling far away cameras. 4) curriculum-inspired strategy that reduces number of aerial views and forces the network to learn correspondances in satellite/ground. Helpful in cases like self-driving, drones for disaster-relief **(CVPR 2026)**.

> * **Layer Query Networks** [[Paper]](https://openreview.net/forum?id=6en51gFQT1): Test-Time-Training [TTT](https://arxiv.org/abs/1909.13231) remains slow because models rely on standard feed-forward mechanism: this means that layer $10$ cannot compute features before layer $9$ has finished processing. Proposed LQN: a student which can take *any* layer-index as input, and predict intermediate features of a teacher in time proportional to student's parameters, making it *independent* of teacher's depth. After training, this student is deployed on edge-devices for better efficiency. Similarly, [classical backpropagation](https://www.nature.com/articles/323533a0) requires neural net to be a directed-acyclic graph (DAG). However, [neuroscientific evidence](https://arxiv.org/abs/2212.13345) points to circular connections in our brain, where both lower/higher layers are connected with each other, forming ‘circles’ of neural-activity. Backpropagation cannot train it, since there is no explicit-order to compute gradients. Proposed a ‘recirculation’ procedure, that allows a neural net to take a $src/dest$ neuron, predict representation at $dest$, and present an ‘open-loop way' to still train it with backpropagation. Showed better results than networks making the DAG assumption. **(Under Review)**.

> * **Occluded Action Detection** [[Paper]](https://openreview.net/pdf?id=0cltUI2Sto) [[Poster]](https://drive.google.com/file/d/1OW0B9J6gdf7owtAzV9Ay21ZKfF7Jw1PQ/view?usp=drive_link) [[Code]](https://github.com/rajatmodi62/OccludedActionBenchmark): Here, we studied impact of realistic-occlusions in video object detectors, eg, our earlier work [VideocapsuleNet](https://arxiv.org/abs/1805.08162). We used capsule networks to learn occluder-centric representations, mask them, and reduce the effect of occlusions. Key contributions were: 1) Introducing the ‘Object Saturation Problem’: Memory of CNNs/Transformers grows with no of objects in the scene, whereas neural fields remain scale-invariant. 2) Providing first evidence of Hinton's islands of agreement, and receiving explicit permission to use his terminologies. **(NeurIPS 2023)**.

>  * **Test Time Training on videos** [[Paper]](https://openreview.net/pdf?id=0cltUI2Sto) [[Poster]](https://drive.google.com/file/d/1OW0B9J6gdf7owtAzV9Ay21ZKfF7Jw1PQ/view?usp=drive_link) [[Code]](https://github.com/rajatmodi62/OccludedActionBenchmark): Existing methods (TTT-Online) perform TTT on videos by adapting a image-based model for *each* incoming frame. Problem is (i) they maintain ‘overlapping’ sliding windows, leading to redundant compute. (ii) they do TTT on every frame, even if no changes across time. Key contributions (i) operate on only the frames which exit/enter the window, still encode temporal context (ii) a SSL-head to ‘anticipate’, if ‘adaptation’ is required. Key results: (i) stabilizes TTT for upto 3 hour long videos, whereas TTT-Online decays past $52 mins$. **(Under Review)**.

> * **Video Action Detection: Analyzing limitations and challenges** [[Paper]](https://openaccess.thecvf.com/content/CVPR2022W/VDU/papers/Modi_Video_Action_Detection_Analysing_Limitations_and_Challenges_CVPRW_2022_paper.pdf) [[Dataset]](https://github.com/rajatmodi62/OccludedActionBenchmark) [[Challenge]](https://tinyactions-cvpr22.github.io/): At CVPR, we organized the ActivityNet workshop. The key challenge was to perform action-detection on 4k videos (upto 2 mins long), consisting of multiple-actors, doing multiple-actions (UCF-MAMA). My contribution was (i) building the dataset used in this challenge (ii) make leaderboard (iii) manage participants. **(CVPR Workshops 2021)**.

> * **Video Foundation Models Survey** [[Paper]](https://arxiv.org/pdf/2405.03770) [[GitHub]](https://github.com/NeeluMadan/ViFM_Survey): Co-Authored the first survey on over 300+ video foundation models covering 14 tasks across generation, understanding, and multimodal reasoning. **(ACM Computing Surveys, Under Review)**.

---

> * **Segression** [[Paper]](https://drive.google.com/file/d/1r14Z_fgD1G_q5kTRR9-xzoVOILqs11yE/view?usp=sharing) [[Demo]](https://drive.google.com/file/d/1MnjRUVUWCTVJH9sSVD_VHhRLZ48xNw3F/view?usp=sharing) [[Code]](https://github.com/rajatmodi62/Segression): Given an image, the task was to segment regions which contain curved-text. Key challenge, was that existing-box based detectors cannot predict irregular curves like circles, ovals etc. Similarly, simple pixel-wise segmentation does not perform that well. Key contributions: (i) Designed a new gaussian-segmentation layer, which defines a gaussian for each pixel, learns to regress mean/ variance of the mixture model. Key results include SOTA on CTW dataset.

> * **IDD-Lite Semantic Segmentation Challenge** [[Code]](https://github.com/rajatmodi62/ncvpr-idd-lite-challenge) [[Leaderboard]](https://idd.insaan.iiit.ac.in/evaluation/ncv19-leader-board/): Implemented a Tiramisu + Deeplab backbone for semantic segmentation of KITTI scenes. Ranked **top 5** among 50+ teams at NCVPRIPG 2019.
---

### **Industry Experience**

**Athena Health** *Senior Member of Technical Staff* | 2021  
> * Built end-to-end ML pipeline using Transformers to predict insurance claim approval likelihood from EHR data. Key experience: i) handling sensitive-data responsibly (ii) discuss AI solutions with doctors.

**Samsung Research Institute** *Software Engineer* | 2017--2021  
> * **Smart TV Media Applications**: Developed high-performance media playback applications in **C++/Qt** for Tizen OS. Shipped to production across 50M+ Samsung devices globally. Optimized video pipeline for low-latency streaming.
* **Personalized Recommendation System** [[US Patent]](https://drive.google.com/file/d/1R4NKRI5nVjcgQI9czmf46MTH1qDG7ECj/view?usp=sharing): Invented GAN-based attribute selection method for personalized content recommendations. Designed sampling steering-vectors for controllable image-generation. **(US A1 Patent- filed)**.
* **Multimodal Context Fusion for Autonomous Systems** [[US Patent]](https://patents.google.com/patent/WO2022245134A1/en?inventor=rajat+modi): Designed cross-stitch neural network architecture for fusing multi-sensor inputs (vision, audio, text) into unified embeddings. **(US A2 Patent- filed)**.

---

### **Community Outreach**
> * (Served as volunteer) at NeurIPS to check badges of people entering poster-room
* (organized ML-collective lunch) at NeurIPS 2023, 2024 
* (organized workshop) on video-action detection at CVPR 2021
* (acted as food-server/ camera-recorder) for ACM ICPC semi-finals (nationals), 
* (showcased demos on real-time object detection, 3D reconstruction/rendering) at Orlando Spark festival to promote AI and STEM education in community
*  (pantry volunteer) to arrange donated food items onto shelves at UCF Knights Pantry. Also helped in weighing incoming-new food items.

---

### **Awards**
> * NeurIPS 2023 Scholar Award, UCF-CSRI Incentive Award 2024, UCF Presentation Fellowship 2023/2024, MLCollective GPU Grant, NCVPR-IG Travel Grant.

---

### **Skills**
> * **Research Areas:** Efficient AI, Representation Learning, Foundational Models, Capsule Networks, GLOM, Test-Time Training, Computer Vision, Object Detection, Image Segmentation 
* **Machine Learning:** LLMs, VLMs, Diffusion, Multi-Modality, CLIP
* **Languages & Frameworks:** Python, C++, PyTorch, Jax 
* **Production Tools:** MLOps, Docker, Model Deployment, Cloud Computing, AWS, GCP, Weights & Biases
* **Data Wrangling:** Preprocessing, Feature Engineering, NumPy, Pandas, Scikit-learn
