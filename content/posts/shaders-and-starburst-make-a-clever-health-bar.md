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
Up until now I've had placeholder health bars that work just fine, but require a ton of manual work and take up a lot of memory. I've always had the goal of making the health bars work programmatically, and I finally got around t doing it. Well, version 1 at least. Have a look at how I've used SKShader, SKCropNode, SKShapeNode and CGPath all rendered to one final texture to make my health system work.

<!--more-->

<div class="inlineimg">
![](/uploads/healthbars.png)
</div>

Alright