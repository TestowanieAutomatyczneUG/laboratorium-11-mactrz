import os

class File:

    def read(self, path):
        file = open(path, 'r')
        response = ''

        for line in file:
            response += line

        return  response

    def write(self, path, text):
        file = open(path, 'w')
        file.write(text)
        file.close()

    def delete(self, path):
        if os.path.exists(path):
            os.remove(path)
            return True
        else:
            raise Exception('File does not exist')