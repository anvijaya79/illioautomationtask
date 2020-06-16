import logging
import datetime

class utils:
 """
    This is a class for supporting utilties.
  """

 @classmethod
 def countrecords(cls,recordlist): #This function returns the count of the records,argument is a list
     count_record = len(recordlist)
     return count_record

 @classmethod
 def datatype(cls,data): #This function returns the type of the given data
     data_type = type(data)
     return data_type

 @classmethod
 def getkeylist(cls, dictrecord): #This function returns the list of keys for the given dictionary
     key_list = [key for key, value in dictrecord.items()]
     return key_list

 @classmethod
 def getvaluelist(cls, dictrecord): #This function returns the list of values for the given dictionary
     value_list=[ value for key,value in dictrecord.items()]
     return value_list


 @classmethod
 def logtests(cls): #This function iniates logs for the test
     time_today = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
     file_name = 'appl'+time_today+'.log'
     logging.basicConfig(filename=file_name, filemode='w', format='%(name)s - %(levelname)s - %(message)s')

 @classmethod
 def calenderdays(cls,fromdate,todate): #This function returns the list of dates for the given date range
     day_list=[]
     from_date = datetime.datetime.strptime(fromdate, "%Y-%m-%d")
     to_date = datetime.datetime.strptime(todate, "%Y-%m-%d")
     delta = to_date - from_date

     for i in range(delta.days + 1):
         day = from_date + datetime.timedelta(days=i)
         str_day = day.strftime('%Y-%m-%d')
         day_list.append(str_day)
     return day_list

 @classmethod
 def keyvalues(cls, record_dict, key_field ): #This function returns the value for the given dictionary and key
     key_value=""
     for key,value in record_dict.items():
         if key in key_field:
             key_value = value
     return key_value

 @classmethod
 def comparevalues(cls,record_dict,key1_field,key2_field): #This function returns a boolean based on the comparison of the values for the given keys in a dictionary

       if float(record_dict[key1_field]) < float(record_dict[key2_field]):

           return True

       else:
           return False


