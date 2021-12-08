# Automated-Data-Entry

This is an project is Automating Data Entry Job.

get_data file: In this file first, we add a URL for for the searched house with all the specification, than using this URL we made a request to Zillow to get all
              the HTML/lxml data on that URL and saved it in zillow.txt file, live data is always good but for testing is better to write data in txt file.
            
              after this we extracted links, addresses and prizes for all of the results shown on that page, around 40 in number, some links were broken we fixed
              them after adding some part of the URl, than we separated integers of prizes from signs as well.

main.py: In main.py we've looped through all the entries in the above mentioned lists, we pass them in form.py where 
         using selenium, we fill different entries like prize, address, and links in their respective fields.
         
When all the entries is been enteres we finally, click excel icon in response section of google forms, where it generate the spreadsheet of all the responses received.
