library(sqldf)

#gathering all datasets
info_names = c("plasmid", "operon", "input", "output", "opr", "optr", "part", "optr", "interactor")

#deleting all old txt files to make room for new ones
delete_file <- function(file_name){
  full_name = paste0(file_name, ".txt")
  if(file.exists(full_name)) {file.remove(full_name)}
}

lapply(info_names, delete_file)

#reading in the unformmated version of linh's database
data = read.csv("database_linh_new.csv")
data = sqldf("select * from data where Checklist = 'X'")
#View(data)

#extracting all plasmid table relevant columns
plasmid = sqldf("select P_ID, P_Name, Title, Authors, Journal, Year from data where O_ID = ''")
#View(plasmid)

#extracting all operon table relevant columsn  
operon = sqldf("select O_ID, Structure, Math from data where O_ID != ''")
#View(operon)

#extracting input/output table relevant information
input = sqldf("select O_ID, Domain from data where O_ID != ''")
#View(input)
output = sqldf("select O_ID, Range from data where O_ID != ''")
#View(output)

#extracting the operon name and plasmid names. Need to map back to 
#operon_id and plasmid_id in python.
opr = sqldf("select O_ID, R_L from data where O_ID != ''")
#View(opr)

part = sqldf("select structure from data where O_ID != ''")
#View(structure)

#extracting the operon_ID and structure. Need to take structure and need 
#parse to get the part_ID. The parts need an id so it would be better to 
#first work on the parts before you get there. 
optr = sqldf("select O_ID, Structure from data where O_ID != ''")
#View(optr)

int_d = sqldf("select Domain from data where O_ID != ''")
int_r = sqldf("select Range from data where O_ID != ''")
names(int_r)[1] = "Domain"
interactor = rbind(int_d, int_r)
interactor = unique(interactor)
names(interactor)[1] = "Interactors"
#View(interactors)

#writing all datasets
write_to_tab <- function(data){
  write.table(get(data), paste0(data,".txt"), sep= "\t", row.names = FALSE)
}
lapply(info_names, write_to_tab)




