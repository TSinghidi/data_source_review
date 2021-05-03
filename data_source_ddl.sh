#!/bin/sh
###########################################################################################
#The below python script generates ddl statements to run against a particular database that is specified
#
#
#Execution :
#
##########################################################################################

# Run Python script

rm /ghs_hdp_qa/log/cdis_hdp_qa/data_source/stats/$3`date '+%Y%m%d'`.hql
python data_source.py $1 $2 2>&1 | tee -a /ghs_hdp_qa/log/cdis_hdp_qa/data_source/stats/$3`date '+%Y%m%d'`.hql 
