---
title: Understanding Shaders in SpriteKit
author: Ryan
type: post
date: 2015-05-28T18:03:09+00:00
url: /2015/05/28/understanding-shaders-in-spritekit/
categories:
  - sirryan
tags:
  - code
  - shader
  - spritekit

---
If you&#8217;re new to game development, you&#8217;ve probably heard of shaders but don&#8217;t quite understand them. If you&#8217;re new to SpriteKit, you&#8217;ve probably hit a few speed bumps working with shaders. Since I&#8217;m still learning more about the two, I figured it would be nice to put up a concrete example that covers cropping and effects using shaders. Specifically, we&#8217;ll cover two concepts:

<!--more-->

  * Using alpha, black, and white pixel values to determine which pixels to display.
  * Porting shaders found on <a href="https://www.shadertoy.com" target="_blank">Shadertoy</a> into SpriteKit.

Here is what it&#8217;ll look like when we&#8217;re done.

<div class="inlineimg">
  [gfycat data_id=&#8221;TemptingSoreAidi&#8221; data_autoplay=true data_controls=false]
</div>

If you have never worked with a shader in SpriteKit before, you should probably check out this <a href="http://chrislanguage.blogspot.com/2015/02/fragment-shaders-with-spritekit.html" target="_blank">quick introductory tutorial</a>. And if you&#8217;re interested in shaders, but not SpriteKit, you may still find a thing or two that grabs you&#8217;re attention.

#### Getting Started

<div class="embedleft floatleft">
  <img class="alignnone size-full wp-image-2161" style="margin-left: -20px !important;border: none !important" src="http://battleofbrothers.com/wp-content/uploads/2015/05/Melee1HeraldryDark.png" alt="Melee1HeraldryDark" width="117" height="118" />
</div>

The first thing to do is find an image that you would like to mask or modify in some way. For this example, I&#8217;ll be using a circular health bar that wraps around a shield graphic. Note the image is a .png, and that in between the black lines along with the outside is fully transparent. We&#8217;ll try to satisfy three requirements.

  * Only show health in between the two black lines outlining the image.
  * Allow for the health section to be partially full.
  * Add movement to the health bar.

#### A Basic Shader

To apply a basic shader to our image, we&#8217;ll need to tell SpriteKit to attach a shader to the SKSpriteNode, and we&#8217;ll also need to create an empty text file ending in .fsh that contains our shader code. First, the shader code:

https://gist.github.com/veeneck/241ad4e3b8153b33518d

Next, attach the shader in SpriteKit:

https://gist.github.com/veeneck/3e0292d872a3146d0620

<div class="embed floatright">
  <img class="alignnone size-full wp-image-2180" style="border: none !important" src="http://battleofbrothers.com/wp-content/uploads/2015/05/Screen-Shot-2015-05-28-at-11.52.26-AM.png" alt="Screen Shot 2015-05-28 at 11.52.26 AM" width="135" height="136" />
</div>

As you can see to the right, the shader turns every pixel green. This is because `main()` is the entry point, and by default `gl_FragColor` is the return value. So, for each pixel of the image, this snippet of code runs. And when the code runs, it is telling each pixel that the color should be green (note the r,g,b,a value of the `vec4()` call).

#### Detecting Alpha Values

Now that we can change the color of pixels, the next step is to only change the color of fully transparent pixels. We&#8217;ll change our shader code to the following:

https://gist.github.com/veeneck/f8601f819b5f1ac9c52e

<div class="embedleft floatleft">
  <img class="alignnone size-full wp-image-2191" style="margin-left: -20px !important;border: none !important" src="http://battleofbrothers.com/wp-content/uploads/2015/05/Screen-Shot-2015-05-28-at-12.08.03-PM.png" alt="Screen Shot 2015-05-28 at 12.08.03 PM" width="133" height="137" />
</div>

Now, our image fully displays, and all transparent pixels have been replaced with green pixels. Specifically, we create `val` which contains the pixel in the actual texture. The alpha value (`val.a`) is transparent if it equals 0.0. So, we either replace the pixel with a green one, or set the return value to the pixel from the actual texture.

#### Masking & Gradients

The obvious problem with the previous step is that we have to get rid of everything outside of the circle. We only want to fill the inside. In addition, we want the inside to fill only a percentage equal to the health of the player. We&#8217;re going to add a separate image to act as both an image mask, and a gradient fill.

<div class="inlineimg">
  <img class="alignnone size-full wp-image-2197" src="http://battleofbrothers.com/wp-content/uploads/2015/05/circleshader.png" alt="circleshader" width="117" height="118" />
</div>

First, let&#8217;s talk about the **mask**. This circle is the exact same size as the shield above. So, if a pixel falls inside of both the circle and the shield, we know we want to draw it. If it falls outside, we can get rid of it. That&#8217;s how we&#8217;ll achieve the health bar look.

Second, let&#8217;s talk about the **gradient**. Notice that a radial gradient has been applied with pure black meeting pure white at the top. The general idea here is that we can check pixel colors. Imagine a player with health of 75%. We can check all pixels that are at least 75% black, and turn them on. Anything else gets turned off.

To make these two concepts, we&#8217;ll have to attach <a href="https://developer.apple.com/library/prerelease/ios/documentation/SpriteKit/Reference/SKUniform_Ref/index.html" target="_blank">SKUniform&#8217;s</a> to the shader. Think of this as passing variables through to the shader. In this case, we&#8217;ll need two variables. One for health, and one for the image above. Our Swift code should now look like:

https://gist.github.com/veeneck/e68c62e4417bfa03a62d

We&#8217;re basically supplying a float and SKTexture to the shader. Then, we can modify the shader to produce our desired result.

https://gist.github.com/veeneck/23854616813f74819d66

Here is the result:

<div class="inlineimg">
  <img class="alignnone size-full wp-image-2201" src="http://battleofbrothers.com/wp-content/uploads/2015/05/Screen-Shot-2015-05-28-at-10.47.08-AM.png" alt="Screen Shot 2015-05-28 at 10.47.08 AM" width="152" height="155" />
</div>

A few notes on the inline code comments:

**[1]** At the beginning of this tutorial, we checked `val.a == 0.0` and now we&#8217;re checking `val.a less than 0.1`. This is because there are partially transparent pixels around the edges of the circle that we&#8217;re being excluded. A limit of 0.1 set the best result.

**[2]** You can test the black value of a pixel against any of the r, g, b values of the vec4. I just used `.r` because that is what I&#8217;ve seen the most.

**[3] **Similar to [1], I could have check the mask for pixels that are fully visible where `grad.a == 1.0`, but a tolerance was needed to produce the best results.

#### Porting From Shadertoy

When browsing <a href="https://www.shadertoy.com" target="_blank">Shadertoy</a>, you&#8217;ll notice certain variables that aren&#8217;t available to you, or that break your script. Here are the most common ones I&#8217;ve seen, and how to use them in SpriteKit.

<table cellspacing="20" cellpadding="15">
  <tr>
    <td>
      iGlobalTime
    </td>
    
    <td>
      <strong>u_time</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      iResolution
    </td>
    
    <td>
      <strong>u_sprite_size</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      fragCoord.xy
    </td>
    
    <td>
      <strong>gl_FragCoord.xy</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      iChannelX
    </td>
    
    <td>
      <strong>SKUniform with name of &#8220;iChannelX&#8221; containing SKTexture</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      fragColor
    </td>
    
    <td>
      <strong>gl_FragColor</strong>
    </td>
  </tr>
</table>

#### Using Existing Animation Examples

Now that we know how to port from Shadertoy, let&#8217;s try it with a few examples.

**Example 1: **<a href="https://www.shadertoy.com/view/Xtl3Dj" target="_blank">Bullseye</a>

<div class="inlineimg">
  [gfycat data_id=&#8221;EdibleDapperDorking&#8221; data_autoplay=true data_controls=false]
</div>

https://gist.github.com/veeneck/8181776f76a112dce239
  
**Example 2:** <a href="https://www.shadertoy.com/view/XtsGDj" target="_blank">Wobble Spiral</a>

<div class="inlineimg">
  [gfycat data_id=&#8221;UnselfishRemarkableJenny&#8221; data_autoplay=true data_controls=false]
</div>

https://gist.github.com/veeneck/eb5c947bc6d8f1efd598
  
**Example 3: **<a href="https://www.shadertoy.com/view/4lB3DG" target="_blank">Glowing Thing</a>

<div class="inlineimg">
  [gfycat data_id=&#8221;MixedMildGroundbeetle&#8221; data_autoplay=true data_controls=false]
</div>

https://gist.github.com/veeneck/21d480aae49482975efe

#### Further Reading & Next Steps

Resources:

  * <a href="http://www.ymc.ch/en/making-a-pixel-shader-for-ios8-with-sprite-kit" target="_blank">Making a Pixel Shader for iOS8 with SpriteKit</a>
  * Hub.ae&#8217;s <a href="https://www.youtube.com/watch?v=rd7pEru73IY" target="_blank">shader intro</a> and <a href="https://www.youtube.com/watch?v=eYHId0zgkdE" target="_blank">bloom/blur tutorial</a>.
  * <a href="https://developer.apple.com/library/prerelease/ios/documentation/SpriteKit/Reference/SKShader_Ref/index.html" target="_blank">SKShader documentation</a>.
  * <a href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0CCkQFjAB&url=http%3A%2F%2Fdevstreaming.apple.com%2Fvideos%2Fwwdc%2F2014%2F606xxql3qoibema%2F606%2F606_whats_new_in_sprite_kit.pdf%3Fdl%3D1&ei=czBnVem6F4PUsAWIpICIBA&usg=AFQjCNE3zOLO0kl8CGsMp_nYpK3vvkXamQ&sig2=VJ7m_6UL2Sh-S_69dwuEFA&bvm=bv.93990622,d.b2w" target="_blank">WWDC14 PDF</a>
  * <a href="https://www.khronos.org/opengles/sdk/docs/reference_cards/OpenGL-ES-2_0-Reference-card.pdf" target="_blank">OpenGL ES 2.0 API Quick Reference Card</a>
  * Alternative to Shadertoy: <a href="http://glslsandbox.com" target="_blank">GLSLSandbox</a>

Beyond this, I&#8217;m still interested in the performance of shaders, and confidently knowing when to use them. For example, the 6th shader in the original gif above starts to lag a bit if you leave it running too long. Is it because of poor code, or is it too intensive? Similarly, would it be better to use 20 static images to represent health chunks of the circle, and just manage the health bar in code? I&#8217;ve often heard that using shaders is the &#8220;right way&#8221;, but I&#8217;d like to know with certainty when that is true. Perhaps another part to this tutorial is in order.