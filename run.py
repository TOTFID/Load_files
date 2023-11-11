from main import download_files


def main():
   url = str(input('Url: '))

   filename = str(input('\nName: '))
   
   download_files(url=url ,filename=filename)


if __name__=='__main__':
   main()