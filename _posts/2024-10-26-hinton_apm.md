---
layout: post
comments: true
title:  "Asynchronous Perception Machine: A little godzilla's journey"
description: "APM is one of the first steps towards getting Hinton's GLOM working. The golden goose is how to encode part-whole hierarchies in a neural net"
date:   2024-10-26 11:00:00
---
> APM is one of the first steps towards getting Geoffrey Hinton's GLOM working. The golden goose is how to encode part-whole hierarchies in a neural net. This goose has now started to have some feathers and lay some eggs. This work was accepted to NeurIPS2024. Paper can be found <a href="URL">here</a>. And all it took was a MLP. There you go GLOM-haters. Chom chom. Hiyaaaaaaa!!!!!! 


<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\baby_hinton.jpg" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>
<div class="caption" style="text-align: center;">
    <b>Geoff Hinton as a baby</b> poses with an anaconda. conda activate <>, he cries. CONDA ACTIVATE <>, he yells. Godammn. But, conda keeps sleeping and then hangs in the terminal. Conda is unable to breathe. Its environment has become too polluted. Arghhh. Bad anaconda. Geoff hinton then takes out a whip and beats the anaconda. Whipppp!!! It still refuses to move. Something needs to be done about this. Something urgent. <b> Maybe a nobel prize? </b> Surely, he knew 60 years ago this day would come. 
</div>

<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\dino1.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>
<div class="caption" style="text-align: center;">
    A huge congratulations to <b> Dr. </b> Geoffrey Hinton for his nobel prize. One small step for a man, but a giant leap for mankind. Robotkind too. I, Robot.
</div>

My lovely PhD advisor Dr. Yogesh is a very strict, punctual and professional man. Every week, he wakes up early in the morning and makes me sit in his office. And then he glares at me from his ivory-spectacles trying to be all serious. I stare at the carpet and bite my lips. It's tough, but I have to remind myself constantly: "Not again rajat. Please don't laugh. Otherwise, he will get angry. Keep my mouth shut and listen.".
 
We don't want him to be angry. Took me two years to learn this simple lesson. Gosh, I wished I had learnt it sooner.

"Rajat, grow up. You are working on Hinton's GLOM.  GLOM= Geoff's Last Original Model. Shift all this non-technical stuff to your blog post. Be professional. How many times do I have to tell you? As always, you keep complaining and never listen. I am really worried about your research" says Dr Yogesh, as he `suits up' for his class. I can't help it, but he reminds me of barney in "How i met your mother" . 

You know what? he really takes all this stuff seriously. A lot of people are excited for computer vision after all. From outside, he is such a cutie-pie and an amazing teacher on whom a lot of girls crush over. Behind the scenes, he is a big godzilla who frequently unleashes his wrath upon little godzillas like me. Poor little godzillas.

As I gather my wits by what just happened, he swivels on his chair. Wheeeee. His desk is 45 degrees away from where I am s(h)itting, but within a constant slapping radius. Openreview is open on his screen for his review. He clicks a button and sends someone's paper back to where it came from.  Shooooo. 

Omg. That really hurts. He is correct, so it hurts even more. And no-one can help me. Who cares about a poor, underfed, and miserable graduate student? Everyone has their battles to fight, hills to climb, grants to write, phds to defend and tenures to track. It seems I have no choice, but to finally listen to him. 

So here we are. On this blogpost. You and me. Safe. Pinky swear. 


And so I will tell  you about this story  of a new model called "Asynchronous Perception Machine". 

Now, ill be upfront and honest: i dont have a grandiose story to tell. There is no eureka moment: Unlike the much cooler Ian goodfellow, i didnt go to a bar or code up APM in a single night. This is a 3 year long journey. And it has just begun. I don't know where it will take us, but if you choose to accept the mission (star trek), we will travel this bandwagon together. 

So the whole story began when Geoff Hinton put out two papers on arxiv. He thought people had become too boring, so why not bring some excitement to the table. This is not his first time hunting, he did it with backprop, alexnet too. It seems that he has a seasonal pattern of sorts: he resurfaces every decade or so and whips up a rollercoaster. And when geoff hinton speaks, we pause whatever we are doing and listen. Because, we want to stay on cutting edge of things and not become extinct like dinosaurs lol. 

So, the first one of his rollercoaster was GLOM, and second one was forward-forward. GLOM was an idea which was not working at all, and forward-forward was a learning algorithm only working well on a dataset of black and white digits. I talked to quite a few people over the years, and they told me:<b>"Hinton's a crazy old nut".</b> That was a big blow to us part-whole nerds and their underground clubs. (Shame Shame, Poppy shame to them!!)

In the perception community, there has been a long term cold-war going on. The clan-warriors can be split among two factions: 

1) <b>The connectionists, aka the cool hinton crowd</b>: guys who believe that brain contains these little neurons. So in a machine, just build some mathematical equivalent of these neurons, and learn the connection strengths between them. Suppose a neural net has to represent an object. Then the presence of an object is governed by some distributed representation that it triggers inside the network. They invented the backpropagation as their weapon: that neural nets with multiple layers could learn interesting internal representations, and overcome the limitations of frank-rosenblatt's perceptron. Frank's perceptron was just a single input layer, and single output layer, and didnt possess any hidden layers. Sad perceptron. But anyways, backpropogation seemed to do the job well. It also effectively shut those people who boooed connectionism. 

2) <b>The symbolists, i.e. the chom chom/minsky crowd</b>. They believe that there are symbols in the brain, like some representation of what an apple means like, what godzilla means like etc. So brain has all this interesting grammar for all these objects. This vocabulary is called symbols. Then these symbols interact with each other at lower levels, and some reasoning happens at the higher level. 

There has been a great deal of bloodshed on both sides. Countless soldiers have sacrificed their lives to their respective causes. <b>There is no clear winner</b>. People have lost hope. There is no settling this debate hmmmm. 

But now we are in the times of <b> peace and love and an occasional tease </b>. So, we need an interesting compromise. A peace treaty of sorts. Something everyone could be happy with. GLOM seems to offer just that. The only problem was that it was a mere philosophy.

> The difference between science and philosophy is that experiments
can show that extremely plausible ideas are just wrong and extremely implausible ones, like learning a entire complicated system by end-to-end gradient
decent, are just right.- Geoff Hinton, GLOM

Stupid ideas work, and everyone seems happy with them. After all publishing is an optimization problem right?: Maximize the number of tier 1 papers in shortest time and in least amount of investment. Who cares about quality and fundamentals, as long as the citation count is high? GLOM is intuitive, but was not working in practice. With APM, we try to rectify this problem and argue that what is in fact intuitive, can actually work better in practice. 

So, what is GLOM about, and how does it settle the debate between the warrior factions of connectionism and symbolism? For that we take a look at hinton's glom paper.

<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\glom_islands.png" style="width: 70%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>
<div class="caption" style="text-align: left;">
    Figure stolen with love. This illustrates the idea of <b>Islands of Agreement</b>
</div>

It talks about a new representation called islands of agreement, and a way to use these islands to somehow do machine perception. But, before we go deeper, we will label his figure a little bit. Trust me, it's a revolutionary idea. 

Let's say you are given an image of mona-sparrow. Something like this: 
<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\mona_sparrow.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>
<div class="caption" style="text-align: center;">
    <b> A mona-sparrow.</b> She is cut into four pieces, and each piece is numbered. This number can be a stupid positional encoding for all we care. 
</div>

And you then chop mona-sparrow into pieces and label those pieces as 1,2,3,4. So basically, each of this piece is a token you feed to the hinton's glom. This is how you feed it from the bottom:

<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\mona_sparrow_glom.png" style="width: 80%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>



<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\neurips_baby.jpg" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

There are still a lot more papers to be shipped to NeurIPS for babies. 

As turing concludes in his seminal paper, "We can see but a short distance ahead, but we can see plenty there that needs to be done". I have done it alone till now. This is a call to action. Please join the ship before it is too late. 

till next time,<br>
love,<br>
rajat



On this lovely rare-occasion, as Nobel prizes are being doled out to AI, which (according to some people) is NOT a fundamental science or a mere application of physics, we have curated a special series of little godzillas just for you. Each one of them took a lot of time, love, and effort to make. We shall now study these godzillas one by one:


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



## Future work

In future, we plan to make more humble godzillas. Each godzilla comes with its own outfit and ablation experiments. You can tell us which ablations you like, and we will combine those to form a nicely-dressed godzilla that remains competitive. One that is customized just for you. And we will do it for free. Without a GPU that is.

## Limitation  

Godzilla-making-addiction. Little godzilla is a mere mortal after all. Sometimes, godzilla is rejected from CVPR/ECCV because he cannot surpass SOTA. Little godzilla is also not that robust: he should be tested extensively in the real world. And for now, poor godzilla only does image-classification. That's not a "real" computer vision task. Godzilla needs to do dense tasks, reasoning and alignment also. And dont even get us started on the hard problem of consciousness. Is it really hard? Alas, only time will tell lol. 

## References
 <div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\godfather.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

"Hinton. <b>Geoff Hinton</b>. The <b>Godfather</b>. How to represent part whole hierarchies in neural nets".

What's next after nobel and turing😂? Fields Medal? Gotta catch them all. Perhaps, I dont need math, because maybe i can learn it with backprop. Or maybe Mars should be next. Really, I'm super serious this time. It's tough to decide. 

There are some rare instances when even NeurIPS panels don't understand what little godzillas are saying. But you cant blame little godzillas, they are still small and have a lot to learn. They dont even have a masters degree yet. For eg, you can play this video. 

Little Godzilla gets nervous easily, and just forgot what he had to say when he grabbed the microphone, he is not comfortable on big stages you know. So he lost his shit and blabbed all over the stage. Luckily there wasn't enough audience to notice little godzilla's nervous breakdown. Do notice the super-cute smirk and nose-wrinkle at timestamp :-). Splendid!!! Just in good-humour hehe. 

And now before i leave, and you go alll sad, i will dump a few videos we created for this project over the years. This jekyll blog is stupid and embedding these videos messes up the spacing. But that shouldnt prevent me from sharing cool stuff with you. So here we go,  

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 0;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/mlXzufEk-2E?si=y3Cw43OabskFb_Jn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 0;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/2yTltN_GZs4?si=3BZz2l3QU9EPhytd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>