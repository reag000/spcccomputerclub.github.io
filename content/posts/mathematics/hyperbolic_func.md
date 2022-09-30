---
title: "Hyperbolic Functions"
description: "Definition of hyperbolic functions and their inverse, and some related identities"
date: 2022-09-29T21:23:06+08:00
draft: false
math: true
tags: ["calculus"]
---

## Definition of Hyperbolic Functions

[basic_hyperbolic](https://www.desmos.com/calculator/o7hmdcceqw) 

Let $f$ be a function. Assume that suppose whenever $f(x)$ is defined implies $f(-x)$ defined, then:

$$
f(x) = \frac{1}{2}(f(x) + f(-x)) + \frac{1}{2}(f(x) - f(-x))
$$

where $\frac{1}{2}(f(x) + f(-x))$ is an even function, and $\frac{1}{2}(f(x) - f(-x))$ is an odd function.

The function $e^x$ is defined for all $x \in \R$, then:

$$
e^x = \frac{1}{2}(e^x + e^{-x}) + \frac{1}{2}(e^x - e^{-x})
$$

We define:

$$
\cosh(x) = \frac{1}{2}(e^x + e^{-x})
$$

and

$$
\sinh(x) = \frac{1}{2}(e^x - e^{-x})
$$

It is easy to see that like $\cos$ and $\sin$, $\cosh$ and $\sinh$ are even and odd respectively.

In a similar fashion as how we define the trigonometric functions, we define:

$$
\tanh(x) = \frac{\sinh(x)}{\cosh(x)}
$$

$$
\coth(x) = \frac{\cosh(x)}{\sinh(x)}
$$

$$
sech(x) = \frac{1}{\cosh(x)}
$$

$$
csch(x) = \frac{1}{\sinh(x)}
$$

## Important Identities Related to Hyperbolic Functions

By definition:

$$
\cosh(x) + \sinh(x) = e^x
$$

$$
\cosh(x) - \sinh(x) = e^{-x}
$$

And hence:

$$
\cosh^2(x) - \sinh^2(x) = 1
$$

Divided by $\cosh^2(x)$:
$$
1 - \tanh^2(s) = sech^2(x)
$$

Divided by $\sinh^2(x)$:
$$
\coth^2(x) - 1 = csch^2(x)
$$

It is easy to verify the following:

$$
\sinh(x \pm y) = \sinh(x)\cosh(y) \pm \cosh(x)\sinh(y)
$$

$$
\cosh(x \pm y) = \cosh(x)\cosh(y) \pm \sinh(x)\sinh(y)
$$

$$
\tanh(x \pm y) = \frac{\tanh(x) \pm \tanh(y)}{1 \pm \tanh(x)\tanh(y)}
$$

And as a consequence:

$$
\sinh(2x) = 2\sinh(x)\sinh(y)
$$

$$
\cosh(2x) = \cosh^2(x) + \sinh^2(x) = 1 + 2\sinh^2(x) = 2\cosh^2(x) - 1
$$

$$
\tanh(2x) = \frac{2\tanh(x)}{1 + \tanh^2(x)}
$$

In particular:

$$
\cosh^2(x) = \frac{\cosh(2x) + 1}{2}
$$

and

$$
\sinh^2(x) = \frac{\cosh(2x) - 1}{2}
$$

