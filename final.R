#load in the RMySQL library
library(RMySQL)

#create the connector
mydb <- dbConnect(MySQL(), user = 'stats', password = 'stats', dbname = 'stats255_final', host = 'localhost')
#conn = dbConnect(RMySQL::MySQL(), mydb)
Rqueries = vector()

#query one
req1 <- dbSendQuery(mydb, "select avg(Percent), std(Percent) from Final_Results")
fetch1 <- fetch(req1)

#query two
req2 <- dbSendQuery(mydb, "select avg(Curved), std(Curved) from Final_Results")
fetch2 <- fetch(req2)

#query three
req3 <- dbSendQuery(mydb, "select Grade, count(Grade) as count
                    from Final_Results
                    group by Grade
                    order by count desc
                    limit 1")
fetch3 <- fetch(req3)


#query four
req4 <- dbSendQuery(mydb, "select Grade_Curve, count(Grade_Curve) as count
                    from Final_Results
                    group by Grade_Curve
                    order by count desc
                    limit 1")
fetch4 <- fetch(req4)

#collate into a list
Rqueries = c(Rqueries, fetch1, fetch2, fetch3, fetch4)

#print the list
print(Rqueries)
