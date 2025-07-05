#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
  echo "Usage: ./load_test.sh <service_url>"
  exit 1
fi

echo "Starting load test on $URL ..."

for i in {1..50}
do
   curl -s "$URL" > /dev/null &
done

wait
echo "Load test completed."
