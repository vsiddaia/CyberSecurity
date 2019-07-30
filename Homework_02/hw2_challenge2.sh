#!/bin/bash
unzip -o ./OrderRecords.zip
mkdir -p -v ./AllRecords/VIPCustomerOrders
grep "Michael"  -ris ./OrderRecords/* | grep  "Davis"  > ./AllRecords/VIPCustomerOrders/michael_davis_orders.output
grep "Michael"  -ris ./OrderRecords/* | grep  "Campbell"  > ./AllRecords/VIPCustomerOrders/michael_campbell_orders.output
echo "Summary" > VIPCustomerDetails.md
echo "Michael Davis has" `cat  ./AllRecords/VIPCustomerOrders/michael_davis_orders.output |wc -l ` " Record(s)" >> VIPCustomerDetails.md
echo "Michael Campbell has" `cat  ./AllRecords/VIPCustomerOrders/michael_campbell_orders.output |wc -l ` " Record(s)" >> VIPCustomerDetails.md


