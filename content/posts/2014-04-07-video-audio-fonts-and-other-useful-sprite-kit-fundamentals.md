---
title: Video, Audio, Fonts and Other Useful Sprite Kit Fundamentals
author: Ryan
type: post
date: 2014-04-07T13:28:54+00:00
url: /2014/04/07/video-audio-fonts-and-other-useful-sprite-kit-fundamentals/
categories:
  - sirryan
tags:
  - code

---
When learning a new language or environment, some things that should be trivial seem to take forever. Once you learn how to do simple tasks, it&#8217;s hard to remember how you originally struggled. So for that reason, I&#8217;ve decided to keep a running log of useful code snippets that were stumbling blocks at some point. Anything that I think I&#8217;ll reuse, or had trouble understanding as a beginner will be added as <a href="https://gist.github.com/veeneck" target="_blank">a gist to my Github account</a>.
<!--more-->

A standard example would be adding video to a Sprite Kit project. Sure, it&#8217;s <a href="https://developer.apple.com/library/ios/documentation/SpriteKit/Reference/SKVideoNode/Reference/Reference.html#//apple_ref/occ/cl/SKVideoNode" target="_blank">easily found in the official docs</a>, but the docs are a bit intimidating when you&#8217;re starting out.



You can view similar, basic examples like adding <a href="https://gist.github.com/veeneck/9943206" target="_blank">background music</a> or <a href="https://gist.github.com/veeneck/9964115" target="_blank">switching scenes</a> over at <a href="https://gist.github.com/veeneck" target="_blank">Github</a>. So far, two memorable behaviors had me frustrated and stuck for longer than expected.

#### Adding Custom Fonts

Adding a custom font turned out trickier than I anticipated because the font wasn&#8217;t recognized as a resource just by adding it to the project (which is what happens with audio, images, etc). I found a <a href="http://stackoverflow.com/a/21738096" target="_blank">perfect answer on stack overflow</a> that sums up what is needed to get custom fonts working.

  * Go to supporting files -> ProjectName.plist. Add am array key of &#8220;Fonts provided by application&#8221; and place one element in the array. The element should be a string with a value of your font <span style="text-decoration: underline">file</span> name. In my case, _dinconra.ttf_.
  * At the top-center of your Xcode window you should see a navigator that starts with your project name. Click on the project name. In the new window that appears, there should be a tab to the right called &#8220;Build Phases&#8221;. Click that, and expand &#8220;Copy Bundle Resources.&#8221; Finally, add your font as a resource by clicking the plus sign in the expanded section.
  * Lastly, and most confusingly, find out the <span style="text-decoration: underline">real name</span> of your font. You can do this in finder by opening the font in Font Book and looking at the title bar on the top of the window that displays the font. In my case, the font name is actually &#8220;DINCond-RegularAlternate&#8221; instead of &#8220;dinconra.&#8221;



#### Delayed Function Calls with Parameters

It is common to see example code calling functions on a delay using performSelector, but the syntax is weird when you need to pass a parameter into the target function. At least, weird if you&#8217;re coming from webdev languages.



As you can see in the snippet, a colon is necessary after the function name (doImageFade) in order to use the withObject parameter.

Be sure to check in on <a href="https://gist.github.com/veeneck" target="_blank">my gists</a> every once in a while if you&#8217;re learning Sprite Kit too. And if anything interesting or noteworthy comes up, I&#8217;ll document it here as well.