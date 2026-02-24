---
layout: post
comments: true
title:  "Navigating Peer Review like a Pro 😎"
description: "How to navigate peer review as a phd student?"
date:   2026-02-23 11:00:00
---
> 
Peer review is meant to be double blind. This means you don't know who your reviewers are. Your reviewers dont know who you are. And you can exploit that anonymity to your advantage.
<div style="border: 3px solid #FF0000; padding: 20px; margin: 20px 0; color: #FF0000; font-family: 'Courier New', Courier, monospace;  font-weight: bold; line-height: 1.4;">
  First a disclaimer: All the advice in this article is risky, controversial, and not safe for work. Skip if you are less than 18 years of age. Everyone deserves an equal playing field. This is not a substitute for hardwork/genuine research. Use sparingly. 
</div>

<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/peer-review/arjuna.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        >
</div>

In earlier years of my phd, when i was freshly minted out of my college,  i thought that i will change the world (and win a nobel prize). I had a big ego problem, and thought there is no one greater than me (like arjuna in the left side of the photograph). My hands were not folded in humility that time. Therefore, God had different lessons in store for me. 

It `only' took 2 rounds of broken shoulders, two visits to ER, one week of stay in a hospital, academic probations, losing my mom to cancer, a semester off from PhD, to reach this state of clarity. So, i wish that no one else has to learn the bitter lesson i learnt the hard way.

Here is how a typical peer-review cycle went : 1) Got a lot of bad reviews 2) Felt upset, and stayed in bed for a whole day binge watching movies. 3) abused the reviewer who gave bad scores, felt he didnt understand anything 4) complained a little bit to my advisor, threatened i will leave my phd (as if i am doing him a favour by doing phd in the first place). At this point, i have threatened my advisor so much, he doesnt care that much lol. So don't threaten that often, otherwise it doesn't work. 5) withdrew the paper if it is not salvagable, and resubmitted to the next venue. 6) forgot my worries for the next two months, until this cycle repeated, and i come back to 1). I stayed in this loop for around 3 years of my phd, and never made any progress. 

To make matters worse, when other people got into tier 1 conferences, it hurted my ego. I never could understand what made them successful. Chances are, you are also stuck in a similar loop, and don't know what to do. You think that peer-review is a "random" game, where most of the reviewers are incompetent and you just landed a bad set of reviewers. You attribute someone else's success to `luck', or 'they had a good day'. You have successfully managed to fool your brain into such an illusion. Congratulations. 

So, today we will try to  ask: what makes some people good at the game of peer-review? Are there any heuristics, we could learn from them, and apply to our own research? On surface, it seems pretty simple: do good research, write good papers, and you will sail through peer-review. However, the reality is sad: good research gets rejected, stupid papers get orals. 

In the beginning i learnt a lot from Devi Parikhs [amazing advice](https://deviparikh.medium.com/how-we-write-rebuttals-dc84742fece1). Additionally, time taught me a few more things which appear to work well on the reviewer 2. The reviewer who will burn your paper to ashes. The reviewer who gives a strong reject, with a confidence of 5. Who is unwilling to budge. He will take down your paper. He will flip the reviewers who supported you. He needs some special "rajat kind" of handling. I will try to explain that mechanism here:


- black ops analogy: imagine yourself as a part of swat team. Your reviewers are your targets. Your job is to hunt them. That requires precision. We will build a fortress first. 

Designing fortress (bulletproofing paper).

- Your paper should inherently use terms like "kindly note, please note...". It intuitively lowers reviewer defence. A little politeness goes long way. 
- Setting baselines: If there is a paper in the area you work, copy their table. Those serve as baselines. Add all baselines uptil last 6 months. Sounds obvious, most don't do it. 
    - arxiv allows an option to download papers source code (in latex). just copy table code from there. Dont start drawing table again. 
- If it is a brand new problem statement, things get messy, take time to figure out realistic baselines. 
    - Maybe ask Gemini (or sota LLM)
- Set expectations: If you are from academia, mention the lack of resources. Do best to get the results. 
- Figures: Most people will tell you to have colorful figures. The most impactful papers have simple black and white figures (check word2vec). No colors. Psychologically, it tells reviewer, " my idea is so strong , i dont need a complex figure to explain it". Humans already live complex lives. Give them simplicity. 
- The illusion of identity.
    - Most people upload their papers on arxiv/twitter. That's stupid. Everyone knows your name. That backfires.  If you come from a company, or a big hot shot lab, you can play the prestige game. But, those who don't have it, cant play it. Anonymity is your weapon. 
    - The key is to psychologically install a `potential identity' in the reviewers mind. Mirror the style of other labs (that's not forbidden!!). 
    - A very famous example is hinton, notice how all his slides, and figures have a pale yellow background. That's his signature.  
- Stupid cartoons don't survive test of time. So do stupid titles. 
    - People put smileys, robots , cartoons in figures. Dont do that. Be mature. 
    - People like the word "machines". Give them machines. Boltzmann machines. Perception Machines. Time Dilation Networks. Neural Nets in Superposition. Artificial Karamuto Oscillatory Neurons. See what i am doing?
- Detach your worth: Psychopaths don't get attached to their target. Don't be attached to your paper. Use third tense: "this paper reveals", "this work shows", "Results suggest that this phenomenon is true".
    - The illusion you want to pass is that you did the work, results came, and anyone can reproduce it. You have discovered some universal truth, a law of nature which machines emulate. Your job now is merely to report the results. 
- People use "will", u shall use "shall": Replace 'will' with `shall'. 
    - Why does relegious scripture sound so authoritative? Because jesus "sayeth", man "witnessed". Behold o reader, let reviewer witness your paper. (Sounds cheesy, i know, but it still works) 
- Don't claim sota: Speak less, show more (really important!!). In contributions never say you beat sota. 
    - Beat is too rough. If the person whose method you beat ends up as your reviewer, it will hurt his ego, he'll give reject. 
    - Say "we demonstrate competitive results over prior state of the art".
- Never say we 'solved' a problem, say we `tried' to solve the problem. 
- Write future work in limitations section instead of writing limitations.
    - People will tell you it's wrong. My advisor taught me this counter-intuitive trick. 
    - In rebuttal you can write: "we apologize that we showed optimism/came across as enthusiastic in our limitations". Our limitations are <>.
        - This creates a reverse psychology. Gain one more point in your favour. 
- Create a flop matched baseline: In ablations, include one line that your method's improvements are not due to simply increasing the no of parameters, and you actually checked by training a larger model of the baseline. 

- Overdress up your method by some silly name: Let's say you are just selling a MLP which takes time as input. It is just a stupid MLP. 
    - But, you `have to' call it "the dense-temporal encoder". Reviewers love fancy names. Give them that. Sells really well. (not that i prefer it, i can see right through bullshit)

- Imagine you have a method. It has two blocks. 
    - Draw a single teaser with those two blocks 
    - Then explain them one by one. Each section should contain its own figure for that block (credits:shehreen for advice)
    - Every subsection has 3 parts: Intuition, mathematical equation, and a takeaway.

- Techniques for `quick' tier1-publications: 
    - I don't appreciate them, but i will be honest: i did resort to them in my PhD. I have to promise myself not to do it again, and do actual research. 
    - Work on something with less data, partially labelled data, semi-supervised learning, constrained-settings. 
    - Open vocabulary also works. You can always strap an adapter to a big llm. And train it with a lora. 
    - build your own problem, own benchmark, and own models (nobody will care out eventually). play the "dataset and benchmark" game. 
    - extend image based models to videos, especially long videos, not many people do videos. 
    - robustness: corrupt inputs to models, check their robustness, techniques for improving them in real world. 
    - Freeze model, finetune some prompts. Call it "adaptation"
- Takeo Kanade came to our lab, he said: "only 3 people read your paper, you, your advisor, and reviewer'. Then, it dies a quick death once it gets published. Noone cares about it. Keep this in mind. 
    - Whatever you built is garbage if no-one uses it. No matter how smart you are. 
