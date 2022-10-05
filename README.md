# hadoop_mr: Counting 5 top airways with highest delays

To run:
 - Check out script parameters with `./flight_delay_counter.sh -h` or open the file 
 - It can be executed with default parameters
  > ./flight_delay_counter.sh
 - if it is not executable run `chmod +x flight_delay_counter.sh`
 
To test it would be great to:
 - Create separate folder with test data (separate small csv file (or files) for each case)
 - Create folder with expected result
 - Run mapper, reducer and mapper+reducer from your test script and redirect output to a file
 - Create test that asserts actual result to the expected one
