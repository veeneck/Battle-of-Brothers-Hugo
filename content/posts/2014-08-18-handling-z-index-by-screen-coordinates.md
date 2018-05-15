---
title: Handling Z-Index by Screen Coordinates
author: chris
type: post
date: 2014-08-18T14:48:27+00:00
url: /sirchris/handling-z-index-by-screen-coordinates/
categories:
  - sirchris
tags:
  - code
  - corona
  - learning

---
One problem that I ran into with my game was that my characters and images were not being properly z-indexed. For example, the dwarf in the image below looks like he&#8217;s pasted on top of the tree, even though his position on the map suggests he should be behind the tree.
<!--more-->

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/08/zindex-incorrect-1.png" alt="zindex-incorrect" width="466" height="303" class="alignnone size-full wp-image-1003" srcset="http://localhost:8888/wp-content/uploads/2014/08/zindex-incorrect-1.png 466w, http://localhost:8888/wp-content/uploads/2014/08/zindex-incorrect-1-300x195.png 300w" sizes="(max-width: 466px) 100vw, 466px" />
</div>

This is because in [Corona][1], objects are z-indexed in the order that they are originally drawn to the screen. The dwarf was originally drawn after the tree, so he will always appear to be in front of the tree, regardless if he&#8217;s supposed to be in front or behind the tree.

What I did to fix this is add a couple of functions that run on every frame, loop over all the images, and re-draw the images ordered by their y coordinates.

https://gist.github.com/codepaladin/efa4c3b68ba5c110cdfa

What happens is that any image positioned further down on the y-axis should appear to be in front of any image that higher up on the y-axis. Since the tree has a lower y coordinate than the dwarf, the tree appears to be in front of the dwarf like this:

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/08/zindex-correct-1.png" alt="zindex-correct" width="466" height="303" class="alignnone size-full wp-image-1004" srcset="http://localhost:8888/wp-content/uploads/2014/08/zindex-correct-1.png 466w, http://localhost:8888/wp-content/uploads/2014/08/zindex-correct-1-300x195.png 300w" sizes="(max-width: 466px) 100vw, 466px" />
</div>

Since the indexing functions runs on each frame, objects are correctly indexed as they move across the screen. The dwarf can move from behind the tree to in front of the tree and the objects will be drawn in the correct order to give the perception of depth.

 [1]: http://coronalabs.com/products/corona-sdk/