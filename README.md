# Repo with some random stuff

As i was (and still am) learning to code, i have made (and sometimes straight up copied) several little programs to check stuff, get some cool famous results, and visualize cool curves. Some stuff here are recent, while other are years old.


## List with some of the stuff you can find here:
1. 'Pet park' i made to learn a bit about [Object Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
2. A terminal-based visualizer for a random-walk. 
3. Lots of random math stuff (added just a few of them)
	1. Approximating $\pi$ with 'darts'
	2. Approximating $e$ with its series representation
	3. Computing the value of the Basel problem
	4. Getting the roots of polynomials using the [Bisection Method](https://en.wikipedia.org/wiki/Bisection_method)
	5. Computing the probability of cutting in between two candles on a cake (from [this Numberphile video](https://www.youtube.com/watch?v=FkVe8qrT0LA))
	6. Integration with [Riemann Summation](https://en.wikipedia.org/wiki/Riemann_sum)
	7. Visualizing [Lissajous Curves](https://en.wikipedia.org/wiki/Lissajous_curve)
	8. [Monte Carlo Integration](https://en.wikipedia.org/wiki/Monte_Carlo_integration) of functions
	9. Calculating Pi using [Wallis product](https://en.wikipedia.org/wiki/Wallis_product)
	10. [Poisson Distribution](https://en.wikipedia.org/wiki/Poisson_distribution)
	11. Prime number sieve (using generators and [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes))
	12. Sum of cubes is equal to sum of naturals squared (Sum($n^3$) = (Sum(n))$^2$)
	13. Computing the probability that a list is a *Chaotic Permutation* (one which an elements value is not the same as its index in the list)
	14. A [Random Walk](https://en.wikipedia.org/wiki/Random_walk) visualizer. Shows the steps of the random walker, and then tells you its final position
	15. A code to compute as many terms as you'd like of the [Look and Say sequence](https://en.wikipedia.org/wiki/Look-and-say_sequence), with whichever seed you want. I'm pretty sure theres lots of optimization i could do to this code, but right now i am happy it works
	16. I read somewhere about a search of N-digit palindromes within the digits of Pi. So i use [Don Cross's code](https://medium.com/@cosinekitty/how-to-calculate-a-million-digits-of-pi-d62ce3db8f58) to generate 1 million digits of Pi, and store it in the file named 'pi_1million_digits.txt', and then use the code (that i made) '9digit-palindrome-inpy.py' to search for N-digit palindromes within Pi
	17. After a Solid State Physics class, i got familiar to the concept of a [Wigner-Seitz cell](https://en.wikipedia.org/wiki/Wigner%E2%80%93Seitz_cell), and wanted to create a visualization for it. Doing some research for it, i stumbled upon the [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram), and thought it would be pretty cool to implement that, and just add the Wigner-Seitz as a special case. So that's what i did. There's and example output image for each case: 'output_voronoi.ppm', for random scattered seeds, and 'output_wignerSeitz_square.ppm' for a Wigner-Seitz cell inside a square lattice.