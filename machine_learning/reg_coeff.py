import math
import statistics
data = {
    'Alan Perlis': {
        'Artificial intelligence': 1.46,
        'Systems programming': 5.0,
        'Software engineering': 3.34,
        'Databases': 2.32
    },

    'Marvin Minsky': {
        'Artificial intelligence': 5.0,
        'Systems programming': 2.54,
        'Computation': 4.32,
        'Algorithms': 2.76
    },

    'John McCarthy': {
        'Artificial intelligence': 5.0,
        'Programming language theory': 4.72,
        'Systems programming': 3.25,
        'Concurrency': 3.61,
        'Formal methods': 3.58,
        'Computation': 3.23,
        'Algorithms': 3.03
    },

    'Edsger Dijkstra': {
        'Programming language theory': 4.34,
        'Systems programming': 4.52,
        'Software engineering': 4.04,
        'Concurrency': 3.97,
        'Formal methods': 5.0,
        'Algorithms': 4.92
    },

    'Donald Knuth': {
        'Programming language theory': 4.33,
        'Systems programming': 3.57,
        'Computation': 4.39,
        'Algorithms': 5.0
    },

    'John Backus': {
        'Programming language theory': 4.58,
        'Systems programming': 4.43,
        'Software engineering': 4.38,
        'Formal methods': 2.42,
        'Databases': 2.80
    },

    'Robert Floyd': {
        'Programming language theory': 4.24,
        'Systems programming': 2.17,
        'Concurrency': 2.92,
        'Formal methods': 5.0,
        'Computation': 3.18,
        'Algorithms': 5.0
    },

    'Tony Hoare': {
        'Programming language theory': 4.64,
        'Systems programming': 4.38,
        'Software engineering': 3.62,
        'Concurrency': 4.88,
        'Formal methods': 4.72,
        'Algorithms': 4.38
    },

    'Edgar Codd': {
        'Systems programming': 4.60,
        'Software engineering': 3.54,
        'Concurrency': 4.28,
        'Formal methods': 1.53,
        'Databases': 5.0
    },

    'Dennis Ritchie': {
        'Programming language theory': 3.45,
        'Systems programming': 5.0,
        'Software engineering': 4.83,
    },

    'Niklaus Wirth': {
        'Programming language theory': 4.23,
        'Systems programming': 4.22,
        'Software engineering': 4.74,
        'Formal methods': 3.83,
        'Algorithms': 3.95
    },

    'Robin Milner': {
        'Programming language theory': 5.0,
        'Systems programming': 1.66,
        'Concurrency': 4.62,
        'Formal methods': 3.94,
    },

    'Leslie Lamport': {
        'Programming language theory': 1.5,
        'Systems programming': 2.76,
        'Software engineering': 3.76,
        'Concurrency': 5.0,
        'Formal methods': 4.93,
        'Algorithms': 4.63
    },

    'Michael Stonebraker': {
        'Systems programming': 4.67,
        'Software engineering': 3.86,
        'Concurrency': 4.14,
        'Databases': 5.0,
    },
}


def pearson_similarity(person1, person2,data={}):

    # find common item.
    common_ranked_items = [itm for itm in data[person1] if itm in data[person2]]

    # length of the common item set.
    n = len(common_ranked_items)

    # calculate sum of the common ranked items for both the persons.
    # find Ex and Ey
    s1 = sum([data[person1][item] for item in common_ranked_items])
    s2 = sum([data[person2][item] for item in common_ranked_items])

    # calculste the sum of square of the rating for each common item for both people.
    # find Ex^2 and Ey^2
    ss1 = sum([pow(data[person1][item], 2) for item in common_ranked_items])
    ss2 = sum([pow(data[person2][item], 2) for item in common_ranked_items])

    # calculate the product of rating of same item for both people
    # find Exy
    ps = sum([data[person1][item] * data[person2][item] for item in common_ranked_items])

    # n*Exy-(Ex*Ey)
    num = n * ps - (s1 * s2)
    # num2= sqrt(( n*Ex^2-(Ex)^2 ) * (n*Ey^2 - (Ey)^2 ) )
    den = math.sqrt((n * ss1 - math.pow(s1, 2)) * (n * ss2 - math.pow(s2, 2)))

    # return Karl Pearson's Correlation coefficient 'r'
    return (num / den) if den != 0 else 0

def recommend(person, bound=4, similarity=pearson_similarity,data={}):
    # Getting the closest people to person, the number of
    # elements included in scores, is given by the arg bound
    scores = [(similarity(person, other,data), other) for other in data if other != person]

    scores.sort()
    scores.reverse()
    scores = scores[0:bound]

    recomms = {}

    for sim, other in scores:
        ranked = data[other]

        for itm in ranked:
            if itm not in data[person]:
                weight = sim * ranked[itm]

                if itm in recomms:
                    s, weights = recomms[itm]
                    recomms[itm] = (s + sim, weights + [weight])
                else:
                    recomms[itm] = (sim, [weight])

    for r in recomms:
        sim, item = recomms[r]
        recomms[r] = ((sum(item) / sim) if sim !=0 else 0)

    return recomms

if __name__ =="__main__":
    print(recommend("Marvin Minsky", 5, pearson_similarity))
