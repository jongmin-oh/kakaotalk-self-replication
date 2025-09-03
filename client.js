const bot = BotManager.getCurrentBot();

/**
 * (string) msg.content: 메시지의 내용
 * (string) msg.room: 메시지를 받은 방 이름
 * (User) msg.author: 메시지 전송자
 * (string) msg.author.name: 메시지 전송자 이름
 * (Image) msg.author.avatar: 메시지 전송자 프로필 사진
 * (string) msg.author.avatar.getBase64()
 * (string | null) msg.author.hash: 사용자의 고유 id
 * (boolean) msg.isGroupChat: 단체/오픈채팅 여부
 * (boolean) msg.isDebugRoom: 디버그룸에서 받은 메시지일 시 true
 * (string) msg.packageName: 메시지를 받은 메신저의 패키지명
 * (void) msg.reply(string): 답장하기
 * (boolean) msg.isMention: 메세지 맨션 포함 여부
 * (bigint) msg.logId: 각 메세지의 고유 id
 * (bigint) msg.channelId: 각 방의 고유 id
 */

function onMessage(msg) {
  if (msg.content === "정보") {
    const info = [
      `방: ${msg.room}`,
      `채널 ID: ${msg.channelId.toString()}`,
      `사용자 해시: ${msg.author.hash}`,
      `로그 ID: ${msg.logId.toString()}`,
      `사용자 이름: ${msg.author.name}`,
      `아바타: ${msg.author.avatar.getBase64()}`
    ].join('\n');
    
    msg.reply(info);
  }
}

bot.addListener(Event.MESSAGE, onMessage);
