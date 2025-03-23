from abc import ABC, abstractmethod


class File(ABC):

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def open(self):
        pass


class JsonFile(File):

    def open(self):
        print(f"oppening json file...") 

    def edit(self):
        print(f"edditing json file...") 


class XmlFile(File):

    def open(self):
        print(f"oppening xml file...") 

    def edit(self):
        print(f"edditing xml file...") 


class FileFactory:

    @staticmethod
    def CreateFile(FileType):
        if FileType.lower() == "json":
            return JsonFile()

        elif FileType.lower() == "xml":
            return XmlFile()

        else:
            return f"invalid filetype"


def main():
    file1 = FileFactory.CreateFile("json")
    file1.open()
    file1.edit()

    file2 = FileFactory.CreateFile("xml")
    file2.open()
    file2.edit()


if __name__ == "__main__":
    main()
