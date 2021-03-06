from controller.database.database_abstract import DatabaseAbstract

class DatabaseLogin(DatabaseAbstract):
    def __init__(self, entry_username, entry_password):
        self.quer_user = "SELECT COUNT(1) FROM player WHERE username = %s"
        self.quer_elo = "SELECT elo FROM player WHERE username = %s"
        self.quer_matches = "SELECT matches FROM player where username = %s"
        self.quer_pass = "SELECT password FROM player WHERE username = %s"

        self.entry_username = entry_username
        self.entry_password = entry_password
        print(self.entry_username)



    def execute_query(self):
        with self.my_connect.cursor(buffered=True) as cursor:
            cursor.execute(self.quer_user, self.entry_username)
            result = cursor.fetchall()
            for row in result:
                #print(row)
                self.corr_user_bool = row[0]

        if self.corr_user_bool == 1:

                with self.my_connect.cursor(buffered=True) as cursor:
                    cursor.execute(self.quer_elo, self.entry_username)
                    result_elo = cursor.fetchall()
                    for row in result_elo:
                        print(row)
                        self.user_elo = row[0]

                with self.my_connect.cursor(buffered=True) as cursor:
                    cursor.execute(self.quer_matches, self.entry_username)
                    result_matches = cursor.fetchall()
                    for row in result_matches:
                        print(row)
                        self.user_matches = row[0]

                with self.my_connect.cursor(buffered=True) as cursor:
                    cursor.execute(self.quer_pass, self.entry_username)
                    result = cursor.fetchall()
                    for row in result:
                        self.pass_temp = row[0]

        else:
            self.user_elo = 0
            self.user_matches = 0
            self.pass_temp = "error"

        #print(self.corr_user_bool, self.user_elo, self.pass_temp)


        return self.corr_user_bool, self.user_elo, self.user_matches, self.pass_temp