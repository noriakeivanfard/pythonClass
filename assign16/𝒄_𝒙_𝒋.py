"""CSV

This format is the least versatile of all three formats. 
This is because a homemade parser is required to convert the CSV data into a native data structure.
As a result, if the data structure changes, there is an associated overhead of having to change or even redesign your parsers.
Furthermore, since the program creating the CSV and the program parsing the CSV reside on different machines 
(remember that we are passing data from one machine to another) then both programs must be updated simultaneously to prevent the receiving program to crash. 
Otherwise, an outage is required to update both programs individually to prevent incompatibility issues.
Finally, CSV does not really support data hierarchies. 

XML

 It was created to better represent data formats with a hierarchical structure.  
 This data format fully supports hierarchical data structures and is very appropriate when receiving complex data as a response. 
 It is also very human readable. Most browsers have built in XML readers that allow you to inspect XML files.
 Since XML was the first standard hierarchical data format, most APIs have built in functionality to automatically convert XML data streams into native data structures like objects.

JSON

This data format supports hierarchical data while being smaller in size than XML. 
As its name implies, it was also created to more easily parse data into native Javascript objects, 
making it very useful for web applications. JSON is the best of both worlds with respect to CSV and XML. 
It’s simple and compact like CSV, but supports hierarchical data like XML. Unlike XML, JSON formats are only about twice as large as CSV formats."""
