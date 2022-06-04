# get-links-from-url
  Returns all links from an URL (and their links, multiple times, if asked) and stores them in an Excel spreadsheet along with the time the link was found.

  i DEFINITELY could have used less libraries but i have no experience on pandas and i decided to go with other libs when writing stuff to Excel, may fix this in the future.
  
## Used libraries
- Requests (Acessing URLs)
- Bs4's Beautiful Soup (Easy HTML parsing and tag finding)
- Regex (Used to only get valid links from the anchor tags list)
- xlsxwriter (Easy Excel writing)
- Pandas (Very wide use but i only added it to remove copies in the final sheet)
- Openpyxl (Necessary for Pandas)
- datetime (Used to get actual minute and hour)

## How to use

Example of function calling:

- URL: Initial url. ("https://github.com/")
- Depth:
0. Only the links contained in the URL page
1. All from URL and the pages that are in the URL link list
2. All the above and the ones that are on the open pages of the previous links etc...
- File Name: The name of the excel file. ("excel.xls")
```
get_links(url, depth, file_name)
```