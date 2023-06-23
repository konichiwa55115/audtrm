import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
bot = Client(
    "myfirs",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6197523213:AAFifXnQq1yZDWCucZow9R1CA8jxLnlrYgU"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت قص الصوتيات , فقط أرسل الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 ",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming & filters.voice | filters.audio | filters.video | filters.document )
def _telegram_file(client, message):

 
  user_id = message.from_user.id 
  file = message.voice
  global file_path
  file_path = message.download(file_name="./downloads/")
  global filename
  filename = os.path.basename(file_path)

  sent_message = message.reply_text(' الآن أرسل نقطة البداية والنهاية بهذه الصورة \n\n hh:mm:ss/hh:mm:ss ')  
@bot.on_message(filters.private & filters.text)
def _start_point(client, message):
   endstart = message.text
   head, tail = os.path.split(endstart)
   strt_point=head 
   end_point = tail
   subprocess.call(['ffmpeg','-i',file_path,'-ss',strt_point,'-to',end_point,'-c','copy',filename])
   with open(filename, 'rb') as f:
        bot.send_audio(message.chat.id, f)
        subprocess.call(['unlink',filename])  
        subprocess.call(['rm','-r',"./downloads/"])

 

bot.run()
