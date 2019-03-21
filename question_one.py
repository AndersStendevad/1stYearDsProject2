import fileManagement as fm
from collections import Counter

def question_one(community_list):

    query_set,customer_queries = read_raw_data()
    print(customer_queries)
    for community in community_list:
        query_counter = Counter()

        community = list(community)
        for customer in community:
            c_q = list(customer_queries[str(customer)])
            for q in c_q:
                query_counter[q] +=1
        print(query_counter.most_common(3))


def read_raw_data():
    queries = set()
    customer_queries = {}

    with open('Data/'+fm.rawData) as rawF:

        lines = rawF.readlines()
        customer = None
        for line in lines:
            #if customer in queries:
            #    break
            line = line.split()
            customer = line[0]
            customer_queries[customer] = set(line[1:])
            queries.update(set(line[1:]))
    return queries,customer_queries
