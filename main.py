import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_TOKEN' with the token you obtained from BotFather
TOKEN = 'YOUR_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your Video Downloader Bot. Use /download <video_url> to get a video.')

def download(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        update.message.reply_text('Please provide the URL of the video. Usage: /download <video_url>')
        return

    video_url = context.args[0]

    try:
        response = requests.get(video_url)

        # Replace 'your_download_directory' with your desired download directory
        with open('your_download_directory/video.mp4', 'wb') as file:
            file.write(response.content)

        update.message.reply_text('Video downloaded successfully!')
    except Exception as e:
        print(f"Error: {e}")
        update.message.reply_text('An error occurred while downloading the video. Please try again later.')

def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("download", download, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
