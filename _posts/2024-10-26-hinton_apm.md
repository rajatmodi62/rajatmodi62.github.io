---
layout: post
comments: true
title:  "Asynchronous Perception Machine: A little godzilla's journey"
description: "APM is one of the first steps towards getting Hinton's GLOM working. The golden goose is how to encode part-whole hierarchies in a neural net"
date:   2024-10-26 11:00:00
---
> APM is one of the first steps towards getting Geoffrey Hinton's GLOM working. The golden goose is how to encode part-whole hierarchies in a neural net. This goose has now started to have some feathers and lay some golden-eggs. This work was accepted to NeurIPS2024. Paper can be found <a href="URL">here</a>. And all it took was a MLP. There you go GLOM-haters. Chom chom. Hiyaaaaaaa!!!!!! 


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

So the whole story began when Geoff Hinton put out two papers on arxiv. He thought people had become too boring, so why not bring some excitement to the table. This is not his first time hunting, he did it with backprop, alexnet too. It seems that he exhibits a seasonal-pattern of sorts: he resurfaces every decade or so and whips up a rollercoaster. And when geoff hinton speaks, we pause whatever we are doing and listen. Because, we want to stay on cutting edge of things and not become extinct like dinosaurs lol. 

So, the first one of his rollercoaster was GLOM, and second one was forward-forward. GLOM was an idea which was not working at all, and forward-forward was a learning algorithm only working well on a dataset of black and white digits. I talked to quite a few people over the years about this, and they told me:<b>"Hinton's a crazy old nut".</b> That was a big blow to us part-whole nerds and their underground clubs. (Shame Shame, Poppy shame!! None of the donkeys will know your name!! I am a professional, even if they are not.)

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

It talks about a new representation called islands of agreement, and a way to use these islands to somehow do machine perception. But, before we define what are islands, what are these little arrows, we will label his figure a little bit. Trust me, it's a revolutionary idea. 

Let's say you are given an image of mona-sparrow. Something like this: 
<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\mona_sparrow.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>
<div class="caption" style="text-align: center;">
    <b> A mona-sparrow.</b> She is cut into four pieces, and each piece is numbered. This number can be a positional encoding for all we care. 
</div>

And you then chop mona-sparrow into pieces and label those pieces as 1,2,3,4. So basically, each of this piece is a token you feed to the hinton's glom. This is how you feed it from the bottom:

<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\mona_sparrow_glom.png" style="width: 80%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

Now we will start introducing some technical terms shall we. You will notice that the figure above has 6 columns. There are 4 tokens, and last two are trash cans. So basically, we only need to look at the leftmost 4 columns. Now, consider the token marked 1. Look at the column sitting on it. That column has 4 arrows and a question mark on it. What are all these arrows? The idea is that this column consists of 5 levels, at lowest level it might be representing the nose of the mona, and at the second highest level, it may be representing the entire mona lisa object. Therefore, the lowest level is representing a part and the second highest level is representing the object. 

Now, you will see there are a bunch of arrows. For eg, consider the three red arrows. Perhaps all those red arrows are representing the mona sparrows face. Now look at the lowst level, those  black arrows. Those might be just rgb pixels, and scattered together. The red arrows are in three of the boxes, and they are pointing in all the same directions. Same directions mean that they are all "agreeing" that it is mona sparrows face at that location. Therefore, this leads us to the following conclusion:
>> As we go up in the GLOM's levels, the amount of agreement increases. There are more number of red arrows at the second highest level which agree with each other, than the  black arrows at the lowest level. 

Next, you will notice that i marked the last level as <b>useless shit</b>. Why did we do that?

Here is the argument: the original idea in GLOM was that at the highest level of the GLOM there is a single representation, which represents the scene level information. So if you took images, say mona sparrow at your home, and mona sparrow in your school, the network will be able to understand the difference between the home and school. But, in practice, it seems very difficult to converge on a scene representation. This is also the reason why the research between  the computer graphics community (aka those neural fields) and perception community is split. The rendering community just focuses on rendering: how to model radiance fields. Their representation just keeps <b>changing </b> with the viewpoint. On the other hand, the perception community does not give a shit about radiance fields: they only model first four levels of glom, i.e. the object level. Not the last one. 

Now, we shall talk about another concept called  <b> The information bottleneck </b> principle. If you look at the figure, you will see there are equal number of arrows at each level (i.e. 6 arrows per level). This means that when information (aka mona sparrow) tokens are fed into the network, they travel through allll these levels and somehow result in these arrows. The number of arrows does not change across levels (there are 6 arrows per level in hintons figure lol),  so there is no loss of information. There is no  downsampling like the one which occurs in CNNs. 

The next insight in APM is as follows: <b> Each of the levels of the GLOM system corresponds to a different layer of the VIT, aka transformer </b>. This assumption works in practice, because in the transformer there is no bottleneck problem: there is no upsampling or downsampling of the input tokens. That remains faithful to the figure that hinton drew. Lolzy. We have marked that <b> L layers of a transformer (VIT) on the Y axis </b> in glom's figure. 

Ok, so now we need to learn all these arrows. Sometimes they are all red, sometimes they are black, and sometimes blue lol. So, how to learn them. Well, the answer is very simple. <b> Don't learn them lol </b>. They are already present in a transformer like Dinov2. Here is a figure that i stole from Shir Amir's paper yo:
<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\shir_dino.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

So if you look along the arrow i show, it shows that as you progress along the different layers of a DINOv2, the representations are pretty cool. At the last layer, all the representations of the DOG like ears, eyes, mouth have automatically given themselves some color. Note that this network was NOT trained with any class labels, just a simple self-supervised loss lol. So this told us that there was something interesting going on in the transformer, and it was able to automatically learn the object parts and their wholes. Somehow, we needed to exploit it. 

Like a cutie pie we are, we were parsing through hintons forward forward paper. And then, we case across this line:

>> A static image is a rather boring video - Dr. Geoff Hinton, Forward forward some preliminary investigations.

And when geoff hinton says something, we do that lol. 

So what did we do? We took a static image. We repeated it many times along through a temporal axis. Then it became a boring video that does not move. And then we gave this boring video to a video-transformer like Mvitv2. Note that this Mvitv2 was trained only for action-recognition, and no semantic information was being used here. So, we took a video and pumped through this transformer. We looked at the second or third layer of it, and selected the higher dimensional tokens corresponding to a particular frame. And then, a cutie pie told us to do three dimensional t-sne clustering on them. And so we did that lol. And this is what we get:

<div class="gif-container">
  <figure style="width: 500px; margin: 0 auto; text-align: center;">
    <img src="{{ '/assets/img/apm/island_hinton.gif' | relative_url }}" alt="Description of GIF" height="300px">
    <figcaption><b> Hinton's Islands of Agreement </b> were shown by us in Neurips2023. Don't they look all cute and beautiful? They are sooo high resolution. No semantic supervision. No boxes. No encoder. No Decoder. Just ya Little Mvitv2. Thku THku <b> Jitendra Malik.</b></figcaption>
  </figure>
</div>

So basically this showed that even lower layer in the transformer could give us such sexy islands. And they were soooo beautiful. And these islands were one of the levels in the GLOM. And if we got these islands from different layers in the transformer, they would serve as <b> free sources of supervision </b> for GLOM. So basically, it would tell each layer of GLOM what arrows are what lol. We dont need to learn them. They are already there. So we will <b> just distill representation from a transformer like Mvitv2 or Dino </b> in GLOM lol. 

Now we wish to redirect your attention to one thing. Notice that the islands in the above figure were obtained after repeating a static image along temporal axis to become a boring video. This is very subtle trick: To converge on a stable representation for a scene (in this case a static image), there are two ways you could go about it. The <b> first way  </b> is to look at the same image recurrently over many iterations. That will make the network know what is the best representation of this image. <b> This is what GLOM said in its original paper. It said take a image and do many routing-iterations on it. But, we don't wanna do that</b>. Instead, we do opposite thing. That is the <b> second way</b>. When we repeat the image along the temporal axis, the network looks at the multiple copies of the <b> same image </b> in <b> parallel  lolzy</b>. This operation occupies more memory but takes less time than having to do  routing in GLOM. And it gives beautiful islands. 

So all the above discussion can be now wrapped up in the following simplified figure:

<div class="text-center" style="margin: 0 auto; max-width: 900;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\zap.png" style="width: 100%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

Now is the time to visualize this whole thing. Trust me you cannot understand it otherwise. 

So, in the above figure, the trash can means that the input sequence is padded. So, we will be not concerned with any of the red marked region. We already know that the good source of supervision for all the remaining locations in the GLOM can come from a teacher. So let us imagine a teacher. And it can hop around the different locations in the hintons diagram and tell the GLOM model which arrow belongs to what location. This transfer of arrow (aka island) from the teacher to the GLOM is called ZAPPPPP!! 

But, there is one last thing in the GLOM diagram that we need to get rid of. Notice the GLOM's figure along the columns. There are four columns (each containing 4 arrows and a question mark in itself. ) In the original GLOM formulation, these columns were communicating among themselves, and telling each other what arrow goes where. But, in our case since the teacher is telling that information to each cell of GLOM, there is <b> no need for having these columns to communicate among themselves. No more routing lol. No routing, no attention. No attention, no memory issue. It's that simple. Hiyaaaaaaaaaa!!!</b>


But it really is not simple. If the columns dont communicate, how does the GLOM know that it is looking at left half of mona-sparrow, or right-half of her. <b>Afterall, machine perception needs all patches to communicate amongst themselves? </b> And that is the idea of attention right? And  using attention means using too much memory. We dont want to do this. So, we will do this another way. The above diagram can be changed as follows:


<div class="text-center" style="margin: 0 auto; max-width: 900;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\glom_col.png" style="width: 100%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

So each column of the GLOM is carrying the whole image in it. Since it contains all the image in itself, there is no more need of attention. The input already carries the context with it. <b> No more routing between columns. That will save memory.</b> Different columns can be numbered according to 1,2,3,4 etc. That way, by concatenating the global image (I, p), where p is the positional encoding, we can create a <b> strong enough </b> column representation for any location. So, the GLOM's architecture will now take this column representation as input and solve the following problem:

>> <b> Given the entire image as input, and a location in the hintons diagram, what is the arrow at that location. That answer can be given by a transformer as a free source of supervision and in this way GLOM can be trained. </b> 

So we now know that teacher is a transformer. The only problem left is what does the architecture of GLOM look like lol. And to put it together with the teacher and train the little boy. So the GLOM architecture now somewhat like this:

<div class="text-center" style="margin: 0 auto; max-width: 800;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\arch.png" style="width: 100%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>


We have a mona sparrow image. THen suppose we consider a single Column 1. The column contains entire mona sparrow, and positional encoding corresponding to 1. And then we give this column to MLP. And it screams an answer. That answer is wrong. The teacher zaps it. And MLP does several iterations on this column and then gives the correct answer. The process is repeated for all such dotted columns. 

We will look at the design of this column. 
<div class="text-center" style="margin: 0 auto; max-width: 1200;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\arch_col.png" style="width: 100%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

So this column contains a single cnn filter. We take mona sparrow and run cnn filter on it. That writes these patches to the column. And we can then generate a hardcoded encoding like 1, 2, 3, 4, attach it to column and in this way create a <b> location-specific</b> query for our little MLP. The learnable parameters of this whole little network are just in one CNN filter and one MLP. That's all. <b> No more attention lol. So much for a transformer. </b>. Thku transformer. We got rid of attention and kept your positional encoding. Positional encoding is all we need. Hiyaaa!!!!!

And the way it takes care of those chom-chom mouths is like this: CNN filter can be thought of as a device which writes <b> symbols </b> on the column. The MLP is akin to a turing machine which reads those symbols and processes information. The output of MLP is vectors. Reasoning is done by operating on vectors in the higher dimensional space, much aking to Word2Vec paper by Mikolov. The only difference is that mikolovs paper did that for words, and talked about analogies in the higher dimensional space. In APM/GLOM the vectors are for images now. 


And here is the final architecture for this cute-little model called Asynchronous Perception Machine. Little godzilla still keeps gazing at the simplicity of it.


<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\apm_arch.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>


<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\neurips_baby.jpg" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

There are still a lot more papers to be shipped to <b> NeurIPS for babies. </b> 

As turing concludes in his seminal paper, "We can see but a short distance ahead, but we can see plenty there that needs to be done". This is a call to action. Please join the ship before it is too late. In any case, this ship is being driven by at least one small mortal machine, for as long as he is on this planet called earth. 

till next time,<br>
love,<br>
rajat

------------------------------------------------------------------------------------------------------------------------------------------------------<br>

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

p.s. shneaked in a little godzilla in our paper. sooo shorrry. Please don't tell my advisor. He'll be angry. We don't want him to be angry. Angry bad. Happy good. Mooooooo............. Ok, you can tell him, but after i graduate. Not that he can do anything much. Neurips camera ready deadline has already passed lol. Hiyaaaaaaa!!!!!!



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

There are some <b> rare instances </b> when even NeurIPS panels don't understand what little godzillas are saying. But you cant blame little godzillas, they are still small and have a lot to learn. They dont even have a masters degree yet. For eg, you can play this video. This was Unireps workshop panel in NeurIPS 2023. <b> Do notice the super-cute smirk and pierced-nose-wrinkle between the  timestamps 1.00- 1.06 :-). </b> Remember to <b> go full screen, playback speed 0.25x and select the highest quality lol.</b>
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 0;">
   <iframe width="560" height="315" src="https://www.youtube.com/embed/b-cgktoep4M?si=yBHRTyl4nd9GGkIY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

<b> Splendid!!! Pure gold ehh :-) Just in good-humour hehe.</b> In his defence, Little Godzilla gets nervous easily. He is not that comfortable on big stages, you know. So he lost his shit and blabbed all over the panel. Shorry. Luckily there wasn't enough audience to notice little godzilla's nervous breakdown. 

And now before i leave, and you go all saaaad, i will dump a few videos we created for this project over the years. This jekyll blog is stupid and embedding these videos messes up the spacing. But that shouldnt prevent me from sharing cool stuff with you. Yes, you: the <b> bigger </b> godzilla. Little godzilla loves you. So here you go. 

All little  godzilla requests in return is protection from being schmidubered. Please protect him. Little godzilla is still small. Very small. Less than a GB of memory. Maybe little godzilla should go to big godzilla for protection and join his gang. Big godzilla has a nobel now, so he might be willing to give mafia protection. 

And before you start thinking that little godzilla is very creative, he isn't. He just stole the idea of folding and unfolding from big godzilla. The last line of big godzilla's paper talks about mental folding. Bulleted below. Hiyaaaa!!

 <div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\hinton_steal.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>

Ok, here are the videos I promised: 

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 0;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/mlXzufEk-2E?si=y3Cw43OabskFb_Jn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 0;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/2yTltN_GZs4?si=3BZz2l3QU9EPhytd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

And now, by the note of sacred academic-tradition, and the blessings of NeurIPS program committee itself, little godzilla hereby claims Yannic Kilcher's "Me-(GLOM)-ania". It's a cool machine learning system after all. (Ok you can claim it too, my lovely big godzilla, little godzilla has no problems  sharing :- ). <br>

<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\claim.gif" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>


It is late night now. Little godzilla will go brush and floss his teeth, gargle on a mouthwash, put on his (k)night-suit and go to bed on time. He becomes sick pulling all-nighters these days. He will hear big godzilla's lullaby which puts him to sweet dreams. Especially the old coursera lectures. Hiyaaaaaaaaaaaa!!<br>

<div class="text-center" style="margin: 0 auto; max-width: 800px;"> <!-- Set max-width as needed -->
    <img class="img-fluid" src="{{ site.baseurl }}\assets\img\apm\lullaby.png" style="width: 50%; height: auto;"> <!-- Image width is 50% of its parent -->
</div>
Big godzilla's lullaby in action. It helps little godzillas wake and then sleep again. Wake-sleep algorithm he he. Wait, the slide says Kevin Swersky. Alex Kryzhvysky. Swesky. Kryzhvysky. Zzzzzzzz.


love, <br>
rajat