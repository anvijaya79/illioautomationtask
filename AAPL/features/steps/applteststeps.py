import requests
from behave import *
import json
import features.steps.apilib as lib

newcore = lib.core()

@given('we have behave installed')
def step_impl(self):
    response = requests.get("http://eodhistoricaldata.com/api/eod/AAPL.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWF Q67YX&period=d.&from=2019-01-01&to=2019-12-01&fmt=json")
    newcore.read()



@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False