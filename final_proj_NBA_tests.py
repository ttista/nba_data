import unittest
from final_proj_NBA import *
import sqlite3



class Test_Data(unittest.TestCase):



    def test_west_teams(self):

        conn = sqlite3.connect('nba.db')
        cur = conn.cursor()

        statement = 'SELECT Home_Score, Home_Team FROM Games '
        statement += 'WHERE Home_Team = "Warriors"'
        results = cur.execute(statement)
        result_list = results.fetchall()

        self.assertEqual(len(result_list), 39)
        self.assertEqual(result_list[2][1], 'Warriors')
        self.assertEqual(result_list[0][0], 121)
        self.assertEqual(result_list[38][0], 107)

        conn.close()

    def test_attendance_rankings(self):

        conn = sqlite3.connect('nba.db')
        cur = conn.cursor()

        statement = 'SELECT Home_Team, AVG(Team_Attendance) FROM Attendance '
        statement += 'GROUP BY Home_Team_ID '
        statement += 'ORDER BY AVG(Team_Attendance) DESC'

        results = cur.execute(statement)
        result_list = results.fetchall()

        self.assertEqual(len(result_list), 30)
        self.assertEqual(result_list[0][0], 'Bulls')
        self.assertEqual(result_list[10][0], 'Celtics')
        self.assertEqual(result_list[6][1], 19596.0)

        conn.close()

    def test_time_rankings(self):

        conn = sqlite3.connect('nba.db')
        cur = conn.cursor()

        statement = 'SELECT Weekday, Clock, AVG(Team_Attendance) FROM Attendance '
        statement += 'GROUP BY Clock '
        statement += 'ORDER BY AVG(Team_Attendance) '
        statement += 'DESC LIMIT 10'

        results = cur.execute(statement)
        result_list = results.fetchall()
        self.assertEqual(result_list[0][2], 20562.0)
        self.assertEqual(len(result_list), 10)
        self.assertEqual(result_list[0][1], '8:01 pm')

        conn.close()

    def test_bar_search(self):
        results = process_command('987')
        self.assertEqual(results, 'invalid command')

        results = process_command('attendance celtics')
        self.assertEqual(results, 'invalid command')

        results = process_command('scores time')
        self.assertEqual(results, 'invalid command')

        results = process_command('random command')
        self.assertEqual(results, 'invalid command')


unittest.main()
