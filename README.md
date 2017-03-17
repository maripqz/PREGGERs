# Motherhood Resource Recommender
Capstone project for Galvanize, a resource recommender for new mothers

## Business Understanding

There are an overwhelming number of resources available for new mothers. Overwhelmed by this abundance, new mothers frequently turn to friends and family for advice rather than sifting through the deluge to find evidence-based nutrition evidence.

This resource recommender asks a few short questions of new mothers and sorts through those resources for them, providing a tailored list of information and experts that address religious and cultural preferences and provides a spectrum of resources from infographics to scientific journal articles that supports mothers regardless of reading level.

## Data Understanding

There will be three inputs to this project:
1. A collection of documents and resources from popular parenting resource websites.
3. A short quiz asking users to answer some basic questions on their experience.

## Data Preparation
Most of the work on this project will be related to web scraping online resources and cleaning them up enough to belong in the repository. There are two different types of resources I will be collecting: pregnancy and maternal health websites (limited to information specifically focused on nutrition), and nutrition websites (limited to information about pregnancy and maternal health).

Pregnancy websites: Baby Center, Kellymom, What to Expect, The Bump, Parenting.com and Babble.
Nutrition-specific keywords: nutrition, food, eat, meal, formula, nutrients, vitamins, supplements, diet, health, wellness,

Nutrition websites: Authority Nutrition, Eat Right, Weight and Wellness, Food Insight, http://www.foodandnutrition.org/,  
Pregnancy-specific keywords: pregnant, baby, breast-feeding, birth, ovulation, postpartum, placenta, trimester,

Psuedoscience websites:
Dr Perl Mutter, FoodBabe, beachbody, Bodybuilding
https://www.infowars.com/search-page/?nutrition
http://search.mercola.com/results.aspx?q=pregnant
http://naturalnews.com/


## Modeling
Resource Repository
The resources will undergo natural language processing. They will be evaluated using TF-IDF Vectorizing and KMeans clustering to group documents into specific categories. I will also sort them into categories of length and unique word counts (as a stand-in for complexity).

## Evaluation
We will ask several mothers that we know to take the quiz and rate the quality of resources the recommender provides.


## Deployment
Eventually the recommender will live on a nonprofit’s website. As this does not currently exist, it will have a standalone website with links out to all of the supporting resources.
