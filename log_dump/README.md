# Log Dump

This script expects to find some log files under your home directory. It will gather them and put them all together in an archive file. 

You will need to provide some log files for this script to collect, their contents is not important (they can be empty). Your test should use an environment variable to specify a path under the control of texttest instead of using files in your home directory. 

Also in this folder is the script 'read_dump.py' which you can use to print out the filenames contained in an archive file. The idea is your tests can use it to check the 'log_dump.py' script created an archive with the correct contents.
