---
layout: post
comments: true
title:  "Modern GLOM: Canonical Locks that encode part-whole hierarchies"
description: ""
date:   2026-11-18 07:00:00
---

<div id="fig-1" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/celeba_hierarchy_preds.png" style="width: 100%; height: auto; display: block; margin: 0 auto;" alt="Figure 1">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 1.</b> Prediction of part-whole hierarchy of a face from Asynchronous Perception Machines. It contains 5 levels (L1-L5), going from finest to coarse grouping. The net generalizes to any unseen image.</p>
</div>

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">Abstract</span>

One of the challenges in representational learning is how to encode part-whole hierarchies in a neural net. Prior works rely on flattening tree-like structures into string-like sequences and training a sequence-to-sequence model via autoregression. While such a representation works for parse-trees in NLP, it is not entirely clear how to make it work for images. Thus, we propose a geometric primitive called canonical locks. The key idea is that parts/wholes can be modelled as higher-dimensional vectors ($$d \geq 4$$), and information can be encoded in their relative phase differences.

Inductively, the net consists of positionally-bound bottom-up and top-down neural fields, which drive each other to achieve a state of thermal equilibrium. Additionally, we show the existence of a few symmetrical configurations in the net. The computational iterations taken to break these symmetries depend on the angle between parts/wholes arranged on a disk (or more precisely a ring) in higher dimensions. It also appears to have connections to the psychological phenomenon of mental rotation.

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">1. The Problem of Part-Whole Hierarchies</span>

Most of the data we encounter in real world, can be modelled as a graph. For example, a molecule can be modelled as a graph of atoms, social networks can be modelled as graphs of people, and even the brain can be modelled as a graph of neurons. More importantly, such graphs often change dynamically according to the input. For eg, a face can be modelled as a graph of parts (eyes, nose, lips, etc), but the structure of this graph changes if the face is rotated or occluded. Similarly, most of the times, this structure is not known apriori, and must be inferred from the input.

This raises the question: how can a neural net encode part-whole hierarchies whose structure can change dynamically given a particular input? Indeed, the importance of this problem has been further articulated at great length  by Geoff Hinton in his 2021 proposal for the GLOM architecture\[[1](#ref-glom)\]. However, an implementation for GLOM has continued to remain elusive for our community.

Over the years several attempts have been made. For eg, \[[2](#ref-Modi2024OnOI)\] showed the existence of islands of agreement inside a video-transformer trained only on recognition\[[3](#ref-fan2021multiscale)\], which was a key theoretical representation in Hinton's GLOM. Recently, it was also suggested that global self attention does not allow part-whole hierarchies to emerge in a transformer and instead inverts them. In ICML 2026, \[[4](#ref-liu2026krause)\] presented Krause synchronization transformers, a form of constrained attention that  appears to promote the  cluster formation .

It was later realized that GLOM might require a new fundamental computational unit (different from McCulloch-Pitts neurons) which could promote cluster formation in a neural net. For eg, Takeru (and collaborators) \[[5](#ref-miyato2025artificial)\] invented a new kind of neuron called AKORN which relies on principles of neural synchronization. Similarly, Sindy \[[6](#ref-lowe2023rotating)\] presented the idea of rotating features as an alternative to slot based representations.

Concurrently, \[[7](#ref-modi2024asynchronous)\] demonstrated a potential implementation of GLOM using the asynchronous perception machine (APM), and a potential validation of GLOM's idea that percept is indeed a field. Of note was their invention of a geometrical operator called ‘the folding-unfolding operator’, which is analogous to the phenomenon of mental folding if one models the brain as an analog memory\[[8](#ref-hinton1979some)\].

Such progress over these past five years motivates us to ask ourselves (yet) again: Could the ideas promised in GLOM/APM be  made to somewhat work? Could what once seemed like a philosophy now lie firmly in our grasps? Indeed, there are three issues with APMs which prevent the philosophy from becoming a  reality. Notably:

- APMs only works for test-time-training. For purely supervised task, for eg, image classification, the internal representations of the net were severely collapsing. It was possible to average them and perform classification (using an external teacher's vision encoder), but attempts to do dense segmentation were met with utter failure.
- Furthermore, applying regularization to different cortical columns in APM to overcome collapse, applying contrastive learning on local patches of a image, or forcing the net to reconstruct masked regions of an image proved too slow to converge. To give an estimate, it took almost a day to train a cifar-10 classifier from scratch including the pre-training phase\[[9](#ref-garau2022interpretable)\].
- Later on it was realized that codistillation across locations from a strong teacher (eg Dinov2) got the training time down to a couple of hours \[[7](#ref-modi2024asynchronous)\]. While APM showed that the net could distill last layers of the teacher, the paper did not consider the subtle matters of part-whole hierarchies. There was also the obvious flaw, that it relied on a teacher, which in turn had to be trained at scale.
- A further assumption APM made was that internal layers of a transformer naturally encoded part-whole hierarchies. However, that quickly proved to be wrong.

To resolve some of the above issues, we propose the second generation of Asynchronous Perception Machines (APM/s). Of note is the ability of APM/s to learn only on one train sample (without any pre-training), and generalize to an entire test set with competitive accuracies. APM's also appear capable of encoding part-whole hierarchies, as well as finally doing dense-segmentation tasks. The decoded features are also robust to occlusions and masking.

This paper is an attempt to interpret GLOM's philosophy into engineering constraints which may in turn be implemented onto parallel distributed memories. A subsequent paper (currently under drafting) shall present our quantitative findings in a clear and succinct manner. Our sole purpose here is to  lay out a language of vector spaces in which one can begin to think about parts, wholes, their compositions, and decompositions. The terminology established here will be used in our subsequent papers.

We begin by discussing two ways of encoding part-whole hierarchies in neural nets.

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">2. Two ways of encoding part-whole hierarchies</span>

<div id="fig-2" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/background.png" style="width: 70%; height: auto; display: block; margin: 0 auto;" alt="Figure 2">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 2.</b> Two ways of encoding part-whole hierarchies.  (i) Encoding hierarchy inside the neural net; (ii) Encoding hierarchy outside the neural net. A darker color on the neural connection indicates a higher probability that a given part chooses a whole in a higher layer as its parent.</p>
</div>

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">2.1. Encoding hierarchy inside the net</span>

Fig[2](#fig-2)(i) illustrates a hierarchy with a sequence length of four, and two levels. An image can be fed through several attention layers (as in a ViT), without loss of spatial resolution. Each layer generates internal representations (marked as grey tokens).  One can encode part-whole hierarchies by taking a dot product between parts and wholes, and calculating attention weights (after squeezing logits through a softmax bottleneck). The resultant matrix can be forced to be the same as a graph's adjacency matrix. A similar coding scheme was used in capsules\[[10](#ref-sabour2017dynamic)\]. However, this raises several interesting issues:

- Routing issue: Each part $$p_i$$ must learn which whole $$w_j$$ it belongs to. For $$N$$ parts and wholes, this represents an $$N^2$$ assignment problem. All this routing information becomes noisy as data passes through different layers, which cannot be compensated for by dynamic routing[^1]. Stacking several such layers appears to make the problem worse.
- Different graphical structure across each layer: The adjacency matrix of part-whole relationships changes across different layers of the net. Encoding this dynamic evolving structure is more challenging than enforcing the same graphical structure through different attention layers\[[12](#ref-velivckovic2017graph)\].
- Collapse issue:  The representations produced in higher layers tend to become identical across different wholes, which means that the net cannot reliably encode multi-level hierarchies.

Typically it is possible to sweep these issues under the rug by pre-training a transformer-like net on vast swaths of data. The scale of data drowns out the natural noise of the system, and thus forces it to learn. At the moment, there are two philosophical schools of thought. Although the connectionist-symbolist war has been (somewhat) pacified and connectionists have won, a new kind of war has brewed in the shadows:

- On one side, we have Sutton's bitter lesson: It states that we should stop thinking about contents of minds in terms of simple ways like objects and symmetries.
- On the other side we have Geometrical school of thought: which says that  canonical frames, mental rotations, part-whole hierarchies, and equivariance ought to be a fundamental component of representational learning.

Indeed, geometrical school of thought is older, for it has been around since the time of Plato. The scaling school of thought is newer, for computing machines have only recently gotten faster. Things that are new, seem shiny, and move faster. Things that are old are heavier, and move slowly. The momentum thus is product of mass and velocity.

Now that the warring factions have been defined, we must continue on. But, you dear reader, must keep your mind open, and judgement neutral, for these are the times of peace. Those who render judgement too quickly are forced to choose one side, and thus only win with a 50% probability. Those who however negotiate peace, and GLOM together everything[^2], have a 100% percent chance of winning, for no man (or woman or transformer\[[13](#ref-Vaswani2017AttentionIA)\]) shall be left behind.

From a biological standpoint, we are still not able to explain why our minds are able to consume so less energy and exhibit vast abilities of generalization. The explanation that generalization emerges from scale does not explain how we as humans, in our limited lifespans, with our limited experiences, can generalize to vastly different scenarios.Indeed, it seems as though we are missing something fundamental.

Our results suggest that it is indeed possible to combine the benefits of scaling with that of faster search: by constraining the neural net by the laws of geometry. For this unification, we introduce this notion of encoding part-whole hierarchies ‘outside’ a neural net.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">2.2. Encoding hierarchy outside the net</span>

Fig [2](#fig-2)(ii) shows an alternate coding scheme. First, a neural net (with weights $$W_{e}$$) takes an image $$I$$, a location $$(i,j)$$ as input and produces an embedding. For a sequence of length $$L$$ and $$N$$ levels, there are $$N*L$$ embeddings. The neural net $$W_{e}$$ could be a  multi-layered perceptron with non-linear activations or a vision transformer (ViT). This kind of model has several advantages over the former:

- Embeddings at different locations $$(i,j)$$ can be computed in parallel, which makes it faster and possible to spread queries across multiple GPUs.
- For a given query $$(i,j)$$, all the neurons in $$W_{e}$$ are used to compute the embedding at that location. The binding is now done by a location-specific query.
- The amount of available neural hardware does not change and remains reusable  no matter how deep the hierarchy gets.

This coding scheme of encoding hierarchies in the latent space outside the net was  proposed by \[[1](#ref-glom)\], and later on inductively realized by \[[7](#ref-modi2024asynchronous)\]. However, it collapses when multiple levels of the hierarchy are considered. This leads us to the notion of canonical locks\[[14](#ref-hinton1981parallel)\].

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">3. Canonical locks for learning machines</span>

We begin with a toy problem. Next, we consider two kinds of computational systems: (i) static feed-forward inference; (ii) dynamical systems like a net of oscillators or continuous Ising machines. Inspired by \[[15](#ref-sejnowski1986learning)\], we isolate several symmetrical configurations in the net and demonstrate how they are resolved.  Simultaneously, we examine the connections between canonical locks and mental rotation.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">3.1. A toy problem</span>

<div id="fig-3" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/teaser.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 3">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 3.</b> (i) Face is at \(\mathtt{90}^{\circ}\) w.r.t lip; (ii) An alternative hypothesis where face is at \(\mathtt{45}^{\circ}\) w.r.t lip. Visually, there is no constraint about which of the angles \(\mathtt{45}^{\circ}/\mathtt{90}^{\circ}\) will be preferred.</p>
</div>

Fig [3](#fig-3) shows a face (whole) and one of its parts (nose). We can draw little arrows through them. The direction of each arrow governs its orientation. For example, in (i), the lip is at $$\mathtt{0}^{\circ}$$ and the face at $$\mathtt{90}^{\circ}$$. Similarly, in (ii), the relative angle between the face and lip is $$\mathtt{45}^{\circ}$$. This arrow can be a vector in $$\mathbb{R}^d$$. A neural net won't be able to learn anything useful if the relative angles between the whole and the part keep changing. It needs to be able to select one among infinitely many such angles. First, we present a way to visualize these vectors.

<div id="fig-4" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/sphere_disk.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 4">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 4.</b> A hypersphere analogy. Each disk is a great circle of the largest possible radius lying on the sphere.</p>
</div>

Fig [4](#fig-4) shows a hypersphere of unit radius. We imagine two disks on the surface of this hypersphere. One disk corresponds to the part vectors, and another to whole vectors. A vector connecting the center of the sphere with the circumference of the disk represents a part/whole vector. At any moment, we are allowed only ‘one’ vector per disk.

For example, the whole's vector can oscillate between one of the states like whole 1, whole 2, whole 3, etc. Similarly, the part's vector can oscillate between part 1, part 2, part 3, etc. There are infinite such states, and a vector can be in any of them at a given time. This representation then starts to bear resemblance to continuous Ising models\[[1](#ref-glom)\].

Please note that a vector possesses a magnitude $$r$$ and a phase $$\theta$$. This does not encode in which direction the vector is spinning (clockwise or anti-clockwise). For some tasks, it may be required, but for our toy problem, we will ignore this (subtle matter of chirality of the digital organism). For the rest of this paper, instead of looking at the sphere (which is tough  to draw), we will visualize the disks themselves.

<div id="fig-5" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/lock.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 5">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 5.</b> A 2D projection of the great circle taken from the hypersphere. Part's and Whole's arrows can be thought of as ‘needles’ oscillating in a compass.</p>
</div>

In Fig [5](#fig-5), the visualization now changes. We can think of the part and whole vectors as little needles lying on a circular compass. Any vector is free to choose any angle on the disk. However, if the part and whole are to be related to each other, they need to decide on a particular angle. This is what we now call a canonical lock\[[14](#ref-hinton1981parallel)\].

<div id="fig-6" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/canonical_lock.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 6">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 6.</b> A perfect canonical lock.</p>
</div>

In Figure [6](#fig-6), the part (lip) is perfectly locked to the whole (face) at an angle of $$\mathtt{30}^{\circ}$$. The left and right parts of the picture show these vectors ‘rotating’ on the disk in different configurations\[[6](#ref-lowe2023rotating)\]. At different instances of time, the part and whole vectors may be at different angles, but the relative angle between them remains constant. The job of a neural net is then to achieve such a ‘canonical lock’.

This form of representation raises several concerns:

- For a single pair of $$\left\langle \text{part}, \text{whole} \right\rangle$$ vectors, what angle should be chosen? This information is not readily available as supervision in the part-whole hierarchy.
- For many such pairs spanning the hierarchy, how can a neural net achieve multiple canonical locks simultaneously? Can simple gradient descent learn this?
- If the input vector is rotated (translated) slightly, the predicted representations of the net should also rotate (translate) in an equivariant manner. The canonical locks however should remain invariant.  How can we enforce both equivariance and invariance at the same time\[[16](#ref-cohen2016group)\], in particular, for the attention mechanism\[[17](#ref-hutchinson2021lietransformer), [13](#ref-Vaswani2017AttentionIA)\]?

We will try to answer these questions as we proceed in the paper. First, we wish to discuss static vs dynamical systems \[[6](#ref-lowe2023rotating), [18](#ref-akorn)\].

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">3.2. Static vs Dynamical systems</span>

We now distinguish between two kinds of recurrent nets in which part-whole hierarchies may be encoded:

- Static System: Models like Deep Equilibrium Models\[[19](#ref-bai2019deep)\] assume that when a recurrent net is run till infinity, it converges to a fixed representation. In such a system, the part and whole vectors might be fixed in both magnitude and direction once the fixed point is reached.
- Dynamical System: Here the vectors are given the freedom to rotate on the disk, but they are locked onto each other. Both magnitude and direction of the part and whole vectors may change, but the relative angle between them remains constant.

Intuition suggests that a static system is better: it is easy to detect when the fixed point is reached by comparing the differences among predicted representations across different timesteps of the recurrent net. However, it has been observed that the best downstream accuracy on a given task is not necessarily achieved at the fixed point. Furthermore, running such a net till infinity often leads to loss in performance, a phenomenon dubbed as ‘overthinking’.

Alternatively, a dynamical system appears to be more robust. The part and whole vectors keep on rotating forever, but retain their canonical locks. The earlier notion of ‘stopping’ the rotating vectors was an interesting  one: Once the machine reaches a potential solution, it stopped, and the obtained solution was verified by an external observer. If the solution was not correct, it was restarted again.

The uncomfortable decision for allowing the part and whole vectors to rotate for eternity has been made for the following reasons: (i) A system which oscillates can encode timing information as spike trains, which may be useful for tasks involving memory. (ii) Kepler's laws of planetary motion suggest that planets rotate around the sun in predictable orbits; (iii) planets at different distances from the sun sweep equal areas in equal intervals of time; (iv) learning algorithms which allow for conservation of angular momentum then become feasible.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">3.3. Information storage in dynamical systems</span>

In the forward-forward paper\[[20](#ref-hinton2022forward)\], it was suggested that vectors fed to a subsequent layer of a neural net must be normalized. The reason was that clamping the magnitude to unity results in loss of goodness, which forces the next layer of the net to learn better features. For some reason, separation in the phase space does not affect the downstream accuracy. This assumption makes sense for a static system.

The system of information organization discussed in Section [2.2](#22-encoding-hierarchy-outside-the-net) however is a dynamical system and differs because the last layer of $$W_e$$ is responsible for generating all the vectors in the hierarchy. It is just a linear layer, and thus free to generate any vector in the latent space, much like CLIP. This means that both the (relative) magnitude and phase of vectors in the hierarchy can be used to encode information.

A (complex) vector written in the Euler form of $$r e^{i \theta}$$ means that $$r$$ is just a scalar, whereas $$\theta$$ is multi-dimensional. This means that the phase of a vector can encode much more information than its magnitude. The original capsules attempted to encode the presence of an entity in the magnitude. However, this only makes sense if the vector represents a single entity. If an entity possesses multiple identities in superposition, such a representation quickly breaks down. This mysterious case manifests itself when a shape can be either a diamond or a tilted square at the same time.

Modelling internal representations as complex vectors \[[21](#ref-lowe2022complex)\] might allow visualizing different kinds of neural nets one might build, much akin to Smith charts found in electrical engineering. Notably, resistance and reactance can be encoded as a single representation called impedance. The impedance of a circuit of electrical elements is well defined. A neural net is indeed a circuit of parallel interconnected elements, and it should thus be possible to quantify the impedance. However, that matter is a digression, and not relevant to the current discussion. The minds of mortals can only focus on one thing at a time. Multi-head attention does not have those issues, and merely appears to be constrained by memory of the machine.

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">4. The Part-Whole Symmetry</span>

<div id="fig-7" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/hypersphere.png" style="width: 70%; height: auto; display: block; margin: 0 auto;" alt="Figure 7">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 7.</b> Some tough symmetrical configurations of parts/whole.</p>
</div>

Now, we consider the case where there is a single whole and multiple parts. For example, in Fig [7](#fig-7), there is one whole and three parts (part 1, part 2, part 3). For the purposes of symmetry, we will illustrate some of their toughest configurations. If we can achieve locking in these configurations, we may be somewhat reassured that the lock may be achieved in other configurations as well.

Figure (i) shows parts/whole arranged perpendicular to each other. If the whole's angle is assumed to be $$\mathtt{0}^{\circ}$$, then part 1 is at $$\mathtt{90}^{\circ}$$, part 2 at $$\mathtt{180}^{\circ}$$, and part 3 at $$\mathtt{270}^{\circ}$$. Let us assume that the whole vector is kept fixed and the part vectors are refined over several learning iterations. We also assume that the part vectors belong to the same object (for example, the lip). The question is: at what relative angle do we expect the part vectors to converge?[^3]

Intuition suggests that the net will choose between part 1, part 2, or part 3 randomly. Alternatively, if we average part 1, part 2, and part 3, the center of gravity lies on part 2. Therefore, we expect the canonical lock to be achieved at part 2. A deeper alternative is that two parts (part 1 and part 3) are at $$\mathtt{90}^{\circ}$$ with respect to the whole, whereas part 2 is at $$\mathtt{180}^{\circ}$$. Thus, there is a $$\frac{2}{3}$$ probability to lock onto part 1 or part 3, and a $$\frac{1}{3}$$ probability to lock onto part 2.

If we consider the entire system (including part/whole), the center of gravity lies at the origin. One may suspect that the part vector will become the zero vector itself. However, that means that the part vector will have zero magnitude and could possess any direction, rendering any notion of canonical locks useless[^4].

An alternate configuration is shown in (ii). Here all parts coincide with the whole. Intuition suggests that the canonical lock is at $$\mathtt{0}^{\circ}$$. However, this might pose an issue: if all the parts and their wholes are identical vectors, there is no relative angle between them. Thus, the net does not encode any meaningful hierarchical structure.

Till now we have talked about vectors lying on spheres/disks. However, they are typically high-dimensional vectors, sometimes extending up to 2048 dimensions. Recent conversations \[[18](#ref-akorn)\] seem to suggest that it is indeed very difficult to achieve a perfect lock in such high dimensions ($$d\geq\mathtt{4}$$), since the volume of the space is just too high.

While nature does (occasionally) respect symmetry, breaking those symmetries leads to new abilities in the machine. Biological organisms, for example, reproduce and break entropy's law by self-organizing into complex structures. When a zygote reproduces and spreads out in a sphere, a mechanism to break the ring symmetry is what makes our legs look different from our heads. Similarly, we may want our learning machines to break the symmetries and achieve these canonical locks.

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">5. The Part-Whole Asymmetry</span>

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">5.1. Breaking the anti-symmetry</span>

<div id="fig-8" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/circular_symmetry.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 8">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 8.</b> Resolving the anti-symmetry</p>
</div>

In Fig [8](#fig-8), we generate 4 vectors which are mutually orthogonal to each other. There is 1 whole, and 3 part vectors. Part 1 and Part 3 are perpendicular to the whole, but part 2 is at 180 degrees. This center of gravity is at 180 degrees with respect to the whole. The assumption here is that the whole vector is held constant, while the part vectors are refined over several learning iterations. The input part vectors are passed through a connectionist net, and the output part vectors are averaged to yield the final part output. We measure the cosine similarity between this part output and the whole vector.

We plot the mean cosine similarity of each part output with respect to the whole. The x-axis is the number of iterations, the y-axis is the mean cosine similarity. We can see that the mutual cosine loss falls to 0 in around 30 iterations. Put simply, given a whole vector, the net discovers an internal representation where all the part outputs are orthogonal to the whole. Note that the net broke this symmetry in $$\mathtt{30}$$ iterations.

An argument may be raised on the grounds that if one samples any two vectors randomly in higher dimensions, they are likely to be orthogonal to each other. What we then claim as a canonical lock is just a random coincidence.

The counterargument is that one can build a machine which can be programmed to satisfy any explicit geometric constraints, be they orthogonal or not. If a bunch of vectors are to be arranged in any pattern in the higher dimensional space, the machine shall learn to arrange them.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">5.2. Breaking the collapsed symmetry</span>

<div id="fig-9" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/collapsed_symmetry.png" style="width: 70%; height: auto; display: block; margin: 0 auto;" alt="Figure 9">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 9.</b> Resolving the collapsed symmetry.</p>
</div>

In Fig [9](#fig-9), we generate 4 vectors which are identical in both magnitude and direction. There is 1 whole, and 3 part vectors. As before, the net settles on identical part vector outputs which are orthogonal to the whole. This means, even in a state of collapse (when part and whole vectors are identical), the net is able to break symmetry and achieve a lock.

A crucial difference between both cases is the time it takes to break symmetry. In Fig[8](#fig-8), it took 30 iterations, whereas in Fig [9](#fig-9), it took around 60 iterations. Intuitively, the second case was more difficult since there was no relative structure in part vectors to begin with. This suggests that nature may have built in some configurations that the system may prefer.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">5.3. A Linear Model for Predicting the Time It Takes to Break Symmetry</span>

An argument made in psychology is that the time it takes for humans to recognize a shape depends on the angle at which they are viewing the shape and the angle of the natural canonical axis they tend to favor\[[23](#ref-palmer1981cannonical)\]. Can a neural net follow similar behavior? A demonstration may indeed be performed.

<div id="fig-10" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/225_degree.png" style="width: 50%; height: auto; display: block; margin: 0 auto;" alt="Figure 10">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 10.</b> Fitting a linear line model to fundamental symmetries. x axis is no of iterations. y axis is the angle of center of gravity of part vectors w.r.t whole vector.</p>
</div>

Consider as before, the case of anti-symmetry in Fig[8](#fig-8) where parts 1, 2, 3 have a center of gravity at 180 degrees with respect to the whole, breaking symmetry at 30 iterations. Similarly, consider the case of collapsed symmetry in Fig [9](#fig-9), where the center of gravity is at 0 degrees with respect to the whole, breaking symmetry at 60 iterations. Thus, we get two pairs of coordinates (0,60), (180,30). We can plot them on a line.

Let us now generate another configuration where parts and wholes are arranged such that the center of gravity is at 225 degrees with respect to the whole. Looking at the linear plot shown in [10](#fig-10), we predict it should take about 22.5 iterations to break symmetry (rounded as needed). Running a connectionist net with such a configuration results in the graph shown on the next page (Fig[11](#fig-11)).

<div id="fig-11" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/225_actual.png" style="width: 75%; height: auto; display: block; margin: 0 auto;" alt="Figure 11">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 11.</b> Any random configuration of part-whole vectors on the disk appears to cut \(y=0\) multiple times. Each x-axis coordinate (eg,  40, 60) may be thought of as a fundamental symmetry.</p>
</div>

In Fig [11](#fig-11), we can see the blue line cut $$0$$ y-intercept at around 22.5, which is the condition when cosine loss tended to zero, indicating perfect lock. Subsequently, we see the oscillation getting damped, cutting the axis again at iteration 40 and 60. Recall that iteration $$\mathtt{60}$$ was the case of collapsed symmetry. One unexplained mode is at iteration 40. Looking back at Fig [10](#fig-10), we see that 40 iterations correspond to a center of gravity of 120 degrees. One way to generate this configuration is as below:

<div id="fig-12" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/120_deg_symm.png" style="width: 35%; height: auto; display: block; margin: 0 auto;" alt="Figure 12">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 12.</b> The tri-fold symmetry</p>
</div>

Figure [12](#fig-12) above represents what we internally have code-named as tri-fold symmetry because all parts are at 120 degrees with respect to each other. The perpendicular components of part 2 and part 3 along the y-axis cancel out, and the center of gravity is at 180 degrees with respect to the whole. However, the true degree of freedom tends to be a bit different.

We can imagine a plane perpendicular to this paper, and rotate this figure by 120 degrees three times to get the same shape each time. We call this figure of $$3$$ as a degree of freedom. Dividing the total plausible angle of rotation (360 degrees) by the degree of freedom (3), we get 120 degrees as the smallest angle of rotation that preserves the shape: It is interesting to note that the machine prefers the axis along which this degree of freedom is maximum out of all other axes. We must precisely note what this means. If we want to represent a canonical frame by means of numbers, then all canonical frames look identical. There is nothing in the representation which tells us the degree of freedom the machine possesses given the choice of a canonical frame.

A way by which the machine can rotate itself along several axis, estimate the degree of freedom along each, and then select the axis along which the degree of freedom is maximum can thus be invented. And it is indeed more elegant than brute-forcing along all the plausible axis. The answer is simply attaching a learnable token to the representation. As long as we break symmetry, the machine shall know what to choose.

The frame with the highest degree of freedom can yield the same object with the least amount of rotation. Therefore, it is easier for it to learn and only requires minor adjustments to the synaptic weights. However, the number of possible objects for which such higher degrees of freedom exist is very low. For example, the shape of a sphere. This means that the sphere is a Gaussian which has folded all information about the organism and only contains the blueprint for its replication.

This suggests that when the machine is modelling minor rotations of a sphere, it has to be sensitive enough to change its weights to great precision. However, simulating the weights on a digital machine (of 128 bits as of 2026AD) does not offer that precision. It therefore gets really tempting to move onto  qubit/analog kind of continuous Ising machines.

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">6. Existence of Other Symmetries</span>

The three symmetries (anti-symmetry, collapsed symmetry, and tri-fold symmetry) presented above can thus be thought of as fundamental symmetries of learning machines.

Any other configuration appears to oscillate between these fundamental symmetries before finally settling on the solution (a.k.a. equilibrium). The key argument here is that these symmetries emerge even when the net is given random input, initialized with many random weights, and run across multiple seeds.

The assumption till now is that vectors of parts/wholes lie on a disk. There may exist some other configurations where these parts/wholes lie on separate manifolds, giving rise to many more higher-dimensional symmetries. It is very tempting to think of them as fundamental particles the physicists (and their supercool colliders) like to discover every now and then.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">6.1. Synchrony vs Asynchrony across levels of the part-whole hierarchy</span>

Next, we examine the proposal on GLOM\[[1](#ref-glom)\]. Specifically, we are concerned with how information might be represented in the hierarchy. We consider two cases: (i) Synchrony across levels; (ii) Asynchrony across levels.

<div id="fig-13" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/synchrony.png" style="width: 50%; height: auto; display: block; margin: 0 auto;" alt="Figure 13">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 13.</b> Synchrony across levels results in loss of information.</p>
</div>

Fig[13](#fig-13) shows two levels of hierarchy. The lower level has two parts (shown as pink arrows), and the higher level has two wholes (shown as blue arrows). The problem with this case is that vectors across different levels of the hierarchy are synchronized, i.e. they are all at zero relative angle w.r.t each other, and thus collapsed. This means that there is no useful information encoded in this configuration.

<div id="fig-14" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/asynchrony.png" style="width: 50%; height: auto; display: block; margin: 0 auto;" alt="Figure 14">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 14.</b> A successful case of encoding information in a hierarchy.</p>
</div>

Alternatively, consider Fig[14](#fig-14). Here, all the parts in the lower level point in the same direction. Similarly, all the wholes in the higher level point in the same direction. However, the relative angle between the parts and wholes is non-zero. This means that useful information has been encoded into the hierarchy. The key takeaway is that relative angles between vectors of different levels of the hierarchy must be non-zero.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">6.2. Relaxing the orthogonality of coordinate frames</span>

We now consider this notion of coordinate frames as in \[[24](#ref-hinton1976using)\].

<div id="fig-15" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/arm.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 15">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 15.</b> An arm analogy. Representing coordinate frames with three layers[<a href="#ref-hinton1977relaxation">22</a>]</p>
</div>

Please consider the human stick diagram. It shows two body parts, a fore-arm and an arm. Several observations may be made:

- There are two coordinate frames, one for the fore-arm and another for the arm.
- Each coordinate frame has an orthogonal basis. For example, the fore-arm has a basis $$W_1$$ and $$P_{1}$$, and the arm has a basis $$W_2$$ and $$P_{2}$$.
- The relative angles between two coordinate frames are encoded as relative angles between the normal vectors of the coordinate frames. For example, the angle between $$W_1$$ and $$W_2$$ is $$\theta$$.

It is possible to model this hierarchy by using a three-layered neural net. One can encode a transformation from $$P_1$$ to $$W_1$$, then from $$W_1$$ to $$P_2$$, and finally from $$P_2$$ to $$W_2$$. Note that the only non-orthogonal canonical lock is between $$W_1$$ and $$P_2$$. The other canonical locks are all at $$90^{\circ}$$, which means that they should be easier to achieve. The non orthogonal lock will take some beating to achieve.

<div id="fig-16" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/alternate_arm.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 16">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 16.</b> Representing coordinate frames with a single layer.</p>
</div>

<div id="fig-17" style="text-align: center; margin: 20px 0;">
  <div style="display: inline-block; border: 1px solid #000; padding: 12px; background: #fff; width: 40%;">
    <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/stick_symmetry.png" style="width: 100%; height: auto; display: block; margin: 0 auto;" alt="Figure 17">
  </div>
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 17.</b> A human stick figure showing the hierarchy of body parts. Each part has chosen its own canonical axis. Similarly, the part corresponding to the left hand knows that its whole is the left forearm. We want a neural net to learn similar hierarchy.  Figure gratefully inspired from [<a href="#ref-hinton1977relaxation">22</a>].</p>
</div>

There are issues with this kind of representation. The neural net is wasteful, because to model two coordinate frames, we require three layers. In principle, it is possible to model the hierarchy with just one layer.

The idea is to just model the relative angle between the normal vectors of the two coordinate frames, and discard the vectors along the body parts ($$P_1, P_2$$) entirely. This reduction in the amount of neural hardware may be termed as ‘relaxing the orthogonality of coordinate frames’.

A canonical lock between a between a single part and a single whole can then result in canonical locks across the entire hierarchy. Fig[17](#fig-17) shows a human stick figure, where each part has chosen its own canonical axis. Similarly, the part corresponding to the left hand knows that its whole is the left forearm. We want a neural net to learn similar hierarchy within itself.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">6.3. Preserving the orthogonality of relaxed coordinate frames</span>

Let us now imagine that the angle between $$W_1$$ and $$W_2$$ is $$60^{\circ}$$. This raises a curious problem: forcing a neural net to achieve this canonical lock will consume a lot of energy.
For simplicity, we will call the vectors $$W_1$$/$$W_2$$ as $$v_1$$ and $$v_2$$. Next, we shall  borrow a theorem from higher-dimensional linear algebra.

<div id="thm-1" style="background: rgba(128,128,128,0.10); border: 0.5px solid rgba(128,128,128,0.40); border-radius: 2px; padding: 6px 12px; margin: 16px 0;">
<p><b>Theorem 1</b> (Near-Orthogonality of Random Vectors on a hypersphere)<b>.</b> <em>Let \(v_1, v_2\) be independent random vectors drawn uniformly from a unit hypersphere \(S^{d-1} \subset \mathbb{R}^d\). Then for every \(\epsilon \in (0,1)\),</em></p>
\[
\mathbb{P}\left(|\langle v_1, v_2 \rangle| \geq \epsilon\right) \;\leq\; 2\exp\!\left(-\frac{d\epsilon^2}{4}\right) + \exp\!\left(-\frac{d}{16}\right).
\]
<p><em>In particular, for any fixed \(\epsilon &gt; 0\), this probability decays exponentially fast in \(d\); equivalently, \(\langle v_1, v_2\rangle = O_P(1/\sqrt{d})\), so two independently and uniformly sampled directions in \(\mathbb{R}^d\) become orthogonal with overwhelming probability as \(d \to \infty\)</em> <span style="float: right;">&#9632;</span></p>
</div>

The above theorem, although obvious in hindsight , does carry several interesting implications for connectionism.

- As the dimensionality of a vector increases, it can encode a lot more information. In principle, a single vector could carry information about an entire scene, and it is possible to decode the entire part-whole hierarchy from it.
- Most of the vectors in a higher-dimensional space are orthogonal to each other.

A neural net in which the vectors are almost orthogonal to each other will need many computational iterations to drive the internal canonical locks to $$60^{\circ}$$. It may be possible to adjust the weights of the net in one rapid update, but that would require making changes to the perceptron convergence procedure.

An alternate way is not to fight the fundamental laws of physics and try to force structure in the net through iterations of gradient descent. Rather, one must embrace the fact that the vectors ‘will be’ orthogonal. Submitting to the laws of nature must happen, if we are to crack the energy barrier in which the current generation of intelligent machines is trapped. Biological beings however repeatedly beat the laws of entropy. Soon after their passing, however, the flow of energy gets reversed.

This leads one to the question: Is there a way to arrange these vectors together into some sort of geometric structure, so that a combination of them could encode part-whole hierarchies?

The motivation stems from trying to resolve Fodor's arguments against connectionism\[[25](#ref-fodor1988connectionism)\]. It has been shown that symbols (characters) and their combinations (words) can be encoded as vectors in neural nets. Similarly, image pixels can be encoded as vectors. However, it is not clear how pixels form objects, for there is no definition of what an object is. In the words of David Marr: ‘what is an object?’
It merely depends on the granularity at which one is observing them.

This further suggests that neural hardware must be designed to abstract higher-order mental functions at different levels of granularity, for eg, representations at level one could also serve as level ten at some other scale. After all, we have no trouble in looking up at the galaxy of stars, or the world of atoms in a microscope. The universe is countless at different scales, which might suggest that there is no informational bottleneck.

If one is willing to accept the premise that neural nets operate on higher vector spaces, two arguments resurface:

- How do vectors arrange themselves to form concepts like ‘face’, ‘lip’, ‘nose’ etc. in a higher-dimensional space? Is there a geometric structure which can be imposed on these vectors, so that they can encode such part-whole hierarchies? If there are infinite concepts, how can they be coded onto finite neural hardware?
- How are concepts represented as distributed patterns? Is it possible to learn them as geometric primitives, whose combination can lead us to the formation of new concepts on the fly? Is it possible to capture these primitives as continuous probability distributions one might sample from? The structure of these hierarchies should be changed dynamically based on the input data vector, and not be fixed a priori.

Indeed, these arguments allow us to probe whether the brain relies on a universal form of grammar of symbols\[[26](#ref-chomsky1965aspects)\]. Does an organism get born with such a universal grammar (or somehow inherit it through the genetic code from its parents), or does it learn it from the environment as it grows up\[[27](#ref-hinton1987learning)\]? If the latter were true, then an organism isolated from the environment should not be able to learn any language.

An alternate possibility is that the language transmitted by the parent is a universal language of syntax, and entities which satisfy it lead to the formation of higher-level concepts, which allows one to encode causal constraints. A rule that A:B gives A+B should hold no matter what A and B are.

This suggests that if a neural net wishes to express the rule of A:B$$\rightarrow$$ A+B in its weights, it needs to adjust the configurations of its internal part-whole vector hierarchy accordingly. A and B are then input data vectors presented to the bottom of the net. The part-whole hierarchy operates on these vectors for certain iterations, undergoes a settling/relaxation process, and then produces the final answer. This then brings us to the notion of a part-whole grammar.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">6.4. The part-whole grammar</span>

<div id="fig-18" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/lattice.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 18">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 18.</b> Lattice of a learning machine. Solid lines are connections already formed. Dotted lines are connections currently being formed. The lattice is equivariant around the origin.</p>
</div>

Fig [18](#fig-18) reveals a model of how representations may arrange themselves as a hierarchical structure inside a higher-dimensional space. The machine operates in a few phases.

First, the internal representations of the net are purely random and have no structure. Given a problem of interest, the net starts to grow a lattice-like structure in a higher-dimensional space. The primitive building blocks of this lattice are vectors and disks. The actual learning mechanism is how to arrange these vectors and disks in a particular configuration, so that they can represent an appropriate part-whole hierarchy.

The picture shows us one such lattice being formed. The solid lines represent connections which have already been formed, whereas the dotted lines represent connections which are currently being formed. Kindly note that the lattice is equivariant around the origin, which means that if the entire lattice is rotated around the origin, it will still represent the same part-whole hierarchy.

The knowledge of a neural net is the set of weights that produce a particular lattice configuration. Intuitively, for a given problem of interest (or an algorithm), there is a unique lattice that encodes the ‘solution’ to that problem. For multiple problems, the net will need to learn multiple lattices. This means that the neural computation may proceed  in the following manner:

- First, a symbolic algorithm (like sorting an array) is presented to the net as a way to solve a problem.
- The net encodes it as a mere lattice configuration in the higher-dimensional space. An indicator that a lattice has been formed is that the part-whole vectors achieve perfect canonical locks, which can be measured by looking at the internal energy of the net between two successive iterations. Forming the lattice should require no example of the problem being solved.
- Once the lattice is formed, the net can then be presented with a problem instance (like an array of numbers to be sorted). The net will then use the lattice configuration to solve the problem. The solution will be produced as a vector which can be eventually decoded into a symbolic answer.
- The structure of the lattice does not change with different instances of the problem

This notion of a field of lattice reduces neural nets to mere hardware that implements higher-order symbolic logic. This implies that connectionism has to bow down to the rigor of formal logic, for it still cannot solve problems of binding and compositionality properly, and remains a mere statistical correlation machine. However, there is no need to feel ashamed of that, because there may be a way to achieve peace between the two schools of thought. To understand the differences, we
must first properly partition the problems we might wish our dear computing machines to solve for us.

<u>Problems whose algorithms exist:</u> Let us imagine the problem of sorting numbers. A sequence of steps to achieve the task is already known. If one is given the algorithm, he does not need any instance of the problem to ‘learn it’. What one desires is the ability to encode the algorithm in weights of the distributed memory of the net. Theoretically, such a neural net should be able to solve any instance of the problem, of any length, and be perfectly generalizable, without any need for pre-training. Here, the algorithm is pre-known and the neural net is merely a compiler to implement higher-order functions of the symbolic mind.

<u>Problems of pattern recognition whose algorithms ought to exist but cannot be written in symbols</u>: There might be a class of problems like face recognition, whose exact algorithm or a hand-crafted representation is not known. Here, the machine is simply shown instances of the problem, and learns from it. If a perfect algorithm exists, the machine forms a suitable lattice configuration in its higher-dimensional space that remains equivariant across computational iterations.

<u>Problems whose algorithms provably don't exist:</u> There might be a class of problems  whose exact algorithm is not known, and it is also provably impossible to write one. Here, the connectionist theory reduces to a mere approximation and cannot provide an exact solution.

<u>Problems whose algorithms might exist but we are not so sure:</u>  A neural net may be able to relax into a perfect solution very quickly for every instance of the problem which is easy to verify. Even if it does, how does one merely look at the weights of the net and mathematically prove that it has indeed learnt the algorithm? This seems difficult because testing a machine on infinite instances of the problem (in our lifetimes) is not the same as proving it has learnt a true universal algorithm. Given two infinite dimensional spaces, each of whose elements have a precise bijection with the other, it is possible to come up with a neural operator. If one can prove that a specific neural operator exists for a particular problem, then there might be some solace\[[28](#ref-kovachki2023neural)\].

<u>A canonical view of algorithms:</u> Men of logic tend to describe algorithms as a set of  rules one ‘ought to follow’ to arrive at a correct answer to the given problem. A proof of an algorithm is thus the mathematical construct that the algorithm is indeed correct no matter what the input. However, mathematics itself is a human construct, and it makes sense to define algorithms in a language of symbols.

It also does not appear to explain intuition, and self-belief: if an intelligent being is guided by an internal set of principles which it cannot describe in symbols, but merely as a ‘state of being’, how can symbols even describe the actions the being takes?  A higher principle of selflessness, appears to overcome what one's external environment tells him to do. The means to suppress one's natural instincts in favor of internal principles might thus be a desirable property to possess.

Even if we accept the view that the brain itself runs same sort of symbolic algorithms (as a higher order mental function) to arrive at an identical solution, we cannot explain this phenomenon of intuitive inference. Perhaps, it means that rules are not the only way to get to the correct answer. Perhaps, the brain ‘glides’ in a continuous vector space by the means of intuition and arrives at the answer.

A digital machine does require the laws of boolean algebra to function. However, an analog machine can simply operate on continuous voltages and currents to arrive at an answer.  A learning machine thus built on canonical locks  does not need to follow symbolism: one may arrive at the answer by running the machine for a long time, and then verifying the answer at the output terminals.

There is no way to verify it, unless one can build a geometric proof that each possible symbolic algorithm maps to a lattice configuration, and shows that the net reaches that exact same configuration with a perfect zero error. In this view, one substitutes symbols with lattices of mental imagery. It  also prevents the requirement for feeding the net with a symbolic program in the first place, for the weights of the net themselves are the algorithm.

This leads one to confront a very uncomfortable question: If families of algorithms map to families of part-whole hierarchies, how does one know the ground truth of the higher dimensional  part-whole vectors (for supervision) in the first place? The answer is that one does not, he merely learns it. One has to abandon the notion of proof. It is still possible to invent a connectionist net to relax to a perfect solution, but one cannot prove it. Perhaps, it is a black box of uncertainty: the moment you poke it, it will give you an answer, but whether that answer is what it actually computed may differ.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">6.5. Reading the wholes of a part in the hierarchy</span>

Assuming that the internal representations of the net can form part-whole hierarchies, we will now describe the mechanisms of how to ‘read’ which parts belong to which wholes.

<div id="fig-19" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/sp_sw_bottom_up.png" style="width: 35%; height: auto; display: block; margin: 0 auto;" alt="Figure 19">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 19.</b> A single part sending a vote to the higher level whole</p>
</div>

Fig[19](#fig-19) shows a single part vector (lip) getting transformed by bottom-up neural net $$W_{f}$$ to yield the whole vector (face). An initial idea was to connect all the parts (in lower level) to all the wholes (in higher level). The actual connectivity pattern could be either convolutional or attention, but for the context of this discussion, we shall assume the operation in a single window where the net attends to elements in a scene (for eg, inside a single kernel of a CNN, or the entire global attention operation).

<div id="fig-20" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/capsule_vote.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 20">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 20.</b> The buggy capsule-voting mechanism</p>
</div>

Fig[20](#fig-20) describes the issues with capsule-style EM/attention based routing. Here, (on the right), we show two separate parts (lip and ear) producing their own votes for the whole (face). If the two parts produced the same whole vector (after transformation), and prediction matched  the original whole vector, then the parts were said to ‘agree’ to that whole. However, that form of representation quickly ran into two troubles (which could not be resolved by training at scale):

- There was only one whole (and hence one neuron) representing the face. This meant that both lip/ear had to ‘route’ information to the same higher level neuron. Given $$N$$ parts, $$M$$ wholes, the routing mechanism needs to encode $$N\times M$$ decisions, a constraint which just expects too much from  gradient descent.
- The transformation matrix $$W_f$$ was assumed to be $$4 \times 4$$ dimensional. The decision was made taking inspiration from computer graphics: a 3D object can be rotated/translated from one point to another using a $$4 \times 4$$ transformation matrix.

The notion of a $$4 \times 4$$ transformation matrix is however deeply flawed. First, it restricts the transformation matrix to be low dimensional, which means that the quality of representation the net learns is sub optimal. Second, even if we assume it to be higher dimensional $$d \geq 4$$, it quickly becomes infeasible to visualize the $$d \times d$$ matrix.

Finally, even if its dimensions are reduced to $$4 \times 4$$ (using tsne, pca etc), the learnt representation does not ensure that the correct indices in the matrix encode rotation/translation, and that the last row is purely homogeneous. One then requires a clever alignment mechanism (like Umeyama's) to see what the net has actually learnt which just takes too much compute. The idea that the brain does inverse graphics albeit powerful does not mean that the brain is actually doing those transformations in a three dimensional world.

<div id="fig-21" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/glom_vote.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 21">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 21.</b> Eliminating part-to-whole transformation matrices</p>
</div>

The key realization is to eliminate the transformation matrix, and instead assume an alternate representation: one that relies on replication of the whole vector across all the parts. Fig[21](#fig-21) shows one such case: there are now two blue vectors at the level of the whole (face). One can contrast it with the capsule representation in Fig[20](#fig-20), which contained only one vector for the whole (face).

The way one measures whether two parts belong to the same whole has now changed: We can directly compare the two face vectors with themselves, and see if they are close to each other. Assuming a more general case of $$M$$ whole vectors, one can assign membership to $$K$$ clusters by using a k-means algorithm.

The key differences of this form of representation are  :

- There is no more routing. There is a separate whole vector being predicted for every part vector.
- The value of K is not known before decoding. Clustering happens after the recognition has happened. There is no need of bounding boxes or Hungarian matching.

This is different from slots which require the number of slots to be known a priori, and rely on competitive learning to latch correct slot onto correct object. This results in an issue where a slot latches onto more than one object and needs to be split using some heuristic or learnt rule.Our mechanism  however is gratefully inspired from neural-synchronization\[[18](#ref-akorn)\].

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">6.6. Brain as a generative model</span>

Earlier, Boltzmann machines proposed the idea that a common set of neurons could be used for both perception and generation. For a given input process, a bottom-up process generates recognition  and a top-down generative process provides a feedback loop of neural activity. Similarly, the brain appears to have both feedforward and feedback connections which operate asynchronously.

Taken together, both these systems iterate over several iterations, to reach what one may now term as ‘islands of agreement’\[[1](#ref-glom), [7](#ref-modi2024asynchronous)\]. This idea also inspired the invention of Helmholtz Machines. Later, AlexNet popularized the effectiveness of a simple bottom-up approach, because it was simpler to implement and train. The notion of a top-down feedback loop was abandoned[^5] and the ideas of a purely feedforward approach (trained at scale) became pre-dominant.

Our implementation of canonical locks is closer in spirit to   GLOM\[[1](#ref-glom)\] (than transformers)  as follows:

- There are now separate bottom-up and top-down neural nets which can synchronize each other.
- We have removed the notion of singular fixation: i.e. the assumption that a neural net can look at an input image only once.

Next, we  consider how issues with the bottom-up net (in the original GLOM formulation) were resolved\[[1](#ref-glom)\]. This has connections to mean field theory. Later, we   will consider the full architecture of the model.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">6.7. Issues with the mean field approximation</span>

Let us consider how the part-whole hierarchy may be formed inside the net.

<div id="fig-22" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/bu_hierarchy_formation.png" style="width: 50%; height: auto; display: block; margin: 0 auto;" alt="Figure 22">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 22.</b> A two level hierarchy showing formation of whole vectors from part vectors</p>
</div>

Fig [22](#fig-22) shows a two-level hierarchy. The lowest level consists of two pink vectors belonging to a single part (nose). We are concerned with how to decide the higher level vector of the face (marked by a question mark). Mean field approximation suggests that the higher level vector could be computed as the average of the lower level vector. This results in the picture shown in Fig [23](#fig-23).

<div id="fig-23" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/bu_collapse.png" style="width: 50%; height: auto; display: block; margin: 0 auto;" alt="Figure 23">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 23.</b> Representational collapse in mean field approximation</p>
</div>

Fig [23](#fig-23) shows the collapse of the hierarchy due to mean field approximation. This is not desirable since this is the same as [13](#fig-13), which means that no amount of useful information can be encoded into the hierarchy.

<div id="fig-24" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/bu_rotate.png" style="width: 50%; height: auto; display: block; margin: 0 auto;" alt="Figure 24">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 24.</b> An alternate solution involves bottom-up net \(W_f\)</p>
</div>

The solution is simply to ‘transform’ all the lower level part vectors into higher level whole vectors using a bottom-up neural net with weights $$W_f$$. This results in several properties:

- The bottom up net $$W_{f}$$ is shared across all part vectors at a particular level.
- One must guarantee that $$W_f\neq \mathbf{I}$$ in order to prevent collapse in Fig [23](#fig-23).

This is easy to guarantee if the bottom-up net is a multi-layered neural net with non-linearities and  initialized with random weights (as long as weights of different layers are not identical). Next, we introduce Asynchronous Perception Machines (APM's). The key upgrade over \[[7](#ref-modi2024asynchronous)\] is that we have now implemented canonical locks.

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">7. Asynchronous Perception Machines</span>

<div id="tab-1" style="margin: 20px 0; overflow-x: auto;">
<p style="font-size: 0.9em; text-align: center;"><b>Table 1.</b> Mathematical notation used in the rest of this paper</p>
<table style="width: 100%; font-size: 0.85em; border-collapse: collapse; border-top: 2px solid currentColor; border-bottom: 2px solid currentColor;">
<thead>
<tr style="border-bottom: 1px solid currentColor;"><th style="text-align: left; padding: 4px;">Symbol</th><th style="text-align: left; padding: 4px;">Description</th><th style="width: 0.3cm;"></th><th style="text-align: left; padding: 4px;">Symbol</th><th style="text-align: left; padding: 4px;">Description</th></tr>
</thead>
<tbody>
<tr><td style="padding: 4px;">\(\mathbf{x} \in \mathbb{R}^{H \times W \times C}\)</td><td style="padding: 4px;">Input image</td><td></td><td style="padding: 4px;">\(W_{f}= \{W_{f,1}, \dots, W_{f,L}\}\)</td><td style="padding: 4px;">All bottom-up weight matrices</td></tr>
<tr><td style="padding: 4px;">\(l \in \{1, \dots, L\}\)</td><td style="padding: 4px;">Current level in the hierarchy, \(L\) total levels</td><td></td><td style="padding: 4px;">\(W_{b}= \{W_{b,1}, W_{b,2}, \dots, W_{b,L}\}\)</td><td style="padding: 4px;">All top-down weight matrices</td></tr>
<tr><td style="padding: 4px;">\((i, j,l)\)</td><td style="padding: 4px;">Spatial grid coordinates at level \(l\)</td><td></td><td style="padding: 4px;">\(W_{outer}= \{W_{e}, W_{f}\}\)</td><td style="padding: 4px;">Outer-loop weights</td></tr>
<tr><td style="padding: 4px;">\(f_e(\cdot)\)</td><td style="padding: 4px;">Encoder</td><td></td><td style="padding: 4px;">\(W_{inner}= \{W_{b}\}\)</td><td style="padding: 4px;">Inner-Loop weights</td></tr>
<tr><td style="padding: 4px;">\(g_{f,l}(\cdot)\)</td><td style="padding: 4px;">Bottom-up Net at level \(l\)</td><td></td><td style="padding: 4px;">\(\text{Opt}_{outer}\)</td><td style="padding: 4px;">Optimizer for \(W_{outer}\)</td></tr>
<tr><td style="padding: 4px;">\(W_{f,l}\)</td><td style="padding: 4px;">Bottom-up Net's weights</td><td></td><td style="padding: 4px;">\(\text{Opt}_{b,l}\)</td><td style="padding: 4px;">Optimizer for top-down net in level \(l\)</td></tr>
<tr><td style="padding: 4px;">\(h_{f,l}(\cdot)\)</td><td style="padding: 4px;">Top-Down net at level \(l\)</td><td></td><td style="padding: 4px;">\(\text{Opt}_{b}\)</td><td style="padding: 4px;">Collection of all top-down optimizers</td></tr>
<tr><td style="padding: 4px;">\(W_{b,l}\)</td><td style="padding: 4px;">Top-Down net's weights</td><td></td><td></td><td></td></tr>
</tbody>
</table>
</div>

<div id="fig-25" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/final_arch.png" style="width: 100%; height: auto; display: block; margin: 0 auto;" alt="Figure 25">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 25.</b> Asynchronous Perception Machine. \(W_e\) is encoder, \(W_f\) is the bottom-up net and \(W_b\) is the top-down net. They may be implemented with either   convolutional or attention based connectivity.</p>
</div>

First, we present an overview of APM's architecture in Fig [25](#fig-25). APM consists of three sets of weights. The input $$x$$ (eg, image of a face)
is transformed by an encoder $$f_e(\cdot)$$ (with weights $$W_e$$) to produce a set of vectors spanning the part-whole hierarchy. For an image of height $$H$$, width $$W$$, and $$L$$ levels of the hierarchy, there are $$H \times W \times L$$ such vectors of d dimensions each.  Fig [25](#fig-25) shows three such levels labelled as sub-part, part, and object levels. Note that $$W_{e}$$ is shared across all these locations.

At the lowest level $$L-1$$, all the vectors in the face are arranged randomly, much like needles in a magnetic field. As one goes up to level $$L$$, the vectors of left eye, right eye, lips begin to point in same directions, indicating that they are part of the same organ. Finally, at the top level $$L+1$$, all the vectors of the face point in the same direction, indicating that they belong to the same object (called face). A pseudocode for APM's operation has been described in Algorithm [1](#alg-1).

<div id="alg-1" style="margin: 20px 0; padding: 8px 12px; border-top: 2px solid currentColor; border-bottom: 2px solid currentColor; font-size: 0.9em; line-height: 1.7;">
<div style="border-bottom: 1px solid currentColor; padding-bottom: 4px; margin-bottom: 4px;"><b>Algorithm 1</b> APM Pseudocode</div>
<div><b>Require:</b> Image \(\mathbf{x}\), \(W_{outer} = \{W_e, W_f\}\), \(W_{inner} = \{W_b\}\), \(\text{Opt}_{outer}\), \(\text{Opt}_b\), levels \(L\), label \(y\)</div>
<div>&nbsp;1: <b>Outer Loop:</b></div>
<div>&nbsp;2: \(\mathbf{z} \leftarrow f_e(\mathbf{x}; W_e)\) {encode image using shared encoder}</div>
<div>&nbsp;3: Freeze \(W_{inner}\), Unfreeze \(W_{outer}\)</div>
<div>&nbsp;4: Predict part-whole hierarchy vectors \(v_{i,j,l}\) {for all \((i,j,l)\) locations}</div>
<div>&nbsp;5: <b>Inner Loop:</b></div>
<div>&nbsp;6: Freeze \(W_{outer}\)</div>
<div>&nbsp;7: <b>for</b> each pair of levels \((l, l+1)\) <b>do</b></div>
<div>&nbsp;8: <span style="padding-left: 1.5em;"><b>for</b> \(t = 1\) to \(T\) <b>do</b></span></div>
<div>&nbsp;9: <span style="padding-left: 3em;">\(v_p \leftarrow\) vectors at level \(l\)</span></div>
<div>10: <span style="padding-left: 3em;">\(v_w \leftarrow\) vectors at level \(l+1\)</span></div>
<div>11: <span style="padding-left: 3em;">\(v_p \leftarrow \text{update}(v_p)\)</span></div>
<div>12: <span style="padding-left: 3em;">\(\langle v_p, v_w \rangle \leftarrow \text{agreement}(v_p, v_w)\)</span></div>
<div>13: <span style="padding-left: 3em;">\(v_w \leftarrow \text{update}(v_w)\)</span></div>
<div>14: <span style="padding-left: 1.5em;"><b>end for</b></span></div>
<div>15: <span style="padding-left: 1.5em;">Update \(W_{inner}\) using \(\text{Opt}_b\)</span></div>
<div>16: <b>end for</b></div>
<div>17: \(v_L \leftarrow\) vectors at level \(L\)</div>
<div>18: \(\hat{y} \leftarrow \text{Decoder}(v_L)\)</div>
<div>19: \(\mathcal{L}_{outer} \leftarrow \text{Loss}(\hat{y}, y)\)</div>
<div>20: Update \(W_{outer}\) using \(\text{Opt}_{outer}\)</div>
</div>

Successive levels of the hierarchy are connected by a bottom-up net $$g_{f,l}(\cdot)$$ (with weights $$W_{f,l}$$) and a top-down net $$h_{f,l}(\cdot)$$ (with weights $$W_{b,l}$$). The bottom-up net transforms the part vectors into whole vectors, whereas the top-down net transforms the whole vectors into part vectors. Together, these two nets undergo a settling process to achieve canonical locks. This process is repeated for all pairs of levels $$(l, l+1)$$ in the hierarchy (line 6 of Algorithm [1](#alg-1)). We term this process as the ‘agreement procedure’, and describe it in detail in a later section. Finally, the vectors at the topmost level $$L$$ are fed to a downstream decoder to produce a task-specific prediction $$\hat{y}$$ (line 14 of Algorithm [1](#alg-1)).

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">7.1. The Weight Update rule</span>

APM is optimized in two loops: an inner loop and an outer loop. The inner loop is the agreement procedure which is run for $$T$$ iterations to achieve canonical locks. The only weights updated in this loop are the top-down weights $$W_{b,l}$$. Each top-down net contains its separate optimizer $$\text{Opt}_{b,l}$$. Note that this loop does not require any task-specific labels.

The outer loop consists of two sets of weights: (i) the encoder weights $$W_e$$ and (ii) the bottom-up weights $$W_f$$ (for every level $$l$$). Both $$W_{e}/W_{f}$$  are optimized using a single optimizer $$\text{Opt}_{outer}$$. Note that the outer loop requires task-specific labels to compute the loss $$\mathcal{L}_{outer}$$, which in turn is used to update $$W_{e}/W_{f}$$. One may also perform a self supervised task like masked image reconstruction. Optimization can be done using a learning algorithm (like backpropagation).

Next, we discuss  the agreement procedure.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">7.2. The agreement procedure</span>

<div id="fig-26" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/agreement.png" style="width: 75%; height: auto; display: block; margin: 0 auto;" alt="Figure 26">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 26.</b> The agreement procedure.</p>
</div>

Fig[26](#fig-26) shows the agreement procedure. We consider a part vector $$v_{p}$$ sampled from level $$l$$ and a whole vector $$v_{w}$$ sampled at level $$l+1$$. First, $$v_p$$ self-attends to other part vectors in a circular  neighborhood of radius $$r$$[^6]. A similar operation is performed for $$V_{w}$$. Mathematically, we denote this by:

$$
v_p \leftarrow \sum_{q \,:\, \lVert q-p \rVert \le r} \mathrm{softmax}_q\big(\mathrm{sim}(v_p, v_q)\big)\, v_q \tag{1a}
$$

The above equation only enables communication within the ‘same’ level *l*. Please note that this neighborhood information aggregation could (in principle) be implemented by  self-attention\[[13](#ref-Vaswani2017AttentionIA)\], Kuramoto synchronization or any other similar mechanism.

Next, we consider the communication agreement ‘between’ different levels *l* and *l+1*. This communication happens as the information is piped through both bottom-up and top-down nets. Note that during this procedure the bottom-up weights $$W_f$$ are frozen, and only the top-down weights $$W_b$$ are updated.

First, the part vector $$v_{p}$$
produces a part vote
$$v_{p}'$$ as:

$$
v_p' = v_p \, W_f \tag{2}
$$

The agreement between $$v_p'$$ and $$v_w$$ is measured by computing the projection of the part vector onto the whole vector as:

$$
v_{proj} = \frac{v_{part} \cdot v_{whole}}{\lVert v_{whole} \rVert^2} \, v_{whole} \tag{3}
$$

A perfect agreement is said to be achieved when $$v_{proj} = v_{w}$$. The whole vector $$v_{w}$$ is itself updated as a combination of the part vote $$v_{proj}$$ and interactions with other whole vectors in the (radial) neighborhood. The update rule is given by:

$$
v_w \leftarrow \sum_{q \,:\, \lVert q-w \rVert \le r} \mathrm{softmax}_q\big(\mathrm{sim}(v_w, v_q)\big)\, v_q \tag{4a}
$$

$$
v_w \leftarrow \left\langle v_w + v_{proj} \right\rangle \tag{4b}
$$

The addition operation between $$v_{w}$$ and $$v_{proj}$$ induces a form of coupling between levels $$l$$ and $$l+1$$. Indeed, there might be many ways to combine (and separate) information from two sources like $$v_{w}$$ and $$v_{proj}$$ together. But, the set transformer paper\[[29](#ref-lee2019set)\] proved that a simple addition operation is sufficient to achieve universal approximation. It also bears deep mathematical connections to Arnold Kolmogorov's superposition theorem (as acknowledged in the original GLOM paper\[[1](#ref-glom)\]), which in turn inspires this choice. An interpretation can also be found in the appendix.

Next, $$v_{w}$$ is fed back through the top-down net $$W_{b}$$ to produce a new part vector $$v_{part-out}'$$ as:

$$
v_{part-out}' = v_{w} \, W_b \tag{5}
$$

We estimate the regression loss between the original part vector $$v_{part}$$ and the new part vector $$v_{part-out}'$$ as:

$$
\mathcal{L}_{agreement} = \lVert v_{part-out}' - v_{part} \rVert^2 \tag{6}
$$

and the top-down weights $$W_b$$ are updated using backpropagation. Next, we *detach* the part vector $$v_{part-out}'$$ from the compute graph and use it to refine the part vector $$v_{part}$$ itself. This refinement procedure is called *the slurp update*,  which we explain next.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">7.3. The Slurp Update</span>

Given an input part vector $$v_{p}$$, and the output of the top-down net $$v_{part-out}$$, we want to ‘nudge’ the part vector $$v_{p}$$ ‘slightly’ in the direction of the $$v_{part-out}$$. It is very tempting to make one rapid update to the part vector $$v_{p}$$ by just setting $$v_{p} = v_{part-out}$$. However, this is not ideal, since then the top-down net gets zero loss, and cannot be updated beyond one iteration. Instead, we propose the slurp-update.

<div id="fig-27" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/slurp.png" style="width: 60%; height: auto; display: block; margin: 0 auto;" alt="Figure 27">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 27.</b> The slurp update.</p>
</div>

First, we normalize both $$v_{p}$$ and $$v_{part-out}$$ so that they lie on surface of a unit hypersphere. Next, we draw an arc on the sphere between $$v_{p}$$ and $$v_{part-out}$$. The slurp update is to move the part vector ‘slightly’ along this arc towards $$v_{part-out}$$. The length of the arc can be said to be $$L$$. We can divide this into small $$n$$ segments of length $$l$$, such that $$n \times l$$  = $$L$$. The vector $$v_{p}$$ is stepped towards $$v_{part-out}$$ by $$l$$ length on the geodesic. The number $$n$$ (a hyperparameter) controls how many partitions of the arc are made.

Thus, the information recirculates freely across the bottom up and top down nets, followed by the slurp update. This is repeated for $$T$$ iterations, and does not need any labels. Finally, in the outer loop, the weights $$W_{e}$$ and $$W_f$$ are themselves updated via backpropagation.

Note that backpropagation updates level $$l+1$$ with larger gradients than level $$l$$. Gradient normalization/clipping is an option, but it is not enough to bypass backpropagation's reliance on chain rule: successive multiplications of gradients across layers result in weaker gradient signal. This means that the signal from the bottom-up net is weaker than the signal from the top-down net. To compensate, one thus needs to run the equation 1a for a greater number of iterations than equation 4.

One issue with $$L_{agreement}$$ is that it only uses the available information in part vectors. There is no constraint on the architectures of the bottom-up and top-down nets  which ensures that  agreement happens in ‘least’ number of iterations. To resolve this, one needs to consider how the architecture of bottom-up and top-down net should be designed. This leads us to the matter of ‘when might perfect agreement arise?’

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">7.4. Promoting Perfect Agreement</span>

<div id="fig-28" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/bu_fixed.png" style="width: 35%; height: auto; display: block; margin: 0 auto;" alt="Figure 28">
  <p style="font-size: 0.9em; text-align: center; margin-top: 8px;"><b>Figure 28.</b> An analysis of the case of perfect agreement.</p>
</div>

We consider the simplest case of a single part vector $$v_p$$ and a single whole vector $$v_w$$. In the case of perfect agreement, the following conditions shall hold:

$$
v_w = W_f v_p \tag{7a}
$$

$$
v_p = W_b v_w \tag{7b}
$$

The regularization constraint to prevent collapse is that $$W_f \neq \mathbf{I}$$ and $$W_b \neq \mathbf{I}$$.  Substituting $$v_p$$, we obtain $$v_w = W_f W_b v_w$$. This implies that $$W_f W_b = \mathbf{I}$$, which means that $$W_b = W_f^{-1}$$. In principle, one could enforce this by estimating the inverse of $$W_f$$ in each iteration of the inner loop, and regressing $$W_b$$ towards that. However, this does not work due to two reasons:

- The bottom-up net consists of multiple layers with non-linearities. There is no guarantee that during every iteration, an inverse actually exists.
- Even if it did, taking an inverse of a matrix is computationally expensive, which means that it does not parallelize as well on GPUs as compared to matrix multiplications.

One tempting way out of this hurdle is to enforce the condition $$W_f W_b = \mathbf{I}$$ on each layer of the nets. We term this procedure as Deep Weight Alignment. However, for this constraint to work, the bottom-up and top-down nets must be layer-wise symmetric as shown in Fig[29](#fig-29)[^7].

<div id="fig-29" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/mirror_arch.png" style="width: 70%; height: auto; display: block; margin: 0 auto;" alt="Figure 29">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 29.</b> Combining  bottom-up and top-down nets together. They are identical in structure. Each box shows the number of  neurons present in that layer. Each neuron is marked as a ‘double circle’ to indicate that it may be used to ‘both’ present an input to the net, as well read output from it. Intermediate activation functions are omitted for clarity.</p>
</div>

During each iteration of the inner loop, we enforce:

$$
W_{pred} = W_f W_b \tag{8a}
$$

$$
L_{weight}= \lVert W_{pred} - \mathbf{I} \rVert^2 \tag{8b}
$$

The total loss $$L_{inner}$$ is then given by:

$$
L_{inner} = L_{agreement} + \lambda L_{weight} \tag{9}
$$

<div id="fig-30" style="text-align: center; margin: 20px 0;">
  <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/sync_plot.png" style="width: 100%; height: auto; display: block; margin: 0 auto;" alt="Figure 30">
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 30.</b> Hinton Diagrams for synchronization: The top-down and bottom-up net  can drive each other to identical weights. They follow signed symmetry: the magnitude of sign of the weight in each box is the same. However, the magnitude of the weight may be different. For eg, the thickness of blue highlighted square, is different in layer L3 of both nets.</p>
</div>

Note that neither $$L_{agreement}$$ nor $$L_{weight}$$ require any labels. The inner loop is thus a self-supervised procedure which promotes islands of agreement inside the net\[[7](#ref-modi2024asynchronous), [1](#ref-glom)\].

Connections to Random Feedback Alignment: On a first glance, the  Deep Weight Alignment procedure appears similar to the idea of random feedback alignment\[[30](#ref-lillicrap2016random)\]. However, there are several differences:

- The top-down net is a mirror symmetric copy of the bottom-up net.
- The top-down net carries agreement signal, and not the gradient signal.
- The bottom up net is not trained at all. It is merely a pathway for the lower level part vectors to send neural activity to the  higher level whole vectors.

We acknowledge that the resultant system is biologically implausible. First, it creates the illusion that brain contains two pathways which must be symmetric.  But such observations have not been made in neuroscience. Second, the notion that a part of the circuit (bottom up net) is never trained seems absurd.

However,  this does appear to work better as compared to training both the nets together.  The job is far from done, and there must be some other  alternative mechanisms by which brain does credit-assignment that does  not rely on gradient descent. A weight update rule $$W = W - \eta \nabla_W L$$ means that both the weights and gradients are stored, which in turn implies there must be two weights on each  synapse[^8]. This seems even more absurd. A better alternative might be to let the weight matrix ‘itself know’ how to update itself, without ever estimating the gradients\[[31](#ref-irie2022modern)\]. This is not a path we have yet explored.

Connections to Kuramoto Oscillatory Neurons: The agreement procedure communicated in Section [7.2](#72-the-agreement-procedure) is similar to the idea of Artificial Kuramoto oscillatory neurons\[[18](#ref-akorn)\]. However, the differences are :

- Synchronization happens between two different levels of the hierarchy, and not within the same level.
- A top-down net is responsible for the synchronization. Therefore, the application of minimum description length principle to $$v_{proj}$$ is not enforced directly, but is an implicit consequence of enforcing $$L_{agreement}$$.
- The constraint that the part vote needs to be in same direction as the whole vector $$v_w$$ need not hold: the net can decide the angle (aka canonical lock) between the two vectors during gradient descent.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">7.5. Hinton diagrams for synchronization</span>

Hinton diagrams were a connectionist weapon designed  during the times of the symbolist-connectionist war\[[25](#ref-fodor1988connectionism)\]. A Hinton diagram is a 2D grid of squares, visualizing the weights of the net. For an N by N weight matrix, the total grid is of size N by N. Each element of the grid is a square. The thickness of the square denotes the magnitude of the weight, and the color (black or white) denotes the sign of the weight. Multiple such squares can then be plotted for each layer of the bottom up/ top-down  net. We show one such plot in Fig[30](#fig-30).

We perform the following experiment: (i) the part vectors in level $$l$$ and level $$l+1$$ are initialized randomly. (ii) Both bottom-up and top-down nets are initialized randomly. The weights of the bottom-up net are frozen. (iii) The agreement procedure  is performed and the weights of both the nets (After T steps) are plotted. $$L_{inner}$$ is used to update the weights of the top-down net.

Fig[30](#fig-30) shows the two rows with weights $$W_f^{-1}$$ and $$W_b$$ visualized. One can see that the weights of top-down net $$W_b$$ are driven to the weights of $$W_f^{-1}$$, which is the inverse of the bottom-up net. The only differences are in the layer $$L_{3}$$ where the thickness (hence the magnitude) of the weights is different.

However, the agreement procedure seems to promote signed symmetry between the two nets, i.e. the ‘color’ of the boxes comes out to be identical. We tested our procedure with different initializations of $$W_f$$ prior to the agreement procedure. Similarly, we tested running the optimization for more than a million iterations, and the results appear somewhat consistent. This suggests that the agreement procedure can indeed allow bottom-up net and top-down net to drive each other to synchrony.

If the vectors at part level and whole level are entirely random, then the agreement procedure still converges to their mean. This means that merely examining the loss is not enough to reveal the quality of islands being formed. However, it the data possesses some structure, (for eg, images), we can indeed see islands of agreement to emerge\[[7](#ref-modi2024asynchronous), [1](#ref-glom)\].

A way to promote formation of islands is to enforce two constraints: (i) attention must be restricted to a circular local neighborhood, much akin to  restricted Boltzmann machines (ii) The radius of the neighborhood is gradually increased as one goes up the different layers of $$W_e$$. This is similar to the idea of receptive fields in convolutional nets. The key issue with CNNs was that they traded off the resolution of the input in favor of increasing channel count in the later layers. This led to a loss of spatial information, which had to be compensated for  via skip connections from a layer $$l$$ of encoder to  layer $$l$$ of decoder.

Our mechanism is different in two ways: (i) As information flows through $$W_{e}$$ there is no loss of spatial resolution (ii) a standard softmax looks at all the locations, and weighs the incoming signal accordingly. This is flawed because it guides the agreement towards a single mean and leads to collapse.

Our procedure instead relies on resonance\[[4](#ref-liu2026krause)\][^9]: a part vector looks at all its neighbors, and chooses the ‘most dominant one’. Once it has done this selection, it does not care about what all other part-vectors are saying. Our part aligns itself in the direction of the dominant neighbor.

In the initial layers of $$W_e$$, there are several part vectors around a given part-vector, pointing in randomly different directions. Thus, there is no structure in the internal representation. Thus, the attention mechanism needs to seek consensus from k top neighbors. As we go up in the hierarchy, the circular neighborhoods we tap into gradually increase in radius. The value of k is gradually stepped down during training from 4 to 1 because by then the system has already beaten the natural entropy, and cluster formation has already happened.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">7.6. Alternating signed symmetry and amplification circuits</span>

Looking closely in Fig[30](#fig-30) shows that the weights in different layers appear to alternate their signs. For eg, the top left square in $$W_f^{-1}$$ (L1) is white, whereas it alternates to black in $$W_f^{-1}$$ (L2), and white again in $$W_f^{-1}$$ (L3). It is also interesting to see that the strength of the weights (the thickness) of the square in L1 is much stronger than $$L3$$. Similarly, the weights of top-down net $$W_b$$ are of lower magnitude in L2/L3 throughout. This leads to several observations:

- Top-down net was trained with backpropagation with the first layer having the strongest gradients. As we go deeper, the gradients become weaker and the ability of the net to have signed bit flips in the weights get reduced which in turn hurts performance. Top-Down net is naturally ‘weaker’ than the bottom-up net.
- An electromagnetic wave travels in a medium with alternative positive and negative flips. So perhaps, weights can be thought of as a medium and the top-down/bottom-up net as electromagnetic waves.
- A combination of top-down and bottom-up net then creates a standing wave, which is a form of resonance. If both waves support each other, one can overcome the weakness of the top-down net. If not, then the top-down net is drowned out by the bottom-up net.

<div id="fig-31" style="text-align: center; margin: 20px 0;">
  <div style="display: inline-block; border: 1px solid #000; padding: 12px; background: #fff; width: 95%; box-sizing: border-box;">
    <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/class_hierarchy_dendrogram.png" style="width: 100%; height: auto; display: block; margin: 0 auto;" alt="Figure 31">
  </div>
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 31.</b> The fixed class-name hierarchy (L1 finest to L5 coarsest) that the model's 5 classification heads are trained against, shown as a dendrogram.</p>
</div>

A careful tuning of the wavelengths of travelling waves in both nets is thus required to make sure that the peaks coincide with the place where output is read off the neural circuit. Similarly, a standing wave forms alternative crest and troughs. It is then possible to ‘tap into’ all the crests of the standing wave to make sure that the decoded representation is the strongest one. A tap at the trough however results in destructive interference which severely diminished the quality of the decoded representation.

The fact that top-down and bottom-up nets create their own travelling waves whose combination results in a standing wave, leads to the question: how do we prevent the crests of the standing wave from blowing up? This is a very important question, since if the crests blow up, then the agreement procedure will not converge. The answer was to simply clamp the weights to a spherical higher dimensional manifold. An alternative is to use Riemann geometry.

During the agreement procedure, there was another finding. Since the magnitude of the weights of bottom up net were more than the top-down net, it was better to  measure the internal Lyapunov energy of the bottom-up net to make a sense of whether the agreement was converging or not. To compensate for the weaker top-down nets, we simply ‘amplified’ the weights of the top-down net by a fixed factor. Alternatively, one can switch directions from which the backpropagation is performed: first operate on the left side of the Fig[30](#fig-30) and then on the right side. On average, it results in weights of top-down net to mirror the weights of bottom-up net.

Let us now assume that weight of bottom up net is $$W_{f,i,j,l}$$ and weight of top-down net is $$W_{b,i,j,l}$$. Here, $$l$$ represents the $$l^{th}$$ layers of the nets and $$(i,j)$$ represent the spatial coordinates $$(i,j)$$ of the weight matrix. The correction factor $$\gamma_{i,j,l}$$ is given by:

$$
\gamma_{i,j,l} = \frac{\lVert W_{f,i,j,l} \rVert}{\lVert W_{b,i,j,l} \rVert + \epsilon} \tag{10a}
$$

$$
\widetilde{W}_{b,i,j,l} = \gamma_{i,j,l} \cdot W_{b,i,j,l} \tag{10b}
$$

The universal approximation theorem leads one to believe that it is possible to abstract away all the families of neural architectures as an abstraction function $$f$$. However, our experience suggests that the rate at which representations learnt by different architectures converge depends on the nature of the wiring pattern itself.

## <span style="font-size: 1.2rem; color: var(--border-header-bottom);">7.7. Replication of top-down and bottom-up nets</span>

Kindly refer again to the architecture in Fig[25](#fig-25).  Consider the top-down and bottom-up nets between level $$l$$ and $$l+1$$ again. One can observe that both the nets are shared across all the locations $$(i,j)$$ in the spatial grid. We wish to consider various ways in which this weight sharing might occur.

Firstly, one could replicate top-down and bottom-up net across locations $$(i,j)$$ in the spatial grid. On a single GPU, this weight copying means that one quickly runs out of memory. However, one gains the ability to exchange information between different copies of the net by weight sharing, which is a much higher bandwidth way of exchanging information than knowledge distillation\[[1](#ref-glom), [20](#ref-hinton2022forward)\]

Secondly, a single copy of the top-down and bottom-up net is kept. Instead, the location based queries $$(i,j)$$ are fed as a batched input to the net\[[7](#ref-modi2024asynchronous)\]. This saves memory on a single device.

Finally, among multiple GPU devices, only one copy of top-down and bottom-up net is kept. Inside the device, the parallelism is achieved by feeding different $$(i,j)$$ queries to the net. Thus, one in principle could reap the benefits of both weight sharing and memory efficiency.

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">8. The visual hierarchical parsing</span>

In NLP, it is easy to parse sentences into parse trees, since it is possible to define which words form a noun, verb etc. In case of vision, the hierarchies are not so well defined. Similarly, existing datasets only contain up to 3 levels of hierarchy, whereas GLOM explicitly requires 5 levels of the hierarchy.

Towards this end, we consider the CelebA-HQ dataset\[[32](#ref-karras2017progressive)\] of faces, and define a 5-level part-whole hierarchy of a face. An example of the hierarchy is shown in Fig[31](#fig-31). The hierarchy is defined at lowest level  as *ground*, *skin*, *left-eyebrow*, *right-eyebrow*, *left-eye*, *right-eye*, *nose*, *upper-lip*, *inner-mouth*, *lower-lip* and *hair*. The remaining levels are derived by merging the parts into wholes. The hierarchy is as follows:

- **L1** ($$11$$ classes) — the raw parser classes above.
- **L2** ($$7$$) — the two eyebrows merge into *eyebrows*, the two eyes into *eyes*, and the three lip/mouth classes into *mouth*.
- **L3** ($$5$$) — *eyebrows* and *eyes* merge into *upper face*; *nose* and *mouth* merge into *mid face*.
- **L4** ($$3$$) — *skin*, *upper face* and *mid face* merge into a single *face*.
- **L5** ($$2$$) — *hair* is absorbed into *face*, leaving only *face* and *background*.

The instance of the problem presented to the net  might change: given any image of a face, the net must parse it correctly. The individual sizes of clusters (eg, face, nose, etc), as well as their locations may differ.

Fig[1](#fig-1) shows the predicted part-whole hierarchy of a face from the APM. Note that all the levels sit above each other. A body part (i,j) at level $$L$$ knows what sub-part it breaks into by examining the representation (i,j) at level $$L-1$$. The visual parsing in this representation can then occur in a backward fashion: starting from level $$L$$, one can examine the representation at level $$L-1$$ to see what sub-parts it breaks into, and so on until the finest level is reached. The net generalizes to any unseen image, and is not restricted to the training set.

<u>Backward Parsing:</u> For a pixel (i,j) at level L, we can know all the children in the parse tree by looking recursively at representation of (i,j) at level L-1, and so on until the finest level is reached. The procedure is repeated for all the locations $$(1,1) \leq (i,j) \leq (H,W)$$ in the spatial grid.

We would like to distinguish this form of visual parsing  from the parsing of sentences in \[[33](#ref-Vinyals2014GrammarAA)\]. In the latter, one partitions a sentence into words spanning indices (i,j), builds a representation, and runs a linear classifier. Running the net for all pairs gives a score. An assignment problem is then solved to find the best parse tree which follows a correct syntax. Along the similar lines, a similar hungarian assignment procedure is used in object detectors to allocate boxes to ground truth.

The parsing of images here does not require any assignment, but instead emerges as a consequence of the agreement procedure. The very act of ‘gluing together’[^10] $$\langle$$sub part, part, object vectors$$\rangle$$ in a single column guarantees that the parent-child relationship can be read off directly, which should significantly speed up the parsing process.

<u>Connections to autoregression</u>: A seq2seq model relies on linearizing the parse-tree and predicting each token via autoregression. This is slow because tokens in the far future cannot be predicted until tokens  in the past have been predicted. At each timestep, the decoded neural activity is fed back through the network input, which means that the network must be run again.

The form of hierarchical parsing proposed here is different: the entire parse-tree across all levels is predicted in a single forward pass and refined over multiple iterations of the bottom up and top down agreement process.

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">9. Conclusion</span>

In this paper, we have presented canonical locks as a geometric primitive for learning machines. This allows them to encode part-whole hierarchies in a neural net. Our key result is that it is possible to train a neural net with just one sample (without any sort of initialization from a pretrained set of weights), and generalize to a given test set of images with competitive accuracies. This generalization also extends to rotational groups that increment in multiples of 90 degrees.

Our running hypothesis is that neural nets are geometrical engines that encode part-whole hierarchies. Overfitting on a single sample leads  to a form of compositional-based learning which learns to combine parts into wholes dynamically\[[34](#ref-hinton1990mapping), [35](#ref-schmidhuber1990towards), [36](#ref-hinton2019representing), [1](#ref-glom)\]. Constraining the weights properly reduces the subspace gradient descent has to search, which in turn significantly speeds up learning.

Given that compute is finally cheap, but the solid-state memory is not, it makes sense to explore learning machines which are higher bandwidth, but lower parameterized. It might be possible for APM/s to meta learn  multiple levels of the  part whole hierarchy. They should meta learn their own architecture, learning algorithms, optimizers, and pretraining task as well. Last but not the least, they should meta learn from the meta learner himself\[[37](#ref-schmidhuber1987evolutionary)\].

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">References</span>

[1] Hinton, G. E. How to represent part-whole hierarchies in a neural network. *Neural Computation*, 35:413–452, 2021. URL [https://api.semanticscholar.org/CorpusID:232046121](https://api.semanticscholar.org/CorpusID:232046121). \[[link](https://arxiv.org/abs/2102.12627)\]
{: #ref-glom}

[2] Modi, R., Vineet, V., and Rawat, Y. S. On occlusions in video action detection: Benchmark datasets and training recipes. *ArXiv*, abs/2410.19553, 2024. URL [https://api.semanticscholar.org/CorpusID:262950334](https://api.semanticscholar.org/CorpusID:262950334). \[[link](https://arxiv.org/abs/2410.19553)\]
{: #ref-Modi2024OnOI}

[3] Fan, H., Xiong, B., Mangalam, K., Li, Y., Yan, Z., Malik, J., and Feichtenhofer, C. Multiscale vision transformers. In *2021 IEEE/CVF international conference on computer vision (ICCV)*, pp. 6804–6815. IEEE, 2021. \[[link](https://arxiv.org/abs/2104.11227)\]
{: #ref-fan2021multiscale}

[4] Liu, J., Yue, Y., Welling, M., and Song, Y. Krause synchronization transformers. In *Forty-third International Conference on Machine Learning*, 2026. \[[link](https://arxiv.org/abs/2602.11534)\]
{: #ref-liu2026krause}

[5] Miyato, T., Löwe, S., Geiger, A., and Welling, M. Artificial kuramoto oscillatory neurons. In *International Conference on Learning Representations*, volume 2025, pp. 44278–44322, 2025b. \[[link](https://arxiv.org/abs/2410.13821)\]
{: #ref-miyato2025artificial}

[6] Löwe, S., Lippe, P., Locatello, F., and Welling, M. Rotating features for object discovery. *Advances in Neural Information Processing Systems*, 36:59606–59635, 2023. \[[link](https://arxiv.org/abs/2306.00600)\]
{: #ref-lowe2023rotating}

[7] Modi, R. and Rawat, Y. S. Asynchronous perception machine for efficient test time training. *Advances in Neural Information Processing Systems*, 37:106020–106058, 2024. \[[link](https://arxiv.org/abs/2410.20535)\]
{: #ref-modi2024asynchronous}

[8] Hinton, G. Some demonstrations of the effects of structural descriptions in mental imagery. *Cognitive Science*, 3(3):231–250, 1979. \[[link](https://doi.org/10.1207/s15516709cog0303_3)\]
{: #ref-hinton1979some}

[9] Garau, N., Bisagno, N., Sambugaro, Z., and Conci, N. Interpretable part-whole hierarchies and conceptual-semantic relationships in neural networks. In *2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, pp. 13679–13688. IEEE, 2022. \[[link](https://arxiv.org/abs/2203.03282)\]
{: #ref-garau2022interpretable}

[10] Sabour, S., Frosst, N., and Hinton, G. E. Dynamic routing between capsules. *Advances in neural information processing systems*, 30, 2017. \[[link](https://arxiv.org/abs/1710.09829)\]
{: #ref-sabour2017dynamic}

[11] Zaheer, M., Kottur, S., Ravanbakhsh, S., Poczos, B., Salakhutdinov, R. R., and Smola, A. Deep sets. *Advances in neural information processing systems*, 30, 2017. \[[link](https://arxiv.org/abs/1703.06114)\]
{: #ref-zaheer2017deep}

[12] Veličković, P., Cucurull, G., Casanova, A., Romero, A., Lio, P., and Bengio, Y. Graph attention networks. *arXiv preprint arXiv:1710.10903*, 2017. \[[link](https://arxiv.org/abs/1710.10903)\]
{: #ref-velivckovic2017graph}

[13] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., and Polosukhin, I. Attention is all you need. In *Neural Information Processing Systems*, 2017. URL [https://api.semanticscholar.org/CorpusID:13756489](https://api.semanticscholar.org/CorpusID:13756489). \[[link](https://arxiv.org/abs/1706.03762)\]
{: #ref-Vaswani2017AttentionIA}

[14] Hinton, G. F. A parallel computation that assigns canonical object-based frames of reference. In *Proceedings of the 7th international joint conference on Artificial intelligence-Volume 2*, pp. 683–685, 1981. \[[link](https://www.ijcai.org/proceedings/1981/129)\]
{: #ref-hinton1981parallel}

[15] Sejnowski, T. J., Kienker, P. K., and Hinton, G. E. Learning symmetry groups with hidden units: Beyond the perceptron. *Physica D: Nonlinear Phenomena*, 22(1-3):260–275, 1986. \[[link](https://doi.org/10.1016/0167-2789%2886%2990245-9)\]
{: #ref-sejnowski1986learning}

[16] Cohen, T. and Welling, M. Group equivariant convolutional networks. In *International conference on machine learning*, pp. 2990–2999. PMLR, 2016. \[[link](https://arxiv.org/abs/1602.07576)\]
{: #ref-cohen2016group}

[17] Hutchinson, M. J., Le Lan, C., Zaidi, S., Dupont, E., Teh, Y. W., and Kim, H. Lietransformer: Equivariant self-attention for lie groups. In *International conference on machine learning*, pp. 4533–4543. PMLR, 2021. \[[link](https://arxiv.org/abs/2012.10885)\]
{: #ref-hutchinson2021lietransformer}

[18] Miyato, T., Löwe, S., Geiger, A., and Welling, M. Artificial kuramoto oscillatory neurons. In *International Conference on Learning Representations*, volume 2025, pp. 44278–44322, 2025a. \[[link](https://arxiv.org/abs/2410.13821)\]
{: #ref-akorn}

[19] Bai, S., Kolter, J. Z., and Koltun, V. Deep equilibrium models. *Advances in neural information processing systems*, 32, 2019. \[[link](https://arxiv.org/abs/1909.01377)\]
{: #ref-bai2019deep}

[20] Hinton, G. The forward-forward algorithm: Some preliminary investigations. *arXiv preprint arXiv:2212.13345*, 2(3):5, 2022. \[[link](https://arxiv.org/abs/2212.13345)\]
{: #ref-hinton2022forward}

[21] Löwe, S., Lippe, P., Rudolph, M., and Welling, M. Complex-valued autoencoders for object discovery. *arXiv preprint arXiv:2204.02075*, 2022. \[[link](https://arxiv.org/abs/2204.02075)\]
{: #ref-lowe2022complex}

[22] Hinton, G. E. Relaxation and its role in vision. 1977. \[[link](https://era.ed.ac.uk/handle/1842/8121)\]
{: #ref-hinton1977relaxation}

[23] Palmer, S. E. Cannonical perspective and the perception of objects. *Attention and performance*, 9:135–151, 1981. \[[link](https://scholar.google.com/scholar?q=%22Canonical+perspective+and+the+perception+of+objects%22)\]
{: #ref-palmer1981cannonical}

[24] Hinton, G. Using relaxation to find a puppet. In *Proceedings of the 2nd summer conference on artificial intelligence and simulation of behaviour*, pp. 148–157, 1976. \[[link](https://www.cs.toronto.edu/~hinton/absps/puppet.pdf)\]
{: #ref-hinton1976using}

[25] Fodor, J. A. and Pylyshyn, Z. W. Connectionism and cognitive architecture: A critical analysis. *Cognition*, 28(1-2):3–71, 1988. \[[link](https://doi.org/10.1016/0010-0277%2888%2990031-5)\]
{: #ref-fodor1988connectionism}

[26] Chomsky, N. *Aspects of the Theory of Syntax*, volume 11. MIT press Cambridge, MA, 1965. \[[link](https://doi.org/10.21236/ad0616323)\]
{: #ref-chomsky1965aspects}

[27] Hinton, G. E., Nowlan, S. J., et al. How learning can guide evolution. *Complex systems*, 1(3):495–502, 1987. \[[link](https://www.complex-systems.com/abstracts/v01_i03_a06/)\]
{: #ref-hinton1987learning}

[28] Kovachki, N., Li, Z., Liu, B., Azizzadenesheli, K., Bhattacharya, K., Stuart, A., and Anandkumar, A. Neural operator: Learning maps between function spaces with applications to pdes. *Journal of Machine Learning Research*, 24(89):1–97, 2023. \[[link](https://jmlr.org/papers/v24/21-1524.html)\]
{: #ref-kovachki2023neural}

[29] Lee, J., Lee, Y., Kim, J., Kosiorek, A., Choi, S., and Teh, Y. W. Set transformer: A framework for attention-based permutation-invariant neural networks. In *International conference on machine learning*, pp. 3744–3753. PMLR, 2019. \[[link](https://arxiv.org/abs/1810.00825)\]
{: #ref-lee2019set}

[30] Lillicrap, T. P., Cownden, D., Tweed, D. B., and Akerman, C. J. Random synaptic feedback weights support error backpropagation for deep learning. *Nature communications*, 7(1):13276, 2016. \[[link](https://doi.org/10.1038/ncomms13276)\]
{: #ref-lillicrap2016random}

[31] Irie, K., Schlag, I., Csordás, R., and Schmidhuber, J. A modern self-referential weight matrix that learns to modify itself. In *International conference on machine learning*, pp. 9660–9677. PMLR, 2022. \[[link](https://arxiv.org/abs/2202.05780)\]
{: #ref-irie2022modern}

[32] Karras, T., Aila, T., Laine, S., and Lehtinen, J. Progressive growing of gans for improved quality, stability, and variation. *arXiv preprint arXiv:1710.10196*, 2017. \[[link](https://arxiv.org/abs/1710.10196)\]
{: #ref-karras2017progressive}

[33] Vinyals, O., Kaiser, L., Koo, T., Petrov, S., Sutskever, I., and Hinton, G. E. Grammar as a foreign language. *ArXiv*, abs/1412.7449, 2014. URL [https://api.semanticscholar.org/CorpusID:14223](https://api.semanticscholar.org/CorpusID:14223). \[[link](https://arxiv.org/abs/1412.7449)\]
{: #ref-Vinyals2014GrammarAA}

[34] Hinton, G. E. Mapping part-whole hierarchies into connectionist networks. *Artificial Intelligence*, 46(1-2):47–75, 1990. \[[link](https://doi.org/10.1016/0004-3702%2890%2990004-J)\]
{: #ref-hinton1990mapping}

[35] Schmidhuber, J. Towards compositional learning in dynamic networks. *Technical University of Munich (Technical Report FKI-129-90)*, 1, 1990. \[[link](https://people.idsia.ch/~juergen/FKI-129-90ocr.pdf)\]
{: #ref-schmidhuber1990towards}

[36] Hinton, G. E. Representing part-whole hierarchies in connectionist networks. In *10th Annual Conference Cognitive Science Society Pod*, pp. 48–54. Psychology Press, 2019. \[[link](https://www.cs.toronto.edu/~hinton/absps/part-whole88.pdf)\]
{: #ref-hinton2019representing}

[37] Schmidhuber, J. *Evolutionary principles in self-referential learning, or on learning how to learn: the meta-meta-... hook*. PhD thesis, Technische Universität München, 1987. \[[link](https://people.idsia.ch/~juergen/diploma1987ocr.pdf)\]
{: #ref-schmidhuber1987evolutionary}

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">A. Decoding the part-whole hierarchy</span>

Let $$\hat{y}_l(i,j) \in \{0, \dots, C_l - 1\}$$ be the class the APM predicts at pixel $$(i,j)$$ and level $$l$$, with $$C_1, \dots, C_5 = 11, 7, 5, 3, 2$$ the class counts of Sec[8](#8-the-visual-hierarchical-parsing). Every level carries its own name table $$N_l$$, and decoding a pixel is the lookup

$$
(i,j) \mapsto \big( N_1[\hat{y}_1(i,j)],\, \dots,\, N_5[\hat{y}_5(i,j)] \big),
$$

whose five entries are the part-whole path of that pixel: the part it occupies at the finest level, and each whole which contains that part as one moves up. Nothing is post-processed to obtain this path. The features are not clustered, the prediction is not matched against a tree, and no assignment is solved. The path is read straight off the five classifier outputs. It is possible to align an open world text-model to each of the locations of the part-whole hierarchies, which means that multiple hierarchies could be decoded together. The decoding scheme shows that the net has the ability to predict the correct vector at the correct location $$(i,j,l)$$.

The tables $$N_l$$ must be reported with the predictions, because every level numbers its classes from zero and an id on its own therefore fixes nothing. The dump below gives them for the face of Fig[1](#fig-1). Its `class_ids` field is $$N_1$$ through $$N_5$$; its `level_accs` field records the accuracy of this sample at each level, rising from $$0.919$$ at L1 to $$0.982$$ at L5; and its `hierarchy` field gives one pixel per class present in the face, each row listing the pair $$[\,$$id, name$$\,]$$ at all five levels.

The rows show three behaviors worth separating. A pixel may change both its id and its meaning as the level rises: pixel $$(88, 89)$$ is id $$2$$ at L1, *left_eyebrow*, and id $$2$$ again at L2, but the table underneath has changed and the two eyebrows are now one class, *eyebrows*; the pixel then becomes *upper_face* at L3 and *face* at L4 and L5. It is a part and a whole at the same time, and which of the two one sees is set by the level one reads. A pixel may equally keep its meaning for several levels: hair stays *hair* up to L4 and joins *face* only at L5. A class may also go unused, since *inner_mouth*, id $$8$$ at L1, has no row at all in this face.

An example of a hierarchy decoded using our visual semantic parser has been provided below.

```
{
  "sample_idx": 221,
  "level_accs": {"l1": 0.919, "l2": 0.900, "l3": 0.916, "l4": 0.969, "l5": 0.982},
  "class_ids": {
    "l1": {"0": "background", "1": "skin", "2": "left_eyebrow", "3": "right_eyebrow",
           "4": "left_eye", "5": "right_eye", "6": "nose", "7": "upper_lip",
           "8": "inner_mouth", "9": "lower_lip", "10": "hair"},
    "l2": {"0": "background", "1": "skin", "2": "eyebrows", "3": "eyes", "4": "nose",
           "5": "mouth", "6": "hair"},
    "l3": {"0": "background", "1": "skin", "2": "upper_face", "3": "mid_face",
           "4": "hair"},
    "l4": {"0": "background", "1": "face", "2": "hair"},
    "l5": {"0": "background", "1": "face"}
  },
  "hierarchy": [
    {"pixel": [209, 112], "l1": [0, "background"],
     "l2": [0, "background"], "l3": [0, "background"],
     "l4": [0, "background"], "l5": [0, "background"]},
    {"pixel": [130, 161], "l1": [1, "skin"],
     "l2": [1, "skin"], "l3": [1, "skin"], "l4": [1, "face"], "l5": [1, "face"]},
    {"pixel": [88, 89], "l1": [2, "left_eyebrow"],
     "l2": [2, "eyebrows"], "l3": [2, "upper_face"],
     "l4": [1, "face"], "l5": [1, "face"]},
    {"pixel": [88, 146], "l1": [3, "right_eyebrow"],
     "l2": [2, "eyebrows"], "l3": [2, "upper_face"],
     "l4": [1, "face"], "l5": [1, "face"]},
    {"pixel": [103, 66], "l1": [4, "left_eye"],
     "l2": [3, "eyes"], "l3": [2, "upper_face"], "l4": [1, "face"], "l5": [1, "face"]},
    {"pixel": [103, 141], "l1": [5, "right_eye"],
     "l2": [3, "eyes"], "l3": [2, "upper_face"], "l4": [1, "face"], "l5": [1, "face"]},
    {"pixel": [124, 98], "l1": [6, "nose"],
     "l2": [4, "nose"], "l3": [3, "mid_face"], "l4": [1, "face"], "l5": [1, "face"]},
    {"pixel": [153, 103], "l1": [7, "upper_lip"],
     "l2": [5, "mouth"], "l3": [3, "mid_face"], "l4": [1, "face"], "l5": [1, "face"]},
    {"pixel": [167, 129], "l1": [9, "lower_lip"],
     "l2": [5, "mouth"], "l3": [3, "mid_face"], "l4": [1, "face"], "l5": [1, "face"]},
    {"pixel": [85, 13], "l1": [10, "hair"],
     "l2": [6, "hair"], "l3": [4, "hair"], "l4": [2, "hair"], "l5": [1, "face"]}
  ]
}
```

<div id="fig-32" style="text-align: center; margin: 20px 0;">
  <div style="display: inline-block; border: 1px solid #000; padding: 12px; background: #fff; width: 65%; box-sizing: border-box;">
    <img class="img-fluid" src="{{ site.baseurl }}/assets/img/modern_glom/sample_221_stacked_levels_3d.png" style="width: 100%; height: auto; display: block; margin: 0 auto;" alt="Figure 32">
  </div>
  <p style="font-size: 0.9em; text-align: left; margin-top: 8px;"><b>Figure 32.</b> The 5 predicted level maps stacked along a z-axis (L1 finest at bottom, L5 coarsest at top), making the part-whole merging across levels visually explicit: individual parts (eyes, nose, mouth) at the bottom converge into a single face region by the top.</p>
</div>

[^1]: which acts as a single feedforward approximation of an EM iterative clustering algorithm as in DeepSets\[[11](#ref-zaheer2017deep)\]
[^2]: GLOM is derived from the slang ”glom together” which may derive from the word ”agglomerate”\[[1](#ref-glom)\]
[^3]: These assumptions are not necessary, but they help reveal internal mechanisms. As we proceed further, we will try to relax them\[[22](#ref-hinton1977relaxation)\].
[^4]: which means we  want it to stay on the hypersphere.
[^5]: It was replaced by feeding top layer activations of a layer in a *previous timestep* into  a lower layer at next timestep. However, this requires backpropagation to take a time-out and unfold the computational graph to form a directed acyclic graph.
[^6]: r is set as a hyperparameter, or locations of vectors $$v_{p}$$ attends to could themselves be learned
[^7]: We tried to use the same net as a top-down and bottom-up net, but it did not work as well as keeping them separate.
[^8]: This is different from slow-fast weights, here one weight is actual knowledge, other is the ‘change’ required to modulate it.
[^9]: A principle that in turn is inspired from echo chambers.
[^10]: Thus folding is the operator of gluing together multiple representations, whereas unfolding is the operator for separating them back into individual pieces. This is inspired from how gluons in physics bind multiple quarks together.
