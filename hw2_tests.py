import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        input1 = data.Point(2,4)
        input2 = data.Point(19,1)
        result = hw2.create_rectangle(input1,input2)
        expected = (data.Point(2, 4), data.Point(19,1))
        self.assertEqual(result, expected)

    def test_create_rectangle2(self):
        input1 = data.Point(10,20)
        input2 = data.Point(1,2)
        result = hw2.create_rectangle(input1,input2)
        expected = (data.Point(1, 20), data.Point(10,2))
        self.assertEqual(result, expected)
    # Part 2
    def test_shorter_duration_time1(self):
        input1 = data.Duration(12,23)
        input2 = data.Duration(13,24)
        result = hw2.shorter_duration_time(input1,input2)
        expected = False
        self.assertEqual(result, expected)

    def test_shorter_duration_time2(self):
        input1 = data.Duration(20,23)
        input2 = data.Duration(13,24)
        result = hw2.shorter_duration_time(input1,input2)
        expected = True
        self.assertEqual(result, expected)

    # Part 3
    def test_song_shorter_than1(self):
        lst = [data.Song("Song 1", "Title 1", data.Duration(2,3)), data.Song("Song 2", "Title 2", data.Duration(4,4))]
        dur = data.Duration(3, 0)
        result = hw2.song_short_than(lst,dur)
        expected = [data.Song("Song 1", "Title 1", data.Duration(2,3))]
        self.assertEqual(result, expected)

    def test_song_shorter_than2(self):
        lst = [data.Song("Song 1", "Title 1", data.Duration(2,31)), data.Song("Song 2", "Title 2", data.Duration(2,29))]
        dur = data.Duration(2, 30)
        result = hw2.song_short_than(lst,dur)
        expected = [data.Song("Song 2", "Title 2", data.Duration(2,29))]
        self.assertEqual(result, expected)

    # Part 4
    def test_running_time1(self):
        lst = [data.Song("Song 1", "Title 1", data.Duration(2,3)), data.Song("Song 2", "Title 2", data.Duration(4,4))]
        lst2 = [0,1]
        result = hw2.running_time(lst, lst2)
        expected = data.Duration(6,7)
        self.assertEqual(result, expected)

    def test_running_time2(self):
        lst = [data.Song("Song 1", "Title 1", data.Duration(2,3)), data.Song("Song 2", "Title 2", data.Duration(4,4))]
        lst2 = [0,1,0]
        result = hw2.running_time(lst, lst2)
        expected = data.Duration(8,10)
        self.assertEqual(result, expected)
    # Part 5
    def test_validate_route1(self):
        city_links = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],['atascadero', 'creston']]
        route = ['san luis obispo', 'santa margarita', 'atascadero']
        result = hw2.validate_route(city_links, route)
        expected = True
        self.assertEqual(result, expected)

    def test_validate_route2(self):
        city_links = [['san luis obispo', 'santa margarita'], ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],['atascadero', 'creston']]
        route = ['san luis obispo', 'atascadero']
        result = hw2.validate_route(city_links, route)
        expected = False
        self.assertEqual(result, expected)
    # Part 6
    def test_longest_repetition1(self):
        lst = [1,1,2,3,4,2,3,3,5,3,10,3,3]
        result = hw2.longest_repetition(lst)
        expected = 0
        self.assertEqual(result, expected)

    def test_longest_repetition2(self):
        lst = [1,1,1,2,2,2,2,3,4,1,1,5]
        result = hw2.longest_repetition(lst)
        expected = 3
        self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()
