# P.R.E.G.G.E.Rs
Pregnancy Resources Encouraging Good Growth & Eating Right. A Capstone project for the Galvanize Data Science Immersive.

## Business Understanding

There are a ton of resources available for new mothers. Overwhelmed by this abundance, new mothers frequently turn to friends and family for advice rather than sifting through the deluge to find evidence-based nutrition evidence.

This project combed over a dozen pregnancy and nutrition sites to aggregate resources in one place.  asks a few short questions of new mothers and sorts through those resources for them, providing a tailored list of information and experts that address religious and cultural preferences and provides a spectrum of resources from infographics to scientific journal articles that supports mothers regardless of reading level.

## Data Understanding

There are be three inputs to this project:
1. A collection of documents and resources from popular parenting resource websites.
3. A short quiz asking users to answer some basic questions on their experience.

## Data Preparation
A lot of the work on this project was related to web scraping online resources and cleaning them up enough to belong in the repository. There are two different types of resources I will be collecting: pregnancy and maternal health websites (limited to information specifically focused on nutrition), and nutrition websites (limited to information about pregnancy and maternal health).
Once I had my articles, I stemmed the content using snowball stemmer to prepare it for TF-IDF vectorization, and created 53 features using NLTK's Part of Speech tagging and additional features I thought might have some correlation with science or psuedoscience (for instance, capital letters and exclamation points in the title).

### Pregnancy websites:
Baby Center, Kellymom, What to Expect, The Bump, Parenting.com and Babble.
Nutrition-specific keywords: nutrition, food, eat, meal, formula, nutrients, vitamins, supplements, diet, health, wellness,

### Nutrition websites:
Authority Nutrition, Eat Right, Weight and Wellness, Food Insight, Food and Nutrition, Mayo Clinic
Pregnancy-specific keywords: pregnant, baby, breast-feeding, birth, ovulation, postpartum, placenta, trimester,


### Psuedoscience websites:
Dr Perl Mutter, FoodBabe, beachbody, Bodybuilding, Weston A Price, Mercola


## Modeling
### Resource Repository
The resources were vectorized using TF-IDF and the resulting then put through a KMeans clustering algorithm to group documents into specific categories. These are then mapped back to .

### Pseudoscience Filtering
Using my psuedoscience and evidence-based science documents as training data, I ran a Naive Bayes classifier to determine the likelihood that new articles are likley to be evidence-based or full of false claims.

## Evaluation
We will ask several mothers that we know to take the quiz and rate the quality of resources the recommender provides.


## Deployment
Eventually the tool will live on a nonprofit’s website, and will be launched later this year as a soft launch for the nonprofit itself.
