---
layout: post
comments: true
title:  "Advice For Young Investigators"
description: "Advice For Young Investigators who are beginning their careers"
date:   2021-02-02 11:00:00
---

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/kajal/kajal.jpg" 
        style="width: 100%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
    <p style="text-align: center; font-style: italic; color: #dbcfcf; margin-top: 8px; font-size: 0.9em;">
        Kajal labours over his microscope. 
    </p>
</div>



# <span style="font-size: 1.5rem; color: var(--border-header-bottom);">An Existential Crisis</span>

I am 32 now. It appears i will soon wrap up my PhD. On the outside, i still appear young. On the inside, however, i feel a deep weariness in my bones. The last decade has been particularly hard. But it has been fulfilling in ways i never quite imagined. 

I like to think that i gained some learnings along the way, things which if i had known before would have made my journey a lot smoother. So i thought to pen them down. The reason is simple: there are many people around this world who want to contribute to science, and they aren't quite lucky to get the chance to work with good people. There is just not enough correct advice around.

The problem with advice is that you can find shit ton of it online: everyone is preaching themselves as a technical messiah, who seems to have cracked the secrets of AI. They call themselves `influencers, technical enthusiasts' and whatever cool name which gets likes on social platforms. This is a good way to farm good karma. It won't give you reliable piece of advice. 

We would like to remember Santiago Ramon Y Cajal (shown in the picture above). He is an old man who lived in the nineteenth century. He happened to get a nobel prize in biology. People know him as `father of neuroscience'. The reason we are interested in him is because he is exact opposite of what we think a successful scientist ought to be. He grew up in Spain, a country which didn't have much scientific establishment. He never went to best of the colleges. Yet, he did good science, inspite of working as assistant to a barber. Similarly, Alan Turing (and colleagues) did some of the best science of their time in Hut 8, and succeeded under miserable conditions of world war 2.  The reason was that they were 'driven' by a mission: to save the lives which would have been lost if the war had kept dragging on. 

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

Will they be your friends after they graduate and move cities/countries? Spouse is a different personal  matter, on which cajal goes into great detail. I will cover that later in this post. 

[5] How do get my name attached to big people? 

Work in their labs. But, it is not possible for everyone to have access. 

The second best way is to pick fight with the big people, and scientifically resolve it. Works really well lol. Check the gelato bet on Alexei Effros's page at UC Berkeley for a nice example. Remember, it is better to gain glory as a loser  in a big fight, rather than as a `no-one'. At least people know you tried. Learn to become a good loser. Humour helps a lot.  Remember, that appears to be schmidubers charm too. That's why women are attracted to him. 

[6] How do i gain collaborators ? I want my name on many papers. I am a paper production machine. 

Do solo work first dude. You need to be able to offer `value' to other person. 

[7] OMG. My citations are so low. I am not popular `enough'.

really? Ok, you can think about it, and it will become 1000 citations in a day just by thinking !!


Cajal calls these afflictions as `plague of the bind'. These questions  often weaken resolve, have no definite answers and prevent the mind from staying to problems which really matter. Learn to avoid these. They consumed years of my energy. Don't let is waste your life too. If you find someone engaging in them, point it out. If they don't listen , let them be. 






