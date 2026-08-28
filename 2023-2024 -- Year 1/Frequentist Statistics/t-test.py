from spicy import stats
import numpy as np

t = -3.3
df = 27

conf_interv = 0.98
onetail_of_conf_interv = (1  - conf_interv ) / 2


#finding critical T score ont=ail
critical_score_t = stats.t.ppf(onetail_of_conf_interv, df)
print("Critical t score = %6.3f.\n" % (critical_score_t))
#finding critical T score twotail
critical_score_t = stats.t.ppf(conf_interv, df)
print("Critical t score !! = %6.3f.\n" % (critical_score_t))


#for one-sided test
pval = stats.t.sf(np.abs(t), df)
print("One-sided:\nT-statistic = %6.3f.\n P-value = %6.4f\n\n" % (t, pval))

#for two-sided test
pval = stats.t.sf(np.abs(t), df)*2
print("Two-sided:\nT-statistic = %6.3f.\n P-value = %6.4f" % (t, pval))

#------------------------------------
print("\n\n\nANOTHER TEST\n\n\n")
#t_score = 0
mu_expected = 1
mean = 53.3
#stand_err = 0
n = 29
significance_level = 0.05
std = 0.3

stand_err = std / np.sqrt(n)
print(stand_err)

t_score = (mean - mu_expected) / stand_err
print(t_score)

def calculate_p_value(T_score, df, two_sided=True):
  if two_sided:
        p_value = 2 * stats.t.sf(np.abs(T_score), df)
  else:
        p_value = stats.t.sf(np.abs(T_score), df)

  return p_value


p_value = calculate_p_value(t_score, df=(n - 1), two_sided=True)
print(p_value)



if p_value < significance_level:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
