#webCrawler.py
               
import urllib.request    ##urllib to connect to the server and get the html page
import bs4               ## BeautifulSoap to get and to walk through the DOM structure the HTML page

##In the function getRespkeyword
##fetching the keyword, and creating the url
##sending it to the server and getting html page of the URL.
##creating beatifulsoap class from the html that we got from the above step.
##fetching the corresponding div to get the results
##(total number of results are displayed in the div which has class numTotalResults, so fetching the class from beautiful structure.
##the result is displayed in the specified format
##example - Results 161 - 200 of 1128
##splitting the above results and getting the last num which represents total number of results for the given query.)

def getTotalCountKeyword(keyword):
    url = "http://www.shopping.com/products"+"?KW="+keyword   #URL which we want to query in Query !
    res = urllib.request.Request(url)                        
    response = urllib.request.urlopen(res)
    soup = bs4.BeautifulSoup(response.read(),"html.parser")   #URL for which we have to use for parsing 
    elems= soup.select('.numTotalResults')
    if len(elems) == 0 :
        count = -1 
        print("No Data Found for"+keyword)
    else:
        count = int(elems[0].text.split(" ")[5].split('\n')[0])
        print("Total number of items for the required keyword ",keyword," is : ",count)
    return count

## Function getResppageNum 
##fetch the pageNum and keyword to form the url
##check if pageNum is int, otherwise return -1
##If the pageNum is 0, then it doesn't exist, so return -1
##In the DOM structure find the form which holds all the results on the page. 
##select all the divs under the form then count the div using beautifulsoap.
##The divs under the form are the displayed items.
##If there are no divs then there are no items, so return -1.

def getTotalCountPageNo(keyword, pageNo):
    if isinstance(pageNo, int):
        if pageNo == 0:
            print("Invalid Page num")
            return -1
        url = "http://www.shopping.com/products"+"~PG-"+str(pageNo)+"?KW="+keyword
        res = urllib.request.Request(url)
        response = urllib.request.urlopen(res)
        soup = bs4.BeautifulSoup(response.read(),"html.parser")
        pages= soup.select("form > div")
        count = len(pages)-2
        if count == -1:
            print("There are no ",keyword," on specified page ",pageNo)
            return -1
        else:
            print("There are ",count," number of ",keyword,"s available on page number ",pageNo)
            return count
    else:
        return -1
 
if __init__ == '__main__':
    getTotalCountPageNo('camera',54)
    getTotalCountKeyword('camera')