# CitiBike Review for iy310
**Reviewed by bb1569** 

### Proposed Statistical Test and Motivation

We have:

*Idea* = Men and women ride citibike for different average durations. 

In this experiment we are comparing whether two means from two samples from a population are equal. <br> (Our samples in this case are male and female riders from July 2017 , the population is all bike riders from all months).

We can use a t-test for sample means -- unpaired samples, where we assume unequal variances. 

Before conducting the test we would want to check that our data is approximately normally distributed (for length of durations). 


Equation in it general form:

```{latex}
T= \frac{\bar{Y_1}-\bar{Y_2}}{\sqrt{\frac{sd^2_1}{N_1}+ \frac{sd^2_2}{N_2}}}
```

Equation for this experiment

```{latex}
T=\frac{mean(menDuration)-mean(womeanDuration)}{\sqrt{\frac{sd^2(menDuration)}{N_{men}}+ \frac{sd^2(womenDuration)}{N_{women}}}}

```
Click here for more readable form:

![ttest](https://github.com/biabbiassago/PUI2017_bb1569/blob/master/HW4_bb1569/ttest.pdf)


Where N_men and N_women is respectively the number of men and women in the sample

* Note that when we are calculating the t-value we are considering the sample means and std deviations. When we formulate the null and alternative hypothesis we are asking questions about the population means. 


### Suggestions and comments

* All variables necessary to answer the question have been extracted -- for the test we would need additionally to calculate the mean trip duration for men and women, the standard deviation for trip duration for mean and women, the number of men in the sample and the number of women in the sample. 

* The download of the data is not reproducible, so it should be downloaded directly from the cdf citibike folder and then moved to your PUIDATA folder. 

* When you state question, null and alternative hyppthesis, you should also include the significance level. E.g., $\alpha=0.05$

* Formulation of Alternative Hypothesis should include that you are comparing average ride lengths, i.e. <br>
__H_A__: Men's average ride duration is different from women's average ride difference. 

* In the mathematical formulation of the Null and Alternative hypothesis, to be more specific you could include the fact that you are considering the mean. For example: <br>
__H_0__ =  *pop.mean(menDuration)=pop.mean(womenDuration)*
__H_A__ = *pop.mean(menDuration) < pop.mean(womenDuration) || pop.mean(menDuration)>pop.mean(womenDuration)* <br> 
Since you are just looking at difference you could also write *pop.mean(menDuration)≠ pop.mean(womenDuration)*
    

* You could make your question investigate a more precise, and thus maybe more interesting idea. For example, check if the average length of women's ride is shorter than the men's average ride. By doing so you could have not just info about whether they are different but also on whether beign a female is correlated with taking shorter rides. In this case you would have: <br> 
__H_0__ = *pop.mean(menDuration)=pop.mean(womenDuration) || pop.mean(menDuration)<pop.mean(womenDuration)*
__H_A__ = *pop.mean(menDuration)>pop.mean(womenDuration)*
