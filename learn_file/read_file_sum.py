# encoding: UTF8


class Read_File_Sum:
    def __init__(self, read_path, write_path, IS_delete_first=False):
        self.read_path = read_path
        self.write_path = write_path
        self.IS_delete_first = IS_delete_first
        self.dataSource = list()

    def read_file(self):
        with open(self.read_path, encoding='utf-8') as fb:
            print('读入数据：' + '\n')
            while True:
                content = fb.readline().replace('\n', '')
                # content = fb.readlines()
                if not content:
                    break;
                print(content)
                print(type(content))
                self.dataSource.append(content)

    def write_file(self):
        if self.IS_delete_first is True:
            dataSource = self.dataSource[1:]
        else:
            dataSource = self.dataSource


        with open(self.write_path, 'a+', encoding='utf-8') as f:
            for i in dataSource:
                f.write(i + '\n')
                print('写入的数据：' + '\n')
                print(i)


if __name__ == '__main__':

    r = Read_File_Sum('file_to_read.txt', 'file_to_write.txt')
    r.read_file()
    # r.write_file()



