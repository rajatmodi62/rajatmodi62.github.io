---
layout: post
comments: true
title:  "Cajal's Advice For Young Investigators"
description: "Advice For Young Investigators who are beginning their careers"
date:   2021-02-02 11:00:00
published: false

---

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/kajal/kajal.jpg" 
        style="width: 100%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
    <p style="text-align: center; font-style: italic; color: #dbcfcf; margin-top: 8px; font-size: 0.9em;">
        Ramon Y Kajal labours over his microscope. Gazing at it long enough allows him to probe deepest secrets of the universe. 
    </p>
</div>



# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">An Existential Crisis</span>

I am 32 now. Almost half of my life has passed by. It appears i will soon wrap up my PhD. On the outside, i still appear young. On the inside, however, i feel a deep weariness in my bones. The last decade has been particularly hard. But it has been fulfilling in ways i never quite imagined. 

Of the half that remains, I would like to think about the learnings i gained  along the way. If i had known these things beforehand, it would have made my journey a lot smoother. So i thought to pen them down. The reason is simple: there are many people in similar shoes. There is just not enough `correct advice' around. 

The problem with advice is that you can find shit ton of it online: everyone is preaching themselves as a technical messiah, who seems to have cracked the secrets of AI. They call themselves `influencers, technical enthusiasts' and whatever cool name which gets likes on social platforms. This is a good way to farm good karma. It won't give you reliable piece of advice. 

We would like to remember Santiago Ramon Y Cajal (shown in the picture above). He is an old man who lived in the nineteenth century. He happened to get a nobel prize in biology. People know him as `father of neuroscience'. The reason we are interested in him is because he is exact opposite of what we think a successful scientist ought to be. He grew up in Spain, a country which didn't have much scientific establishment. 

He never went to best of the colleges. Yet, he did good nobel-worthy science, inspite of working as assistant to a barber. Similarly, Alan Turing (and colleagues) did some of the best science of their time in Hut 8, and succeeded under miserable conditions of world war 2.  The reason was that they were 'driven' by a mission: to save the lives which would have been lost if the war had kept dragging on. 

Chances are your conditions are a lot better than them. You live in a time of peace. You might wiggle out of the argument saying `they were geniuses, so managed to get quite a lot of work done'. You might be correct, but there are high odds that is just an excuse:  you 'do not have' courage to face your laziness and incompetencies (indeed, i still don't have that). You might also argue that you need 'a lot of GPU resources for ai'. You will do well to remember that connectionists of the past (hinton) worked on CPUs, and still invented backpropagation, mixture of experts and all the basics we still use today. 

Thus the ability to do good science only `in part' depends on one's financial condition. I beg of you, please don't let  it  be your excuse. A man who wants to make excuses will never be happy no matter what you give him. A man who just wants to work will eventually find a way. It is that simple. 

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">The Mindset</span>

The mindset of a young investigator should be `i want to do good work, and make contributions that outlive me'. This is a very important property, the 'lack' of which has killed many scientific careers even before they even started. 

If your motivation is `i need a lot of  money after i finish my studies and lead a comfortable life', it will not work out in the long run. The reason is pretty simple: you will run after what is popular and find yourself trapped. You will feel like  a little boat which is forced by the waves of the sea in whatever direction it wants you to go. 

Once you go after where everyone is going you realize: what unique things do i bring to the table? You will be at the mercy of homogenization: your work, and your achievements will be identical to the ones around you. If there is no differentiating factor, how can you hope to get things which others wish for, but never manage to get? You might be willing to settle for an ordinary life. It's a perfectly reasonable option, but it might not be as fullfilling. 


A PhD is a terminal degree, but don't let it  terminate your future scientific work. It is merely a  'license to practice': you have a formal acknowledgement of the institution that you produced 'some science'. People `might' listen a bit more seriously, had you never gotten it in the first place. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">The chicken egg problem</span>

You might find yourself trapped in the following dilemma: you just started your career. you want to work with good people. But, those people require publications and good work to even consider you. But, you  `cannot do good work' without them guiding you. And just like the question of whether the egg/hen came first, you are endlessly trapped in this loop. Years pass by, and you realize that you have been kicked out of the program. Is there a way to break this loop?

First, you must know the good researchers in your field. Read their papers. Print them. Underline them. Tear them. You must know what they did, and why they did it. Most papers 'hide' the 'why they did the thing they did'. You must learn to extract those secrets. A good way is to read those papers, and run their code. Reproduce their numbers. Ask AI to explain that code. Open their code on a monitor, and code it yourself by typing the words on a keyboard. Dont just copy-paste, since that kills understanding. 

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">Papers who have `no' code still deserve to be read</span>

There is another weird thing going around in community: `if someone does not release code, their paper is not good'. While this may be true, learn to separate the signal from the noise. 

It is good to remember some of the most fundamental papers like backpropagation never came with explicit code from authors: they just worked. Aim to write your paper in a clear and succinct manner: even if you don't share code, the results should be reproducible. An unfortunate reality is that many people resort to cherry picking results, or fabrication. Please avoid those, if you ever hope to have a scientific career. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">The three levels of research</span>

Make sure you understand at what different levels ai research operates. 

[1] Benchmark level: Understanding why existing models fail. Most people think benchmarks are not good contribution. That's not true. Benchmark reveals what our next technical efforts should be redirected towards. However, a note of caution here: don't get into endless trap of benchmarking. It is good to know how to break models. But, it is amazing to try and fix them. There are many problems in this world. It is the solution that matters. 

[2] Algorithm level: You will find most people take a popular architecture (say transformer) and apply it to their own domain (say medical AI). `Novelty' is then defined in a specific subarea: nobody used transformer in this area before, so your paper gets accepted. It turns out that this approach works in short term. 

The problem however is that architectures keep replacing each other. As soon as a new kid is on the block, people will go to use it. Your work will be forgotten. Such is the nature of science. Progress comes on the shoulders of the giants who stood before us. 

[3] Abstract Level: This is the most difficult level to operate at. People who work here generally ask: what are the `general principles' which might hold across any learning machine? What properties can machines still not achieve? How does nature do it? How do i build a computational model which 'mimics' those properties in a machine?

The issue with this approach is: 1) you must have an ability to connect across fields, and force people of different communities to talk with one another. This kind of thing automatically happens if you are in a system where many researchers sit together in a common space. For the young investigator it presents a problem: he is often alone. My only advice: claude is your friend. Ask it what you need to ask. The problem however is `what to ask it'?

Before i answer this question, make sure you decide which level you want to operate at. It is tempting to choose [3] but it is hard. [1] is easier to do, and more worthwhile. It requires grunt work (often years on end), but it does pay dividends. Don't get carried away by those who [2] on a variety of different problems: they have breadth, but might lack depth. 

Let me also mention other thing i observed: when i began, i thought neural nets have nothing to do with physics. They are just cute little things you train on computer vision tasks. In my mind, computer vision reigned supreme, and machine learning took a later spot. 

Now i have realized: the principles of learning are governed by laws of thermodynamics. Statistical learning theory is based on probability. Digital machines are based on boolean algebra. Together, thermodynamics, boolean algebra, and proababilities are fundamental sciences. Find a mistake and break one of them. Once you find a loophole, the whole castle will come toppling down. And OMG, it is just so much fun lol. 

I will now give you a 'magical' term: symmetry breaking. Find a way to break it everywhere. The key skill is realizing what does `symmetry' mean. Turns out their is no precise answer, it just comes from intuition lol. Don't treat boltzmann, or shannon or turing as gods: they were people far ahead of their time. But surely, they may have made at least one mistake? Your job is to find that. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">Don't get emotional. Grow up. </span>

Our young investigator is often driven by passion, emotions, and hormones (yours truly included). The logic often takes the backseat, or entirely gets thrown out of the window (yours truly again :-)). Some examples of emotions are:

[1] What will happen to my paper? Will they reject it? OMG, i put so much effort. Stupid reviewer does not understand it. Peer review is purely `random'. The system does not work. 

It works. And it has saved me on multiple occasions. And it will save you too.

[2] There are so many successful people around me. What is special about me?

Nothing is special. IQ tests are fake. Now get to work .

[3] What does my advisor think? How do i please him?

Will you marry your advisor and babies with him? Please get to work. 


[4] What do my friends/spouse think? 

Will they be your friends after they graduate and move cities/countries? Spouse is a different personal  matter, on which cajal goes into great detail. I will not cover it here. But i will just say i dont agree with cajal: his remarks are too derogatory to women , and it is not at all acceptable in these times where both spouses should have `equal contributions' in household chores and rearing of the children. 

[5] How do get my name attached to big people? 

Work in their labs. But, it is not possible for everyone to have access. 

The second best way is to pick fight with the big people, and scientifically resolve it. Works really well lol. Check the gelato bet on Alexei Effros's page at UC Berkeley for a nice example. Remember, it is better to gain glory as a loser  in a big fight, rather than as a `no-one'. At least people know you tried. Learn to become a good loser. Humour helps a lot.  Self-depreciation works wonders to bond with others. 

[6] How do i `gain' collaborators ? I want my name on many papers. I am a paper production machine. If i dont get 5 icml/iclr/neurips/cvpr/eccv in a year, i will die.

Do solo work first dude. You need to be able to offer `value' to other person. Otherwise, you are just a baggage. Everyone in this world has to pay a 'tax'. Be willing to pay it. Often, in comes with low pay and long hours. Own it. Don't fight it. But, don't allow tax to turn into exploitation. It's a delicate balance. 

[7] OMG. My citations are so low. I am not popular `enough'.

really? Ok, you can think about it, and it will become 1000 citations in a day just by thinking !!

[8] my group only got 8 papers in xx conference. Other dude got 20 papers. My students are not working hard enough. let me pressure them. 

dude, you should be grateful that you are in a position to mentor people. Secondly, please fix your self esteem. Spending a night in a homeless shelter will do wonders for you. Get out of your ivory tower, and live with less privileged for a day. Wear used clothes. you will know what hardship really means. 

Cajal calls these afflictions as `disease of the mind'. These questions  often weaken resolve, have no definite answers and prevent the mind from staying to problems which really matter. Learn to avoid these like a plague. They consumed years of my energy. Don't let it waste your life too. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">The public performer </span>

Our young investigator is indeed notorious: he can invent all sort of curious ways to get distracted and feed his ego. 

One of the ways goes as follows: 1) he gets his paper accepted 2) he posts a message on linkedin 3) people like it 4) he constantly tracks how many likes he got 5) the more the better. 6) then, he looks at people who checked his profile 7) he messages people who followed him. 8) checking instagram/email often. 

Often our young investigator will also operate under the `illusion of being a mentor': he will build a group of people who know less than him, and  'mentor them'. The fact they listen to him gives him great source of pleasure.

 The issue is that there is no one telling the group leader what all he does not know. In that case, the group only "learns" what the routing node (aka the leader) knows. The achievements of the group are then limited by the leader. The students never outshine the master. A true master (yoda) however becomes happy when his students solve things that he could not solve alone. The first is a parasitic relationship and drains energy. The second is a self-sustaining relationship (which i like to call as the recirculation mechanism), whose constituents are vibrant personalities. 

Be really wary not to become a public performer in your early career. A certain presence is required later on to establish an ecosystem and give a place for young minds to grow. But, if you are starting off, perhaps you don't need social media. (Although you can use tiktok to post your gym photos ). A young scientist trapped in a laboratory will spend `best years' of his life alone. SO there is indeed a need to mate, an endeavour we ourselves didnt have much success in. Keep making friends, and hanging out. Don't let research become your grave.  

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">The trust issues </span>

Let us imagine that our young investigator goes to work under someone 'famous'. He is very happy at the opportunity. But, when he arrives at the laboratory,  he is deeply disappointed: he is given a boring task, which has nothing to do with what he actually wanted to do. He spends his energy trying to argue with his mentor. In this act, he loses peace of his mind, and energy which would have been better spent on the scientific pursuits. The mentor begins to doubt the mentees ability to complete non-trivial tasks, does not trust him, and never teaches him the deepest darkest secrets of the art. 

The issue here is patience: 1) the mentor is famous due to a reason 2) the mentor is simply 'testing' the young man's resolve. There is a common misconception in the young investigator's head: his value is measured by his skillset. If he is most skilled, he will advance further than others. However, this is not true. The true thing that matters is 'compliance': are you easily coachable or do you have an ego the size of a  balloon? Are you there to advance your agenda or your mentor's agenda? Technical skill can be taught, character cannot. 

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">The mistake of thinking you outgrew your mentors </span>

Let us imagine that our dear investigator is wildly successful in his endeavours. He has managed to accumulate many papers, many orals and  tier-1 internships.  Now, he will start thinking their mentor is a 'does not understand' their work anymore. While it may be scientifically accurate, the issue at hand is ego. 

I beg of you, don't let it get to your head. Remember who made you what you are. Remember their sacrifices. Remember their belief when you were a `no one'. Unfortunately, most people treat their phd's as a transaction: you do xx papers, and then you graduate. You leave your mentors, and never talk to them again. It DOES NOT work like that. Make sure your mentors become your collaborators, and not people you lose with your success. Otherwise, like Steve Jobs you will lay at your death bed and find it hollow. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">Everything you were taught is wrong</span>

It appears that AI undergoes shifts over every five years. RNNs overcame LSTMS. Transformers overcame LSTMS. Mamba (sorta) overcame Transformer. AI is pretty young: chances are everything you know about it is wrong. My advice is `be suspicious'. Question everything. 

Let me give you an example. People told me MLPs cannot do segemntation. I showed in my APM paper that you can do that. People told attention is fundamental. I showed you can do same computation with a shared MLP across locations. People thought we need data augmentation/routing. In making GLOM work, we got rid of all of it. Indeed, now people are realizing we don't need all this fluff. Yann lecunn recently removed layer norm too. Takeru/sindy got rid of mccullough pitts neuron. 

At this point, i am deeply suspicious of backpropagation, contrastive learning, and gradient descent. I think it all needs to go away. 

Do not make the mistake of thinking that science is a democracy. Opinions of most may turn out to be wrong. The only real thing that matters is the code, and the results. If you can see computational effects which you hypothesized about, then opinions of other people become irrelevant. Once i realized this fact, my life got a lot smoother. You must have one or two people you implicitly trust. For eg, a few people whose 'head' you can 'pick' ,to validate your own intuitions. Keep hunting for such people. But, be aware, that there are not many such people. At the highest levels, posturing does not work. Only the truth matters.

There is some whose opinion matters more than the democracy: for eg, 'originator' of a particular concept. Let me take an example. Say you have a problem with graph convolutional networks. You go and talk to Thomas Kipf. If he agrees, chances are your intuition is correct. It does not matter what others around you think. I have noticed that people who invented a particular thing have often the most depth about that particular concept. Don't shy away from emailing `big people'. What's the worst that can happen? They won't reply. But if they do, it will change/validate your line of thinking. The potential of reward seems obvious. Yet, most young investigators  tend to self-reject before hitting send. 

