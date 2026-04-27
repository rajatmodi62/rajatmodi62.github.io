---
layout: post
comments: true
title:  " Unsolved problems on Part Whole Hierarchies and mere speculations "
description: ""
date:   2026-03-01 07:00:00
---

P.S. This is a speculative post and may be scientifically inaccurate. 



# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> A risky  bet   </span>

<!-- `Hinton is a crazy old nut - A wise man.` -->


One of the big mysteries is if one should bet on encoding  `part whole hierarchies` in neural nets. Indeed, there are high chances `it is a WRONG bet`. 

One reason to still stick to it is that geoff hinton wrote about it [4 decades ago](https://dl.acm.org/doi/abs/10.1016/0004-3702(90)90004-J), and even [5 years ago](https://arxiv.org/pdf/2102.12627). And perhaps he deserves to be listened to, given the amount of successful bets, although some took decades to be deemed correct. 

There are  two other people  who took this issue seriously. By serious, we don't mean that someone spends two months on it, forks a github library, finds it does not beat a benchmark and then gives up. 

The seriousness we are concerned here with borders on borderline `obsession`, a constant aching `itch` in the head that something about AI is wrong.  


Who are those two people?


First,   Jeff Hawkins in his book [Thousand Brains](https://www.amazon.com/Thousand-Brains-New-Theory-Intelligence/dp/1541675819). He eventually founded Numenta, and Celeste/Vivian/Sabutai (and team) there are doing some pretty cool work on theories of neo-cortex/ sparse-distributed memories. 

Similarly,  David Marr in his [Vision book](https://www.amazon.com/Vision-Computational-Investigation-Representation-Information/dp/0716715678), investigated the  nature of coordinate frames, and higher order shape representations in the brain. 

Finally, Hinton spent a couple of decades arguing for shape invariance/equivariance of rigid bodies, thereby closing this love triangle.  Please note Hinton never talked about dynamics of moving bodies, since that gets messy really fast. Proponents who claim to work on video, often add time as an additional dimension, and just create 3D versions of image models. 

So, we will stick to the same assumptions of `rigid bodies` for now, in spirit of original capsule paper. 

<!-- For now, indeed, it appears i am alone on this problem, but i will gladly but my eggs in this basket, for i have not yet found a better one.  -->

We shall now merely attempt to `formally` lay down those problems (for anyone who `may` be interested). Some of these, are articulated in-verbatim from other papers and some are the ones  derived of our own musings, or discussions among members of the knights templar. 

Whatever progress will be made, might have to rest on the shoulders of [geometric deep learning](), and [graphical models for structured learning](). 
<!-- 
I am not yet knowledgeable enough  to build upon them. So, i will just cover what i think i do know. And hopefully, time shall give me more answers, that what i currently do have.  -->


<!-- # <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Dispelling our notions </span>

First, we must dispel our notions. If you are looking for quick benchmark wins, quick ways to publish tier-1 papers, you better stop reading this post, for you shall not learn anything new. We are merely trying to improve our own understanding. -->



# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> The Lost Problem of Knights Templar </span>

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

Of those infinite lines, there is `only one 1 red line` which humans seem to prefer for the face as the choice of coordinate axis, and similarly for lip. 

However, in the image pixel space, there is no constraint governing "which" of the lines should be explicitly preferred by a neural network (since a face is an oval/circle for fat guys like me, and any line passing through the face divides it into two identical semicircles, which means it has infinite symmetry). 


<!-- 
And geez, as we know, infinities blew cantor's mind😬😬😬, and landed him in [hospital](https://www.bsmath.hu/INSANE_MATHEMATICIANS.pdf). So, we need to remind ourselves again to be careful. -->


<!-- First, we have to give  this problem of infinity  a cool name.  -->

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> The canonical lock </span>


An alternate name is the `problem of rotating potatoes`, first posed in GLOM. Funnily, this is also the core reason that capsules `didn't` work. (Please dont tell me they ever did, i will just   `roll my eyes`. Merely stacking capsules, and training them to get sota results doesnt mean that they really work).

Now, we will try to define this problem.  
<div style="display: flex; justify-content: center; align-items: flex-start; gap: 20px; width: 100%; margin-bottom: 20px;">
    
    <div style="text-align: center; flex: 1; max-width: 45%;">
        <img 
            src="{{ site.baseurl }}/assets/img/akorn_followup/rotating_pen.gif" 
            style="width: 100%; height: auto; display: block;" 
            alt="face"
        >
        <p style="margin-top: 10px; font-weight: bold; font-family: monospace;">face</p>
    </div>

    <div style="text-align: center; flex: 1; max-width: 45%;">
        <div id="lip-container" style="width: 100%; height: auto; min-height: 10px;">
            <div style="width: 100%; aspect-ratio: 16/9; background: transparent;"></div>
        </div>
        <p style="margin-top: 10px; font-weight: bold; font-family: monospace;">lip</p>
    </div>

</div>

<script>
    (function() {
        // 3000 milliseconds = 3 seconds
        setTimeout(function() {
            var container = document.getElementById('lip-container');
            var img = document.createElement('img');
            
            // Adding a unique timestamp (?t=...) forces the GIF to start from Frame 1
            var timestamp = new Date().getTime();
            img.src = "{{ site.baseurl }}/assets/img/akorn_followup/rotating_pen.gif?t=" + timestamp;
            
            img.style.width = "100%";
            img.style.height = "auto";
            img.style.display = "block";
            img.className = "img-fluid";
            
            // Clear the placeholder and add the image
            container.innerHTML = '';
            container.appendChild(img);
        }, 3000);
    })();
</script>
Consider the pen given above. There are two copies of the same pen. One pen represents the face. Another pen represents the lip.  

Computationally, you can think of these two pens as two vectors rotating in a higher dimensional space. For clarity, here we can assume those two vectors in the 2d space. 

At any moment, the rotations of these two vectors is `independent` of one another. Now let us further `imagine`, again a face consisting of nose and lip. 


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/face_o_1.svg" 
        style="width: 80%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

The picture (left) above assumes that the lip is horizontal, nose is vertical, mutual angle is 90 degrees. On the (right), we rotate the image by a little bit. Both the lip, and nose rotate a little bit, but the `mutual` angle between them remains `constant`. For the purpose of this post, we shall only focus on 2D images, and their rotations. 


We will `not` focus on a 3D scene with two images belonging to same scene , but with differing viewpoints. 

Similarly, now consider the image below:


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/face_o_2.svg" 
        style="width: 80%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>


Here we choose two `different` vectors which may pass through nose/ lip. (left) vector through nose is horizontal, and through lip is downwards. (right) even thought the face rotates, the mutual angle is ninety degrees. 

On surface, we may ask: `hey dude, why look at a face, why not real world image?`. The reason is that such a thought experiments helps abstract away a few principles: 

[1] Internally, a computational model of brain would rely on vectors, which can exchange information with each other. The way these vectors interact, leads to the internal structure. 

[2] If the vectors of face, and lip rotate independently, and are given the `freedom` to choose whatever they want, there is `no meaningful structure` we may learn. 

[3] If the vectors of face, and lip rotate together in a space such that the `relative orientation` between them remains constant, then we may learn `something` meaningful.  

[4] The relative magnitude of orientation between these vectors matters.  In other words, we need to be able to understand whether one is lagging behind or moves forward with respect to another. 


This becomes evident in picture (i) where if we assume the basis vector to be the line passing through the lip, the nose makes `+90 degree`. Whereas in picture (ii), the same constraint of `+` sign holds. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> The machine must choose among `one` of the many plausible relative angles (hypothesis) between parts and wholes </span>


If the vector of the whole (face) and the part (lip) can rotate independently, the machine `must decide` over multiple iterations, what is the relative angle between them. For our purposes, let us image that there is a single part (lip). It advertises three or four possible `relative angles` that the lip/face could have relative to each other. 

Pictorially, this constraint is represented by:





By synchronization we mean, that the 


 Imagine the pen to be an arrow which is rotating constantly in a spae. 

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



