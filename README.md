# parsing-alibaba

მოცემულ კოდში რექუესთი იგზავნება аlibaba.com-ზე სადაც მოძებნილია კატის სათამაშოები. 
ციკლის საშუალებით მიღებული შედეგის 20 გვერდიდან მოაქვს თითოეული პროდუქტის დასახელება, 
რამდენი ცალი იყიდება მითითებულ ფასში და პროდუქცის ლინკი alibaba-ს საიტზე. 
(იმის გამო რომ ყველა პროდუქტის ფასი არ არის მითითებული გაწერილია მეთოდი 
იმისთვის რომ თუ ფასი არ არის მითითებული არ ამოაგდოს შეცდომა)
წამოღებული მონაცემები ინახება csv ფაილში. 
რიქუესთებს შორის ინტერვალის გასაკეთებლად გამოყენებულია random  და time მოდული. 



In the given code a request is sent to alibaba.com where cat toys are found. 
The result of the cycle obtained from 20 pages brings the name of each product, 
how many pieces are sold at the indicated price and a link to the product on the alibaba site. 
(Because not all product prices are listed, there is a method to avoid making a mistake if the price is not specified)
The extracted data is stored in a csv file.
A random and time module is used to make the interval between requests.
