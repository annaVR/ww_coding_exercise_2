"""
Utilities for Studio page
"""

class Util():


    def print_workshops(self, schedule):
        """
        Prints for each day: for each person: number of workshops
        :param schedule: takes a list of elements - days
        :return: prints for each day > for each person: number of workshops
        """
        for day in schedule:
            meetings_count = {}
            meetings = day.find_elements_by_xpath('.//following-sibling::div[@class="meeting-14qIm"]')
            for meeting in meetings:
                time_and_name = meeting.text
                data = time_and_name.splitlines()
                # print("Data: {}".format(data))
                name = data[1]
                if name not in meetings_count:
                    count = 1
                    meetings_count[name] = count
                else:
                    meetings_count[name] += 1
            if meetings_count:
                print(day.text)
            for k, v in meetings_count.items():
                print("{} {}".format(k, v))

