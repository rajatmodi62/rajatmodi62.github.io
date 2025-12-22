---
layout: page
title: Talks
permalink: /talks/
includelink: true
---

{: style="color: red;"}
**I am currently on the job market and actively searching for new opportunities!**

I have given several talks over the years, which are linked below.


## Paper Talks

[1] [Making GLOM Work:](https://www.youtube.com/watch?v=Ab90OVre8ok)
GLOM was an idea by Geoffrey Hinton in 2021. Here, we discuss what were some key ideas towards getting it to work. <br>
[2] [Putting an End to End to End Gradient Descent:](https://www.youtube.com/watch?v=4nNsZ6Spw3E&t=1907s)
A learning algorithm which trains each layer of a neural net in 'isolation' greedily. Optimization is based on a local-constraint, and gradients are  'not propagated' among different layers. Each layer predicts activations for what will happen in the given input sequence 'k' steps into the future. Uses ideas from InfoMax principles from Van Oord et. al. Core idea is that the representation at current time step t, assumes representation at time t+k is positive sample, whereas t+k+1....t_k+N is negative.  <br>
[3] [Forward Forward Algorithm: Part 1/2:](https://www.youtube.com/watch?v=bnhT2aM2_nY&t=3081s)
Algorithm by Geoff Hinton. Neural net is optimized by piping input data sequentially with two forward passes 1) first pass involves positive data 2) second pass involves negative data. Each layer is trying to learn a separate classification problem of outputting high responses for positive data, and low responses for negative data. <br>
[4] [Forward Forward Algorithm: Part 2/2:](https://www.youtube.com/watch?v=yOf4vs1u2DI&t=1939s)
Discussions on philosophical ideas in Forward Forward paper, for eg, getting rid of gradient descent, optimizing neural nets in a single step with extreme weight updates, mortal computation. <br>
[5] [ComputerVision Talks: Asynchronous Perception Machine:](https://www.youtube.com/watch?v=6qpTrLBmeqM&t=2522s)
Explaining how APMs were a step towards getting Geoff Hinton's GLOM to work well. <br>
[6] [MLCollective: The problems with scaling up:](https://youtu.be/2yTltN_GZs4)
Discussing how scaling up presents a big issue to existing neural nets. <br>

## System Design 

The talks below are not of high quality, but merely for archival purposes. Better talks on these topics exist. <br>
[1] [YouTube Recommendation System](https://www.youtube.com/watch?v=zIIU8D-_jhM)<br>
[2] [Collaborative Filtering and Federated Averaging](https://www.youtube.com/watch?v=qS5YOfD9dJg)<br>
[3] [Tweet Generation System](https://www.youtube.com/watch?v=YpAv3CUL6HA)<br>

