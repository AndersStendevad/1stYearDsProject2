import fileManagement as fm
from collections import Counter
import pandas as pd
import math
import measures as me


def question_one():
    measures = me.Measures(fm.rawData)
    list_files = ["communityDataPropsMaximumSpanningTree.csv","communityDataPropsNaive.csv","communityDataPropsNoiseCorrected.csv","communityDataSimpleMaximumSpanningTree.csv","communityDataSimpleNaive.csv","communityDataSimpleNoiseCorrected.csv"]
    query_set,customer_queries = read_raw_data()
    print(customer_queries)

    for file in list_files[1:3]:
        list_communities = measures.readCommunity(file)
        for community in list_communities:
            query_counter = Counter()
            customer_importance = Counter()
            for customer in community:
                customer_importance[customer] = measures.find_customer_degree(customer)

                c_q = list(customer_queries[str(int(customer))])
                for q in c_q:
                    query_counter[q] +=1
            m_i_query = query_counter.most_common(1)[0][0]
            print(m_i_query)
            m_i_customers = customer_importance.most_common(len(customer_importance))
            customers_to_suggest = []
            for customer,importance in m_i_customers:
                if m_i_query in customer_queries[str(int(customer))]:
                    customers_to_suggest.append(str(int(customer)))
                if len(customers_to_suggest) == 5:
                    break
            print(customers_to_suggest)

def read_communities():

    return pd.read_csv('Data/communityData.csv')

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



question_one()
