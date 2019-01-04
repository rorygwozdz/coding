- Examining the CAPM model with the efficient frontier and capital market line
    - The beta is mathematically derived by dividing the covariance of returns between the stock and the market with the variance of the market returns.
    - if you expect the stock to out/underpeform, you would (maybe) consider this in risk terms. I.e. if the expected return derived from the capm >|< your predicted return
• Solving for the security market line using regression
    - import scipy.stats as s
    - s.linregress(returns, mkt_returns)
* Examining the APT model and performing a multivariate linear regression
    - essentially, since market risk is diversified away, stocks need a better way to be valued than capm. this is that way
    - statsmodels.api as sm
    - OLS = ordinary least squares
• Understanding linear optimization in portfolio allocation
    - essentially, you have some collection of assets
    - you also have some restraints on those assets
    - and that causes a problem
    - a _linear optimization_ problem
• Linear optimization using the PuLP package
    - see script when the big boy comes in. use camel case
• Understanding the outcomes of linear programming
    - what do you get?
    1. a local solution (global's a bit harder to know)
    2. an infeasible problem if you can't find no solution
    3. an unbounded solution if it's infinite/unbounded
• Introduction to integer programming
    - more art than science
    - comes up when fractions aren't realistic (like with binary decisions in the extreme, or a whole pieces in the more moderate)
• Implementing a linear integer programming model with binary conditions
    - see notebook
    - make sure _all_ the unkowns are involved when trying to solve the equation, you can't just try one at a time - kis, stupid
• Solving systems of linear equations with equalities using matrix linear algebra
    - using numpy, matricies are loaded in as a list lof lists, where it's an array of rows
    - some stars have to align for this to work properly but they can and do on occasion
    - so just be aware of when the matrix is orthogona, or positive or definite
    doing lower upper always isn't the best forever
    - also, make sure that you're not forgetting that each rows a constraint equation - like faster pulp
• Solving systems of linear equations directly with the LU, Cholesky, and QR decomposition
    - lu = lower upper || transforms the _square_ matrix into two, where there's an upper missing triangle and lower missing triangle in the respective halves. think np.array([[1,0,0], [1,2,0], [1,2,3]]) as L (where U is the opposite and U*L = A)
    - choelsky si just for specific instances where lu is intensive, little over my head
    - qr is for orthogonal matricies. Transoped matrices are A.T, multiply matricies by np.dot(A.T, B)
• Solving systems of linear equations indirectly with the Jacobi and Gauss-Seidel method
    - jacobi is iterative, like previous optimizations but row by row
    - gauss-siedel's sick
        - essentially, you lower/upper the matrix (A in Ax=B) and then solve it as x = L ^ -1 (B - Ux)
• Big takeaways
    - there's a ton of tools for optimizing
    - when working with matrix data, be careful to use little tricks for big runtiome cutdown
    - lower upper is great, both on a pure basis and on an interative basis
    - Ax = B, (L + U)x = B, Lx = B - Ux, x = L^-1 (B - Ux)
