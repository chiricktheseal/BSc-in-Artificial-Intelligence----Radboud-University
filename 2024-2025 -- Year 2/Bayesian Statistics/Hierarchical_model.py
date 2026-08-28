#Иерархическая модель в JAGS

model {
    # prior on theta _ hat 
    theta _ hat ~ dbeta (a , b )
    
    # deterministic tr ansfor mation
    a _ transformed <- theta _ hat * ( kappa - 2) + 1
    b _ transformed <- (1 - theta _ hat ) * ( kappa - 2) + 1
    
    for ( i in 1: M ) {
        # prior on theta [ i ]
        theta [ i ] ~ dbeta ( a _ transformed , b _ transformed )
        
        # likelihood
        y [ i ] ~ dbin ( theta [ i ] , n [ i ])
    }
}