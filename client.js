const bot = BotManager.getCurrentBot();

function onMessage(msg) {
  if (msg.content === "정보") {
    const info = [
      `방: ${msg.room}`,
      `채널 ID: ${msg.channelId}`,
      `사용자 해시: ${msg.author.hash}`,
      `로그 ID: ${msg.logId}`,
      `사용자 이름: ${msg.author.name}`,
      `아바타: ${msg.author.avatar.getBase64()}`
    ].join('\n');
    
    msg.reply(info);
  }
}

bot.addListener(Event.MESSAGE, onMessage);
