---
layout: post
comments: true
title:  "Group Equivariant Convolutional Nets"
description: ""
date:   2026-08-07 07:00:00
published: false

---



<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/shinchan.png" 
        style="width: 60%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>


So, today our Shinchan had to smoke a cigar. The stress was just too high and getting to his nerves.  for us  guys  in the dirty GLOM business, the matters have become very subtle. So today we will turn to Taco Cohen and Max welling for their guidance and help. The paper we will be talking about is called `Group Equivariant Convolutional Networks'. 

We must clearly spell out the stakes: 1) camp 1 is suttons bitter lesson 2) camp 2 is glom guys. Our job is to bring peace to both. (just kiddin lol)

Rather than rely on abstract mathematics, let us try to build our intuitions physically. 

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Invariance vs Equivariance</span>


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/dino_rotate.png" 
        style="width: 60%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> The arrogant and humble turtle</span>


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/arrogant_rotate.png" 
        style="width: 60%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/humble_turtle.png" 
        style="width: 60%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Mental rotation on a gpu</span>




# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Template matching in a CNN</span>



# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Storing templates of different orientations in a parallel memory</span>



# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> The scaling issue </span>


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Convolution encodes translation equivariance </span>



# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Convolution does not  encode rotation equivariance </span>


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Building the first layer of Group Convolution </span>


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Building the second layer of Group Convolution </span>

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Coreset pooling in the end </span>

# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Training the whole thing together </span>



# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> What is still not clear to me </span>


```python
# --- Node features: identity matrix (one-hot per node) ---
X = torch.eye(N)
print("Feature matrix shape:", X.shape)
# node features are one-hot encoded

plt.figure(figsize=(5, 5))
plt.imshow(X.numpy(), cmap='Greys')
plt.title("Node features matrix ")
plt.xlabel("node j"); plt.ylabel("node i")
plt.show()
```

Now we have finally reached the end of the post. We have done a lot of hard work together in trying to build our intuitions. So now we deserve to have some fun. We will recall Shin-chan’s bori bori dance from our childhood.

<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/gan/bori_bori.gif" 
        style="width: 60%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

we love shin-chan. Maybe you should too.

until we meet next, <br>
love, <br>
rajat


