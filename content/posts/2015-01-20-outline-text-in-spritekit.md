---
title: Outline Text in SpriteKit
author: Ryan
type: post
date: 2015-01-20T20:31:57+00:00
url: /2015/01/20/outline-text-in-spritekit/
categories:
  - sirryan
tags:
  - code
  - spritekit

---
It&#8217;s funny how the tasks that should be easy end up consuming the most amount of time. As of this writing, there is no easy way to outline text in SpriteKit. It&#8217;s common to see approach that <a href="http://stackoverflow.com/questions/19211827/what-would-be-the-best-approach-for-outlining-or-dropshadowing-a-font" target="_blank">add a shadow node</a>, but sometimes more contrast is needed. Here&#8217;s what I have discovered.

<!--more-->

<div class="inlineimg">
  [gfycat data_id=&#8221;LavishFearfulBighornsheep&#8221; data_autoplay=true data_controls=false]
</div>

The first approach is to use `NSMutableAttributedString` with a `UILabel`. Have a look at the code below:

https://gist.github.com/veeneck/fd7928b86d695aae4465

Oddly enough, those two notes above caused me an hour or two of frustration. But, aside from those, the idea is relatively straightforward. The one complaint I have with this approach is that the text is added as a subview. It would be much easier if the text was an object SpriteKit was familiar with.

Fortunately, <a href="https://github.com/alex-alex/ASAttributedLabelNode" target="_blank">ASAttributedLabelNode</a> was shared with the world, and makes the text into a `SKSpriteNode`. Implementation is identical to the above except for the last 3 lines. They will become:

       let myLabel = ASAttributedLabelNode(size: self.size)
       myLabel.attributedString = myMutableString
       myLabel.position = CGPoint(x:CGRectGetMidX(self.frame), y:CGRectGetMidY(self.frame));
       self.addChild(myLabel)

This is perfect since we can now work with positions, children, SKActions, and so on.