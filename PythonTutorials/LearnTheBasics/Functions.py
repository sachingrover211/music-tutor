__author__ = 'Jitter'

# Modify this function to return a list of strings as defined above
def list_benefits():
    benefits = []
    benefits.append("More organized code")
    benefits.append("More readable code")
    benefits.append("Easier code reuse")
    benefits.append("Allowing programmers to share and connect code together")
    return benefits

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    sentence = benefit + " is a benefit of functions!"
    return sentence

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

