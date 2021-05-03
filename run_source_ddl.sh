#!/bin/sh
###########################################################################################
#The below script will load select statements results in to CSV File
#
#
#Execution :
#
##########################################################################################

# Run Beeline Commands


beeline-auto -f  /ghs_hdp_qa/log/cdis_hdp_qa/data_source/stats/$1`date '+%Y%m%d'`.hql --showHeader=false --outputformat=dsv --delimiterForDSV=','> /ghs_hdp_qa/log/cdis_hdp_qa/data_source/$1`date '+%Y%m%d'`.csv 

