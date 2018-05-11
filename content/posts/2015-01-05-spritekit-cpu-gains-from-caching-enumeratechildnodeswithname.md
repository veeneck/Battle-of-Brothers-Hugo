---
title: 'SpriteKit: CPU gains from caching enumerateChildNodesWithName'
author: Ryan
type: post
date: 2015-01-05T18:48:27+00:00
url: /2015/01/05/spritekit-cpu-gains-from-caching-enumeratechildnodeswithname/
categories:
  - sirryan
tags:
  - code
  - sprite kit
  - swift

---
Those of you who follow me know that I&#8217;m working on a game that will have ~200 nodes on the screen updating every frame. Because of that requirement, I&#8217;m <a href="http://battleofbrothers.com/sirryan/joy-of-debugging-command-swiftc-failed-with-exit-code-1" target="_blank">constantly looking</a> at <a href="http://battleofbrothers.com/sirryan/memory-usage-in-sprite-kit" target="_blank">how I can</a> incrementally <a href="http://battleofbrothers.com/sirryan/now-were-rolling" target="_blank">improve performance</a>. Slowly but surely, I&#8217;m making this game a well oiled machine. Today, I stumbled on a significant slow down, and the resulting fix that shaved off 16% CPU usage: caching `enumerateChildNodesWithName`.

<!--more-->

This discovery came from reading WWDC 2014 transcripts while discussing said function.

> This is very fast, so you can do it often but we do recommend your cache results if it becomes a performance problem.
> 
> <a href="http://asciiwwdc.com/2014/sessions/608" target="_blank">Best Practices for Building SpriteKit Games</a>

If it warranted a mention in Apple&#8217;s discussion, it deserved a closer look. So, I set up a test with 105 nodes running in the update loop. Here are the results:

  * Calling **enumerateChildNodesWithName** each frame: **44%** CPU
  * Caching update callbacks in an array: **28%** CPU

Huge gains, and the best part that the caching is relatively painless to implement.

#### Implementation

First, we&#8217;ll start with an array to hold our callback functions.

<pre>var updateListeners : Array&lt;((CFTimeInterval) -&gt; ())&gt; = []</pre>

Here is an example of what one of those callbacks would look like:

<pre>    func updateWithTime(currentTime:NSTimeInterval) { 
        // do something 
    }
</pre>

With that in place, all we have to do is cache the callback functions on the first run through of `enumerateChildNodesWithName<strong>` in the Scenes update loop.</strong>

https://gist.github.com/veeneck/a5f2dd16bf11843141cd

Now, let&#8217;s say one of our characters dies. We don&#8217;t want the update function to keep running on that character. We&#8217;ll have to clear the cache by emptying the array. Then, it will automatically rebuild on the next update loop.

<pre>self.updateListeners = []</pre>

I&#8217;ve consolidated all of this into a small class that I call from my scene object in case it gets more complicated down the road. You can see my full code here:

https://gist.github.com/veeneck/f1d534a87133415bfd6d

#### Notes & Concerns

Each time you clear the cache, it fully rebuilds. If you&#8217;re pushing CPU limits already, this could cause some delayed frames. Two solutions to improve this:

  * Add a removeUpdateListener() function, and a key/value store, so that you can remove a specific item on demand.
  * Or, break apart your objects into smaller cache groups with the goal of minimizing the amount of objects removed from the cache at any given time.

Consider expanding `updateService` to dynamically control what would be in the cache. My example is hard coded to `Characters` and `Heraldry`, but the situation could be different each level.

Also, this can be a useful way to begin separating out updates for different objects by different time intervals if everything doesn&#8217;t have to tick 60 times per second.