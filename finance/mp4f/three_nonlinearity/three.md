+ Examining the definition of nonlinearity
    - implied volatility is often different from realized.
+ Discussing the volatility smile in implied volatility modeling
 - you know most of this shit already:
    - ITM ~ intrinsic value ++
    - ATM ~ technically OTM because they don't exercise, relevant for pinning though, because they have the lowest implied volatility.
    -  The reason that the ATM has the lowest implied volatility is because you would expect whatever underlying to be most likely to stay at the money (the center of the bell)  possible volatilities to stay exactly there, whereas the farther up or down you go the wilder things get, and the higher the volatility. The reason it has the lowest implied volatility is because it's the bottom of the smirk, things have to be the least wild for it to be most likely to stay there. 
+ Discussing Markov switching models, threshold models, and smooth transition models as nonlinear models
    - Markov:
        + moves based on some state
        + sharp transistion thing
        + which can be fixed wither a gradient transition
+ An overview of root-finding to find the optimal point of nonlinear models
+ Examining the incremental search algorithm, bisection algorithm, Newton's algorithm, and secant method in root-finding
+ Combining root-finding methods with Brent's method
+ SciPy's implementation of root-finding methods as scalar functions
+ SciPy's general nonlinear solvers in root-finding
