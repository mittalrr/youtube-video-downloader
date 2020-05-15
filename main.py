from pytube import YouTube

link=input('\n\nEnter the link of the video to be downloaded: ')
yt = YouTube(link)

print('\nVideo Title:', yt.title, '\n\nVideo Thumbnail: ', yt.thumbnail_url, '\n\n')

i=0
for strms in yt.streams:
    i+=1
    print(f'{i} --> {strms}')

print(f'\n\nTotal streams available = {len(yt.streams)}')
choice = int(input("\nEnter itag number of stream to be downloaded: "))

if input("\nPress 'y' to download else program terminates: ").lower()=='y':
    print(f'\nDownloading....{yt.streams.get_by_itag(choice)}\nDownloading...\n.\n.\n.')
    print(yt.streams.get_by_itag(choice).download())
    print("\nVideo Downloaded !")