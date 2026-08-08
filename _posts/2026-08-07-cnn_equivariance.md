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

We must clearly spell out the stakes: 1) camp 1 is suttons bitter lesson 2) camp 2 is glom guys. Our job is to bring peace to both. (just kiddin lol).

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

First we begin with an image of a little dino. Suppose we rotate him by 90 degree clockwise. The right side of the above figure presents the rotated dino. The question we wish to ask is: `what might be happening in our heads when we see the rotated dino?'.

There are two answers:
- Nothing happens. Even if it is rotated, it is still a dino. 
- Brain builds an internal representation of the dino. Let's call it R1. Upon rotation of dino, brain computes a new representation R2. R1 and R2 are related to each other in some predictable way. So brain then does some sort of computation to see that R1 and R2 are in fact similar. 

On a single glance, it seems the first one is more desirable. The representation never changes, so there is no need of post-processing. That is called `invariance' 

The second one seems undesirable. It comes at the cost of defining how the representation in brain might work, figure out a bunch of weird math. Then, it requires all complicated bookkeeping to relate R1 and R2 to each other. That is called `equivariance'. 

If someone asked you: `hey dude, should i choose invariance or equivariance when building my neural net?` . Your answer will be: `Geez, build invariance man. It's simple, faster, and cheaper to compute`. 

The argument for the rest of this post is counterintuitive: that equivariance is far better than invariance. However, to understand it, we have to bring in a cute turtle. There are two types of turtle we wish to consider: 1) the arrogant turtle, 2) the humble turtle. Most of the turtles of this world are arrogant. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> The arrogant turtle</span>


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/arrogant_turtle.png" 
        style="width: 60%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>


On the left, we show a blue turtle. He is represented by a red vector. There is a target vector (in yellow) perpendicular to him. The target vector sits in the outside world. The blue turtle is the neural net. The task is to align the two arrows together (just for the fun of it). 

Recall, that the turtle is arrogant. He would rather stick at his place, and wait for the world to `adjust` according to him. But, this world is big, and whims of a little turtle do not concern it. But, for the moment we assume that the world does bend to the whims of the turtle. 

The yellow target turns `clockwise' and the two vectors align. Both the turtle and the world are now happy. 

Let us consider the same case from an opposite perspective.




# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> The humble turtle</span>


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/humble_turtle.png" 
        style="width: 60%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

The turtle in the above figure (extreme left) is humble. He knows the world won't bend to his whims. There are just so many turtles in the world. The only option turtle has is to adjust himself. The turtles who submit themselves to what the world demands of them, outlive those turtles that refuse to adjust. Darwin called that survival of the fittest lol. 

So anyways, our turtle (in middle part of the picture) rotates clockwise and aligns himself with the world. They are happy. However, you dear reader are not happy. You see both of them rotated now. So, you would rather prefer them to be upright. So, you tell the turtle: `dear turtle, can you please rotate yourself to align with me`? 

The turtle  says: `Sure master, i am humble, i will do whatever you say.` So he takes `his perception of the world (yellow vector)` , along with his own vector (red), and rotates `both` to align vertically on the screen. Every thing looks beautiful once again. 

The humble turtle thinks: `alas what is beauty? i can feel it, but i have no way of quantifying it. How may i even start to model it?`. He makes a note to ask schmiduber for [guidance later](https://people.idsia.ch/~juergen/beauty.html). For now, however, the turtle has grown weary. All that rotation and counterrotation have deeply exhausted him. 

Our dear turtle closes his eyes, retreats into his shell, and enters a deep state of trance. Smoking a little cigar always helps. Our turtle then goes into a deep silence, for only then mother nature reveal her mysteries. The musings of the outer world no longer concern it. The turtle only opens it's eyes,  when it is time to make other turtles by the sea. For some reason, turtle just lays eggs and continues on its merry way. He does not have to mate for life or pledge its allegiance to a female turtle forever. 

The above story leads one to believe that we have made a mistake of `public posturing'. However, that might not be correct. One may also believe that we could learn from humble turtle more than the arrogant turtle. However, the turtles who are arrogant in the eyes of few are merely committed to their own ways of existing. So, we will turn to the arrogant turtle to learn from him. It might be the time to move away from the realm of the mystics to the realm of the engineering. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Mental rotation of the arrogant turtle </span>




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


