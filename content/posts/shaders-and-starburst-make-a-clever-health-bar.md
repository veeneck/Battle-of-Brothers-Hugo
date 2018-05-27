+++
author = "Ryan"
categories = ["sirryan"]
date = "2018-05-26T23:44:41+00:00"
draft = true
tags = ["code", "spritekit", "shader"]
title = "Shaders and Starburst Make a Clever Health Bar"
type = "post"
url = "/sirryan/shaders-and-starburst-make-a-clever-health-bar-"

+++
Up until now I've had placeholder health bars that work just fine, but require a ton of manual work and take up a lot of memory. I've always had the goal of making the health bars work programmatically, and I finally got around t doing it. Well, version 1 at least. Have a look at how I've used `SKShader`, `SKCropNode`, `SKShapeNode` and `CGPath` all rendered to one final texture to make my health system work.

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

Now, that assume you have some sort of `degreesToRadians` function in your library. Other than that, it's all straightforward. After that, just render the path into a `SKShapeNode`, and finally into a texture.