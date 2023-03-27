import pandas as pd
import datetime
import time
import os.path


now2 = time.strftime('%d-%m-%Y %H-%M')


class Main:
    temp_index = 0
    df = pd.DataFrame(columns=['Data', 'Title', 'Body'])

    def addNote(self, df):
        title = input('Enter a title: ')
        body = input('Take a note: ')
        temp_list = [[now2], [title], [body]]
        return temp_list


    def createNoteBook(self):
        df = pd.DataFrame(columns=['Data', 'Title', 'Body'])
        df.to_csv('notes.csv', sep=';', index=True)
        return df


    def appendListToDF(self, data, list):
        data.loc[len(data)] = list


    def searchByDate(self):
        year = str(input('Enter date: '))
        try:
            df = pd.read_csv('notes.csv', sep=';', usecols=['Data', 'Title'])
            df_out = df.loc[df.loc[:, 'Data'].str.lower().str.contains(year.lower()), :]
            if df_out.empty:
                print('Empty!')
            else:
                print(df_out)
        except KeyError:
            print('Invalid index, going back...\n')


    def deleteRow(self):
        try:
            self.printAllNotes()
            inp = int(input('Enter the index of a note to delete it: '))
            df = pd.read_csv('notes.csv', sep=';')
            df = df.drop(inp, axis=0)
            df.to_csv('notes.csv', sep=';', index=True)
        except KeyError:
            print('Invalid index.')


    def saveToCsv(self, data, name):
        if (os.path.isfile(name)):
            data.to_csv(name, sep=';', mode='a', index=True, header=False)
        else:
            data.to_csv(name, sep=';', index=True)

    def printAllNotes(self):
        dd = pd.read_csv('notes.csv', sep=';', usecols=['Data', 'Title'])

        if dd.empty:
            print('You don\'t have notes.')
        else:
            print(dd, '\n')


    def printSpecificNote(self):
        try:
            user_input = int(input('Enter an index of a note: '))
            temp_index = user_input
            df = pd.read_csv('notes.csv', sep=';', usecols=['Data', 'Title', 'Body'])
            row_list = df.loc[int(user_input), :].values.flatten().tolist()
            for i in range(len(row_list)):
                print(str(row_list[i]))
            input('Press "enter" to continue: ')
        except (KeyError, ValueError):
            print('Invalid index.\n')


    def editNote(self):
        inp = int(input('Enter an index of a note to edit it: '))
        df = pd.read_csv('notes.csv', sep=';', usecols=['Data', 'Title', 'Body'])
        inp2 = int(input('Enter 1 to edit the title, 2 to edit the note: '))
        if int(inp2) == 1:
            new_title = input('Enter new title: ')
            df.loc[inp, ['Title']] = new_title
            df.to_csv('notes.csv', sep=';', index=True)
        elif int(inp2) == 2:
            new_note = input('Enter new note: ')
            df.loc[inp, ['Body']] = new_note
            df.to_csv('notes.csv', sep=';', index=True)
        else:
            print('Invalid syntax...')


class Interface:


    def buttonClick(self):
        f = Main()
        a = f.df
        switch = True

        while switch:
                try:
                        user_input = int(input('1. Add a note.\n2. View all notes.\n3. Edit a note.\n4. Delete a note.\n'
                                               '5. Search a note by date.\n6. Save a note.\n7. Exit.\nEnter a number: '))
                        print('\n')
                        if user_input == 1:
                            f.appendListToDF(a, f.addNote(a))
                            a.to_csv('notes.csv', sep=';')
                        elif user_input == 2:
                            f.printAllNotes()
                            f.printSpecificNote()
                        elif user_input == 3:
                            f.printAllNotes()
                            f.editNote()
                        elif user_input == 4:
                            f.deleteRow()
                        elif user_input == 5:
                            f.searchByDate()
                            temp_input = input('1. View a note. 2. Back: ')
                            try:
                                if temp_input == '1':
                                    f.printSpecificNote()
                                elif temp_input == '2':
                                    self.goBack()
                            except KeyError:
                                print('Invalid syntax.')

                        elif user_input == 6:
                            f.saveToCsv(a, 'notes.csv')
                        elif user_input == 7:
                            switch = False
                except FileNotFoundError:
                    print('Not a single note yet.')
                except ValueError:
                    print('Invalid number!')


    def goBack(self):
        self.buttonClick()



class Button:
    a = Interface()
    a.buttonClick()






















