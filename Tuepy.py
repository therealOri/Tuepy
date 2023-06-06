import os
import yt_dlp
import beaupy
from pystyle import Colors, Colorate
import subprocess





def banner():
    banner = """

                ▄▀▀▀█▀▀▄  ▄▀▀▄ ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▀▀▄
               █    █  ▐ █   █    █ ▐  ▄▀   ▐ █   █   █ █   ▀▄ ▄▀
               ▐   █     ▐  █    █    █▄▄▄▄▄  ▐  █▀▀▀▀  ▐     █
                  █        █    █     █    ▌     █            █
                ▄▀          ▀▄▄▄▄▀   ▄▀▄▄▄▄    ▄▀           ▄▀
               █                     █    ▐   █             █
               ▐                     ▐        ▐             ▐

        Made by Ori#6338 | @therealOri_ | https://github.com/therealOri
    """
    colored_banner = Colorate.Horizontal(Colors.purple_to_blue, banner, 1)
    return colored_banner



def clear():
    os.system("clear||cls")




def download_video(url, output_dir=None):
    # you can change these extensions if you wish.
    video_extension = 'mp4'
    audio_extension = 'm4a'
    ydl_opts = {
        'format': f'bestvideo[ext={video_extension}]+bestaudio[ext={audio_extension}]/best[ext={video_extension}]/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s') if output_dir else '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'avi'
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



def check_installed(program):
    try:
        subprocess.call([program, '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) #send output and errros to NULL (basically the void).
        #If the command that has been ran is successful then return True.
        return True
    except OSError:
        return False



def get_player():
    # You can change these around if you wish.
    # If you prefer mpv over vlc then make mpv preferred and vlc the backup.
    preferred = 'vlc'
    backup = 'mpv'
    if check_installed(preferred):
        return preferred
    elif check_installed(backup): #if preferred is found, the backup won't even be checked for.
        return backup
    else:
        return None



def main():
    clear()
    while True:
        main_options = ["Download Video?", "Play Video?", "Exit?"]
        print(f'{banner()}\n\nWhat would you like to do?\n-----------------------------------------------------------\n')
        main_option = beaupy.select(main_options, cursor_style="#ffa533")

        if not main_option:
            clear()
            exit("Keyboard Interuption Detected!\nGoodbye! <3")

        if main_options[0] in main_option:
            url = beaupy.prompt("Url of video to download?")
            if not url:
                clear()
                continue

            if beaupy.confirm("Want to save the video to a different directory/folder?"):
                directory_path = beaupy.prompt("Path to save video. - Example: /home/me/Desktop/Tuepy/yt_videos/creator0987/")
                if not directory_path:
                    clear()
                    continue

                clear()
                download_video(url, directory_path)
                input('Video has been saved/downloaded!\n\nPress "enter" to continue...')
                clear()
                continue
            else:
                clear()
                download_video(url)
                input('Video has been saved/downloaded!\n\nPress "enter" to continue...')
                clear()
                continue

        if main_options[1] in main_option:
            selected_player = get_player()
            if selected_player:
                video_file = beaupy.prompt("Video to watch - (drag & drop)")
                if not video_file:
                    clear()
                    continue
                video_file = video_file.replace("'", "").replace("\\", "").strip()

                clear()
                subprocess.call([selected_player, video_file])
                clear()
                continue
            else:
                clear()
                input('No valid media player has been found. Please make sure "mpv" or "vlc" is installed.\n\nPress "enter" to continue...')
                clear()
                continue

        if main_options[2] in main_option:
            clear()
            exit("Goodbye! <3")








if __name__ == '__main__':
    clear()
    main()
