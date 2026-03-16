from math import gamma

def binomial_theorem(a, bx, n):
    
    b = float(bx[:-1])  
    
    result_terms = []
    
    for k in range(n + 1):
        
        binomial_coeff = gamma(n + 1) / (gamma(k + 1) * gamma(n - k + 1))
        
        
        term_a = a ** (n - k)
        term_b = b ** k
        
        
        result_terms.append(f"{binomial_coeff:.1f}*{term_a:.1f}*{term_b:.1f}x^{k}")
    
   
    result = '+'.join(result_terms)
    return result