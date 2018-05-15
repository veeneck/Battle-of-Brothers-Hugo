---
title: Create Skippable Cutscenes in SpriteKit with Timing Functions
author: Ryan
type: post
date: 2015-01-26T15:05:10+00:00
url: /2015/01/26/create-skippable-cutscenes-in-spritekit-with-timing-functions/
categories:
  - sirryan
tags:
  - code
  - spritekit
  - swift

---
Cutscenes are a labor of love, so it is hard accepting that some people just don&#8217;t care. That story that took months to bring together may be amazing to you, but to others it is just an inconvenience. So, for that reason, we have to make cutscenes skippable. However, I didn&#8217;t want to just settle at skipping the entire scene. I wanted to also make it skimmable for the speed readers, or those who are mildly interested.
<!--more-->

{{< youtube bhU8LTOGd0g >}}
  
Watching the video above, you can see how skimmable cutscenes could bring about all sorts of complications. The worst of those challenges is how to handle placement of the camera. Take this example:

  * 1. Camera starts zooming to character A
  * 2. Dialogue A
  * 3. Pan camera to character B
  * 4. Dialogue B

How would you solve the problem if the user skips step 1 and 2? My first attempt was to store information inside of step 4 that contained the expected camera position. Then, if the camera wasn&#8217;t at that position, immediately jump it there. That solution worked just fine, but it caused me to duplicate the information. Step 3 and 4 both had to know the ending position of the camera.

An alternate solution to this problem is to use `SKAction` and `timingFunction`. When an action is running, it will immediately fast forward to the end when the `timingFunction` returns 1. For example:

{{< gist veeneck691ab2e2a8eca3f6138d >}}

Now that we know how to end an action, the next step is to make it dynamic. In my findings, `timingFunction` can not be altered once the action starts running. So, I had to make a class for each cutscene action, and use a member variable to determine when it should finish.

{{< gist veeneck9ae95b8d4b59280f916d >}}

In the code above, the timing function will work as expected until the member variable `finishEarly` is set to true. Once set, the `SKAction` will instantly run to completion. This can be taken much further to accommodate sound, in game items, and other events. I plan to break it down one a line by line basis to give granular control. But, we&#8217;ve got a good starting point for now. The example below shows my original scene being skimmed, which saves 5 seconds off of reading time.

<div class="inlineimg">
  {{< gfycat data_id="WearyEverlastingBee" >}}
</div>