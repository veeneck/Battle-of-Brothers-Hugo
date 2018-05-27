+++
author = "Ryan"
categories = ["sirryan"]
date = "2018-05-26T23:44:41+00:00"
tags = ["code", "spritekit", "shader"]
title = "Shaders and Starburst Make a Clever Health Bar"
type = "post"
url = "/sirryan/shaders-and-starburst-make-a-clever-health-bar-"

+++
Up until now I've had placeholder health bars that do their job as intended,  but require a ton of manual work and take up a lot of memory. I've always had the goal of making the health bars work programmatically, and I finally got around to doing it. Well, version 1 at least. Have a look at how I've used `SKShader`, `SKCropNode`, `SKShapeNode` and `CGPath` all rendered to one final texture to make my health system work.

<!--more-->

<div class="inlineimg">
<img src="/uploads/healthbars.png" width="100%" />
</div>

I'm not going to walk through every line of code, but there are a few concepts worth point out.

#### Making a Sunburst Effect in SpriteKit

Because squads can have anywhere from 1 to 50 units, I didn't want to manually create sunbursts with each amount of rays. Fortunately, I stumbled across this [Stack Overflow post](https://stackoverflow.com/questions/10399958/iphone-ios-generate-star-sunburst-or-polygon-uibezierpath-programmatically), which explains how to do it in Swift. I had to make a few minor modifications for my needs:

* Use `CGPath`
* Make the burst thicker, and the spacing smaller
* Always start at 90 degrees

With that in mind, here is the updated code:

{{< gist veeneck ecd0790dbfbfeafdf3d2c6d9b6090b2c >}}

Now, that assumes you have some sort of `degreesToRadians` function in your library. Other than that, it's all straightforward. Next, just render the path into a `SKShapeNode`, and finally into a texture.

#### Cropping & Shading

Let's have a look at the image again, this time with labels.

<div class="inlineimg">
<img src="/uploads/healthbars2.png" width="100%" />
</div>

As you can see, the bulk if the work is done by cropping the sunburst shape out of the gradient, and the shield shape out of the white health bars. **Note:** Both of these steps should be achievable with a shader, but I'm having a ton of problems with SpriteKit shaders right now. Simple steps aren't working. I plan to revise and update this, but for now a brute force approach (`SKCropNode`) is performing well enough.

Speaking of shaders, the only one being used right now is the shader to calculate health.

    void main() {
    
        vec4 val = texture2D(u_texture, v_tex_coord);
        
        if (val.a > 0.95 && val.r < u_health) {
            gl_FragColor = vec4(1.0,1.0,1.0,1.0);
        } else {
            discard;
        }
    }

It's super simple. `u_health` is passed in and the underlying image will be colored white up until the gradients r value is greater than the health. So, if a unit is at 75% health, 0.75 is passed in. Another tip that took me ever to find: `discard` will throw away a pixel. I couldn't get SpriteKit to make fully transparent pixels with `gl_FragColor`, so `discard` does the trick.

Aside from that, the final two images are placed on top, and we have health bars. The cool part about this is that it works no matter what the heraldry shape is.

#### Large Squads & Performance

The example image is for a squad with 10 units, but how does a large squad handle?

<div class="inlineimg">
<img src="/uploads/largesize.png" width="100%" />
</div>

In my opinion, it looks pretty good. 50 units is definitely pushing it, and is the most my game can handle. Still, the player would know at a glance how the squad is doing. The idea isn't to know exactly how many units are dead -- just the percentage. You may ask, "why not just show a normal health circle?" I don't have a great answer. Mainly, this looks unique. Also, at lower levels, it gives you an at a glance feel for how many units you can revive, bandage and purchase. But, yeah, it looks neat.

As for performance with all of these crop nodes, it's decent enough. Everything has to be rendered to one final texture or else it would choke. That entire process takes about **50ms**. Because it has to happen for every squad whenever an event happens (i.e: a unit dies), I run it in a separate thread and it seems to be happy.

#### Improvements

As I touched on earlier, the main improvements are to use shaders instead of `SKCropNodes`. While that may not increase execution time, it will definitely improve clarity of code. Aside from that, I'm interest if anyone has additional ideas for this sort of implementation. Keep in mind that it has to work for any shield shape, and any amount of units.