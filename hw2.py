import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(nums1: data.Point, nums2:data.Point):
    highest_y = max(nums1.y, nums2.y)  #looks for top left point
    left_most_x = min(nums1.x, nums2.x)
    right_most_x = max(nums1.x, nums2.x)  #looks for bottom right
    lowest_y = min(nums1.y, nums2.y)
    top_left = data.Point(left_most_x,highest_y)  #creates top left
    bottom_right = data.Point(right_most_x, lowest_y) # creates bottom right
    rectangle = (top_left, bottom_right)
    return rectangle

# Part 2
def shorter_duration_time(input1:data.Duration, input2:data.Duration):
    total_seconds1 = input1.minutes * 60 + input1.seconds
    total_seconds2 = input2.minutes * 60 + input2.seconds
    if total_seconds1 > total_seconds2:
        return True
    else:
        return False
# Part 3
def song_short_than(lst: list[data.Song], tim: data.Duration):
    short_songs = []
    max_time = tim.minutes * 60 + tim.seconds
    for data.Song in lst:
        song_duration_seconds = data.Song.duration.minutes * 60 + data.Song.duration.seconds
        if song_duration_seconds < max_time: short_songs.append(data.Song)
    return short_songs
# Part 4
def running_time(lst: list[data.Song], lst2: list[int]):
    seconds = 0
    minutes = 0
    for idx in lst2:
        if 0 <= idx < len(lst):
            minutes += lst[idx].duration.minutes
            seconds += lst[idx].duration.seconds
    minutes += seconds // 60
    seconds = seconds % 60
    total_time = data.Duration(minutes, seconds)
    return total_time

# Part 5
def validate_route(lst:list[list[str]], lst2:list[str]):
    if not lst2 or len(lst2) == 1:
        return False

    for idx in range(len(lst2)-1):
        if [lst2[idx], lst2[idx + 1]] not in lst:
            return False
        else:
            return True
# Part 6
def longest_repetition(lst:list[int]):
    longest_index = None
    longest_length = 0
    current_length = 1
    current_index = 0

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_length += 1
        else:
            if current_length > longest_length:
                longest_length = current_length
                longest_index = current_index
            current_length = 1
            current_index = i
    if current_length > longest_length:
        longest_index = current_index

    return longest_index