const bot = BotManager.getCurrentBot();

function onMessage(msg) {
  if (msg.content == "정보") {
    msg.reply(msg.room + "\n" + msg.author.name + "\n" + msg.author.avatar.getBase64());
  }
}
bot.addListener(Event.MESSAGE, onMessage);
