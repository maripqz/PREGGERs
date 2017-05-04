# P.R.E.G.G.E.Rs
Pregnancy Resources Encouraging Good Growth & Eating Right. A Capstone project for the Galvanize Data Science Immersive.

## Business Understanding

There are a ton of resources available for new mothers. Overwhelmed by this abundance, new mothers frequently turn to friends and family for advice rather than sifting through the deluge to find evidence-based nutrition evidence.

This project scraped over a dozen pregnancy and nutrition websites to aggregate resources in one place.  Mothers then answer a few short questions and the resource recommender uses Kmeans clustering to sort through the resources for them, providing a tailored list of information that provides a spectrum of resources that supports mothers nutritional information needs. It also provides a psuedosience detector that allows users to copy and paste nutrition-related information into a form and provides the probability that the information is science-based or psuedoscience.

## Data Understanding

There are be three inputs to this project:
1. A collection of nutrition-related documents and resources from trusted parenting resource websites.
2. A collection of pregnancy-related documents and resources from trusted health and nutrition websites.
3. Psuedoscience articles scraped from disreputable health and nutrition websites.

## Data Scraping
A lot of the work on this project was related to web scraping online resources and cleaning them up enough to belong in the repository. I saved the title, link and content of each article. I did not save pictures, videos or infographics.

### Pregnancy websites:
Baby Center, Kellymom, What to Expect, The Bump, Parenting.com and Babble.
Nutrition-specific keywords: nutrition, food, eat, meal, formula, nutrients, vitamins, supplements, diet, health, wellness,

### Nutrition websites:
Authority Nutrition, Eat Right, Weight and Wellness, Food Insight, Food and Nutrition, Mayo Clinic
Pregnancy-specific keywords: pregnant, baby, breast-feeding, birth, ovulation, postpartum, placenta, trimester,

### Psuedoscience websites:
Dr Perl Mutter, FoodBabe, beachbody, Bodybuilding, Weston A Price, Mercola

## Data Preparation
Once I had my corpus of scientific and pseudoscientific articles,  I combined everything into one overarching corpus and then stemmed the words using snowball stemmer to prepare it for TF-IDF vectorization.
I also created 53 text features. NLTK's Part of Speech tagging made up the vast majority of these, but were complemented with additional features I thought might have some correlation with science or psuedoscience (for instance, capital letters and exclamation points in the title).

## Modeling
### Resource Repository Clustering
Using only the scientific documents, I vectorized the documents using TF-IDF and then put through a KMeans clustering algorithm to group documents into specific categories. These are then mapped (by hand) back to different quiz responses.

### Pseudoscience Filtering
Using 80% of my psuedoscience and evidence-based science documents as training data, I ran a Naive Bayes classifier to determine the likelihood that new articles are likley to be evidence-based or full of false claims. I combined this with a Gradient Boosted Classifier built on the 53 text features.

## Evaluation
This ensemble model was very accurate in discerning science from pseudoscience in the remaining 20% of the testing data. Below is the ROC curve demonstrating that at a probability threshold of about .9 the true positive rate is around .9 and the false positive rate is low, only about .04.

![ROC curve image](/img/ROC-curve.png)

We will ask several mothers that we know to take the quiz and rate the quality of resources the recommender provides.


## Deployment
Eventually the tool will live on a nonprofit’s website, and will be launched later this year as a soft launch for the nonprofit itself.
