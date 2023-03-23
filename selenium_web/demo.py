class TestSort():
    def setup(self):
        self.data = [3, 1, 5, 7, 2]
        self.expect_data = [1, 2, 3, 5, 7]

    def bubble_sort(self, data: list):
        size = len(self.data)
        for i in range(size):
            for j in range(size - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data
    def select_sort(self,data:list):
        size = len(self.data)
        for i in range(size):
            min_id = i
            for j in range(i+1,size):
                if data[min_id] > data[j]:
                    min_id = j
            data[i],data[min_id] = data[min_id],data[i]
        return data



    def test_bubble_sort(self):
        assert self.expect_data == self.bubble_sort(self.data)

    def test_select_sort(self):
        assert self.expect_data == self.select_sort(self.data)
if __name__ == '__main__':
    test1 = TestSort()