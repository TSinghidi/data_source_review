###########################################################################################
#The below python script generates ddl statements to run against a particular database that is specified
#
#
#Execution :
#
##########################################################################################

# Run Python script

import json
import sys


with open("/ghs_hdp_qa/source_code/prod/cfg/" + sys.argv[1]) as f:
  data = json.load(f)
for tbl in data:
    columns = tbl["columns"]
    colCount = tbl["numberOfColumns"]
    for x in range(colCount):
        col = columns[str(x+1)]
        field = col.split("|")[0]
        dataType = col.split("|")[1]


### Generate Select statements for tables with timestamp/date columns


        stmt = "SELECT "
        if (dataType == "TIMESTAMP" or dataType == "DATE") : 
            stmt = stmt + "max(" + field + ") "+"as maxdt"+","+"'"+col.split("|")[0]+"'"+ "as colName"+",'"+ tbl["tableName"].replace(".","_") +"' as tableName" 
            stmt = stmt + " FROM " + sys.argv[2] +"." +  tbl["tableName"].replace(".","_")+";"
            print(stmt + "\n")
