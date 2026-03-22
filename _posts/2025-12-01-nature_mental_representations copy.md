---
layout: post
comments: true
title:  "On the necker-cube illusion and superposition of representations"
description: "Discussions on mental rotation, and other psychological experiments conducted by hinton back in the 80's"
date:   2026-03-21 11:00:00
---
Discussions on some optical illusions and other experiments conducted back in the 1980's.

>> You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions. Never consider yourself to be the cause of the results of your activities, nor be attached to inaction. 



<!-- <div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/decahedron.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div> -->


<!-- <div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/dec_top_down.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div> -->
<!-- 

<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/dec_square.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>

<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/dec_alternate_frame.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div> -->
<!-- <div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/dec_hex_model.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>
<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/cube_on_table.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>

<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/cube_representation.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div> -->

<!-- <div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/hex_rec_flaps_original.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>
<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/hex_with_rec_flaps.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>
<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/hex_with_flaps.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div> -->
<!-- <div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/hex_with_flaps_annotated.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div> -->

<!-- 
<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/necker.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>
<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/necker_1.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>
<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/necker_2.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div> -->

Today, we will discuss about two kinds of optical illusions which still trouble the best of cognitive scientists. The relation between cognitive science, and neural nets is that of perception: the way our brain sees, is the way, a neural network ought to see. 

Consider, for a moment, a variant of necker cube presented below. Stare at it, for upto 5 minutes. You will start to notice something weird. 

<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/rec_necker.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>

Your brain starts oscillating between two states. For eg, here is  one plausible state you observe. The stuff marked in the red, is the bottom. Thus, we observe the face marked as black, as the top face. 
<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/rec_necker_1.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>

Alternatively, our interpretation of the cube can flit. Now, the bottom becomes the top, and top becomes the bottom. 
<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/rec_necker_2.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>

The key point is: at a particular time, we can only see `one' of these plausible interpretations. For some reason, our brain keeps oscillating between these two. This means, that although it found one explanation of the plausible input, it is not satisfied. It waits for a moment, and quickly switches to the next plausible interpretation. 


For our purposes, we shall hence term the internal representations of this nature as `switching representations'.


A plausible interpretation in energy models is that the model converges to a fixed energy point. But, it stays static, and its weights remain fixed at the time of inference. Thus, existing neural nets, don't show this switching behaviour. However, gases in a container can change their states multiple times at a constant sample pressure, volume, temperature. 

Now, we must distinguish this representation from the field of test-time-training. In TTT, the model's weights change during inference, but only if it is given some external input. In a container of gas, an isolated system, with no connection to external environment, can still adjust it's weights. 

There is another class of representations possible. 

<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/square_diamond.png" 
        style="width: 80%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>

Please consider the shapes (i) and (ii) shown above. Intuition suggests that (i) is a square, and (ii) is a diamond. However, an alternate interpretation may be possible.

The shape shown in (iii) can be obtained by rotating the diamond in (ii) by 45 degrees clockwise. Thus (iii) is a diamond. Similarly, the shape in (iv) can be obtained by rotating square (i) by 45 degrees clockwise. Thus, (iv) is a square.

However, both shapes (i) and (iii) look identical.

This raises the question: are they a square OR a diamond?. Please pause to think for a moment.

The answer is that they are both. It depends on the choice of the viewpoint (canonical frame) we may impose. For eg, in (i), the dotted line (canonical frame) is vertical, hence it is a square. In (iii) the dotted line is at 45 degrees, hence it becomes a diamond. It  may suggest that a single shape (i/iii), can  simultaneously be `both' square and a diamond. This ability of an object to exist in two (or infinite) such states together, is  known as [superposition in physics](https://www.youtube.com/watch?v=vYlZoKIfZcM)


Thus, this kind of representations, which allow a similar shape to hold multiple plausible meanings at the same time can be known as `superpositioned representation'.


Next, we describe the differences in these two kinds of representations. 

In 'switching representations' , the physical structure of the object actually changes (like the necker cube illusion). In `superpositioned representations', the structure never changes physically. 

Autoregressive models like LLMs belong to `switching representations'. As soon as you compute the output word (say w1), you can condition the network (on w1). The next representation the network predicts is different than if you sampled a different word (w2), and conditioned it. Since, the representation changes, it thus belongs to the family of 'switching representations'.

The second class, a.k.a superpositioned representations have only recently been explored (check anthropics blog on toy models in superposition)



<!-- <div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/shear.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>
<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/equilateral_three_fold.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div>
<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/mental_rotation/equilateral_two_fold.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Your image description">
</div> -->


