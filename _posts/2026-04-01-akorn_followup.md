---
layout: post
comments: true
title:  " On Unresolved problems of Part Whole Hierarchies"
description: ""
date:   2026-03-01 07:00:00
---

P.S. This is a speculative, scientifically inaccurate post, which does not surpass any state of the art .

P.S. The problem between science and philosophy is that extremely implausible ideas like gradient descent are just right, and intuitive ideas like part-wholes have proven to be incorrect. 


P.S. Indeed, we  `must learn` from sutton's bitter lesson: given enough data, a brute-force algorithm like transformer, can surpass anything we care to invent. 

P.S There is no way to deny that scaling leads to increased performance. 

---
`At this point, all we can do is wonder. And indeed, we have nothing respectable to show for it, even after half a decade (except APM by your truly)` 



# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> A risky  bet  indeed. </span>

<!-- `Hinton is a crazy old nut - A wise man.` -->


One of the big mysteries is if one should bet on encoding  `part whole hierarchies` in neural nets. Indeed, there are high chances `it is a WRONG bet`. 

One reason to still stick to it is that geoff hinton wrote about it [4 decades ago](https://dl.acm.org/doi/abs/10.1016/0004-3702(90)90004-J), and even [5 years ago](https://arxiv.org/pdf/2102.12627). And perhaps he deserves to be listened to, given the amount of successful bets he made, although some took decades to pan out. But, by all means, he is a winner.  

There are  only two other people  who took this issue seriously. By serious, we don't mean that someone spends two months on it, forks a github library, finds it does not beat a benchmark and then gives up. 

The seriousness we are concerned here with borders on borderline `obsession`, a constant aching `itch` in the head that something about AI is wrong.  One problem with `obsession` is that it leads to arrogance: you start thinking what you say is the only way, and there are no alternate paths. So, one needs to be careful as to not make such `blunders`. 


Who were those two people?


First,   Jeff Hawkins in his book [Thousand Brains](https://www.amazon.com/Thousand-Brains-New-Theory-Intelligence/dp/1541675819). He eventually founded Numenta, and Celeste/Vivian/Sabutai (and team) there are doing some pretty cool work on theories of neo-cortex/ sparse-distributed memories. Some curious comments on Numenta's work can be found [here](https://www.reddit.com/r/MachineLearning/comments/2lmo0l/comment/clykjsi/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

Similarly,  David Marr in his [Vision book](https://www.amazon.com/Vision-Computational-Investigation-Representation-Information/dp/0716715678), investigated the  nature of coordinate frames, and higher order shape representations in the brain. 

Finally, Hinton spent a couple of decades arguing for shape invariance/equivariance of rigid bodies, thereby closing this love triangle.  Please note Hinton never talked about dynamics of moving bodies, since that gets messy really fast. Proponents who claim to work on video, often add time as an additional dimension, and just create 3D versions of image models. 

So, we will stick to the same assumptions of `rigid bodies` for now, in spirit of original capsule paper (and Ramon Y Cajal :-)). For now, indeed, it appears we are alone on this problem, but we will gladly but our eggs in this basket, for we have not yet found a better one. And trust me, we have looked.  

We shall now merely attempt to `formally` lay down those problems (for anyone who `may` be interested). Some of these, are articulated in-verbatim from other papers and some are the ones  derived of our own musings, or discussions among the secret members of the knights templar. 

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
Consider the pen given above. There are two copies of the same pen. One pen represents the face. Another pen represents the lip.  Both the pens are having a `phase difference` in their motion.  However, their trajectory is `identical`. 

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


If the vector of the whole (face) and the part (lip) can rotate independently, the machine `must decide` over multiple iterations, what is the relative angle between them. 



To investigate this, we need to conduct some `thought experiments`.  For fun, we will treat this experiment as a `parody` of sorts between a part and whole. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> A single part and a single whole, in a `mutual` relationship together </span>


Let us imagine the most simple case, when there is only one whole and one part. Let's `imagine` data generating process $f$ produced two vectors $v_{whole}$ and $v_{part}$. These vectors are now going to undergo an `agreement protocol`, to decide what will be their relative orientations. Eventually, they will form little `islands of agreement`.


We are considering a timestep $t$ in GLOM. The part advertises a vector to the whole. Let's get into the parody. 

<div style="margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/single_part_advertise.svg" 
        style="width: 40%; height: auto; display: block; margin-left: 10vw; margin-right: 25vw;" 
        alt="Image 16"
    >
</div>


`Part: Dear nose, my vector is` $v_{part}$ `. I think you are my real daddy (whole)`

`Whole: Really dude, then you should look like me. Let me see how similar are you to me`

Whole takes $v_{part}$ and projects it onto itself. Lets call it $Proj<v_{part}, v_{whole}>$. 

Then whole substracts this proj from $v_part$ to get the component in the perpendicular direction. If that component is small, then it means $v_{part}$ is similar to whole. 

`Whole: Hey man, i just finished checking,   you are still a lot different than me, so i don't think you are my son. You better go find other dad`

Part went really sad. He really wanted to be whole's son. Rrecall that this was single part-whole case. If whole didnt accept him, he would be orphaned. And world does not look kindly to orphans.

`Part: You are the only whole left in my world . I really want to be your son`

`Whole: Geez. Then you gotta look like me`

`Part: Sure, what to do?`

`Whole: Ok, here is a value:` $Proj<v_{part}, v_{whole}>$, `subtract it from yourself, and you will become same as me`

`Part: Sure`

Part then does $v_{part} =  v_{part} - Proj<v_{part}, v_{whole}>$. Next time it shares the vector $v_{part}$ with whole, he accepts him as his kid. 


However, it creates a problem: <u>something we call collapse</u> in this messy business. Part and whole are identical vectors. A similar case happens when part in turn  `act as a parent` to a `sub-part` at a `lower` level. Basically, you can imagine every vector in the network starts looking similar to one other, and we have a big mass of  `homogenous population`. And where is the fun in life, if there is   `no variety`?

One other problem (or as i like to shamelessly call it a desirable property) here is that `part` was able to `rapidly` change its vector `in a single iteration`. It didn't need many iterations of learning. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Preventing collapse with non-linearity </span>


The problem where $v_{part}$ becomes equal to $v_{whole}$ could be solved by imagining a matrix $w$. Basically, $w$ multiplies this part $v_{part}$ and outputs a new vector $v'$. This v' should be similar to $v_{whole}$. 

If we make a simplistic assumption that $w!=I$, where $I$ is identity matrix, then we can prevent such a collapse. And indeed, if $W$ is a neural network with non-linearities in between, it is very hard for collapse to occur. 

So, the figure above now starts looking a bit like:

<div style="margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/bottom_up.svg" 
        style="width: 40%; height: auto; display: block; margin-left: 10vw; margin-right: 20vw;" 
        alt="Image 16"
    >
</div>

Let us call the $W$ matrix a `bottom-up network`, since it takes a vector from part, and transforms it into a vector $v'$ through which the  `whole` can measure the agreement. <u> Please note that the figure above refers to lip as part, nose as whole. Therefore, i shall internchangebly use $v_{part}= v_{lip}$ and $v_{whole} = v_{nose}$</u>

It now becomes important to look at the machine from two different perspectives. There are only minor differences technically, but it leads one to interesting interpretation.


<u> Perspective 1: The matrix w is NOT changed during agreement phase</u>




<div style="margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/bottom_up_inverse.svg" 
        style="width: 60%; height: auto; display: block; margin-left: 10vw; margin-right: 20vw;" 
        alt="Image 16"
    >
</div>


Here, the vector `part` advertises to whole is $v' = W v_{part}$. From whole's perspective, it `does not` have access to $W$. Then, the whole measures projection error $e =  Proj<v',v_{whole}>$. Next,  the whole needs to pass `some information` to the part so that it can make a correction. But, it cannot merely pass error $e$, since $v'$ was computed when it got transformed via weight matrix $W$. 


So, the `correct information` the whole needs to send the part is $W^{-1}e$. Let us now make the assumption, which is intrinsically wrong, but convenient:

`There exists an easy way to compute $W^{-1}$`

Once the part receives this information, it can make an update $v_{part}- e$. And voila, we have achieved locking!! What do we mean by locking?

<!-- --- -->


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> The condition for interdimensional lock. </span>

If the machine manages to achieve a perfect lock, the following constraint will hold. 
$W v_{part}$ will give $v_{whole}$. Similarly, $W^{-1}v_{whole}$ will give back $v_{part}$. We can check this by putting $W v_{part}$ in place of $v_{whole}$, which gives , $WW^{-1}v_{part}$, and indeed, the two W's cancel out, and we get back $v_{part}$. 


Next, let us tackle our earlier assumption. Is it possible to compute $W^{-1}$. Well, if bottom-up network is a neural net with many layers, each layer matrix $W$ can (in theory) be inverted. However, there are indeed cases, when no matrix exists. This means that the problem can be solved in two ways (i) either `force` bottom up net to have weights whose inverses are possible. (ii) accept that this is a issue, and find a way to `bypass` that. 

<!-- By now, you may know, that we are very `lazy😏😏`. So we will take a shortcut. 
Neural nets are like puppies: 🐶🐶🐶, they need to be  `constrained` properly. -->


<u> Perspective 2: Finding the alternate to computing $W^{-1}$</u>

<div style="margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/top_down.svg" 
        style="width: 50%; height: auto; display: block; margin-left: 12vw; margin-right: 10vw;" 
        alt="Image 16"
    >
</div>
 We can imagine that instead of computing $W^{-1}$, we have a top-down neural net with weights $W'$. Now, we can make two design choices:

[1] W is kept `fixed`. No learning. <br>
[2] $v_{whole}$ is kept `fixed`. <br>
[3] Only $v_{part}$, and $W'$ can be changed. <br>
[4] Architecture of W' is `mirror symmetry` of W. <br> 


A  learning algorithm  then modulates the weights of top-down network W' as follows: <br>
[1] First, $v_{part}$ is multiplied by $W_{bottom-up}$ to yield $v'$.<br>
[2] Next, the whole computes e = $proj<v',v_{whole}>$ <br>
[3] We feed-forward $e$ through $W_{top-down}$ network to yield  output $v_{out}$ <br>
[4] $v_{out}$ should be equal to $v_{part}$. If not, backpropagate error, and update top-down network $W'$


<u> Reasons behind mirror symmetry</u>: The top-down neural network $w'$ has to be forced to learn a weight matrix $w^{-1}$. The catch is that we `don't want` to take the inverse. Each layer of $w'$ is same as $w$. Let us imagine looking at layer l of both. 


We can then imagine enforcing $w_{l}w'_{l} = I$. Basically, multiply the matrices of both layers,and they should become the identity matrix. If you multiply this equation by $w^{-1}_l$ on both sides, 
you get $w^{-1}_l w_l w'_l = w_l^{-1}$, which simplifies to $ w'_l = w_l^{-1}$. <br>


This means that $w^{l}$ will `tend to` learn the inverse matrix. The `trick` here is that we never took inverse, but merely `forced` the product of matrices to become identity. One can then imagine doing this for `every` internal layers of $w'$. This is `only possible` when $w'$ is mirror image of $w$, thereby justifying the design choice of `mirror symmetry`. Since this involves aligning weight matrices together, we call this procedure `deep weight alignment`. Indeed, a very similar idea called `random feedback alignment` was also proposed by Timothy Lillicrap in his `Backpropagation and Brain Paper`. The mirror symmetry then becomes similar to bifold symmetry in DNA, and isomers/chirality of molecules. 

<u> Calibration of $w'$</u>: Once the weights of top-down network have been updated over several gradient descent iterations, it has become calibrated to $W$. At this point the part/ whole have a `relative rotation matrix` of $W$. 




# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Resisting the  temptation to supervise rotation matrix W </span>
<!-- <u> Perspective 3:  Resisting the temptation to supervise $W$</u> -->

Given a part, and a whole, there are `infinite` rotation matrices $W$ which could be used to transform the part into the whole. Which of those is the correct one? And again, this boils down to a `physical symmetry` question. One beautiful thing i realized, is that symmetries are all over the place. It is not merely a construct of physics, but a fundamental law of nature. 


There are only two plausible answers. Let us now consider both, for that shall reveal the next choice we must make. 

<u> Answer 1: There exists a UNIQUE $W$ for every pair <part/whole></u>

This school of thought believes that given a lip, and a nose, they should definitely lie perpendicular to each other (because psychological evidence points that every human favours this constraint). The matrix $w$ which makes those vectors orthogonal is the `only correct answer`. <br>

If we accept `orthogonality`, we can supervise bottom-up neural net to learn $w$ corresponding to that. This means that, we `know` in advance a  precise W for every pair of <part/whole>. And indeed, that is what `3D computer vision` does. 








<div style="margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/top_down.svg" 
        style="width: 50%; height: auto; display: block; margin-left: 12vw; margin-right: 10vw;" 
        alt="Image 16"
    >
</div>


<!-- w_l w'_{l} = w_l^{-1}$,  -->

<!-- which is $w'_{l} = w_l^{-1}$. -->


<!-- Basically, multiply the matrices of both layers, and they should become the identity matrix. If you multiply this equation by $w_{l}^{-1}$ on both sides,   -->









<div style="margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/part_symmetry_break.svg" 
        style="width: 70%; height: auto; display: block; margin-left: 10vw; margin-right: 10vw;" 
        alt="Image 16"
    >
</div>




<div style="margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/akorn_followup/inner_outer.svg" 
        style="width: 70%; height: auto; display: block; margin-left: 6vw; margin-right: 10vw;" 
        alt="Image 16"
    >
</div>


This is a <u>piece of underlined text</u> in my writing.


It advertises three or four possible `relative angles` that the lip/face could have relative to each other. 

Pictorially, this constraint is represented by:






# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Should parse-tree be linearized? </span>








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



