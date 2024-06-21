from neo4j import GraphDatabase
import pandas as pd

NEO4J_URI='neo4j+ssc://8b846fb2.databases.neo4j.io'
NEO4J_USERNAME='neo4j'
NEO4J_PASSWORD='lyqmmZFF8yvsqWfcMBtnkgTnSWzqZCFsGT2EFbqbrm0'
AURA_INSTANCEID='8b846fb2'
AURA_INSTANCENAME='Instance01'

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))


def read_query(query, params={}):
        with driver.session() as session:
            # print(driver.verify_connectivity())
            try:
                result = session.run(query, params)
                return result.to_df()
                # response = [r.values()[0] for r in result]
                # if response == []:
                #         return "Either there is no result found for your question Or please help me with additional context."
                
                # return response
            except Exception as inst:
                if "MATCH" in query:
                    return "Either there is no result found for your question Or please help me with additional context!"
                else:
                    return query