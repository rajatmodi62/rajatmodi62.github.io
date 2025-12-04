---
layout: post
comments: true
title:  "On energy based models"
description: "Course notes of stefano ermons lectures at stanford"
date:   2024-10-26 11:00:00
---
Course notes of stefano ermons  CS230 lectures 11/12/13 at stanford.

>> The sun illumines the world, but the light is one. Similarly, the energy of the Supreme illuminates the whole world, and yet the energy remains one.


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/animation.gif" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Animation GIF"
    >
</div>


If you are like me, you don't understand how the diffusion models work. In fact, you tried reading it, but it didnt just make sense. The math just seems crazy, and it just seems like you have to memorize it to ace those interviews lol. Recently, i had the privilege to audit stanford CS230.  It is taught by Dr. Stefano Ermon, who also happened to be coauthor of several diffusion papers. So, without further ado, let us get in the trenches and learn directly from him. Here we are going to talk about **Energy Based Models**, namely lectures $11, 12,13$. 

<div style="text-align: center;"> 
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        >
</div>

The core purpose of energy models is that they are very flexible. Consider that your input data comes from a ground truth distribution named as $p_{data}$. The aim of the model to learn a model $p_{\theta}$, which wants to approximate this $p_{data}$. So during learning, we will be given several iid samples $x_1, x_2, .....x_n$. We want to "fit" $p_{\theta}$ on it, and form a generative model. So, if we sample images from it, we should get new images never seen during training. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-1.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 1"
    >
</div>

What are the properties that we want our model $p_{\theta}$ to satisfy. For now, let us call $p_{\theta}=p(x)$. For a given image $x$, the probability should be greater than $0$. Let us assume there are one million input samples, our model $p_{\theta}$ will spit out a million probabilities. The sum of these probabilities should be $1$. The next question becomes: How to choose the model $p_{\theta}$. In practice, several kinds of models are possible. As you can see in the slides, the output of $p_{\theta}$ is passed through an activation function $g_{\theta}$. So, there are several ways to choose this activation function $g_{theta}$. For eg, it can be a quadratic function, exponential function, mod operator, or a log sigmoid. Anything will work in practice. 

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-2.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 2"
    >
</div>
In the figure above, you see a pie. Intuitively, that pie represents a volume. Each slice of the pie represents the probability of occurence of a particular input sample. In case of million of samples, our pie consists of infinitesmal small pieces, the sum of which should be equal to entire pie. So let us say, that we pass a particular sample through the network, and get a value of 2. To calculate the probability of that sample occuring, we need to know the size of the total pie. This appears problematic due to two reasons: 1) you will need to feed-forward all plausible input samples to get their values (and hence the volume of the pie). This is not possible in practice, since we don't know all the plausible images in the world. This means, it is not possible to get the total size of the pie which is denoted by $z(\theta)$ here. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-3.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 3"
    >
</div>
The way around this huddle is to assume that the "output" of a neural network, follows a preknown probability distribution. So, for sanity, let us assume that our output is defined by $g_(\mu, \sigma) = e^{\frac{(x-\mu)^2}{2\sigma^2}}$. This is equation for a gaussian distribution. Now, we `analytically' can integrate this function over a plausible values of $x$, and get $\sqrt({2\pi\sigma^2})$. Note that this calculation required us to make an assumption: i.e. the outputs of our neural network follow a normal distribution. On surface, it seems weird to make such an assumption. On the other hand, the law of large numbers says that if we take a lot of samples, they tend to follow a normal distribution. So, it means that our assumption might not be wrong.

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-4.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 4"
    >
</div>
Assuming that we can integrate our $g_{\theta}(x)$ analytically, it becomes easy to calculate the likelihood $p(\theta_{x})$ by simply dividing  $g_{\theta}(x)$ by its total volume $z(\theta)$. This $z(\theta)$ is also known as a partition function. Now, one can imagine that there are several such "neural nets" modelling $p_{theta}$. We can cascade several such learning blocks in increasing order of complexity. For eg, one option is to consider a mixture of models, with one model parameterized by $\theta$ and other one being $\theta^{'}$. Similarly, we can imagine a cascade of neural nets, where output of 1 net goes to input of another. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-5.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 5"
    >
</div>
The most relevant way to define a model is to use an exponential function, where output of the net $\theta$ is raised to the exponents power, and divided by $\int e^{f_{\theta}(x)}dx$. The denominator term is called the partition function. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-6.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 6"
    >
</div>
It is very hard to calculate this partition function in practice, especially when the input variable x can take many values, or is high dimensional.(For eg, x can be an image, even a image of $32\times 32\times  3)$ dimensions comes out to be 3072 variables, which makes computing the partition function to be a really difficult job). Also note that computing the partition function requires knowing the entire set of $x$, which is really difficult to do sometimes. Lucky for us, there are some tasks possible where we don't need the partition function at all!!
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-7.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 7"
    >
</div>
Let us assume we are given two samples $x$ and $x'$. Each of their likelihoods will involve the partition function. But, if you take their 'ratio' the partition function cancels out. So, what this means is that we can do tasks where we require `comparisons' between relative occurences of two-samples, and not knowing their 'actual' probabilities. This has generally found application in LLMs, which are trained to model the relative ratios between different human responses. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-8.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 8"
    >
</div>
So consider the leftmost figure. If we are given image of cat, and a text caption saying it is cat, the resultant energy of the system is low (low energy means high likelihood). Similarly, we can think of other tasks where two images could be compared for eg, image restoration, which we discuss next.  
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-9.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 9"
    >
</div>
We shall now describe a kind of image denoising model called Ising Model. Assume that we are given a corrupted image $x$ and we wanna denoise it to a clean image $y$. So, we want to learn a discriminative model $p(y|x)$ or a generative $p(x,y)$. Modelling $p(x,y)$ is better since it also encodes the distribution of $p(x)$, as well as $p(y|x)$. A key property of ising model is that the output $y$ has each pixel either 0/1. This is discrete ising model. Continuous versions also exist, but that is not the subject of this lecture. So, the figure presents a $3 \times 3$ model. Note that, the $x$ input is the observed variable. We wanna learn a one-to-one mapping $<y,x>$, i.e. how does each y change give a particular x. Another constraint is that the nearby pixels of y $y_i,y_j$ should be smooth. These two terms are the constraints in the above equation. Note that $<x_i,x_j>$ is not modelled, because the input $x$ is already observed in practice. 

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-10.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 10"
    >
</div>
We shall now describe this idea of product of experts, which was originally invented by Geoff Hinton. Assume that you are given three models $p,q,r$, we want to somehow combine their predictions. The notion of combining is same as how democracy works: multiple people vote together to reach the consensus, and provided a large no of votes are captured, the individual bias, and noise gets cancelled out, and leads to a stable prediction. Therefore, the joint probability is given as a 'product' of these experts. Note that the notion of expert means that one model specializes in some task, another model specializes on another task etc. So when such a model seems an input x, it somehow has to decide, which of the models (p,q,r) will specialize in it. This requires a selection mechanism to be inbuilt inside the neural net. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-11.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 11"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-12.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 12"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-13.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 13"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-14.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 14"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-15.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 15"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-16.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-17.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 17"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-18.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 18"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-19.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 19"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-20.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 20"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-21.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 21"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-22.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 22"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-23.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 23"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-24.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 24"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-25.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 25"
    >
</div>

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-26.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 26"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-27.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 27"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-28.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 28"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-29.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 29"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-30.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 30"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-31.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 31"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-32.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 32"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-33.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 33"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-34.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 34"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-35.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 35"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-36.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 36"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-37.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 37"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-38.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 38"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-39.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 39"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-40.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 40"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-41.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 41"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-42.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 42"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-43.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 43"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-44.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 44"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-45.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 45"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-46.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 46"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-47.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 47"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-48.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 48"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-49.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 49"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-50.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 50"
    >
</div>

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-51.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 51"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-52.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 52"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-53.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 53"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-54.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 54"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-55.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 55"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-56.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 56"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-57.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 57"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-58.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 58"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-59.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 59"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-60.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 60"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-61.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 61"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-62.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 62"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-63.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 63"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-64.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 64"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-65.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 65"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-66.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 66"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-67.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 67"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-68.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 68"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-69.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 69"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-70.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 70"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-71.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 71"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-72.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 72"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-73.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 73"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-74.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 74"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-75.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 75"
    >
</div>
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-76.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 76"
    >
</div>


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/animation.gif" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Animation GIF"
    >
</div>
