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
Let us now assume that such experts exist. For eg, one expert specializes in generating a woman, one specializes in generating young people, one generates smiling people etc. So, you can combine the outputs of all to generate a smiling young person (and they look very beautiful lol, i wish i had a girlfriend like that). 

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-12.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 12"
    >
</div>
Geoff hinton could not stay still, so he invented another kind of machine called the restricted boltzmann machine. It contains two set of units, visible units and hidden units.  Each input pixel is connected to N*N possible outputs, which means this would generate an image of size N by N. The boltzmann machine is called restricted because it does not connect input/output units among themselves. Neither does it consist of more hidden layers. The key reason behind this was that at that time, it was not clear how to train neural nets of more than one layer (since backpropagation was not invented yet). 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-13.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 13"
    >
</div>
Another variant was deep boltzmann machines. It consists of multiple hidden layers. Training is done in a greedy way, first layer is trained, and frozen, the output features are used to train second layer and so on. Note that this procedure of greedy layer by layer training was ultimately replaced by alexnet in 2012, which used backpropagation to train the neural net end to end. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-14.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 14"
    >
</div>
We can notice some shitty samples boltzmann machine generated. But at that time, it was a pretty big deal, to have a neural net generate new samples at all!!. Boltzmann machines have been succeeded with other class of generative models, but their key ideas still remain as fundamental guiding principles. 
<!-- <div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-15.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 15"
    >
</div> -->

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-16.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

As an example, consider the joint probability distribution of a botlzmann machine. It looks very ugly, i know (sigh). However, it is time to focus on the denominator $Z$. Z is given by summing over all plausible values input x, output y. Evaluating this $Z$ is computationally very hard. However, note that if this denominator Z did not exist, we would have no issues, since the numerator consists of merely W, b, c. Alas, we can only dream, if only there was some way to get rid of this stupid z. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-17.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 17"
    >
</div>
So, can we come up with a training strategy. Well to increase the likelihood, we wanna push the numerator up, denominator down. So, at the input x we are observing, we want probability to be high, and at "some other" points we want this probability to be low. 'If' we had some way of knowing these other points we would be in a good shape.  So intuitively, there is a push-pull game going on. The probability curve $f_{\theta}$ vs input x, at the correct input x, should be high, and around it should be pressed down. In other words, x should function something like a hill, with many valleys lying around it. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-18.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 18"
    >
</div>
We shall now focus on the problem of how to know these "other points" we should minimize. Well the idea is "generate these other points from the NEURAL NET itself!!, and treat these samples as the negative samples!!". Provided, you sample enough of these samples, you can make a good estimate of the gradient required to update this model. This idea is known as Monte-Carlo Estimate. There is no need to remember this fancy name, as long as you understand the key concept. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-19.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 19"
    >
</div>
We shall now derive the expression of how to optimize a boltzmann machine. As you can see in the slides, it consists of two parts. First, is the gradient w.r.t input sample $x_{train}$. Next, we have to take a derivative of the partition function. If you track it closely, you can see that it can be written as gradient w.r.t some input $x_{sample}$, which is generated from the network itself. This leads us to the idea of sampling: how to generate these samples, which will ultimately be used to optimize the weights of the boltzmann machine?
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-20.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 20"
    >
</div>
A closer look at the second term shows partition function in the denominator. As we discussed earlier, calculating it is computationally difficult!!. So how to sample lol :-). This leads to this idea of MCMC. The algorithm is to start with some sample $x_{0}$. We generate some noise, and compute a new sample $x'$. If probability of this sample is high, we choose it. If not, we choose it sometimes with a weight which is difference in the energy of $x_t$ and $x$. We can repeat this procedure for certain no of iterations. As you can imagine, it is extremely slow!!. For each iteration, you have to generate a lot of such samples, and then take a gradient. A core problem is this: 1) suppose you are standing at $x_{0}$, what will be the optimal direction to take a step during the sampling process. Is there something better we could do?
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-21.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 21"
    >
</div>
Well the idea is simple. You are standing in a probability space. You choose the direction, moving along which shall result in the max increase in the probability. This is known as a gradient. So, you can compute $\nabla p_{\theta}(x)$. And you know the next step you wanna take. So, it becomes easy to plug this in the MCMC equation. As you can see, you take the current $x_t$, move in the direction of gradient by a amount weighed by $\epsilon$, and sprinkle in some gaussian noise along the way. This is because, you want to explore the gradient space, and not converge to the same point after equal no of iterations. 

The probability density function for an Energy-Based Model is defined as:
$$
\begin{equation*}
p_{\theta}(\mathbf{x}) = \frac{e^{f_{\theta}(\mathbf{x})}}{Z(\theta)}
\end{equation*}
$$ Where $Z(\theta)$ is the partition function, $Z(\theta) = \int_{\mathbf{x}} e^{f_{\theta}(\mathbf{x})} d\mathbf{x}$.We take the logarithm of the probability density function:
$$
\log p_{\theta}(\mathbf{x}) = \log \left( \frac{e^{f_{\theta}(\mathbf{x})}}{Z(\theta)} \right) \\
= \log \left( e^{f_{\theta}(\mathbf{x})} \right) - \log \left( Z(\theta) \right) \\
= f_{\theta}(\mathbf{x}) - \log Z(\theta)
$$ Next, we take the gradient with respect to the input data $\mathbf{x}$:
$$
\nabla_{\mathbf{x}} \log p_{\theta}(\mathbf{x}) = \nabla_{\mathbf{x}} f_{\theta}(\mathbf{x}) - \nabla_{\mathbf{x}} \log Z(\theta)
$$. Since the partition function $Z(\theta)$ is a scalar value that results from integrating over all possible $\mathbf{x}$, it depends only on the parameters $\theta$ and is independent of the specific input $\mathbf{x}$. Therefore, the gradient of $\log Z(\theta)$ with respect to $\mathbf{x}$ is zero:
$$
\nabla_{\mathbf{x}} \log Z(\theta) = 0
$$ Substituting this back into the equation yields the score function identity:
$$
\nabla_{\mathbf{x}} \log p_{\theta}(\mathbf{x}) = \nabla_{\mathbf{x}} f_{\theta}(\mathbf{x})
$$
Note that this a very powerful idea, since the gradient now becomes independent of the partition function. So, we dont need to estimate any negative samples from the network at all, during INFERENCE. However, training is still a bottleneck, since you still need to generate negative samples. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-22.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 22"
    >
</div>
The figure shows some good faces generated via the sampling mechanism. 
<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/ebm/image-23.png" 
        style="width: 50%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 23"
    >
</div>
And these are some cute imagenet samples generated by some modern methods (not boltzmann machines). We are still left with a question: Can we build a generative model where we don't need to sample negatives during TRAINING, and allow its optimization to be pretty fast. That ladies and gentlemen, is the subject for our next lecture. 
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
