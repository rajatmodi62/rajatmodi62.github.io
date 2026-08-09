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


So, today our Shinchan had to smoke a cigar (courtesy of the roommate). The stress was just too high and getting to his nerves.  For the  guys  in the dirty GLOM business, the matters have become very serious. So we will have to seek solace from the warriors of symmetry: Taco Cohen and Max welling.

The paper we will be talking about is called `Group Equivariant Convolutional Networks'. 

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

The above story leads one to believe that we have made a mistake of `public posturing'. However, that might not be correct. One may also believe that we could learn from humble turtle more than the arrogant turtle. However, the turtles who are arrogant in the eyes of few are merely committed to their own ways of existing. So, we will turn to the arrogant turtle to learn from him. 

It is now time to move away from the realm of the mystics to the realm of the engineering. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> Lessons from the arrogant turtle </span>


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/kernel_fire.png" 
        style="width: 80%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

We would now like to think of our turtle as a kernel of a convolutional net. The picture above shows a rotated (and inverted) image of a letter F. The kernel can either be sad or happy in this case. Left part of the picture shows that turtle as sad. This is because the turtle `does not` align with the larger horizontal line on the F. In the right picture, the image has been rotated clockwise. The turtle now begins to face the latter F. (Upper line in F). So,it is happy. 

Now, let us consider the matter of how we actually rotate an image in a computer. First, let me dump some code i wrote, and then explain what it means. 


```python 
import matplotlib.pyplot as plt
import numpy as np

# 1. Create a dummy feature map f(x) with an asymmetrical pattern (an 'F')
N = 11  # Grid size (11x11, centered at origin (0,0))
f = np.zeros((N, N))

# Draw an "F" pattern on the grid
f[2:9, 3] = 1.0  # Vertical stem
f[2, 3:8] = 1.0  # Top bar
f[5, 3:6] = 1.0  # Middle bar

# 2. Define grid coordinates centered at (0, 0)
coords = np.stack(
    np.meshgrid(np.arange(N) - N // 2, np.arange(N) - N // 2), axis=-1
)

# 3. Define transformation g: 90-degree counter-clockwise rotation matrix
R_g = np.array([[0, -1], [1, 0]])
R_g_inv = R_g.T

# 4. Compute [L_g f](x) = f(g^{-1}x)
L_g_f = np.zeros((N, N))

for i in range(N):
    for j in range(N):
        x = coords[i, j]  # Target coordinate [x_1, x_2]
        x_src = R_g_inv @ x  # Inverse lookup: g^{-1} x

        src_i, src_j = x_src[1] + N // 2, x_src[0] + N // 2

        if 0 <= src_i < N and 0 <= src_j < N:
            L_g_f[i, j] = f[src_i, src_j]

# 5. Plotting: Original f(x) -> Forward Mapping -> Transformed [L_g f](x)
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# --- Panel 1: Source Domain f(x) ---
axes[0].imshow(f, cmap="Blues", origin="lower")
axes[0].set_title(r"1. Source Domain $f(x)$", fontsize=13)
axes[0].set_xticks(np.arange(N))
axes[0].set_yticks(np.arange(N))
axes[0].grid(True, color="gray", alpha=0.3)

# --- Panel 2: Coordinate Mapping (Forward Vectors) ---
axes[1].imshow(f, cmap="Blues", alpha=0.25, origin="lower")
axes[1].set_title(
    r"2. Forward Mapping: $x_{\text{dest}} = g \cdot x_{\text{src}}$", fontsize=13
)
axes[1].set_xticks(np.arange(N))
axes[1].set_yticks(np.arange(N))
axes[1].grid(True, color="gray", alpha=0.3)

# Overlay vector field showing where non-zero points in f(x) move to under g
for i in range(N):
    for j in range(N):
        if f[i, j] > 0:
            # Source coordinate (x, y) centered at origin
            x_src = np.array([j - N // 2, i - N // 2])

            # Forward coordinate transformation: x_dest = g * x_src
            x_dest = R_g @ x_src

            # Convert to array plotting indices
            src_col, src_row = j, i
            dest_col, dest_row = x_dest[0] + N // 2, x_dest[1] + N // 2

            # Compute displacement vector (dx, dy)
            dx = dest_col - src_col
            dy = dest_row - src_row

            # Draw mapping arrow from source to destination
            axes[1].quiver(
                src_col,
                src_row,
                dx,
                dy,
                angles="xy",
                scale_units="xy",
                scale=1,
                color="darkorange",
                alpha=0.8,
                width=0.015,
                headwidth=4,
            )

# --- Panel 3: Destination Domain [L_g f](x) ---
axes[2].imshow(L_g_f, cmap="Oranges", origin="lower")
axes[2].set_title(
    r"3. Destination Domain $[L_g f](x)$" + "\n(Rotated 90° CCW)", fontsize=13
)
axes[2].set_xticks(np.arange(N))
axes[2].set_yticks(np.arange(N))
axes[2].grid(True, color="gray", alpha=0.3)

# Highlight single point pair across all three subplots
target_x, target_y = 2, -3  # Target point in L_g_f
target_i, target_j = target_y + N // 2, target_x + N // 2

src_coords = R_g_inv @ np.array([target_x, target_y])
src_i, src_j = src_coords[1] + N // 2, src_coords[0] + N // 2

axes[0].scatter(
    src_j,
    src_i,
    color="red",
    s=110,
    zorder=5,
    label=r"Source $g^{-1}x$",
    marker="X",
)
axes[1].scatter(
    src_j, src_i, color="red", s=110, zorder=5, marker="X", label=r"Source"
)
axes[1].scatter(
    target_j, target_i, color="red", s=110, zorder=5, label=r"Destination"
)
axes[2].scatter(
    target_j, target_i, color="red", s=110, zorder=5, label=r"Target $x$"
)

axes[0].legend(loc="upper right")
axes[1].legend(loc="upper right")
axes[2].legend(loc="upper right")

plt.tight_layout()
plt.show()
```

Rather than look at all the mess, just look at the picture below:


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/rotation_operator.png" 
        style="width: 80%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

The middle panel shows (by the means of arrows), which source point in the original image goes to which destination point of the final image. That is all the above code is trying to achieve. Specifically, the code begins by defining a rotation matrix R. When this rotation matrix acts on any src point (x,y), it transforms it into a new dest point. One other way to do it as follow:

```python
for i in range(N):
    for j in range(N):
        x = coords[i, j]  # Target coordinate [x_1, x_2]
        x_src = R_g_inv @ x  # Inverse lookup: g^{-1} x

        src_i, src_j = x_src[1] + N // 2, x_src[0] + N // 2

        if 0 <= src_i < N and 0 <= src_j < N:
            L_g_f[i, j] = f[src_i, src_j]
```

You draw a single canvas called L_g_f. Then you go through each row and each col, and choose a point. Let's call it `dest`. You ask: `Dear dest, i should fill you with value of which source`. You can get that x_src by the operation of `R_g_inv @ x`. x here is the coordinate on the `dest` grid, and not the `src` grid. Once you make sure that the `src` point actually lies in the bounds of your grid, you can replace it with the value. 

What is the point of this entire exercise? Two things stand out:

- If a src image has to be rotated by 90 degrees clockwise, we can precompute a dictionary mapping every src to dest. The `contents` of this dictionary never change. 

- The mapping stored in this dictionary `does not depend` on what is actually drawn on it. No matter what content there is, the same dictionary will hold true. 

-  An `action` of this dictionary is the physical act of creating a dest canvas and manually copying the pixels from `src`  to `dest` image. 

- Now let us assume that the image is to be rotated three times clockwise. We can merely `perform action` of applying dictionary to the image `three times one after another`. 

In a sense the mapping which the dictionary holds, is the `representation` of the potential act of rotating the image by `multiples of 90`. For the case of `two dimensional` images, there are 4 possible rotations of 90, 180, 270, 360. A full rotation of 360 recovers the original image without the loss of information. 

So say we start from 0. We wanna get to 270. So we need three rotations 0 -> 90 -> 180 -> 270. Is it possible to directly get to 270? Perhaps. But, we will assume that reaching 270 still requires a repeated `action` of the dictionary. Why? `It seems nonsense`. To go from 0 -> 270 is possible by multiplying the dictionary $D$ three times like $D.D.D$ and apply the resultant operator directly to the input image. This is far faster than doing $D$, $DD$, $DDD$. This makes `no sense`. 

Well my dear reader, the fact that you can just apply $D$ three times `recursively` even if it took long is of interest because compute is cheap, memory is not: it is easier to store D, than store 3 separate operators $D$, $DD$, $DDD$ together. So, let us make this assumption for now. Those of us who are in the GLOM business now call this $D$ as a `geometric operator`. It might be learnt, or it might be a stupid hardcoded mapping for transforming input (like hintons transforming autoencoder hehe)

Now, we will start asking ourselves a few stupid questions, and gradually build towards a more general solution.

q1. `Suppose we want to build a neural net which can detect 90 degree rotations of an object?. How do we build one`. 

Answer: Indeed, when we used only one turtle, it was able to detect only one rotation. So, a group of 90 degree rotations contains 4 possible rotations of 90,180,270,360. So perhaps, we need 4 possible turtles. So, we are tempted to invent a generic `data structure of turtles` called a `filter bank`. 

Here is how it may look:




<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/filter_bank.png" 
        style="width: 40%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

The above filter bank contains 4 turtles (4 filters) arranged in a nice fashion. Now, let us imagine that we are one of the turtles. In other words, we are a CNN filter. Now, an image in the outside world can undergo 4 rotations. We want to study how the `combined set' of filter banks will respond to the changing images. A pictorial description is provided below:


<div style="text-align: center; margin-bottom: 20px;">
    <img 
        class="img-fluid" 
        src="{{ site.baseurl }}/assets/img/conv_mental_rotation/filter_bank_rotate_example.png" 
        style="width: 80%; height: auto; display: block; margin: 0 auto;" 
        alt="Image 16"
    >
</div>

A yellow rectangle in the filter bank states `which` of the turtles gets activated. As you can see, the yellow box undergoes an `anticlockwise' rotation. This leads us to two very subtle points:

- case 1: If the world outside changes anticlockwise, the pattern of responses in a filter bank also trigger anticlockwise over time.  

- case 2: Now, suppose the world outside `doesn't change`. The image being fed to the network is of a `single orientation` (for example the leftmost image of inverted letter F). We still want to achieve the similar `pattern of activity` which were triggered by the `actual rotation` of the letter F in the previous case. This `mental act` of simulating an actual rotation of the world inside the neural net itself is what is termed as `mental rotation (shephard)`.

We must understand a few more subteltities of case 1 and case 2. The representation `R` produced in `both cases` is same. It is the fundamental nature of computation that has now changed. 

In case 1, `the world rotated`, therefore the input was `fed 4 times` to the network (for each of the 0 degree, 90 degree, 180 degree, and 270 degree rotations). In second case, input was fed `only once`, but the mental rotation happened for the $4$ filters in parallel. Case 1 consumes more compute since the data may have to travel through the network 4 times. On the other hand, Case 2 consumes less compute. I will come back to this later, but for now, let's stay on track. Please email me if i forget to cover this here. 

Thus, it has now become really tempting to use case 2: `after all it uses less compute, gives same answer, so why not use it lol ?`. However, as they say, good things in life don't come free. Everything comes at a cost. You must be willing to pay it. Even if you are not, a transformer architecture is extracting it from you. 


# <span style="font-size: 1.5rem; color: var(--border-header-bottom);"> The cost of mental rotation</span>




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


