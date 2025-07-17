from main_func_db import adding_data_into_table, deleting_data_from_table, mydb, mycursor
#It's a local library. This main_func_db file contains full code


def main():
	choice = input("Press 1 to delete data\nPress 2 to add data\nEnter your choice: ")

	if choice == '1':
		
		deleting_data_from_table()
	
	elif choice == '2':

		adding_data_into_table()

	else:

	  print("Wrong entry!")
	  																			# mydb.close()
	mydb.commit()


if __name__ == "__main__":
    main()