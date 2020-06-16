import requests
from behave import *
import json
import features.steps.utilslib as utilib
import features.steps.apilib as apilib
import logging

utilib.utils.logtests()
log = logging.getLogger(__file__)


@given('we are connected to AAPL US "{url}" for dates from "{fromdate}" to "{todate}" with "{apitoken}"')
def step_impl(context,url,fromdate,todate,apitoken):
    payload = {'api_token':apitoken,'period':'d.','from':fromdate,'to':todate,'fmt':'json'}
    context.newcore = apilib.core(url,payload) # connecting to the given URL
    result = context.newcore.getstatus()   #Verifying if the connection is successful
    if result == True:
        log.info("Successfully connected to the url")
        assert(True)
    else:
        log.error("Unable to connect to the given url")
        assert(False)


@when('we get the data')
def step_impl(context):
   result = context.newcore.getresponsedata()
   print(result)
   if len(result)!= 0:
       assert(True)
   else:
       log.error("No response data")
       assert(False)

@then('we verified the keyvalue pairs "{data}"')
def step_impl(context,data):
    response_record = context.newcore.getresponsedata()
    log.info(response_record)
    expected_key =data.split()
    actual_key= utilib.utils.getkeylist(response_record[1])
    value_list = utilib.utils.getvaluelist(response_record[1])
    count_actualvalue = len(value_list)
    count_expectedvalue = len(expected_key)
    if actual_key == expected_key and count_actualvalue == count_expectedvalue: #Matching the key value pairs
        assert(True)
    else:
        assert(False)

@then('we verify if the all "{totalrecords}" records inclusive of from date to date are present')
def step_impl(context,totalrecords):
    response_record = context.newcore.getresponsedata()
    if len(response_record) == totalrecords:
        assert(True)
    else:
        assert(False)

@then('we verify if all calender dates within the given range from "{fromdate}" to "{todate}"')
def step_impl(context,fromdate , todate):
    response_record = context.newcore.getresponsedata()
    expecteddate_list = utilib.utils.calenderdays(fromdate,todate)
    print(expecteddate_list)
    actualdate_list =[]
    for record in  response_record: #Looping through the response list to get the key value pairs
      actualdate_value = utilib.utils.keyvalues(record,"date")
      actualdate_list.append(actualdate_value)

    print(actualdate_list)
    if actualdate_list == expecteddate_list:
        log.info("The dates are in the given range")
        assert(True)
    else:
        log.error("The dates are not in the given range")
        assert(False)

@then('we verify no close prices can be zero or negative')
def step_impl(context):
    response_record = context.newcore.getresponsedata()
    actualcloseprice_list = []
    for record in response_record: # Looping through the response list to get the key value pairs
        actualcloseprice_value = utilib.utils.keyvalues(record, "close")
        actualcloseprice_list.append(actualcloseprice_value)
    for actual_closeprice in actualcloseprice_list:
        if float(actual_closeprice) == 0:
            assert(False)
        elif float(actual_closeprice) < 0:
            assert(False)

@then('we verify that "{key1}" price must always be greater than or equal to "{key2}" price')
def step_impl(context,key1,key2):
    response_record = context.newcore.getresponsedata()
    for record in response_record:
        result = utilib.utils.comparevalues(record,key1,key2)
        if result == True:
                log.error(f'The {key2} is higher than {key1}')
                assert(False)



