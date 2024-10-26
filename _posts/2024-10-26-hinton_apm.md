---
layout: post
comments: true
title:  "Asynchronous Perception Machine: A little godzilla's journey"
description: "APM is one of the first steps towards getting Hinton's GLOM working. The golden goose is how to encode part-whole hierarchies in a neural net"
date:   2024-10-26 11:00:00
---
> APM is one of the first steps towards getting Geoffrey Hinton's GLOM working. The golden goose is how to encode part-whole hierarchies in a neural net. This work was accepted to NeurIPS2024. Paper can be found <a href="URL">here</a>. And all it took was a MLP.


<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\baby_hinton.jpg" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>
<div class="caption" style="text-align: center;">
    <b>Geoff Hinton as a baby</b> poses with an anaconda. conda activate <>, he cries. CONDA ACTIVATE <>, he yells. Godammn. But, conda keeps sleeping and hangs in the terminal. Conda is unable to breathe. Its environment has become too polluted. Arghhh.
</div>

My lovely PhD advisor Dr. Yogesh is a very strict, punctual and professional man. Every week, he wakes up early in the morning and makes me sit in his office. And then he glares at me from his ivory-spectacles trying to be all serious. I stare at the carpet and bite my lips. It's tough, but I have to remind myself constantly: "Not again rajat. Please don't laugh. Otherwise, he will get angry. Keep my mouth shut and listen.".

We don't want him to be angry. Took me two years to learn this simple lesson. Gosh, I wished I had learnt it sooner.

"Rajat, grow up. You are working on Hinton's GLOM.  GLOM= Geoff's Last Original Model. Shift all this non-technical stuff to your blog post. Be professional. How many times do I have to tell you? As always, you keep complaining and never listen. I am really worried about your research" says Dr Yogesh, dressed in a charming black-suit, as he suits up for his class. I can't help it, but he reminds me of barney in "How i met your mother" .

You know, he really takes all this stuff seriously. A lot of people are excited for computer vision after all. As always he is such a cutie-pie and an amazing teacher. 

As I gather my wits by what just happened, he swivels on his chair. Wheeeee. His desk is 45 degrees away from where I am s(h)itting, but within a constant slapping radius. Openreview is open on his screen for his review. He clicks a button and sends someone's paper back to where it came from.  Shooooo. 

Omg. That really hurts. He is correct, so it hurts even more. And no-one can help me. Who cares about a poor, underfed, and miserable graduate student? Everyone has their battles to fight, hills to climb and grants to write. It seems I have no choice, but to finally listen to him. 

So here we are. On this blogpost. A safe space. You and me. A safezone. Promise. And I will tell  you about this story  of a new model we developed called "Asynchronous Perception Machine". 

Now, i dont have a grandiose story to tell. There is no eureka moment: Like the cooler goodfellow et al, i didnt go to a bar, and or code up APM in a single night. This is a 3 year long journey. And it has just begun. I don't know where it will take us, but if you choose to accept the mission, we will travel this bandwagon together. 



<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\dino1.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>
<div class="caption" style="text-align: center;">
    A huge congratulations to Dr. Geoffrey Hinton for his nobel prize. One small step for a man, but a giant leap for mankind. Robotkind too. I, Robot.
</div>

On this rare occasion, as Nobel prizes are being doled out to AI, which (according to some people) is NOT a fundamental science or a mere application of physics, we have curated a special series of little godzillas just for you. Each one of them took a lot of time, love, and effort to make. We shall now study these godzillas one by one:


<div class="text-center" style="margin: 0 auto; max-width: 700px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\dino2.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>
This is a godzilla with a crown. He is used when he is doing well on some benchmarks. But most of the days, he looks like this when the experiments fail: 


<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\dino3.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

But there is no smile on his face, because he is sad that experiments didnt work. 

On an occasional weekend, things get too intense. Godzilla has to get out of the lab. His roommate has been very kind to take him to places, because godzilla does not know how to drive. Afterall, Godzilla is not invincible: there are things he cannot do alone. In return, Godzilla buys his roomate food. Food for the car's gas is the deal. Roommate happy, godzilla happy. Their wallet is happy. Win Win. 


<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\dino4.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

Sometimes, Godzilla has to read papers on the arxiv. But, he has poor eyesight. So, he resorts to wearing spectacles. Contact lenses dry up too fast. He gets long hair before paper deadlines, and godzilla even forgets to comb them. He gets all sweaty and smelly in those tough times. You really don't wanna annoy this version of him. This godzilla also looks like my friend Sarinda, although it's a matter of debate: Sarinda has long maroon hair and he says that this godzilla's hair are red. I don't agree. Maybe i am colour blind too lol.

p.s. shneaked in a little godzilla in our paper. sooo shorrry. Please don't tell my advisor. He'll be angry. We don't want him to be angry. Angry bad. Happy good. Mooooooo............. Ok, you can tell him, but after i graduate. 

There are still a lot more papers to be shipped to NeurIPS for babies. 

till next time,<br>
love,<br>
rajat

## Future work

In future, we plan to make more humble godzillas. Each godzilla comes with its own outfit and ablation experiments. You can tell us which ablations you like, and we will combine those to form a nicely-dressed godzilla that remains competitive. One that is customized just for you. And we will do it for free. Without a GPU that is.

## Limitation  

Godzilla-making-addiction. Little godzilla is a mere mortal after all. Sometimes, godzilla is rejected from CVPR/ECCV because he cannot surpass SOTA. Little godzilla is also not that robust: he should be tested extensively in the real world. And for now, poor godzilla only does image-classification. That's not a "real" computer vision task. Godzilla needs to do dense tasks, reasoning and alignment also. And dont even get us started on the hard problem of consciousness. Is it really hard? Alas, only time will tell lol. 

## References
 <div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\godfather.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

"Hinton. <b>Geoff Hinton</b>. The <b>Godfather</b>. How to represent part whole hierarchies in neural nets".

What's next after nobel and turing😂? Fields Medal? Gotta catch them all. Or maybe Mars should be next. Really, I'm super serious this time. It's tough to decide. 

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 0;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/mlXzufEk-2E?si=y3Cw43OabskFb_Jn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 0;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/2yTltN_GZs4?si=3BZz2l3QU9EPhytd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

