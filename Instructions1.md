# PS1 - Your first job as an engineer

## Deadline: 24.10.2021 23.00 (Sunday)

You are an engineer at a data science company and they assign you a new task, which is an hyperparameter optimization task.
Your job will be finding the optimal parameter that maximizes a polynomial function. For this, you need to try out different values
and select the best one. You will be given a search range, polynomial coefficients and a point which you need to maximize the value of the function at.
At the end, you need to find the optimal parameter that maximizes the polynomial function's value at the given point.

### Inputs

`L, U, S -> Lower limit, Upper Limit, Step size`

`a, b, c, d, indicator -> Coefficients of the polynomial function`

`x -> The point where you need to maximize the value of function`

Let's call the value that we will maximize `H`.

The function will be calculated as:

`if indicator is True`


&nbsp;&nbsp;&nbsp; ` f(x) = ((H^3)*x^3+a*H*x^2+b*x+c)**d`

`if indicator is False`


&nbsp;&nbsp;&nbsp; ` f(x) = ((H^3)*x^3+a*H*x^2+b*x+c)/d`




There will be two parts of this PS. The first part will use a linear search (exhaustive). You will start from the lower limit and try *nearly* every value until the upper limit. You will increase the values by the given step parameter. In the second part, you will use bisection method. Instead of going in linear fashion, you will check lower and upper limits' value and select the half that is closer to the maximum of those values. That is, you will compare the values of the function at lower limit and upper limit. If lower value is greater than the upper one, you need to select the half of the search range that is closer to the lower limit, and if upper value is greater than the lower one, you need to select the half of the search range that is closer to the upper limit. The parts will be explained in detailed below.



## PART A

In this part, you will use linear search and search the interval, [Lower limit, Upper limit] (both included) exhaustively. For example, you will first find the value of function at lower limit, `L`, and compare it with the values at other points, `L+S, L+2S, ..., U`. You need to select the point where the value of the function is maximum with respect to other points you have tried.



## PART B

In this part, you will use bisection method to search the interval. You will find the values of the function at lower limit, `L`, and upper limit, `U`. Let's call these values, `f(L)` and `f(U)`. You will compare these values. If value of the function at lower limit is greater than upper limit, `f(L) > f(U)`, we will set the upper limit to middle value of the interval, `U_new = (U+L)/2`. If value of the function at upper limit is greater than lower limit, `f(U) > f(L)`, we will set the lower limit to middle value of the interval, `L_new = (U+L)/2`. We will do these comparisons and limit updates continuously until we will have a very close lower limit and upper limit. That is, search interval is too small to search. For this part, you can discard the step input and directly search in between the interval.




## Rules

1. You need to write your solutions to `ps1a.py` and `ps1b.py`. 
2. The maximum runtime for this problem set will be **1 minute**. If your code does not end in 1 minute, there is probably something wrong in your code.
3. Please use the template we provided, `template.py`, to take the input and print the output. You can copy it to files "ps1a.py" and "ps1b.py" for your solutions below.
4. We will use GitHub autograder to grade the assignment. If you do not change input and output format, given in the `template.py`, there will not be any problem.


## Example cases

### Input 1

<code>
-1 1 0.0001 <br>
-5 -12 1.2 2 True <br>
-1.5 <br>
</code>

### Output 1

`Value: -1.000000, Result: 1144.130625`

### Input 2

<code>
-22 24 0.0001 <br>
-5 -12 1.2 2 False <br>
1.2 <br>
</code>

### Output 2
`Value: -22.000000, Result: -9127.272000`

### Input 3
<code>
-0.12 0.13 0.0001 <br>
12 -12 1.2 2 False <br>
15 <br>
</code>

### Output 3
`Value: 0.130000, Result: 89.807438`