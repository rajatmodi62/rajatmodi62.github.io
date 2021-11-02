---
layout: post
comments: true
title:  "On building emotions into machines."
description: "For a learning machine, 'possessing emotion' and 'predicting emotions of others' are two different things. We try to understand more about how a human brain can be modelled computationally as a society of emotion-based agents."
date:   2021-01-21 11:00:00
---

> I see your infinite form in every direction, with countless arms, stomachs, faces, and eyes. O Lord of the universe, whose form is the universe itself, I do not see in you any beginning, middle, or end.- Says Arjuna to Krishna 

I am deeply troubled by how we think about the emotions being modelled into intelligent agents. Researchers think that emotions can be treated as a problem of prediction, where a machine can learn to  'look' at a person and infer his emotions. They describe the ability to detect emotions better as being equivalent to the goal of becoming more humane. Consider how Winston et al explains the operation of a robotic arm in form of traversing a goal tree:

<div class="text-center">
<img class="img-fluid" src="{{ site.baseurl }}\assets\img\emotion-in-machine\0.png">
</div>
<!-- <div class="caption">
    Detail of the face of Mona Lisa showing the use of sfumato, particularly in the shading around the eyes. Source:Wikipedia
</div> -->
<div class="text-center">
<img class="img-fluid" src="{{ site.baseurl }}\assets\img\emotion-in-machine\1.png">
</div>
The above figure shows a situation where we devise a mechanical arm to arrange blocks into a tower. A typical step for a machine would be simple, it has to start somewhere and search for the block to be added. However, this ADD operation consists of several granularities:

<div class="text-center">
<img class="img-fluid" src="{{ site.baseurl }}\assets\img\emotion-in-machine\3.png">
</div>

The machine would need to find the exact region where a block is present, and then pick up the block and place the block on top of a block in the tower. Thus, the process of building a tower can be broken into a subtree of goals. This tree could then be traversed in a postorder. 

Now, the problem in Winstons approach starts from coming here. An outside observer would analyze Winstons robotic arm from two perspectives:
1. Outside: The arm does cool things. It is intelligent. 
2. Inside: The arm only follows a goal tree. It is a sequence of well defined steps, thus the machine is not truly intelligent. In other words, it cant still form a goal tree for itself , given the specification of a task. Nor, can it write the subroutines to fulfill those subtasks. 
This concept is illustrated by the diagram:

<div class="text-center">
<img class="img-fluid" src="{{ site.baseurl }}\assets\img\emotion-in-machine\4.png">
</div>

It is wrong to create an illusion of intelligence into the machine, when in fact does not have true intelligence. This is what all statistical inference is doing- fitting large no of parameters on a blind input. We need the ability to build a generic nature into our machines. The answer is to understand the basic workings of our brain. 

The first question you might pose is why do we really need an intelligent machine. Minsky answers it by saying that our lifespans shall increase to 200 years. Then, most of us shall become old and we would require intelligent agents to take care of us. Now, do we prefer a machine that responds to our emotions through its actions, or do we need a machine which truly understands the fluctuations of our brains. The answers is latter. 

The current approach of neuroscientists to understand the brain at a structural level (through modelling interconnections) is fundamentally wrong. The first reason is that a brain contains thousands of neuron synapses, which all of them interconnected. Modelling the transmission of electrical impulses is impossible, since the best MRI machine can do is measure the diffusion rate of chemicals. Also, even if we resolve the structural view of our brain down to a single neuron, it fails to explain the principle of how do the thoughts occur from a collection of neurons. Physically, a neuron represents a typical cell. But, when these cells form groups, a certain phenomenon of thought becomes evident. If a group, is a collection of neurons, then shouldn't it show the properties of its constituents instead of new concepts like thoughts.  We know for a fact that a single neuron does not hold a stream of consciousness. This means that we cannot explain human thought (or hope to model it) unless we can devise a working theory (from computational viewpoints) of how our minds work. Till now, the progress could only have been made in vision, since an image on our retina triggers activation of our visual cortex. Scientists can model this through magnitude of electrical impulses recieved in pre-frontal cortex and use those theories into neural networks. However, the thoughts in a human brain can come even when no sensory input is there (you can think, even while staring at a wall).  This can create activations in random parts of the brain, which is impossible to decipher (in case of visual image, the parts of brain formed an image. But, we dont have visual techniques to explain activations in terms of thoughts]. Thus, isolating a precise region of brain which explains a particular thought seems to be a fundamentally difficult task. [although we have some rough idea of what fear centres in brain look like].

Parsing through Minsky and Turing's work, a fundamental theory of how brain might work has started to reveal itself. To, illustrate those concepts I shall explain the functioning in form of scattered thought experiments. Forgive me , if the ideas appear to be disconnected for the very nature of our intelligence comes from a diffused thought. Seemingly simple ideas combine to paint a beautiful image of human psyche like a mosaic. 

### Experiment 1: Do you remember all you learnt in the childhood (the true meaning of common sense)?

If i ask you, how the buildings are built. We would take for guaranteed that the buildings can be build by bricks. This "obviousness" of our brains, is in fact the curiousness which we have when we build a toy tower in our childhoods. However, over time these concepts get ingrained in our psyche, which becomes part of our selves. 

Thus learning occurs in brain in two stages. First, we learn simpler concepts which seem difficult. Finally, we learn higher level concepts on top of them & 'forget' that we ever learnt the simpler concepts in the first place. (obviously, while thinking about buildings, we only think bricks. We dont think how we stacked toys in childhood). Thus, the overall processing which occurs at a higher level, comes through the learning which has already occured at lower level. Since, this lower level has already been learnt the processing for higher level is almost instantenous, thus accounting for how we think blazingly fast. (Said lord krishna to arjun: O partha, the mind is as swift as horses & light, for it can reach the vast expanse of the cosmos at one moment, and your surroundings in other). However, the current CNN architectures stack lower level layers under higher order concepts. Everytime a forward pass is made, the network has to recompute the lower representations. This is exactly opposite of how human thinking works, which is what troubles me. 

### Experiment 2: Consider you are playing with blocks. Your arms are working, and following the goal tree i showed above. Now, you become confused about which of the two blocks to choose. At the same time you are hungry. Would you keep on figuring out how to choose blocks or would you go ahead and eat food, and later resume the thinking process?

This experiment illustrates the fact that there are separate agents in the brains controlling 'hunger' and 'block playing'.  Something is switching between these two things. While we are playing with the blocks and encounter the conflict, we tend to focus more on whether we are hungry or not.  Once our frustrations reach a certain level, we 'interrupt' our block playing and switch to quench our hunger. 

Now, consider that these two activites i.e. block playing and hunger are governed by two separate agents. Each agent is responsible for following its goal tree. When the conflict occurs in one of the agents goal tree (i.e. the play block agent), the other agents tend to take over(the hunger agent). Hence, our brains can be thought of a society of agents, each of which are constantly preempting their functions. 

### Experiment 3: Do brains re-use agents 

If each brain region is specialized agent, this means that there must be a limit on max no of different tasks we perform. However, this is not true. This means that an agent in fact can participate in several different goal trees. So, suppose an agent (a localized part of the brain) switches different functions. How will it remember the set of all possible goal trees it must be a part of? It appears, that then it must possess a local memory. 

The next order of business, has to be to build these individual agents and devise a sort of switching mechanisms between their goal trees. Each such agent will possess a local memory which tells it which goal tree it is a part of. But, still this does not explain how the 'ether of thought' which arises in human brains could be modelled.  We need to account for the meaning of 'self' and 'consciousness' and how it can be explained in a society of agents. 

Another important question is that the 'play blocks' has its goal tree. At it's level their had been another agent (hunger). But how was the first agent triggered (play block was triggered initially even if child was slightly hungry)? We might say that the baby saw a toy and his play-blocks goal tree became activated. However, thoughts can still come without stimuli (blank wall stare). So, what we are missing is a way to select among agents of same level. Will try to think on it next time.  

rajat 