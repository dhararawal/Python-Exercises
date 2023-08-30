#function to filter through data to see if department entered matches records
def search_by_department(department, data):
    matches = [match for match in sorted(data) if match[2] == department]
    if len(matches) > 0:
        print('Registration. No\t| Name')
        print('-------------') # line separator to make it more visually pleasing
        for match in matches:
            print(f'{match[0]}\t| {match[1]}') #prints department matched registration number and their name
    else:
        print('No matching records found!') # prints if no records in department

 #function to read and split data file and for user to search students by department
def main():
    filename = input('Enter file name: ') #asks user to input file name
    data = [] #declaring data variable as list
    with open(filename, 'r') as data_file:
        for line in data_file:
            name, registration_number, department = line.strip().split(',') #splits data file by (,)
            data.append((registration_number, name, department)) #adds registration number, name and department to the list
    print(f'data -> {data}')
    running = True
    while running:
        department = input('Enter department: ') #asks user to input department
        search_by_department(department, data) #uses above function to search through department
        running = input('Check another department? (Y/N) ').lower() == 'y' #asks user if they want to input another department to search


if __name__ == '__main__':
    main()
