


# functions to clean the title
def title_capitals(title):
    title = str(title).strip()
    return sum([1 for letter in title if letter.isupper()])/float(len(title))
