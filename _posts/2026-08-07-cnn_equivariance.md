---
layout: post
comments: true
title:  "Group Equivariant Convolutional Nets"
description: ""
date:   2026-08-07 07:00:00
---



<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/shinchan.png" 
        style="width: 60%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>


Shinchan is in a foul mood, and pretty stressed out. So, he had to smoke a cigar. He's a bit high, but now it is the time for serious business. Neural nets are notorious little creatures. If you try to peek under the hood, they will find all the clever ways to make themselves a black box. To make a sense of them, this time we again turn to dear grandpa geoff hinton (And a little bit of Taco cohen and max welling too). It is time to finally invoke the wrath of  the gods of symmetry. 

First, we need to take care of rich sutton's bitter lesson. He says symmetry is a fool's endeavour, and it is better to brute force representations using a transformer. Good for their camp. Let them scale.  Alas, who can argue. The fight continues. 

However, for us  guys  in the dirty GLOM business, the matters are a bit more subtle. It turns out that symmetry is  indeed useful. Let us imagine that you show a face of a cat to a neural net. It recognizes it as cat. Next, you translate the cat a little bit. Neural net should still detect it is a cat, even if it has not seen this position or pose of the cat before. Hell, if you only trained a neural net with cat's front, and then showed it the cat's back (extreme viewpoint), it should still work !! Grandpa Hinton has repeatedly told us that part whole hierarchies are a key to building generalization in neural nets. 

For the rest of this post, there are three `axioms' we shall use. We take them for granted. They need not be, but if something has to be rebuilt from ground up, it has to stand on some foundation. Indeed, you can rid of the foundation and replace it with something else. But, for now, let us assume that the following set of axioms are the truth of representations in a neural net:

- Neural nets work in higher dimensional vector spaces. So many dimensions that you cannot see them (say 1024 dimensions). So, the best way to visualize it is to think of a 3d space, and say 1024 to yourself. 

- God's Universe follows some laws of symmetry. Machines are made of silicon. Since silicon is matter, it has to have a similar symmetry. By extension, computer chips are made of silicon, and neural nets live in silicon.  Therefore, they inherit the symmetries of the physical law from their parents. An organism which sits on a machine however need not possess the limitations of the biological organism. Therefore, we can isolate symmetry groups, and intentionally break them in the neural nets. This then leads to new properties in the organism. 

- What makes matter or a collection of cells living or non living?  Animate or Inanimate? What gives them Life. These are the questions in the realm of the mystics, and we shall steer away from that. This does not mean that the mystical laws do not exist. It is just that we are not at the level to understand them yet. We also are not yet capable to develop a computational theory for hard problem of consciousness. 

sThe matter then is to precisely identify which symmetries to break. Breaking them can be trivial. So trivial, that once it reveals itself to us, we can only laugh. The entire problem is how to identify the fundamental symmetries of learning machines in the first place. And that gets at the core of representational learning. It is possible to invent all sort of clever mathematics, and abstract hilbert spaces, reimannan geometry and what not. But, there has gotta be some intuition to it all. We will merely try to scratch that itch. 







# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Why is it important?</span>

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


