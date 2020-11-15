from apis_k import API_SECRET_KEY
import requests

"""Function for handling api call to get search queries"""


def get_ballots_for_queries(year=None, month=None, subject=None, pass_or_fail=None, 
                type_measure=None, by=None, keyword=None):
    """
    Function to fetch ballots based on queries from SF APIS.

    Return [] array if no ballots found, 
        else: array of ballot dictionaries like[{month, year, letter, subject, 
        yes_votes, no_votes, pass_or_fail, percent, type_measure, by, keyworkd1 
        keyword2, or keyword3, or keyword4 or keyword5}]
    
    Year is the only Integer, the rest of the parameters are strings.

    year: Integer.
    month: abbreviated months.
    subject: string with each word in Camel case.
    pass_or_fail: string, must be in F (Fail) or P (Pass).
    type_of_measure: max 2 capital letter to indicate the type of measure.
    by (measure_placed_by in forms.py): max 2 capital letter to indicate
        how the how the measure was placed on the ballot.
    
    keyword: String Camel case, can be 1-2 words for input. 
      Will use 1 keyword to make 5 API calls to maximize outputs. There will not 
      be dupliates from api result because each word in the keyord1,2,3,4,5 is
      unique.

      be overlap based on how the API is set up. 
      5 keywords queries strings: keyword1, keyword2, keyword3, keyword4, keyword5. 
    """
     
    api_url = "https://data.sfgov.org/resource/xzie-ixjw.json?"

    #if no keyword provided,then make one api call, else make 5 api calls
    if keyword is None:
      resp_with_keyword1 = requests.get( api_url,
                                       params={"$$app_token": API_SECRET_KEY, 
                                                "year": year, 
                                                "month": month, 
                                                "subject": subject, 
                                                "pass_or_fail": pass_or_fail,
                                                "type_measure": type_measure,
                                                "by": by,
                                                "keyword1": keyword}
                                                )
      return resp_with_keyword1.json()


    resp_with_keyword1 = requests.get( api_url,
                                       params={"$$app_token": API_SECRET_KEY, 
                                                "year": year, 
                                                "month": month, 
                                                "subject": subject, 
                                                "pass_or_fail": pass_or_fail,
                                                "type_measure": type_measure,
                                                "by": by,
                                                "keyword1": keyword}
                                                )

    resp_with_keyword2 = requests.get( api_url,
                                       params={"$$app_token": API_SECRET_KEY, 
                                                "year": year, 
                                                "month": month, 
                                                "subject": subject, 
                                                "pass_or_fail": pass_or_fail,
                                                "type_measure": type_measure,
                                                "by": by,
                                                "keyword2": keyword}
                                                )

    resp_with_keyword3 = requests.get( api_url,
                                       params={"$$app_token": API_SECRET_KEY, 
                                                "year": year, 
                                                "month": month, 
                                                "subject": subject, 
                                                "pass_or_fail": pass_or_fail,
                                                "type_measure": type_measure,
                                                "by": by,
                                                "keyword3": keyword}
                                                )                                                
    
    resp_with_keyword4 = requests.get( api_url,
                                      params={"$$app_token": API_SECRET_KEY, 
                                                "year": year, 
                                                "month": month, 
                                                "subject": subject, 
                                                "pass_or_fail": pass_or_fail,
                                                "type_measure": type_measure,
                                                "by": by,
                                                "keyword4": keyword}
                                                )
        
    resp_with_keyword5 = requests.get( api_url,
                                      params={"$$app_token": API_SECRET_KEY, 
                                                "year": year, 
                                                "month": month, 
                                                "subject": subject, 
                                                "pass_or_fail": pass_or_fail,
                                                "type_measure": type_measure,
                                                "by": by,
                                                "Keyword5": keyword}
                                                )
    
    resp_keyword1_json = resp_with_keyword1.json()
    resp_keyword2_json = resp_with_keyword2.json()
    resp_keyword3_json = resp_with_keyword3.json()
    resp_keyword4_json = resp_with_keyword4.json()
    resp_keyword5_json = resp_with_keyword5.json()

    print ('API RESPONSE1', resp_keyword1_json)
    print ('API RESPONSE2', resp_keyword2_json)
    print ('API RESPONSE3', (resp_with_keyword3.json()))
    print ('API RESPONSE4', (resp_with_keyword4.json()))
    print ('API RESPONSE5', (resp_with_keyword5.json()))

    final_list = resp_keyword1_json + resp_keyword2_json + resp_keyword3_json + \
                 resp_keyword4_json + resp_keyword5_json

    return final_list



# Print statements to reuse

    # print ('API RESPONSE1', (resp_keyword1_json))
    # print ('API RESPONSE2', (resp_keyword2_json))
    # print ('API RESPONSE3', (resp_with_keyword3.json()))
    # print ('API RESPONSE4', (resp_with_keyword4.json()))
    # print ('API RESPONSE5', (resp_with_keyword5.json()))