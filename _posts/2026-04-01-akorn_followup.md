---
layout: post
comments: true
title:  " Some Unsolved problems on Part Whole Hierarchies and mere speculations "
description: ""
date:   2026-03-01 07:00:00
---


<!-- I'm 31 now. I still feel like a kid, but old in my bones. Everyone around me tells me to grow up, but i really don't know what that looks like :-). You can tell me when i do manage to lol.

I stand at a juncture of my life, where i have mentally `wrapped' up my PhD. The work is done, but as usual peer review crawls many years behind the actual progress. Reviewers keep arguing about small details like hyperparameters etc. It is easier to dole out rejects, and never answer rebuttals. However, the world keeps going on. Indeed, life is fleeting, and time is the only constant factor. 

I cannot help, but reflect further what i did over these 5 years. Did i focus on correct problems? Will they actually have an impact? Or will it fade away over time, as what happened to Nerfs, CNNs.  But, surely there are some abstract principles which shall not change.  -->


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Should we bet on Part-Whole Hierarchies at all? </span>

The biggest question is if one should bet on encoding  `part whole hierarchies` in neural nets. Indeed, there are high chances `it is a WRONG bet`. The reason i stick to it is that geoff hinton wrote about it [4 decades ago](https://dl.acm.org/doi/abs/10.1016/0004-3702(90)90004-J), and even [5 years ago](https://arxiv.org/pdf/2102.12627).

There are only two other people i know who took this seriously, to the point it acts as a constant `itch` in their heads, and really `irritates them`. First,   Jeff Hawkins in his book [Thousand Brains](https://www.amazon.com/Thousand-Brains-New-Theory-Intelligence/dp/1541675819). He eventually founded Numenta, and Celeste/Vivian/Sabutai (and team) there are doing some pretty cool work on theories of neo-cortex/ sparse-distributed memories. 

Similarly,  David Marr in his [Vision book](https://www.amazon.com/Vision-Computational-Investigation-Representation-Information/dp/0716715678), investigated the  nature of coordinate frames, and higher order shape representations in the brain. Surprisingly, Hinton spent a couple of decades arguing for shape invariance/equivariance of rigid bodies, thereby closing this love triangle.  

<!-- For now, indeed, it appears i am alone on this problem, but i will gladly but my eggs in this basket, for i have not yet found a better one.  -->

Here, we shall now merely attempt to `formally` lay down those problems (for anyone who `may` be interested). Some of these, are articulated in-verbatim from other papers and some are the ones  derived of our own musings. 

<!-- # <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Dispelling our notions </span>

First, we must dispel our notions. If you are looking for quick benchmark wins, quick ways to publish tier-1 papers, you better stop reading this post, for you shall not learn anything new. We are merely trying to improve our own understanding. -->



# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> The Problem lost to Knights Templar </span>

The problem we are interesting in solving can be explained with the help of a face. Please gaze at the face presented below. 


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/face.svg" 
        style="width: 40%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/face_canonical.svg" 
        style="width: 80%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

(a) For all sense and purposes, you will consider this face to be upright, at an angle of 90 degrees with regards to x axis. <br>

(b) We are interested in breaking this face into a part-whole parse tree. Basically, it is a data structure in which a lower `level 1` represents the parts, and  a higher `level 2` represents the entire face (whole). Each node in this tree consists of an arrow. For eg, here nose's arrow is also at 90 degrees, whereas arrow through lip is at 0 degrees. Thus, nose and lip are both perpendicular to each other. Similarly, nose is at the same angle as that of the face. <br>

This is an interpretation which we grow up to take for guaranteed. <br>

However, an alternate case is possible. <br>

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/alternate.svg" 
        style="width: 40%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>


It is possible to structure a tree in which the arrow through the face makes 135 degrees, nose 45 degree, and lip 135 degree. In such a situation, nose is at 90 degree angle to face, whereas lip/face are parallel to each other. 


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/canonical_lock.svg" 
        style="width: 80%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

Thus, from a face's perspective there are infinite lines which could pass through it's center. Similarly, infinite lines can pass through lip. 

Of those infinite lines, there is `only one 1 red line` which humans seem to prefer for the face as the choice of coordinate axis, and similarly for lip. However, in the image pixel space, there is no constraint governing "which" of the lines should be explicitly preferred by a neural network (since a face is a oval, and any line passing through the face looks identical).

We can call this problem as the problem of searching for a canonical lock. 






unstability till infinity 

oscillator visualization 

does not scale to higher dim 

analysis of encoding in phase vs magnitude 
 - destruction of info as we go deeper. 




inversion of part-whole 
    - fergus work 
    - my work 
    - their work 
    - why i was wrong. 



phase based multiplexing 


thinking that the features form hierarchy


how to evaluate it. 



marr's obsession with coordinate frames, hawkins, eventually hinton 


the canonical lock 


why it cannot be solved 




nlp connection in parse trees. 

no way to evaluate it 


why i should look at unconstituency parsing.. 



