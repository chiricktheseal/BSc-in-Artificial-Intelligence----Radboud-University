
#Deterministic variables in JAGS
model {
  theta_hat ~ dbeta(a, b)
  a_transformed <- theta_hat * (kappa - 2) + 1
  b_transformed <- (1 - theta_hat) * (kappa - 2) + 1
  for (i in 1:M) {
    theta[i] ~ dbeta(a_transformed, b_transformed)
    y[i] ~ dbin(theta[i], n[i])
  }
}

samples = model.sample(num_iter, vars=[‘a_transformed’, ‘b_transformed’])





#---------------------------------------------------------------------------------

#Inference of the (Gaussian) mixture model with JAGS
model {
  pi ~ ddirch(alpha)
  for (k in 1:K) {
    mu[k] ~ dnorm(170, 0.01)
    sigma[k] ~ dunif(0.0, 10.0)
    tau[k] <- pow(sigma[k], -2)
  }
  for (i in 1:n) {
    z[i] ~ dcat(pi[])
    x[i] ~ dnorm(mu[z[i]], tau[z[i]])
  }
}
#K=2, alpha=np.array([1.0, 1.0])



#Removing symmetries
model {
  for ( k in 1: K ) {
    mu0 [ k ] ~ dnorm (170 , 0.01)
  }
  mu <- sort ( mu0 )
}
# all zi = 1 will always refer to the component with the smallest μk




#Marginalize a discrete variable

pj.load_module(’mix’)
for ( i in 1: n ) {
  x [ i ] ~ dnormmix ( mu , tau , pi )
}
# with mu , tau and pi defined as before.






#------------------------------------------------------------

#Bayesian linear regression with JAGS
model {
  w0 ~ dnorm (0 , 1e -3)
  w1 ~ dnorm (0 , 1e -3)
  tau <- pow ( sigma , -2)
  sigma ~ dgamma (0.001 , 0.001)
  
  for ( i in 1:n ) {
    mu [ i ] <- w0 + w*x[i]
    y [ i ] ~ dnorm ( mu [ i ] , tau )
  }
}
#We have p predictors, and n observations.
#μi = w0 + w⊤xi





#Bayesian multiple linear regression with JAGS
model {
  w0 ~ dnorm (0 , 1e -3)
  tau <- pow ( sigma , -2)
  sigma ~ dgamma (0.001 , 0.001)
  for ( j in 1: p ) {
    w [ j ] ~ dnorm (0 , 1e -3)
  }
  for ( i in 1: n ) {
    mu [ i ] <- w0 + inprod ( w [] , x [i , ])
    y [ i ] ~ dnorm ( mu [ i ] , tau )
  }
}
#We have p predictors, and n observations.
#μi = w0 + w⊤xi



#Get the HDI from MCMC output
np.percentile(samples, q=2.5)
np.percentile(samples, q=97.5)






#Logistic regression in JAGS
model {
  # Приоритетные распределения
  w0 ~ dnorm(0, 1)
  for (j in 1:p) {
    w[j] ~ dnorm(0, 1)
  }
  # Правдоподобие
  for (i in 1:n) {
    theta[i] <- ilogit(w0 + inprod(w[], x[i, ]))
    y[i] ~ dbern(theta[i])
  }
}
