#-*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
botStart = time.time()
cl = LINE("EtifbObmUdEpXzuw9UZ5.uchYEek3yK9RnG3EudU+bq.DBs4aVRq6aKL5xEW6iMTwrcl8MqMW+4VK3qgFO12Ako=")
cl.log("Auth Token : " + str(cl.authToken))
print ("====Ykino登入成功====")
oepoll = OEPoll(cl)
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
try:
    settings['bot'] = {}
    settings["bot"][clMID] = True
    print ("設置bot清單成功")
except:
    print ("設置bot清單失敗")
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
msg_dict = {}
bl = [""]
god=['ue0edee01d554184c78f2a5d68af285c8']
admin=['ue0edee01d554184c78f2a5d68af285c8']
f = open("crsadmins.txt","r")
for x in f:
    admin.append(x.rstrip("\n"))
f.close()
Bots=['ud3ba4420d59a3bc5cbb3a23e3cf85143','uebfc691069fe81f04275077e5cf93273','u8a6cec5a5b754726aca7e27930613a78','u698c89309d565f5c68f7de9df689d203','u1097cec04bb410170f2bd7972fd552a3']
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "やっほー{}！ 追加ありがとう！CRS専用neginiran-botです！".format(str(contact.displayName)))
                cl.sendMessage(op.param1, "通常版neginiran-botの権限購入、連絡は↓")
                cl.sendContact(op.param1, "u22db032049b35c0f566a481626daabf8")

        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            GS = group.creator.mid
            print ("[ 13 ] 通知邀請群組: " + str(group.name) + "\n邀請者: " + contact1.displayName + "\n被邀請者" + contact2.displayName)
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        cl.acceptGroupInvitation(op.param1)
                        cl.sendMessage(op.param1, "ﾈｷﾞﾈｷﾞｯﾈｷﾞｯ^-ﾈｷﾞｯ、ﾈｷﾞｯﾈｷﾞﾈｷﾞｯﾈｷﾞｯ^-ﾈｷﾞｷﾞｯｷﾞｷﾞｯﾈ↓\n\n和訳:CRS専用neginiran-botです。\n通常版保護botのご用命などはこちら↓\n\nhttp://line.me/ti/p/%40ubg0555p")
                        cl.inviteIntoGroup(op.param1,Bots)
                    if op.param2 in Bots:
                        cl.acceptGroupInvitation(op.param1)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s " %("[投稿者]\n")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[内容]\n " + msg.contentMetadata["text"] + "\n[URL]\n " + msg.contentMetadata["postEndUrl"]
                            cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "\n[内容]\n " + msg.contentMetadata["text"]
                        ret_ += "\n[URL]\n " + msg.contentMetadata["postEndUrl"]
                        cl.sendMessage(msg.to, ret_)
            if msg.contentType == 0:
                if text is None:
                    return
                if sender in settings['limit']:
                    if msg.text in settings['limit'][sender]['text']:
                        if settings ['limit'][sender]['text'][msg.text] >= 3:
                            settings ['limit'][sender]['text']['react'] = False
                        else:
                            settings ['limit'][sender]['text'][msg.text] += 1
                            settings ['limit'][sender]['text']['react'] = True
                    else:
                        try:
                            del settings['limit'][sender]['text']
                        except:
                            pass
                        settings['limit'][sender]['text'] = {}
                        settings['limit'][sender]['text'][msg.text] = 1
                        settings['limit'][sender]['text']['react'] = True
                else:
                    settings['limit'][sender] = {}
                    settings['limit'][sender]['stick'] = {}
                    settings['limit'][sender]['text'] = {}
                    settings['limit'][sender]['text'][msg.text] = 1
                    settings['limit'][sender]['text']['react'] = True
                if settings['limit'][sender]['text']['react'] == True:
                    if sender in god:
                        if text.lower() == 'add on':
                            settings["autoAdd"] = True
                            cl.sendMessage(to, "自動で友達追加します")
                        elif text.lower() == 'add off':
                            settings["autoAdd"] = False
                            cl.sendMessage(to, "自動友達追加をオフにしました")
                        elif text.lower() == 'ar on':
                            settings["autoRead"] = True
                            cl.sendMessage(to, "自動已讀已開啟")
                        elif text.lower() == 'ar off':
                            settings["autoRead"] = False
                            cl.sendMessage(to, "自動已讀已關閉")
                        elif text.lower() == 'join on':
                            settings["autoJoin"] = True
                            cl.sendMessage(to, "自動加入群組已開啟")
                        elif text.lower() == 'join off':
                            settings["autoJoin"] = False
                            cl.sendMessage(to, "自動加入群組已關閉")
                        elif text.lower() == 'leave on':
                            settings["autoLeave"] = True
                            cl.sendMessage(to, "自動離開副本已開啟")
                        elif text.lower() == 'leave off':
                            settings["autoLeave"] = False
                            cl.sendMessage(to, "自動離開副本已關閉")
                        elif text.lower() == '権限更新':
                            restartBot()
                    if sender in admin:
                        if text.lower() == 'Negi:解雇':
                            G = cl.getGroup(msg.to)
                            cl.leaveGroup(msg.to)
                        elif text.lower() == 'Negi:生存確認':
                            cl.sendMessage(msg.to, "client異常なし")
                    if sender in Bots:
                        if text.lower() == '権限者に追加しました':
                            f = open("crsadmins.txt","r")
                            for x in f:
                                admin.append(x.rstrip("\n"))
                            f.close()

    except Exception as e:
        logError(e)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
