import pypyodbc;

class SqlConnection(object):
    """description of class"""
    def __init__(self):
        self.myConnection = pypyodbc.connect('Driver={SQL Server};'
                                            'Server=SIMON-HP\SQLEXPRESS;'
                                            'Database=AlkimiiAdmin;'
                                            'uid=sa;pwd=12345')
        self.myCursor = myConnection.cursor();

    def userLogin(self, UserId, Password):
        self.myConnection
        self.myCursor

        SQLCommand = ("SELECT * FROM Users "
                      "WHERE UsererId = '" + UserId +
                      "' AND Pword = '" + Password + "'")
        self.myCursor.execute(SQLCommand)
        self.myConnection.commit()
        self.myConnect.close()

    
